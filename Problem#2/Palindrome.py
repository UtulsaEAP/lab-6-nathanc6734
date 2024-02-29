'''
Name: Nathan Carr
Lab Time: Thursday @ 2pm
'''
def check_palindrome(user_input):
    reversed = ""
    for c in user_input:
        reversed = c + reversed
    if reversed == user_input:
        print("palindrome: " + user_input)
    else:
        print("not a palindrome: " + user_input)
if __name__ == "__main__":
    user_input = input()
    check_palindrome(user_input)
