def bmi():
    """Calculates user's Body Mass Index"""
    m = float(input('What is your mass (kilograms)? : '))
    h = float(input('What is you height? (meters) : '))
    result = m / (h**2)
    print("your Body Mass Index is: " + str(result))




with open('pi.txt') as file_object:
    lines = file_object.read()

print(lines.rstrip())
