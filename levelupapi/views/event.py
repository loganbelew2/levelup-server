from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from levelupapi.models import Event, Gamer, Game, EventLog


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
         gamer = Gamer.objects.get(user=request.auth.user)
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
         serializer = EventSerializer(event)
         return Response(serializer.data, status=status.HTTP_201_CREATED)
    
    def update(self, request, pk):
        game = Game.objects.get(pk = request.data['game'])
        event = Event.objects.get(pk=pk)
        organizer = Gamer.objects.get(pk = request.data['organizer'])
        event.title = request.data["title"]
        event.date = request.data["date"]
        event.location = request.data['location']
        event.game = game
        event.organizer = organizer
        event.save()
        
    def destroy(self, request, pk):
        event = Event.objects.get(pk=pk)
        event.delete()
        return Response(None, status=status.HTTP_204_NO_CONTENT)    
class EventSerializer(serializers.ModelSerializer):
    """JSON serializer for event types
    """
    class Meta:
        model = Event
        fields = ('id', 'title', 'date', 'location', 'organizer', 'game', 'attendees')
        depth = 2