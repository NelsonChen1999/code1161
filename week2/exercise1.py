"""
Commenting skills:

TODO: above every line of code comment what you THINK the line below does.
TODO: execute that line and write what actually happened next to it.

See example for first print statement
"""
import platform

# I think this will print "hello! Let's get started" by calling the print function.
print("hello! Let's get started")  # it printed "hello! Let's get started"
# I think this will associate the list "['what', 'does', 'this', 'line', 'do', '?']" with the variable "some_words"
some_words = ['what', 'does', 'this', 'line', 'do', '?']
# I think this will print the words that are in the list in the variable "some_words"
for word in some_words: #This line printed each each word in the list "some_words" on their own lines
    print(word)

for x in some_words:
    print(x)
# I think this will just print "['what', 'does', 'this', 'line', 'do', '?']" as it is
print(some_words) #It printed "['what', 'does', 'this', 'line', 'do', '?']" as it was

if len(some_words) > 3:
    print('some_words contains more than 3 words')

def usefulFunction():
    """
    You may want to look up what uname does before you guess
    what the line below does:
    https://docs.python.org/3/library/platform.html#platform.uname
    """
    print(platform.uname())

usefulFunction()
