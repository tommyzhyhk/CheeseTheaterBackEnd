from django.contrib import admin
from movieshow.models import Movie,Theater,MovieShip
class MovieshipInline(admin.TabularInline):
      model=MovieShip
      extra=1


class MovieAdmin(admin.ModelAdmin):
   list_display=('name','image','detail','money','year')
   search_fields=['name','detail']
   inlines=(MovieshipInline,)

class TheaterAdmin(admin.ModelAdmin):
   list_dispaly=('name',)
   inlines=(MovieshipInline,)
admin.site.register(Movie,MovieAdmin)
admin.site.register(Theater,TheaterAdmin)



# Register your models here.
