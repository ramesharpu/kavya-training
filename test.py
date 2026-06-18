# this is a single line comment

"""
This is 
a doc
string 
example
"""

'''
This is a multi line comment
for demo purpose
'''

def add():
    a = 5
    b = 10
    result = a + b
    print("sum of a and b = ", result)
    print(__name__)
   

if __name__ == "__main__":
    print("this is direct exectuion")
    add()
    