# User inputs height and weight
# Calculate BMI using the inputs

# BMI = weight / (height ** 2)

height = float(input("How tall are you (in m)? "))
weight = int(input("How much do you weigh (in kgs)? "))

bmi = weight / (height ** 2)

print(bmi)
