def palindrome(s):
        x=len(s)
        # s1=mystack(x)
        x=x-1
        reverse=""
        while x>=0:
            reverse+=s[x]
            x=x-1
        if s==reverse:
            print(s,"is a palindfrom.")
        else:
            print(s,"is not a palindrome.")
palindrome("imomi")
palindrome("TENET")
def is_palindrome():
    print("useing Direct method")
    # a="malayalam"
    a=input("\nGive a word to check palindrome: ")
    a=a.lower()
    if a==a[::-1]:
        print(a,"is a palindrome.")
    else:
        print(a,"is not a palindrome.")
is_palindrome()