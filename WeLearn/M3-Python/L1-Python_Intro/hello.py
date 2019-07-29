"""string = "hello there "
for letter in string:
    print(letter.upper())

x = 1
while x <= 5:
    print(x)
    x = x + 1

for i in range(11):
    print(i)

my_name = "Zach Solomons"
friend1 = "Ivan Drago"
friend2 = "Steve Buschemi"
friend3 = "Bob Saget"

print(
    "My name is %s and my friends are %s, %s, and %s." %
    (my_name, friend1, friend2, friend3)
)

name = "Zach"
age = "18"

print("My name is " + name + " and I'm " + str(age) + " years old." )


def greetAgent(first_name, last_name):
    print("%s. %s. %s." % (last_name, first_name, last_name))

greetAgent("James", "Bond")"""

def findSum(x):
    sum = 0
    for i in range(x):
            sum = sum + i
    return sum+x
print(findSum(20))
