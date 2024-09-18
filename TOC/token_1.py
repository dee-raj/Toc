txt="program to make tokenize"
print(txt.split())

import nltk
print(nltk.word_tokenize("here is the example of tokenizetion"))



from nltk.tokenize import sent_tokenize
text = "God is Great! I won a lottery. This is of worthly than i expect."
print(sent_tokenize(text))