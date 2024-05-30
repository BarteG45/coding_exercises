#DESCRIPTION
'''Move the first letter of each word to the end of it, then add "ay" to the end of the word. Leave punctuation marks untouched.

Examples

pig_it('Pig latin is cool')
Output: igPay atinlay siay oolcay'''

#MY SOLUTION
def pig_it(text):
  words = text.split()
  pig_latin = ""
  for word in words:
    pigged_word = word[1:] + word[0] + "ay "
    pig_latin += pigged_word
  return pig_latin