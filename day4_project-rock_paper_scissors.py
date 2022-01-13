import random
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#Write your code below this line 👇
print ("Welcome to Rock Paper Scissors Game!")
print ("You will be competing against the computer!\nWish you luck!")

print ("Rock, Paper, Scissors.")
yourchoice = int(input ("What is your choice? Type 0 for Rock, 1 for Paper, 2 for Scissors\n"))

if yourchoice >= 3 or yourchoice < 0:
  print ("You chose an invalid number. You lose!")
else:
  if yourchoice == 0:
    print (rock)
  elif yourchoice == 1:
    print (paper)
  else:
    print (scissors)

  computerchoice = random.randint(0,2)
  if computerchoice == 0:
    print ("Computer Chose: \n" + rock)
  elif computerchoice == 1:
    print ("Computer Chose: \n" + paper)
  else:
    print ("Computer Chose: \n" + scissors)

  if computerchoice == yourchoice:
    print ("It's a draw")
  elif (computerchoice == 0 and yourchoice == 1) or (computerchoice == 1 and yourchoice == 2) or (computerchoice == 2 and yourchoice == 0):
    print ("You win!") 
  else:
    print ("You lose") 
