my_file = open("output.txt","r")
print my_file.read()

my_file.close()
"""
Declare a variable, my_file, and set it equal to the file object returned by calling open() with both "output.txt" and "r".
Next, print the result of using .read() on my_file, like the example above.
Make sure to .close() your file when you're done with it! All kinds of doom will happen if you don't.
"""