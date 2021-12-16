from django.shortcuts import render
from django.views import generic
from .models import PC, Workplace, Room, Floor, Building

def index(request):
    num_pc = PC.objects.all().count()
    num_rooms = Room.objects.all().count()
    num_workplaces = Workplace.objects.all().count()
    num_floors = Floor.objects.all().count()
    num_buildings = Building.objects.all().count()

    return render(
        request,
        'index.html',
        context = {'num_pc':num_pc,'num_rooms':num_rooms,'num_workplaces': num_workplaces ,'num_floors':num_floors,'num_buildings':num_buildings}
    )

class PCListView(generic.ListView):
    model = PC

class PCDetailView(generic.DetailView):
    model = PC
# Create your views here.