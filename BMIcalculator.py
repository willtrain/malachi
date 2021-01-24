height = float(input("Enter height in inches: "))
weight = float(input("Enter weight in pounds: "))



bmi=(weight/(height**2)*703)



print("Your BMI is: {0} and you are: ".format(bmi), end='')


if ( bmi < 16):
   print("Slenderman")

elif ( bmi >= 16 and bmi < 18.5):
   print("billy")

elif ( bmi >= 18.5 and bmi < 25):
   print("Healthy")

elif ( bmi >= 25 and bmi < 30):
   print("dying of diabetes")     
