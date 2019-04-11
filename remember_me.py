import json


def get_stored_name():
    """Get stored name if available"""
    filename = 'username.json'
    try:
        with open(filename) as obj:
            username = json.load(obj)
    except FileNotFoundError:
        return None
    else:
        return username


def get_new_username():
    """Gets the new username"""
    username = input('What is your name?: ')
    filename = 'username.json'

    with open(filename, 'w') as obj:
        json.dump(username, obj)
    return username


def check_user():
    username = str(get_stored_name())
    check = input("Last login was as " + username + ". Is that you? (Yes / No): ")
    if check.lower() == 'yes':
        return True
    else:
        return None


def greet_user():
    """Greet the user by name"""
    if check_user():
        username = get_stored_name()
        print('Welcome back, ' + username + '!')

    else:
        username = get_new_username()
        print("We'll remember you when you come back, " + username + '!')


greet_user()
