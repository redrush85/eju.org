#password generation
def passgen(size=None):
  import random
  import string

  if not size:
    size = 8
  return ''.join(random.choice(string.letters + string.digits) for i in range(size))
  
  
print passgen()
input()
