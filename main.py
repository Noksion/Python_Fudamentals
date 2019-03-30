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


def formatted_name(first_name, last_name, middle_name=''):
    if middle_name:
        process = first_name + " " + middle_name + " " + last_name
    else:
        process = first_name + " " + last_name
    return process.title()


scientist = formatted_name('albert', 'einstein')


def build_person(first_name, last_name, age=''):
    """Return a dictionary of information about a person."""
    person = {'first': first_name, 'last': last_name}
    if age:
        person['age'] = age
    return person


def build_profile(first, last, **user_info):
    """Build a dictionary containing everything we know about a user."""
    profile = {}
    profile['first_name'] = first
    profile['last_name'] = last
    for key, value in user_info.items():
        profile[key] = value
    return profile


user_profile = build_profile('albert', 'einstein', location='princeton', field='physics', age=58)
print(user_profile['last_name'])
