from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from levelupapi.models import Event, Gamer, Game


class EventView(ViewSet):
    """Level up event types view"""

    def retrieve(self, request, pk):
       event = Event.objects.get(pk=pk)
       serializer = EventSerializer(event)
       return Response(serializer.data)

    def filter_events_by_game(events, game_id):
        filtered_events = []
        for event in events:
            if event.game_id == game_id:
                filtered_events.append(event)
        return filtered_events


    def list(self, request):
        events = Event.objects.all()
    
        if 'game' in request.query_params:
            game_id = int(request.query_params['game'])
            events = filter(lambda event: event.game_id == game_id, events)
        else:
            pass
        serializer = EventSerializer(events, many=True)
        return Response(serializer.data)

    def create(self, request):
         gamer = Gamer.objects.get(pk=request.data["gamer"])
         game_played = Game.objects.get(pk = request.data['game'])
        # create a instance of event class with request body as values
         event = Event.objects.create(
             title = request.data['title'],
             organizer = gamer,
             date = request.data['date'],
             location = request.data['location'],
             game = game_played
         )
         event.attendees.set([gamer])
         event.save()
         serializer = EventSerializer(event)
         return Response(serializer.data, status=status.HTTP_201_CREATED)
class EventSerializer(serializers.ModelSerializer):
    """JSON serializer for event types
    """
    class Meta:
        model = Event
        fields = ('id', 'title', 'date', 'location', 'organizer', 'game', 'attendees')
        depth = 2