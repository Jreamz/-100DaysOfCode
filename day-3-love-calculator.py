## JREAMZ VERSION ##
####################

print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")

lower_name1 = name1.lower()
lower_name2 = name2.lower()

t_counter = lower_name1.count("t") + lower_name2.count("t")
r_counter = lower_name1.count("r") + lower_name2.count("r")
u_counter = lower_name1.count("u") + lower_name2.count("u")
e_counter = lower_name1.count("e") + lower_name2.count("e")

true_total = str(t_counter + r_counter + u_counter + e_counter)

l_counter = lower_name1.count("l") + lower_name2.count("l")
o_counter = lower_name1.count("o") + lower_name2.count("o")
v_counter = lower_name1.count("v") + lower_name2.count("v")
e_counter = lower_name1.count("e") + lower_name2.count("e")

love_total = str(l_counter + o_counter  + v_counter + e_counter)

true_love_str = true_total + love_total

true_love = int(true_love_str)

if true_love <= 10 or true_love > 90:
  print(f"Your score is {true_love}, you go together like coke and mentos.")
elif true_love >= 40 and true_love <= 50:
  print(f"Your score is {true_love}, you are alright together.")
else:
  print(f"Your score is {true_love}.")


## INSTRUCTOR VERSION ##
########################

print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")

combined_string = name1 + name2
lower_case_string = combined_string.lower()

t = lower_case_string.count("t")
r = lower_case_string.count("r")
u = lower_case_string.count("u")
e = lower_case_string.count("e")

l = lower_case_string.count("l")
o = lower_case_string.count("o")
v = lower_case_string.count("v")
e = lower_case_string.count("e")

true = t + r + u + e
love = l + o + v + e

love_score = int(str(true) + str(love))

if (love_score < 10) or (love_score > 90):
  print (f"Your love score is {love_score}, you go together like coke and mentos.")
elif (love_score >= 40) and (love_score <=50):
  print (f"Your score is {love_score}, you are alright together.")
else:
  print(f"Your score is {love_score}.")
