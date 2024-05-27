#DESCRIPTION
'''Write a function generate_password(length) that generates a random password of a given length. The password should contain uppercase and lowercase letters, digits, and special characters.'''

#MY SOLUTION
def generate_password(length):
    import random
    import string
    a = list(string.ascii_lowercase)
    b = []
    for x in range(0,10):
        b+=str(x)
    c = list(string.punctuation)
    d = list(string.ascii_uppercase)
    lists = a+b+c+d
    return "".join(random.choices(population=lists,k=int(length)))