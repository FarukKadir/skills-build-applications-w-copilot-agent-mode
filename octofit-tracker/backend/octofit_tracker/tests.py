from django.test import TestCase
from .models import User, Team, Workout, Activity, Leaderboard

class ModelTests(TestCase):
    def setUp(self):
        self.team = Team.objects.create(name="Marvel", description="Marvel superheroes")
        self.user = User.objects.create(name="Spider-Man", email="spiderman@marvel.com", team=self.team)
        self.workout = Workout.objects.create(name="Pushups", description="Upper body workout", difficulty="Easy")
        self.activity = Activity.objects.create(user=self.user, workout=self.workout, duration_minutes=30, calories_burned=200)
        self.leaderboard = Leaderboard.objects.create(team=self.team, total_points=100, rank=1)

    def test_user_creation(self):
        self.assertEqual(self.user.name, "Spider-Man")
        self.assertEqual(self.user.team.name, "Marvel")

    def test_workout_creation(self):
        self.assertEqual(self.workout.name, "Pushups")

    def test_activity_creation(self):
        self.assertEqual(self.activity.user.email, "spiderman@marvel.com")
        self.assertEqual(self.activity.workout.name, "Pushups")

    def test_leaderboard_creation(self):
        self.assertEqual(self.leaderboard.team.name, "Marvel")
        self.assertEqual(self.leaderboard.rank, 1)
