from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from levelupapi.models import Game, Gamer, GameType

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
            type=game_type_id
        )
        serializer = GameSerializer(game)
        return Response(serializer.data, status=status.HTTP_201_CREATED )




class GameSerializer(serializers.ModelSerializer):
    """JSON serializer for game types
    """
    class Meta:
        model = Game
        fields = ('id', 'title', 'maker', 'type', 'skill_level', 'number_of_players')
        depth = 2