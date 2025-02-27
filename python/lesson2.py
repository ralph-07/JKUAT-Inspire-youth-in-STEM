# variables in python
student_name ="Ralph" # string
student_second_name = 'Ntari' # string
student_age = 18 # integer
student_height = 1.77 #float
student_admited= True #boolean

# Operators in python
#1. Arithmetic operators
num1 = 10
num2 = 20
addition = num1 + num2
# print (addition)
subtraction = num1 - num2 
# print(subtraction)
print(num1 == num2) # false
print(num1 != num2) # true
print(num1 > num2) #false
print(num1 < num2) # true


#3. Logocal operators
# and, or, not
#print(num1< num2 and num1 > num2) # false
print(num1 < num2 or num1 < num2) # true
print(not num1 < num2)

#4. Assignment operators
#=, +=, *=, /=
num1 += 5
print(num1) #15
num1 -= 5
print(num1) # 10
num1 *= 5 
print(num1) # 50

#5. Identity operators
#is, is not
print(num1 is not num2) # true
print(num1 is num2) # false

#6. Conditional statements
# if, elif, else

if student_age >= 18:
    print("you are an adult")

    enter_name = input("Enter yur name")
    enter_age = int(input("enter your age: "))
    if enter_age >= 18:
        print(enter_name, " is an adult")

        enter_speed = input("Enter your speed: ")
        enter_speed = int(input("enter your speed: "))
        if enter_speed >= 100:
            print(enter_speed, " is ovrespeeding")
            