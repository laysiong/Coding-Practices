print("Love Calculator")

name1 = input("What is your name? \n")
name2 = input("What is their name? \n")

combine_name = name1.lower()+name2.lower()

t = combine_name.count("t")
r = combine_name.count("r")
u = combine_name.count("u")
e = combine_name.count("e")

l = combine_name.count("l")
o = combine_name.count("o")
v = combine_name.count("v")
e = combine_name.count("e")

first_digit= t+r+u+e 
second_digit=l+o+v+e
score = str(first_digit)+str(second_digit)
text ="."

if int(score)< 10 or int(score) >90:
    text =', you go together like coke and mentos'
elif int(score)> 40 and int(score) <50:
    text =', you are alright together'
else:
    text = text

print(f"Your score is {int(score)}{text}")