from django.shortcuts import render, redirect
from django.contrib import messages
from projectt.db_connect import get_db_connection  # Import your MongoDB connection
from pymongo import MongoClient
from bson import ObjectId
from django.conf import settings
import json


db=get_db_connection()
collection=db['login']

# View to handle login form

import requests
from django.http import JsonResponse

def get_recipe(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        ingredients = data.get('ingredients')

        # Call the Gemini API with the ingredients
        api_key = 'AIzaSyBOo7xZ6pMNKh94XvW8eQoX-8grj1NChdk'  # Replace with your actual API key
        api_url = 'https://api.gemini.com/v1/recipes/suggest'  # Replace with actual Gemini API endpoint
        
        # Prepare the request
        response = requests.post(api_url, json={'ingredients': ingredients}, headers={'Authorization': f'Bearer {api_key}'})

        if response.status_code == 200:
            result = response.json()
            if result:  # Assuming the API returns a dish suggestion
                dish = result['dish_name']  # Modify based on the actual response structure
                recipe = result['recipe_steps']  # Modify based on the actual response structure

                return JsonResponse({
                    'dish': dish,
                    'recipe': recipe
                })
            else:
                return JsonResponse({'error': 'No dish found based on the ingredients provided.'})

        return JsonResponse({'error': 'Failed to fetch data from the Gemini API.'})

    return JsonResponse({'error': 'Invalid request method.'})


def home(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        
        # Establish MongoDB connection
        db = get_db_connection()
        users_collection = db['logindata']
        
        
        # Check if the user exists in the database
        user = users_collection.find_one({'email': email})
        
        # Validate user credentials
        if user and user['password'] == password:  # In a real app, remember to hash passwords
            return redirect('homie')  # Redirect to the main page after successful login
        else:
            messages.error(request, 'Invalid login credentials. Please register if you haven\'t.')
            return redirect('home')  # Redirect back to the login page
        

    return render(request, 'index.html')

# View to handle user registration
def register(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')

        # Validate passwords
        if password != confirm_password:
            messages.error(request, "Passwords do not match.")
            return redirect('register')

        # Establish MongoDB connection
        db = get_db_connection()
        users_collection = db['logindata']

        # Check if the email already exists
        if users_collection.find_one({"email": email}):
            messages.error(request, "Email already exists. Please log in.")
            return redirect('register')

        # Insert the new user into the database
        users_collection.insert_one({
            "name": name,
            "email": email,
            "password": password  # Make sure to hash the password in a real application
        })

        messages.success(request, "Registration successful! Please log in.")
        return redirect('home')  # Redirect to login or home page after registration

    return render(request, 'register.html')
    


def homie(request):
    return render(request, 'homie.html')  # Correctly render the homie.html template


def ai(request):
    return render(request, 'ai.html')

def ap1(request):
    # Get MongoDB connection
    db = get_db_connection()
    collection = db['logindata']

    # Retrieve the Bruschetta recipe
    bruschetta_recipe = collection.find_one({'recipe_name': 'Bruschetta'})

    # Check if the recipe is found
    if bruschetta_recipe:
        context = {
            'recipe_name': bruschetta_recipe['recipe_name'],
            'ingredients': bruschetta_recipe['ingredients'],
            'instructions': bruschetta_recipe['instructions']
        }
    else:
        context = {
            'error': 'Recipe not found'
        }

    return render(request, 'ap1.html', context)

def ap2(request):
    # Get MongoDB connection
    db = get_db_connection()
    collection = db['logindata']

    # Retrieve the Bruschetta recipe
    mozzarella_sticks_recipe = collection.find_one({'recipe_name': 'Mozzarella Sticks'})

    # Check if the recipe is found
    if mozzarella_sticks_recipe:
        context = {
            'recipe_name': mozzarella_sticks_recipe['recipe_name'],
            'ingredients': mozzarella_sticks_recipe['ingredients'],
            'instructions': mozzarella_sticks_recipe['instructions']
        }
    else:
        context = {
            'error': 'Recipe not found'
        }

    return render(request, 'ap2.html', context)

def ap3(request):
    # Get MongoDB connection
    db = get_db_connection()
    collection = db['logindata']

    # Retrieve the Bruschetta recipe
    recipe = collection.find_one({'recipe_name': 'Spring Rolls'})

    # Check if the recipe is found
    if recipe:
        context = {
            'recipe_name': recipe['recipe_name'],
            'ingredients': recipe['ingredients'],
            'instructions': recipe['instructions']
        }
    else:
        context = {
            'error': 'Recipe not found'
        }

    return render(request, 'ap3.html', context)



def ap4(request):
    # Get MongoDB connection
    db = get_db_connection()
    collection = db['logindata']

    # Retrieve the Bruschetta recipe
    recipe = collection.find_one({'recipe_name': 'Chicken Wings'})

    # Check if the recipe is found
    if recipe:
        context = {
            'recipe_name': recipe['recipe_name'],
            'ingredients': recipe['ingredients'],
            'instructions': recipe['instructions']
        }
    else:
        context = {
            'error': 'Recipe not found'
        }

    return render(request, 'ap4.html', context)




def ap7(request):
    # Get MongoDB connection
    db = get_db_connection()
    collection = db['logindata']

    # Retrieve the Bruschetta recipe
    recipe = collection.find_one({'recipe_name': 'Paneer Tikka'})

    # Check if the recipe is found
    if recipe:
        context = {
            'recipe_name': recipe['recipe_name'],
            'ingredients': recipe['ingredients'],
            'instructions': recipe['instructions']
        }
    else:
        context = {
            'error': 'Recipe not found'
        }

    return render(request, 'ap7.html', context) 

def yours(request):
    return render(request, 'yours.html')