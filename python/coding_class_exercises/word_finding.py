#DESCRIPTION
'''
Create a string "Python is awesome". Split this string into a list of words. Check if the word "awesome" is in this list; if it is, print "Found!", if not, print "Not found!".
'''
#MY SOLUTION
def awesome_check(string):
    if 'awesome' in string.split():
        print("Found it")
    else:
        print("Not found")