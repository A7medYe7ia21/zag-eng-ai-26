#Q1:
name=str(input("enter your name :"))
print(type(name))

age=int(input("enter your age :"))
print(type(age))

height=float(input("enter your height :"))
print(type(height))

student=bool(input(" your are student Y/N:"))
print(type(student))
####################
#Q2:
num_1=float(input("enter number 1:"))
num_2=float(input("enter number 2:"))
print(f"the sum {num_1+num_2}")
print(f"the difference {num_1-num_2}")
print(f"the division {num_1/num_2}")
print(f"the product {num_1*num_2}")
######################
#Q3:
num=int(input("enter number :"))
if num<0:
    print ("number is negative")
elif num>0:
    print ("number is positive")
else:
    print ("number is Zero")
#######################
#Q4:
for i in range(2,20,2):
    print(i)
#######################
#Q5:
secret = 7

guess = int(input("Guess the number: "))

while guess != secret:
    print("Wrong guess, try again!")
    guess = int(input("Guess the number: "))

print("Congratulations! You guessed it right " )
#########################
#Q6:
with open("data.txt", "r") as file:
    content = file.read()
    print(content)
#########################
#Q7:
numbers = [1, 2, 3, 4, 5]

print("Sum:", sum(numbers))

print("Maximum:", max(numbers))

numbers.reverse()
print("Reversed list:", numbers)
#########################
#Q8:
cities = ("Cairo",   "Aswan", "Luxor")

print("First city:", cities[0])
print("Last city:", cities[-1])
#########################
#Q9:
# Two sets of student names
groupA = {"Ahmed", "Sara", "Omar", "Mona"}
groupB = {"Omar", "Mona", "Youssef", "Ali"}

common_students = groupA.intersection(groupB)

print("Students in both groups:", common_students)
############################
#Q10:
try:
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))

    result = num1 / num2
    print("Result:", result)

except ZeroDivisionError:
    print("Error: You cannot divide by zero.")

except ValueError:
    print("Error: Please enter valid numbers.")

else:
    print("Division successful!")

finally:
    print("Program finished.")
#############################################
#Q11:

def celsius_to_fahrenheit(c):
    return (c * 9 / 5) + 32


def fahrenheit_to_celsius(f):
    return (f - 32) * 5 / 9


def average_temperature(temp_list, scale):
    avg = sum(temp_list) / len(temp_list)
    if scale == 'F':
        return celsius_to_fahrenheit(avg)
    return avg


def highest_temperature(temp_list, scale):
    highest = max(temp_list)
    if scale == 'F':
        return celsius_to_fahrenheit(highest)
    return highest


try:
    user_input = input("Enter temperatures in Celsius (comma-separated): ")
    
    
    temps_celsius = [float(temp.strip()) for temp in user_input.split(",")]

    avg_c = average_temperature(temps_celsius, 'C')
    avg_f = average_temperature(temps_celsius, 'F')

    high_c = highest_temperature(temps_celsius, 'C')
    high_f = highest_temperature(temps_celsius, 'F')

    print("\nResults:")
    print(f"Average Temperature: {avg_c:.2f} | {avg_f:.2f} ")
    print(f"Highest Temperature: {high_c:.2f}  | {high_f:.2f} ")

except ValueError:
    print("Error: Please enter valid numeric temperatures only.")
except ZeroDivisionError:
    print("Error: Temperature list cannot be empty.")


