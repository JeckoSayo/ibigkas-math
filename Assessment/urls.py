from django.urls import path
from . import views

app_name = 'Assessment'

urlpatterns = [
    path("ibigkas-menu/<uuid>/", views.mainPage, name="mainMenu"),

    path("", views.loginPage, name="login_page"),

    path("signIn", views.multiplayer_signIn, name="SignIn_multi"),
    path("create-account/", views.createAccount, name="createAccount"),
    
    # Assessment urls
    path("personality-test/<uuid>/", views.personalityTest, name="personality_test"),
    path("demographics/<uuid>/", views.demographicsQuestion, name="demographics"),

    path("pre-test/<uuid>/", views.pre_test, name="pre_test"),

    # AJAX URL PATH
    path("pre_test_ans/", views.pre_test_answer, name="pre_test_ans"),
    path("signIn_multi/", views.multi_signIn_ajax, name="multi_signIn"),
    path("demo_ansOne/", views.demographicsAnswerOne, name="demoOneAnswer"),
    path("demo_ansTwo/", views.demographicsAnswerTwo, name="demoTwoAnswer"),
    path("pre_assessment_ans/", views.personalityTestAnswer, name="preAnswer"),
    path("createAccoutAjax/", views.createAccountAjax, name="createAjax"),




]
