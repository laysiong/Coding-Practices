print("Numbers of week left if we live until 90 years old")

your_age = input("What is your age? \n")

diff_age = 90 - int(your_age)
num_of_weeks = (diff_age * 52)
print(f"You have {int(num_of_weeks)} weeks left")
