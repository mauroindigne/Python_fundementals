'''
Write a script that takes a string of words and a symbol from the user.
Replace all occurrences of the first letter with the symbol. For example:

String input: more python programming please
Symbol input: #
Result: #ore python progra##ing please

'''

text = input("Type any string here:")
symbol = input("Type any symbol you want:")
change = text[0]
print(text.replace(change, symbol))