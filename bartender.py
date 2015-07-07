questions = {
    "strong": "Do ye like yer drinks strong?",
    "salty": "Do ye like it with a salty tang?",
    "bitter": "Are ye a lubber who likes it bitter?",
    "sweet": "Would ye like a bit of sweetness with yer poison?",
    "fruity": "Are ye one for a fruity finish?"
}

ingredients = {
    "strong": ["glug of rum", "slug of whisky", "splash of gin"],
    "salty": ["olive on a stick", "salt-dusted rim", "rasher of bacon"],
    "bitter": ["shake of bitters", "splash of tonic", "twist of lemon peel"],
    "sweet": ["sugar cube", "spoonful of honey", "spash of cola"],
    "fruity": ["slice of orange", "dash of cassis", "cherry on top"]
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
            
    print boolResponses

bartender()



#drink function

# def makeDrink(bartender):
#     drink = []
#     for i in ingredients:
        
    
