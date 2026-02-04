from django.test import TestCase
from .models import Team, UserProfile, Activity, Workout, Leaderboard

class ModelSmokeTest(TestCase):
    def test_team_create(self):
        t = Team.objects.create(name='Test Team')
        self.assertEqual(str(t), 'Test Team')
    def test_userprofile_create(self):
        t = Team.objects.create(name='T')
        u = UserProfile.objects.create(name='U', email='u@test.com', team=t)
        self.assertEqual(str(u), 'U')
    def test_activity_create(self):
        t = Team.objects.create(name='T')
        u = UserProfile.objects.create(name='U', email='u@test.com', team=t)
        a = Activity.objects.create(user=u, type='Run', duration=10, date='2026-02-04')
        self.assertEqual(str(a), 'Run - U')
    def test_workout_create(self):
        t = Team.objects.create(name='T')
        w = Workout.objects.create(name='W', description='desc')
        w.suggested_for.set([t])
        self.assertEqual(str(w), 'W')
    def test_leaderboard_create(self):
        t = Team.objects.create(name='T')
        l = Leaderboard.objects.create(team=t, points=5)
        self.assertEqual(str(l), 'T - 5 pts')
