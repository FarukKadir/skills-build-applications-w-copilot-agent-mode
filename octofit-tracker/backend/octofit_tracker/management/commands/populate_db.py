
from django.core.management.base import BaseCommand
from octofit_tracker.models import User, Team, Workout, Activity, Leaderboard
from pymongo import MongoClient

class Command(BaseCommand):
    help = 'Populate the octofit_db database with test data'

    def handle(self, *args, **kwargs):
        # Drop the entire database to avoid schema issues
        client = MongoClient('localhost', 27017)
        client.drop_database('octofit_db')

        # Teams
        marvel = Team.objects.create(name="Marvel", description="Marvel superheroes")
        dc = Team.objects.create(name="DC", description="DC superheroes")

        # Users
        users = [
            User(name="Spider-Man", email="spiderman@marvel.com", team=marvel),
            User(name="Iron Man", email="ironman@marvel.com", team=marvel),
            User(name="Wonder Woman", email="wonderwoman@dc.com", team=dc),
            User(name="Batman", email="batman@dc.com", team=dc),
        ]
        for user in users:
            user.save()

        # Workouts
        workouts = [
            Workout(name="Pushups", description="Upper body workout", difficulty="Easy"),
            Workout(name="Running", description="Cardio workout", difficulty="Medium"),
        ]
        for workout in workouts:
            workout.save()

        # Activities
        Activity.objects.create(user=users[0], workout=workouts[0], duration_minutes=30, calories_burned=200)
        Activity.objects.create(user=users[1], workout=workouts[1], duration_minutes=45, calories_burned=400)
        Activity.objects.create(user=users[2], workout=workouts[0], duration_minutes=25, calories_burned=180)
        Activity.objects.create(user=users[3], workout=workouts[1], duration_minutes=60, calories_burned=500)

        # Leaderboard
        Leaderboard.objects.create(team=marvel, total_points=600, rank=1)
        Leaderboard.objects.create(team=dc, total_points=680, rank=2)

        self.stdout.write(self.style.SUCCESS('octofit_db database populated with test data.'))
