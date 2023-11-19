##Caculate BMI

height = input('What is your height(Metre)?\n')
weight = input('What is your weight(Kg)?\n')

BMI = round(float(weight)/(float(height)**2),0)

print("Your BMI is " + str(BMI))