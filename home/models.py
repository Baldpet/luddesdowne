from django.db import models

# Create your models here.

class FixtureUpdate(models.Model):
    last_update = models.DateField()

    def __str__(self):
        return str(self.id)
    

class Clubs(models.Model):
    name = models.CharField(max_length=150)
    play_cricket_ID = models.IntegerField()
    team_badge = models.CharField(max_length=150, blank=True)
        
    def __str__(self):
        return self.name


class Fixtures(models.Model):
    play_cricket_fixture_ID = models.IntegerField()
    last_updated = models.DateField()
    status = models.CharField(max_length=50)
    luddes_team = models.CharField(max_length=50)
    match_date = models.DateField()
    match_time = models.CharField(max_length=50)
    ground_name = models.CharField(max_length=150)
    ground_ID = models.CharField(max_length=50)
    home_club_id = models.ForeignKey(Clubs, on_delete=models.CASCADE, related_name='home_club')
    away_club_id = models.ForeignKey(Clubs, on_delete=models.CASCADE, related_name='away_club')
    competition_type = models.CharField(max_length=150)

    def __str__(self):
        return str(self.play_cricket_fixture_ID)
    
