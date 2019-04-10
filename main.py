def bmi():
    """Calculates user's Body Mass Index"""
    m = float(input('What is your mass (kilograms)? : '))
    h = float(input('What is you height? (meters) : '))
    result = m / (h**2)
    print("your Body Mass Index is: " + str(result))


num1 = input('First number: ')
num2 = input('Second number:')

try:
    sum = int(num1) + int(num2)
except ValueError:
    print('Please enter numbers, not words')
else:
    print(sum)
