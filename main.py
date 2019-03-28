def bmi():
    """Calculates user's Body Mass Index"""
    m = float(input('What is your mass (kilograms)? : '))
    h = float(input('What is you height? (meters) : '))
    result = m / (h**2)
    print("your Body Mass Index is: " + str(result))


# describe_pet is an example of default value in the function argument
def describe_pet(animal_type, pet_name='Tom'):
    """Display information about a pet."""
    print("\nI have a " + animal_type + ".")
    print("My " + animal_type + "'s name is " + pet_name.title() + ".")


def formatted_name(first_name, last_name):
    process = first_name + " " + last_name
    return process.title()


scientist = formatted_name('albert', 'einstein')
print(formatted_name('ruslan', 'olkhovsky'))
print(scientist)