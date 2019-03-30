favorite_language = {
 'jen': 'python',
 'sarah': 'c',
 'edward': 'ruby',
 'phil': 'python',
 }
for i in set(favorite_language.values()):
    print(i.title())


favorite_languages = {
 'jen': ['python', 'ruby'],
 'sarah': ['c'],
 'edward': ['ruby', 'go'],
 'phil': ['python', 'haskell'],
 }
for name, languages in favorite_languages.items():
    print("\n" + name.title() + "'s favorite languages are:")
    for i in languages:
        print("\t" + i.title())
