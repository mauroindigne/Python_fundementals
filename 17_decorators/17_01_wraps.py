"""
Write a decorator function that wraps text passed to it in a html <p> tag.
"""

def my_func(msg):
    def inner_func():
        print("</p>"+msg+"</p>")
    return inner_func

message = "Now we have an argument!"
woohoo = my_func(message)
woohoo()
