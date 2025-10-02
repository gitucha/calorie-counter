from django.shortcuts import render
from .models import Food

# Create your views here.
def index(request):
    context = {
        'message': 'Welcome to the Calorie Tracker App!'
    }
    return render(request, 'index.html', context)

def view_food(request):
    foods = Food.objects.all()
    total_calories = sum(food.calories for food in foods)
    context = {
        'foods': foods,
        'total_calories': total_calories
    }
    return render(request, 'view_food.html', context)

def add_food(request):
    if request.method == 'POST':
        food_item = request.POST.get('food_item')
        calories = request.POST.get('calories')
        
        Food.objects.create(name=food_item, calories=calories)
        context = {
            'message': f'Added {food_item} with {calories} calories.'
        }
    
    return render(request, 'add_food.html')

def remove_food(request, food_id):
    Food.objects.filter(id=food_id).delete()
    context = {
        'message': f'Removed {Food.name} with {Food.calories} .'
    }
    return render(request, 'remove_food.html', context)

def calculate_total(request):
    
    total_calories = sum(food.calories for food in Food.objects.all())
    context = {
        'total_calories': total_calories
    }
    return render(request, 'total_calories.html', context)

def reset_calories(request):
    Food.objects.all().delete()
    context = {
        'message': 'Calorie tracker has been reset.'
    }
    return render(request, 'reset_calories.html', context)