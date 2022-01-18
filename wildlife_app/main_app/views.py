from django.shortcuts import render
from .models import Animal
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .forms import FeedingForm
from django.shortcuts import render, redirect

# # Create your views here.

# class Animal:  # Note that parens are optional if not inheriting from another class
#   def __init__(self, name, sort, description):
#     self.name = name 
#     self.breed = sort 
#     self.description = description
  

# animals = [
#   Animal('Bonbon', 'Cheetah', 'foul little demon'),
#   Animal('Suzie', 'tortoise', 'diluted tortoise shell'),
#   Animal('Lerly', 'Raven',  'black as night')
# ]


def home(request):
    return render(request, 'homepage.html')

def about(request):
    return render(request, 'about.html')

def animals_index(request):
  animals = Animal.objects.all()
  return render(request, 'animals/index.html', { 'animals': animals})

def animals_detail(request, animal_id):
  animal = Animal.objects.get(id=animal_id)
  feeding_form = FeedingForm()
  return render(request, 'animals/detail.html', { 'animal': animal, 'feeding_form': feeding_form })

def add_feeding(request, animal_id):
  print("add_feeding")
  form = FeedingForm(request.POST)
  # validate the form
  if form.is_valid():
    # don't save the form to the db until it
    # has the cat_id assigned
    new_feeding = form.save(commit=False)
    new_feeding.animal_id = animal_id
    new_feeding.save()
  return redirect('animals', animal_id=animal_id)

class AnimalCreate(CreateView):
  model = Animal
  fields = '__all__'
  success_url = '/animals/'

class AnimalUpdate(UpdateView):
  model = Animal
  fields = ['name', 'breed', 'description']

class AnimalDelete(DeleteView):
  model = Animal
  success_url = '/animals/'

