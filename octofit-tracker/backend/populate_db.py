import os
import django
from bson import ObjectId

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'octofit_tracker.settings')
django.setup()

from octofit_tracker.models import User, Team, Activity, Leaderboard, Workout

# Clear existing data
User.objects.all().delete()
Team.objects.all().delete()
Activity.objects.all().delete()
Leaderboard.objects.all().delete()
Workout.objects.all().delete()

# Add test data
users = [
    User(_id=ObjectId(), username='john_doe', email='john@example.com', password='password123'),
    User(_id=ObjectId(), username='jane_doe', email='jane@example.com', password='password123')
]
User.objects.bulk_create(users)

teams = [
    Team(_id=ObjectId(), name='Team Alpha', members=[users[0]]),
    Team(_id=ObjectId(), name='Team Beta', members=[users[1]])
]
Team.objects.bulk_create(teams)

activities = [
    Activity(_id=ObjectId(), user=users[0], activity_type='Running', duration='00:30:00'),
    Activity(_id=ObjectId(), user=users[1], activity_type='Cycling', duration='01:00:00')
]
Activity.objects.bulk_create(activities)

leaderboard = [
    Leaderboard(_id=ObjectId(), user=users[0], score=100),
    Leaderboard(_id=ObjectId(), user=users[1], score=150)
]
Leaderboard.objects.bulk_create(leaderboard)

workouts = [
    Workout(_id=ObjectId(), name='Morning Run', description='A quick morning run to start the day'),
    Workout(_id=ObjectId(), name='Evening Yoga', description='Relaxing yoga session in the evening')
]
Workout.objects.bulk_create(workouts)

print("Test data has been populated successfully.")
