import re
grammar = {'S': ['ad', 'ABd'],
           'A': ['bB'],
           'B': ['c']}

def generate_regex(non_terminal):
    regex = ""
    for production in grammar[non_terminal]:
        production_regex = ""
        for symbol in production:
            if symbol.isupper():
                production_regex += generate_regex(symbol)
            else:
                production_regex += symbol
        regex += "" + production_regex + "|"
    return regex[:-1]

s = generate_regex('S')
print(s)
match = re.fullmatch(s,'bcd' )
if match:
    print("Yes")

else:
    print("no")