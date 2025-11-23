#################################################
#KRAM- Keyword Recognition And Matching AI      #
#                                               #
#Under MIT license, feel free to fork and modify#
#                                               #
#Copyright 2025 CoolGuy158-Git                  #
#################################################
#_________________________________________________#
#KRAM barebones Ver, GUI version under development#

import random
print("K  KKKKK   RRRRRR         A         MM           MM")
print("K K        R     R       A A        M M         M M")
print("KK         R     R      A   A       M  M       M  M")
print("KK         RRRRRR      A     A      M   M     M   M")
print("K K        RR         AAAAAAAAA     M     M  M    M")
print("K  K       R R       A         A    M       M     M")
print("K   K      R  R     A           A   M       M     M")
print("K    K     R   R   A             A  M       M     M")
print()
keywords_negative = ["bad", "depressed", "sad", "hurts", "hurt", "unhappy"]
keywords_positive = ["happy", "amazing", "good", "jolly", ]
keywords_neutral = ["meh", "ok", "yes"]
keywords_greetings = ["hello", "hey", "hi", ]
keywords_aggressive = ["hate", "sybau", "stfu", "shut", "stupid", "idiot", "fat", "stupid", "unworthy", "clueless"]
keywords_goodbye = ["goodbye", "bye"]
keywords_serious = ["suicide"]
keywords_unusual = ["unusual", "alien", "ufo", "weird"]
keywords_celebration = ["yay!", "yippee", "birthday", "wedding", "lottery"]
keywords_special = ["KRAM"]
keywords_political = ["biden", "trump", "corruption", "vote", "war"]
keywords_memes = ["doge", "memes", "67", "69",]
keywords_spec1 = ["dawg"]
keywords_spec2 = ["bro"]
keywords_spec3 = ["bruh"]
keywords_spec4 = ["dude"]
keywords_quesgreet = ["wassup", "whatsup", "sup"]
keywords_disappointed = ["aw", "aww", "awww", "awwww", "disappointed"]
keywords_unknown = []
# TODO add more keywords so its a bit smarter

categories = {
    "aggressive": keywords_aggressive,
    "negative": keywords_negative,
    "positive": keywords_positive,
    "neutral": keywords_neutral,
    "greetings": keywords_greetings,
    "goodbye": keywords_goodbye,
    "serious": keywords_serious,
    "unusual": keywords_unusual,
    "celebration": keywords_celebration,
    "special": keywords_special,
    "unknown": keywords_unknown,
    "political": keywords_political,
    "memes": keywords_memes,
    "spec1": keywords_spec1,
    "spec2": keywords_spec2,
    "spec3": keywords_spec3,
    "spec4": keywords_spec4,
    "quesgreet": keywords_quesgreet,
    "disappointed": keywords_disappointed,
}

priority_order = ["serious", "aggressive","political", "negative", "positive", "celebration","disappointed", "neutral", "greetings", "spec1", "spec2", "spec3", "spec4","quesgreet", "goodbye", "unusual","memes", "special"]

responses = {
    "negative": ["Tell me more, I would love to help",
                 "Would you like to tell me more about why you're feeling like that?",
                 "It's fine, I'm here for you, tell me more", ],
    "positive": ["WOW! What happened?", "Tell me more, I'm excited to know why you are so happy!",
                 "Really?? Why?"],
    "neutral": ["Tell me more...", "Ok", "How are you doing?", "I would like to know more!"],
    "aggressive": ["No need to be angry, tell me why you're feeling like that", "Ok, chill", "I'm sorry"],
    "greetings": ["hello", "hey", "hi"],
    "goodbye": ["bye", "goodbye", "See you later ig"],
    "serious": [
        "Im so sorry you're feeling like that, help is available, please contact your nearest therapist YOU ARE NOT ALONE!"],
    "unusual": ["That's so weird...", "I don't understand...", "How weird is that?"],
    "celebration": ["Yay! im so happy for you!", "Lets go!", "That is so cool!"],
    "special": ["Wassup?", "How are you doing?", "Yeh?", "What?"],
    "unknown": ["you please clarify?", "I dont understand...", "unfortunately I cannot understand what you're saying would you please clarify?","Please clarify", "Can you say that again but differently?", "what?", "WHAT?", "wat", "Bro what?", "Erm excuse me but what???", "Yo what???"],
    "political": ["We getting political now?", "Im sorry but im not into politics", "Yea no i aint talking talking about that"],
    "memes": ["Yo you like memes to!?", "Ah you're a gen-z or gen-a i believe", "memes are cool and i think you agree", "Nice memes am I right or am I right?"],
    "spec1": ["sup dawg?", "yea dawg?", "Dawg? yea dawg?"],
    "spec2": ["yea bro?", "sup bro", "k bro"],
    "spec3": ["Yea bruh?", "k bruh", "sup bruh"],
    "spec4": ["What dude?", "yea dude?"],
    "quesgreet": ["Im good", "Not much", "Meh im fine"],
    "disappointed": ["aww what happened?", "What happened?", "Aww its fine"]
}

while True:

    user_input = input("You: ").lower()

    words = user_input.split()
    detected_category = "unknown"

    for category in priority_order:
        if any(word in categories[category] for word in words):
            detected_category = category
            break

    print(">>>", random.choice(responses[detected_category]))