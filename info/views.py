from django.shortcuts import render
import json

def all_animals(request):
    #data = get_animal_data()
    #return render(request, 'animals_list.html', data)
    #directly:
    return render(request, 'animals_list.html', get_animals_data())

def single_animal(request, id):
    #printing to the cmd to check it (page will crush as we didnt send a response yet)
    #print("you requested animal number", id)
    #brcause in this function we also want to read the animals data, it's better to create a specific 
    # function for that (get_animal_data fun below)  
    data = get_animals_data() #before if(!)
    if id > 0 and id <= len(data['animals']): 
        single_animal = data['animals'][id-1] # getting the first animal (lists: position 0)
        #print(single_animal)
        return render(request, 'animals_detail.html', {'animal': single_animal})

def get_animals_data(): #doesnt take anything
    #open the file (don't forget to import json)
    with open('animals.json', 'r') as f:
        #read all animals into a dictionary
        data = json.load(f)
    #print(data) we get the data in the cmd but the page crushed as we didnt return a response
    #returning a response in the other functions, as this function is only purpose is for getting data
    return data
