def is_palindrome(word):
    x=len(word)
    # x=x-1
    reverse="";a=0
    while x>0:
        reverse=reverse+word[x-1]
        x=x-1
    if word==reverse:
        print(f"\n'{word}' is a palindrome.")
        return True
    else:
        print(f"\n'{word}' is not a palindrome.")
        return False
print(is_palindrome("mom"))
print(is_palindrome("tenet"))
print(is_palindrome("Dhurbaraj"))