from import_export import resources
from revise_multiplayer.models import *

class StudentResource(resources.ModelResource):
    class Meta:
        model = Player
        fields = ('username', 'surname', 'pre_assessment', 'personality_test', 'game_scores', 'game_answer_history')