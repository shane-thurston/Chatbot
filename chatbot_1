import random
# Sentences we'll respond with if the user greeted us
GREETING_KEYWORDS = ("hello", "hi", "greetings", "sup", "what's up",)

GREETING_RESPONSES = ["'sup bro", "hey", "*nods*", "hey you get my snap?"]

def check_for_greeting(sentence):
    for word in sentence.split():
        if word.lower() in GREETING_KEYWORDS:
          return random.choice(GREETING_RESPONSES)

chat = input('> ')
while chat != 'exit':
  print(check_for_greeting(chat))
  chat = input('> ')
