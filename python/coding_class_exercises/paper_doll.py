#DESCRIPTION
'''
Given a string, return a string where for every character in the original there are three characters
paper_doll('Hello') --> 'HHHeeellllllooo'
paper_doll('Mississippi') --> 'MMMiiissssssiiippppppiii'
'''
#MY SOLUTION
def paper_doll(text):
     tripled_string = ""
     for letter in text:
          tripled_string += letter*3
     return tripled_string