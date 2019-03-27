name = input("Hello. What's your name? : ")


def bmi():
    """Calculates user's Body Mass Index"""
    m = float(input('What is your mass (kilograms)? : '))
    h = float(input('What is you height? (meters) : '))
    result = m / (h**2)
    print(name + ", your Body Mass Index is: " + str(result))


def greeting():
    """Greeting the user"""
    print("Ok " + name.title() + ", Let's get to BMI test.")


greeting()
bmi()
