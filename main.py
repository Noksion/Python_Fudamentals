def bmi():
    """Calculates user's Body Mass Index"""
    m = float(input('What is your mass (kilograms)? : '))
    h = float(input('What is you height? (meters) : '))
    result = m / (h**2)
    print("Your Body Mass Index is: " + str(result))


def greeting():
    """Getting the user's name and greeting them"""
    name = input("Hello. What's your name? : ")
    print("Ok " + name.title() + " Let's get to BMI test.")


greeting()
bmi()
