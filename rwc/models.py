from django.db import models
from django.utils import timezone

class Post(models.Model):
    author = models.ForeignKey('auth.User')
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


class Person(models.Model):
    """
    Class to model each user
    Each user has:
    name
    password
    current points scored
    collection of guess objects

    method to make a guess
    """
    name = models.CharField(max_length=200)
    points = models.PositiveSmallIntegerField(default=0)

    def __str__(self):
        return self.name

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
    Model for each persons guesses
    """
    #def __init__(self, match):
    #    self.match = match

    match = models.ForeignKey(Match, null=True)
    user = models.ForeignKey(Person)  #takes a person many to one
    score_chosen = models.PositiveSmallIntegerField()
    team_chosen = models.ForeignKey(Team, null=True)

    def __str__(self):
        return str(self.user) + ": " + str(self.match)