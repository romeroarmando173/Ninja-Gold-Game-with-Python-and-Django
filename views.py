
from django.shortcuts import render, redirect
import random


def index(request): 
    if not "gold" in request.session:                 # if no gold activity, then set to 0
        request.session["gold"] = 0        

    if not "activities" in request.session:    # if no activities, set array to blank
        request.session["activities"] = []     # activities is a reserved word for session                  
    return render(request,"al_ninjagoldgame/index.html")   # this is connected to urls pattern variable in urls.py



def find_gold(request):   
    if request.method == 'POST':
        if request.POST["building"] == "farm":  #if client clicent cliks on this button
            rand10To20 = random.randint(10,20)    #rand10t020 is just a dummy
            request.session["gold"] += rand10To20      # adding last number to new numebr
            request.session["activities"].append(f"Entered a farm and win {rand10To20} gold")
        
        if request.POST["building"] == "cave":
            rand10To20 = random.randint(5,10)
            request.session["gold"] += rand10To20
            request.session["activities"].append(f"Entered a cave and win {rand10To20} gold") 

                                                                
        if request.POST["building"] == "house":
            rand10To20 = random.randint(2,5)
            request.session["gold"] += rand10To20
            request.session["activities"].append(f"Entered a house and win {rand10To20} gold")    
        
        if request.POST["building"] == "casino":
            rand10To20 = random.randint(-50,50)
            request.session["gold"] += rand10To20
            request.session["activities"].append(f"Entered a casino and win {rand10To20} gold")                              #????
        return redirect("/")