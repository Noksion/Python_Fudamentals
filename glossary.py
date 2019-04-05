from collections import OrderedDict


glossary = OrderedDict()
glossary['python'] = 'a programming language'
glossary['string'] = 'represents characters'
glossary['list'] = 'represents containers for other types of data'
glossary['function'] = 'is a piece of code that can be issued at any time'
glossary['dictionary'] = 'represents advanced lists with key-value storage'
glossary['integer'] = 'represents a whole number'

for term, meaning in glossary.items():
    print('\n' + term.title() + ': ' + meaning)
