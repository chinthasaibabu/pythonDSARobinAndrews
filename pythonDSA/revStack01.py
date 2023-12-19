import stack01
# Reverse a string using a Stack

string = 'gninrael nIdekniL htiw tol a nrael'

rev_string = ''

s = stack01.Stack()


for char in string:
  s.push(char)
  
while not s.is_empty():
  rev_string += s.pop()
print(rev_string)