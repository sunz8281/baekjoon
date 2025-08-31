weight = float(input())
height = float(input())
BMI = weight / (height * height)
print("Overweight" if BMI>25 else "Underweight" if BMI<18.5 else "Normal weight")