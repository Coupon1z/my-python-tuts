import random

attempt= 1
maxattempt= 3
while attempt <=  maxattempt:
    guess= int(input('Please Enter your choice:'))
    computer=random.randint(1,100)
    print('You chose ',guess,'and Computer chose ',computer)
    if guess == computer:
      print('Congratulations! ,You WIN')
    elif guess < computer:
      print('Your guess is lower than our secret number')
    else:
        print('Your guess is higher than our secret number')
        
    attempt = attempt + 1
if  attempt >= maxattempt:
      print('Maximum attempt exceeded')
      
    