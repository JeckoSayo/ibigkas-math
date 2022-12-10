from typing import NoReturn
from urllib.parse import parse_qs
from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse

# from Ibigkas.ibigkas_project.revise_multiplayer.views import room
from .models import *
from revise_multiplayer.models import *
from .forms import *

from django.contrib.sessions.models import Session
from django.contrib import messages

from datetime import datetime
import pytz
import json


def mainPage(request, uuid):
    # Creating user session and save to database
    user = Player.objects.get(uuid=uuid)
    group = user.group

    IST = pytz.timezone('Asia/Manila')
    datetime_ist = datetime.now(IST)
    date = datetime_ist.strftime('%Y-%m-%d')
    user.date = date

    session = request.session._get_or_create_session_key()
    user.user_session = session
    user.save()

    user_uuid = uuid
    request.session['uuid'] = user_uuid

    create_room_for_every_group(user)
    auto_assign_room_if_has_group(user, group)

    out = {
        "group": group
    }
    
    return render(request, "Assessment/main.html", out)

def personalityTest(request, uuid):
    #Saving uuid to session request to use on client side
    user_uuid = uuid
    request.session['uuid'] = user_uuid

    assessment = PersonalityTest.objects.all()
    
    out = {'assess': assessment}
    return render(request, "Assessment/assessment/personalityTest.html", out)

def demographicsQuestion(request, uuid):
    Player.objects.filter(uuid=uuid).update(player_mode="MultiPlayer")
    user = Player.objects.get(uuid=uuid)
    user_uuid = uuid
    request.session['uuid'] = user_uuid

    if user.demographics != '':
        if user.personality_test != '':
            # If all assessment is done, user will redirect at waiting area
            # REMINDER!! Please change the url path to waiting area.
            # Add condition to url path for pre test
            return redirect('revise_multiplayer:room_list', uuid=uuid)
        else:
          return redirect('Assessment:personality_test', uuid=uuid)
    else:
      demographics_question = DemographicsModel.objects.all()
      questionTwo = DemographicsTwoModel.objects.all()
      out = {'questionsOne': demographics_question,'questionTwo': questionTwo} 
      return render(request, "Assessment/assessment/Demographics.html", out)

def demographicsAnswerOne(request):
    if request.method == 'POST':
        studentAnsOne = request.POST['studentAnsOne']
        studentUUID = request.POST['studentUUID']
        Player.objects.filter(uuid=studentUUID).update(demographics=studentAnsOne)
        message = 'Pre assessment save'
        return HttpResponse(message)

def demographicsAnswerTwo(request):
    if request.method == 'POST':
        studentAnsTwo = request.POST['studentAnsTwo']
        studentUUID = request.POST['studentUUID']
        newAnswer = []

        models = Player.objects.filter(uuid=studentUUID).first()
        ans = models.demographics
        newAnswer.append(ans)
        newAnswer.append(studentAnsTwo)
        new_string = ''.join(str(x) for x in newAnswer)
        Player.objects.filter(uuid=studentUUID).update(demographics=new_string)

        out = {'stud_uuid': studentUUID}
        return JsonResponse(out)

#AJAX function to save student answer key on personality test database 
def personalityTestAnswer(request):
    if request.method == 'POST':
        studentAns1 = request.POST['studentAns']
        studentUUID = request.POST['studentUUID']
        Player.objects.filter(uuid=studentUUID).update(personality_test=studentAns1)
        message = 'Personality Test Save!'
        return HttpResponse(message)


def createAccountAjax(request):
    if request.method == 'POST':
        userName = request.POST['user_name']
        usersSurname = request.POST['users_surname']
        section = request.POST['section']
        gender = request.POST['user_gender']

        age = request.POST['user_age']
        age = int(age)

        userName = userName.capitalize()
        usersSurname = usersSurname.capitalize()
        section = section.capitalize()

        # Check if the user name is already use
        if Player.objects.filter(username=userName).exists():
            message = f'{userName} already exist. Please try another username'
            return HttpResponse(message)
        else:
            models = Player(username=userName, surname=usersSurname, age=age, gender=gender, section=section)
            models.save()
            user_uuid = models.uuid
            user_uuid = str(user_uuid)
            request.session['uuid'] = user_uuid
            message = user_uuid
            return HttpResponse(message)

def createAccount(request):
    try:
        session = request.session._get_or_create_session_key()
        user_key = Player.objects.get(user_session=session)
        if user_key.user_session != None:
            sessionTwo = request.session._get_or_create_session_key()
            user_key = Player.objects.get(user_session=sessionTwo)
            # if a user is already have a session id it will redirect to main menu urls. 
            return redirect('Assessment:mainMenu', uuid=user_key.uuid)
    except:
        session = None
        return render(request, "Assessment/createAccount.html")     

        

def loginPage(request):
    sample = ResearchStatus.objects.all()
    out = {
        "check":sample
    }
    return render(request,"Assessment/login.html", out)


def multiplayer_signIn(request):
    return render(request,"Assessment/signIn.html")

def multi_signIn_ajax(request):
    if request.method == 'POST':
        signIn_user = request.POST['signIn_user']
        signIn_user = signIn_user.capitalize()

        user_model =  Player.objects.filter(username=signIn_user)
        if user_model.exists():
            user_get_credentials = Player.objects.filter(username=signIn_user).first()
            credential_id = user_get_credentials.uuid
            out = {
                'credential': credential_id
            }
            return JsonResponse(out)
        else:
            message = "Please check your username!"

        return HttpResponse(message)

def pre_test(request, uuid):
    user_uuid = uuid
    request.session['uuid'] = user_uuid
    modelPretest = PreTest.objects.all()

    out = {
        "pretest": modelPretest
    }

    return render(request,"Assessment/PreTestAndPostTest/preTest.html", out)

def pre_test_answer(request):
    if request.method == 'POST':
        pretestAnswers = request.POST['pretestAnswers']
        pretestScore = request.POST['pretestScore']
        studentUUID = request.POST['studentUUID']
        Player.objects.filter(uuid=studentUUID).update(pre_test_score=pretestScore, pre_test_answer=pretestAnswers)


        message = "Nice"
        return HttpResponse(message)

# In every group there must be an uqual room name
def create_room_for_every_group(user):
    group_list = Group.objects.all()

    for i in range(len(group_list)):
        if not chk_has_room(group_list[i].name):
            new_room = Room.objects.create(
                room_name = group_list[i].name,
                group_name = group_list[i],
                password = "",
                is_research = True,
                # players = user.username if user.group == group_list[i] else "",
            )
            new_room.save()

def chk_has_room(group):
    room_list = Room.objects.all()
    for i in range(len(room_list)):
        if room_list[i].room_name == group:
            return True 
    return False

def auto_assign_room_if_has_group(user, group):
    # print("Group: " + group)
    if group != None:
        room = Room.objects.get(group_name=group)
        if user.username not in room.players:
            player_list = room.players
            player_list = player_list + ", " + user.username
            room.players= player_list
            room.save()
        

# Checks if in research mode
# ResearchStatus.object().research_mode

    







