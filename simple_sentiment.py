from textblob import TextBlob

repeat = True
while repeat == True:
  # 1. Ask an open ended question
  print('What do you think about Computers?')
  ans = input('> ')
  blob = TextBlob(ans)

  print(blob.polarity) #- 1 to 1

  # 3. Respond appropriately to positive and negative sentiment
  if blob.polarity > 0.0:
    print('This is a positive response')
  else:
    print('This is a negative response')

  print('Would you like to continue?')
  ans = input('> ')
  if ans == 'no':
    repeat = False

print('Thanks for using')
