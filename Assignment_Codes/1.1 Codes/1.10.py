weight = float(input("Enter weight in kg: "))
height = float(input("Enter height in metres: "))

bmi = weight/(height**2)

print("BMI =", bmi)

if bmi < 18.5:
    print("Underweight")
elif bmi <= 24.9:
    print("Normal")
elif bmi <= 29.9:
    print("Overweight")
else:
    print("Obese")