'''
Improve the decorator from the previous exercise by allowing it to take
any specified HTML tag as an input - making it more general.

'''

def my_func(start_tag, msg, end_tag):
    def inner_func():
        print(start_tag+msg+end_tag)
    return inner_func

html_tag = input("Which html tag do you want?:")

message = "Now we have an argument!"
html_start_tag = "<"+html_tag+">"
html_end_tag = "</"+html_tag+">"
html_code = my_func(html_start_tag, message, html_end_tag)



html_code()