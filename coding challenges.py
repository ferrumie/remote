# challenge 2

# Create a list of your favorite food items, the list should have minimum 5 elements.
# List out the 3rd element in the list.
# Add additional item to the current list and display the list.
# Insert an element named tacos at the 3rd index position of the list and print out the list elements

food = ['rice', 'noodles', 'chicken', 'plantain', 'egg']
print(food)
food.append('yam')
print(food)
print(food[2])
food.insert(3,'tacos')
print(food)

food[3] ='youth'
print(food)


# challenge 3
# Using a for -loop and a range function, print "I am a programmer" 5 times.
for x in range(0,5):
    print('I am a programmer')

# Create a function which displays out the square values of numbers from 1 to 9.

def func():
    for x in range(1,10):
        print(x*x)

func()

#challenge 4

print('hello, to calculate your bmi')
print('we need your weight in kg and your height in meters')

weight = int(input('what is your weight\n'))
height = float(input('what is your height\n'))

total = weight/(height*height)
intotal = int(total)
print('your bmi is ',intotal,'kg/m')


try:
    a=20
    b=0
    print(a/b)
except ZeroDivisionError:
    print('there is a division error')
finally:
    print('\n\n\nhello world')

