from textblob import TextBlob

repeat = True
while repeat == True:
  # 1. Ask an open ended question
  print('What do you think about Computers?')
  ans = input()
  blob = TextBlob(ans)

  print(blob.polarity) #- 1 to 1

  # 3. Respond appropriately to positive and negative sentiment
  if blob.polarity < -0.5:
    print('Less than -0.5')
  elif blob.polarity < -0.1:
    print('Less than -0.1')
  elif blob.polarity >= -0.1 and blob.polarity < 0.1:
    print('Greater than -0.1 and less than 0.1')
  elif blob.polarity >= 0.1 and blob.polarity < 0.5:
    print('Greater than 0.1 and less than 0.5')
  else:
    print('Greater than or equal 0.5')

  ans = input('Would you like again')
  if ans == 'no':
    repeat = False

print('Thanks for using')
