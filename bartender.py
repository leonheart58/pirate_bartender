import random

questions = {
    "strong": "Do ye like yer drinks strong?",
    "salty": "Do ye like it with a salty tang?",
    "bitter": "Are ye a lubber who likes it bitter?",
    "sweet": "Would ye like a bit of sweetness with yer poison?",
    "fruity": "Are ye one for a fruity finish?",
    "savory": "Do you like savory?"
}

ingredients = {
    "strong": ["glug of rum", "slug of whisky", "splash of gin"],
    "salty": ["olive on a stick", "salt-dusted rim", "rasher of bacon"],
    "bitter": ["shake of bitters", "splash of tonic", "twist of lemon peel"],
    "sweet": ["sugar cube", "spoonful of honey", "spash of cola"],
    "fruity": ["slice of orange", "dash of cassis", "cherry on top"],
    "savory": ["chips","noodles"]
}

responses = {}

def bartender():
    for i in questions:
        responses[i] = raw_input(questions[i])
 

    boolResponses = {}
    for i in responses:
        if responses[i] == 'yes':
            boolResponses[i] = True
        elif responses[i] == 'no':
            boolResponses[i] = False
        else:
            boolResponses[i] = "Not an acceptable answer"
          
    #print boolResponses  
    return boolResponses



def makeDrink(boolResponses):
    recipe = []
    for i in boolResponses:
        if boolResponses[i] == True:
            recipe.append(random.choice(ingredients[i]))
    print recipe

    
if __name__ == '__main__':
        
    drink = bartender()
    print drink
    makeDrink(drink)