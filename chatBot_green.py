import random

pos_replies = [
  "I'm glad to hear you're having a good time!",
  "That's wonderful!",
  "It's great to know you're having a good time."
]

positive_words = ['good','great','amazing','well']

print("Hi there, my name is Eliza. What's your name?")
name = input('> ')
print(f'Hi there {name}, do you have a nickname?')
nName = input('> ')
if nName.lower() == 'no':
  nName = name
  print(f'Ok, I will call you {nName}')
  print('nice to meet you')
else:
  print(f'Nice to meet you {nName}')

repeat = True
while repeat == True:
  # 1. Ask an open ended question
  print("How are you feeling right now?")
  ans = input('> ').lower()
  for word in positive_words:
    if word in ans:
      print('Im glad to hear it.')
  print(random.choice(pos_replies))

  print('Would you like to continue?')
  ans = input('> ').lower()
  if ans == 'no':
    repeat = False

print('Thanks for using')
