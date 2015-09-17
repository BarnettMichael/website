from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User as authUser


class User(models.Model):
    """
    Class to model each user
    Each user has:
    name
    password
    current points scored
    collection of guess objects

    method to make a guess
    """
    user = models.OneToOneField(authUser)

    name = models.CharField(max_length=200)
    points = models.PositiveSmallIntegerField(default=0)

    def __str__(self):
        return self.name

class Post(models.Model):
    author = models.ForeignKey(User)
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(
        default=timezone.now)
    published_date = models.DateTimeField(
        blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title

class Team(models.Model):
    name = models.CharField(max_length=200, null=True, unique=True)

    def __str__(self):
        return self.name

class Match(models.Model):
    """
    Model for each match
    Each match has:
    two teams as strings
    a time as a datetime
    a winning team as string
    and a final points difference as an int
    """
    time = models.DateTimeField()
    home_team = models.ForeignKey(Team, null=True, related_name='home_team')
    away_team = models.ForeignKey(Team, null=True, related_name='away_team')
    winning_team = models.ForeignKey(Team, blank=True, null=True)
    points_difference = models.PositiveSmallIntegerField(blank=True, null=True)

    def __str__(self):
        return str(self.home_team) + " vs " + str(self.away_team)


class Guess(models.Model):
    """
    Model for each Users guesses
    """

    match = models.ForeignKey(Match)
    user = models.ForeignKey(User)
    points_difference = models.PositiveSmallIntegerField(blank=True, null=True)
    winning_team = models.ForeignKey(Team, blank=True, null=True)

    def __str__(self):
        return str(self.user) + ": " + str(self.match)