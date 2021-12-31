print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")

combined_string = name1 + name2
lowercase_string = combined_string.lower()

t = lowercase_string.count('t')
r = lowercase_string.count('r')
u = lowercase_string.count('u')
e = lowercase_string.count('e')

true = t + r + u + e

l = lowercase_string.count('l')
o = lowercase_string.count('o')
v = lowercase_string.count('v')
e = lowercase_string.count('e')

love = l + o + v + e

lovescore = str (true) + str(love)

if int(lovescore) < 10 or int(lovescore) > 90:
    print (f"Your score is {lovescore}, you go together like coke and mentos.")
elif int(lovescore) >= 40 and int(lovescore) <=50:
    print (f"Your score is {lovescore}, you are alright together.")
else:
    print (f"Your score is {lovescore}.")