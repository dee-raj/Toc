from nltk import parse_cfg, ChartParser
from random import choice

def produce(grammar, symbol):
    words = []
    productions = grammar.productions(lhs = symbol)
    production = choice(productions)
    for sym in production.rhs():
        if isinstance(sym, str):
            words.append(sym)
        else:
            words.extend(produce(grammar, sym))
    return words

grammar = parse_cfg('''
S -> NP VP
PP -> P NP
NP -> Det N | Det N PP | 'I'
VP -> V NP | VP PP
V -> 'shot' | 'killed' | 'wounded'
Det -> 'an' | 'my' 
N -> 'elephant' | 'pajamas' | 'cat' | 'dog'
P -> 'in' | 'outside'
''')

parser = ChartParser(grammar)

gr = parser.grammar()
print (''.join(produce(gr, gr.start())))