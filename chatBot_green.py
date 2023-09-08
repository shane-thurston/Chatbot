import random

pos_replies = [
  "I'm glad to hear you're having a good time!",
  "That's wonderful!",
  "It's great to know you're having a good time."
]

positive_words = ['good','great','amazing','well']

print("Hi there, my name is Eliza. What's your name?")
name = input('> ')
# 1. Personalised greeting
print(f'Hi there {name}, do you have a nickname?')
nName = input('> ')
if nName.lower() == 'no':
  nName = name
  print(f'Ok, I will call you {nName}')
  print('nice to meet you')
else:
  print(f'Nice to meet you {nName}')

print('Ready?')
# 2. Looping until the user decides to exit
line = input('> ')
while line:
  # 1. Ask an open ended question
  print("How are you feeling right now?")
  line = input('> ').lower()
  # 2. Check for user response. Exit if nothing is typed in
  if line:
    # 3. Simple response to user input
    for word in positive_words:
      if word in line:
        print('Im glad to hear it.')
    # 4. Basic social good feature
    print(random.choice(pos_replies))

print('Thanks for using')
