from django.contrib import admin
from .models import Fixtures, FixtureUpdate, Clubs

# Register your models here.

admin.site.register(FixtureUpdate)
admin.site.register(Fixtures)
admin.site.register(Clubs)