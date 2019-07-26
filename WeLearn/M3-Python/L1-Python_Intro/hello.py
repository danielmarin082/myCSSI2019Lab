print("Hello world!")
print("Bye World!")

num1 = int(raw_input("Enter number #1"))
num2 = int(raw_input("Ender number #2"))
total = num1 + num2
print("The sum is " + str(total))

num = int(raw_input("Enter a number: "))
if num > 0:
    print("That is a positive number!")
elif num < 0:
    print("That is a negative number!")
else:
    print("Zero is neither positive nor negative")

string = "hello there"
for letter in string:
    print(letter.upper())

for i in range(5):
    print(i)

x = 1
while x <= 5:
    print(x)
    x = x + 1

my_name = "Daniel"
friend1 = "Sam"
friend2 = "Goat"
friend3 = "Devin"

print(
    "My name is %s and my friends are %s, %s, and %s" %
    (my_name, friend1, friend2, friend3)
)

name = "Daniel"
age = 18

print("My name is " + name + " and I'm " +str(age) + " years old.")

print("My name is %s and I'm %s years old." % (name, age))

print("Eat your chair")

def greetAgent():
    print("Bond. James Bond")

def greetAgent(first_name, last_name):
    print("%s, %s %s." % (last_name, first_name, last_name))
greetAgent('James', 'Bond')

def createAgentGreeting(first_name, last_name):
    return "%s, %s %s." % (last_name, first_name, last_name)
