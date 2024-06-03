#DESCRIPTION
'''
OLD MACDONALD: Write a function that capitalizes the first and fourth letters of a name
old_macdonald('macdonald') --> MacDonald
'''
#MY SOLUTION
def old_macdonald(name):
  return name[0].upper() + name[1:3].lower() + name[3].upper() + name[4:].lower()