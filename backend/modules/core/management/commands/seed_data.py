import random
from datetime import timedelta
from django.core.management.base import BaseCommand
from django.utils import timezone
from faker import Faker

from modules.authentication.models import CustomUser, ActivationToken
from modules.habits.models import Habit, Day
from modules.users.models import User, UserInfo, UserProfile

# Initialize Faker to generate random data
faker = Faker()

class Command(BaseCommand):
    help = 'Seed the database with habits, days, and tasks for users.'

    def handle(self, *args, **kwargs):

        self.stdout.write(self.style.SUCCESS('Seeding data...'))
        self.stdout.write(self.style.WARNING('Warning: This command is intended for development purposes only!'))

        # Number of users to create
        num_users = 10

        # Create users
        for i in range(num_users):
            email = f'user{i}@example.com'
            user = CustomUser.objects.create_user(
                email=email,
                password='password123',  # Simple password for testing purposes
                is_active=random.choice([True, False])  # Randomly set active or inactive
            )
            self.stdout.write(self.style.SUCCESS(f'Created user: {email}'))

            # Create an activation token for the user
            token_expiration = timezone.now() + timedelta(days=random.randint(1, 7))
            activation_token = ActivationToken.objects.create(
                user=user,
                expiration_date=token_expiration
            )
            self.stdout.write(self.style.SUCCESS(f'Created activation token for user: {email}'))

        self.stdout.write(self.style.SUCCESS('Seeding completed!'))

        self.stdout.write(self.style.SUCCESS('Seeding data...'))
        self.stdout.write(self.style.WARNING('Warning: This command is intended for development purposes only!'))

        # Fetch all users (assuming CustomUser is already populated)
        users = CustomUser.objects.all()

        # Number of habits and days to create
        num_habits_per_user = 3
        num_days_per_user = 5

        # Create habits for each user
        for user in users:
            # Create random habits for each user
            for _ in range(num_habits_per_user):
                habit_content = faker.sentence(nb_words=4)  # Generate random habit content
                habit = Habit.objects.create(
                    user=user,
                    content=habit_content
                )
                self.stdout.write(self.style.SUCCESS(f'Created habit for {user.email}: {habit_content}'))

            # Create random days and tasks for each user
            for day_offset in range(num_days_per_user):
                day_date = timezone.now().date() - timedelta(days=day_offset)
                day = Day.objects.create(
                    user=user,
                    date=day_date
                )
                self.stdout.write(self.style.SUCCESS(f'Created day for {user.email}: {day_date}'))

                # Tasks are automatically created in Day's save method, so we don't need to create them manually
                # But we can access them and mark some of them as done for testing purposes
                for task in day.tasks.all():
                    task.is_done = random.choice([True, False])  # Randomly mark tasks as done or not
                    task.save()
                    self.stdout.write(self.style.SUCCESS(f'Task for {user.email} on {day_date}: {task.content} - Done: {task.is_done}'))

        self.stdout.write(self.style.SUCCESS('Seeding completed!'))

        self.stdout.write(self.style.SUCCESS('Seeding data...'))

        # Number of users to create
        num_users = 10

        users = []

        # Create users, profiles, and info
        for i in range(num_users):
            # Create UserProfile
            user_profile = UserProfile.objects.create(
                is_dark_mode=random.choice([True, False]),
                is_private=random.choice([True, False])
            )

            # Create UserInfo
            user_info = UserInfo.objects.create(
                first_name=faker.first_name(),
                last_name=faker.last_name(),
                streak=random.randint(0, 100)
            )

            # Create User
            email = f'user{i}@example.com'
            user = User.objects.create(
                email=email,
                user_profile=user_profile,
                user_info=user_info
            )
            users.append(user)
            self.stdout.write(self.style.SUCCESS(f'Created user: {email}'))

        # Randomly assign friends to each user
        for user in users:
            # Select a subset of other users to be friends
            friends = random.sample([u for u in users if u != user], random.randint(0, 5))
            user.friends.set(friends)
            user.save()
            self.stdout.write(self.style.SUCCESS(f'Assigned friends for user: {user.email}'))

        self.stdout.write(self.style.SUCCESS('Seeding completed!'))