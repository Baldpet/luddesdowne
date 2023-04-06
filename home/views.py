from django.conf import settings
from django.shortcuts import render
from socialevent.models import Events
from .models import Fixtures, FixtureUpdate, Clubs
from datetime import date, datetime
import requests

# Create your views here.

def home(request):
    today = date.today()
    fixturesFirst = Fixtures.objects.filter(luddes_team="1st XI").exclude(match_date__lt=today).exclude(status='Deleted').order_by('match_date')[:1]
    fixturesSecond = Fixtures.objects.filter(luddes_team="2nd XI").exclude(match_date__lt=today).exclude(status='Deleted').order_by('match_date')[:1]
    fixturesLadies = Fixtures.objects.filter(luddes_team="Womens 1st XI").exclude(match_date__lt=today).exclude(status='Deleted').order_by('match_date')[:1]
    events = Events.objects.exclude(date__lt=today).order_by('date')[:3]
    context = {
        'events': events,
        'fixturesFirst': fixturesFirst,
        'fixturesSecond': fixturesSecond,
        'fixturesLadies': fixturesLadies
    }
    return render(request, 'home/index.html', context)

def contact(request):
    return render(request, 'home/contact.html')

def fixtures(request):
    today = date.today()
    #Gets the info from Play Cricket API
    dataJSON = requests.request('GET', f'https://play-cricket.com/api/v2/matches.json?&site_id=7938&season=2023&api_token={settings.PLAY_CRICKET_API}')
    data = dataJSON.json()

    #Pulls the last update that we have done to the fixtures
    lastServerUpdateQS = FixtureUpdate.objects.all().order_by('-id')[:1]
    hasUpdate = False

    #Changes the Queryset for the fixture into a Date format that we can use to compare agains the JSON data for the fixtures
    if lastServerUpdateQS:
        lastServerUpdate = lastServerUpdateQS.values()[0]['last_update']
        hasUpdate = True

    for matches in data['matches']:
        if matches['home_team_name'] == "Luddesdowne CC":
            luddesTeam = "home"
        else:
            luddesTeam = "away"
        #Checks to see if there has ever been an update before
        if hasUpdate:     #has a previous update date so we can filter which fixtures need to be updated
            lastUpdate = datetime.strptime(matches['last_updated'], "%d/%m/%Y").date()
            if lastUpdate > lastServerUpdate:
                clubCreation(matches)
                fixtureCreation(matches, True, luddesTeam)
        else:
            #first time the function has run - therefore we can just add all the information
            clubCreation(matches)
            fixtureCreation(matches, False, luddesTeam)

    fixtureUpdate = FixtureUpdate(
        last_update = today
    )
    fixtureUpdate.save()

    template = 'home/test.html'
    context = {
        'data': data,
    }
    return render(request, template, context)

#Checks if the club exists in the database - If they do not it adds them to the Clubs database
def clubCreation(fixture):
    if not Clubs.objects.filter(play_cricket_ID=fixture['home_club_id']).exists():
        newClub = Clubs(
            name=fixture['home_club_name'],
            play_cricket_ID=int(fixture['home_club_id']),
        )
        newClub.save()
    if not Clubs.objects.filter(play_cricket_ID=fixture['away_club_id']).exists():
        newClub = Clubs(
            name=fixture['away_club_name'],
            play_cricket_ID=int(fixture['away_club_id']),
        )
        newClub.save()
    return 
#Checks if the fixture exists in the database - If they do not it adds them to the Fixtures Database
def fixtureCreation(fixture, update , luddesTeam):
    if update:
        #Get the current object in the database
        newFixture = Fixtures.objects.get(play_cricket_fixture_ID=fixture['id'])

        #update the object with the newly gathered info
        newFixture.play_cricket_fixture_ID = int(fixture['id'])
        newFixture.luddes_team = fixture[f'{luddesTeam}_team_name']
        newFixture.last_updated = datetime.strptime(fixture['last_updated'], "%d/%m/%Y").date()
        newFixture.status = fixture['status']
        newFixture.match_date = datetime.strptime(fixture['match_date'], "%d/%m/%Y").date()
        newFixture.match_time = fixture['match_time']
        newFixture.ground_name =  fixture['ground_name']
        newFixture.ground_ID = fixture['ground_id']
        newFixture.home_club_id = Clubs.objects.get(play_cricket_ID=fixture['home_club_id'])
        newFixture.away_club_id = Clubs.objects.get(play_cricket_ID=fixture['away_club_id'])
        newFixture.competition_type = fixture['competition_type']

        #save the new object
        newFixture.save()
    else:
        if not Fixtures.objects.filter(play_cricket_fixture_ID=fixture['id']).exists():
            newFixture = Fixtures(
                play_cricket_fixture_ID = int(fixture['id']),
                luddes_team = fixture[f'{luddesTeam}_team_name'],
                last_updated = datetime.strptime(fixture['last_updated'], "%d/%m/%Y").date(),
                status = fixture['status'],
                match_date = datetime.strptime(fixture['match_date'], "%d/%m/%Y").date(),
                match_time = fixture['match_time'],
                ground_name =  fixture['ground_name'],
                ground_ID = fixture['ground_id'],
                home_club_id = Clubs.objects.get(play_cricket_ID=fixture['home_club_id']),
                away_club_id = Clubs.objects.get(play_cricket_ID=fixture['away_club_id']),
                competition_type = fixture['competition_type'],
            )
            newFixture.save()
    return 