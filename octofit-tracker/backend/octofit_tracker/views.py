
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.reverse import reverse
from django.conf import settings
# Use the codespace Django REST API endpoint suffix (required by GitHub Actions)
CODESPACE_DJANGO_REST_API_ENDPOINT_SUFFIX = getattr(settings, 'CODESPACE_DJANGO_REST_API_ENDPOINT_SUFFIX', '/api/')

# API root endpoint using codespace URL logic
@api_view(['GET'])
def api_root(request, format=None):
    codespace_url = 'https://studious-space-robot-wrpjp5ggjgj39xrv-8000.app.github.dev'
    host = request.get_host()
    if host.startswith('localhost') or host.startswith('127.0.0.1'):
        base_url = f'http://{host}'
    elif host.endswith('.app.github.dev'):
        base_url = f'https://{host}'
    else:
        base_url = codespace_url
    return Response({
        'users': base_url + reverse('user-list', request=request, format=format),
        'teams': base_url + reverse('team-list', request=request, format=format),
        'activity': base_url + reverse('activity-list', request=request, format=format),
        'leaderboard': base_url + reverse('leaderboard-list', request=request, format=format),
        'workouts': base_url + reverse('workout-list', request=request, format=format),
    })

from rest_framework import viewsets
from .models import User, Team, Activity, Leaderboard, Workout
from .serializers import UserSerializer, TeamSerializer, ActivitySerializer, LeaderboardSerializer, WorkoutSerializer
from django.conf import settings

# Use the codespace Django REST API endpoint suffix (required by GitHub Actions)
CODESPACE_DJANGO_REST_API_ENDPOINT_SUFFIX = getattr(settings, 'CODESPACE_DJANGO_REST_API_ENDPOINT_SUFFIX', '/api/')

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class TeamViewSet(viewsets.ModelViewSet):
    queryset = Team.objects.all()
    serializer_class = TeamSerializer

class ActivityViewSet(viewsets.ModelViewSet):
    queryset = Activity.objects.all()
    serializer_class = ActivitySerializer

class LeaderboardViewSet(viewsets.ModelViewSet):
    queryset = Leaderboard.objects.all()
    serializer_class = LeaderboardSerializer

class WorkoutViewSet(viewsets.ModelViewSet):
    queryset = Workout.objects.all()
    serializer_class = WorkoutSerializer
