from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from levelupapi.models import Game, Gamer, GameType
from rest_framework.decorators import action
class GameView(ViewSet):
    """Level up game types view"""

    def retrieve(self, request, pk):
       game = Game.objects.get(pk=pk)
       serializer = GameSerializer(game)
       return Response(serializer.data)


    def list(self, request):
       games = Game.objects.all()
       serializer = GameSerializer(games, many=True)
       return Response(serializer.data)


    def create(self, request):
        """Handle POST operations

        Returns
            Response -- JSON serialized game instance
        """
        gamer = Gamer.objects.get(user=request.auth.user)
        game_type_id = GameType.objects.get(pk=request.data["game_type"])

        game = Game.objects.create(
            maker=gamer,
            title=request.data["title"],
            number_of_players=request.data["number_of_players"],
            skill_level=request.data["skill_level"],
            game_type =game_type_id
        )
        serializer = GameSerializer(game)
        return Response(serializer.data, status=status.HTTP_201_CREATED )
    
    def update(self, request, pk):

        game = Game.objects.get(pk=pk)
        game.title = request.data["title"]
        game.number_of_players = request.data["number_of_players"]
        game.skill_level = request.data["skill_level"]

        game_type = GameType.objects.get(pk=request.data["game_type"])
        game.game_type = game_type
        game.save()

        return Response(None, status=status.HTTP_204_NO_CONTENT)

    def destroy(self, request, pk):
        game = Game.objects.get(pk=pk)
        game.delete()
        return Response(None, status=status.HTTP_204_NO_CONTENT)
        


class GameSerializer(serializers.ModelSerializer):
    """JSON serializer for game types
    """
    class Meta:
        model = Game
        fields = ('id', 'title', 'maker', 'game_type', 'skill_level', 'number_of_players')
        depth = 2