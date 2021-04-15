'''
Using f-strings, print out the name, last name, and favorite
office supply item of each person in the given dictionary,
formatted like so:

LASTNAME, Name           Office supply item
LONGERLASTNAME, Name     Office supply item

'''

office = [
    {"full_name": "Michael Scott", "item": "world's best boss mug"},
    {"full_name": "Dwight Schrute", "item": "pepper spray"},
    {"full_name": "Jim Halpert", "item": "phone"},
    {"full_name": "Pam Beesly", "item": "post-its"},
    {"full_name": "Ryan Howard", "item": "business cards"},
    {"full_name": "Stanley Hudson", "item": "crossword-puzzle"},
    {"full_name": "Kevin Malone", "item": "m&ms"},
    {"full_name": "Meredith Palmer", "item": "flask"},
    {"full_name": "Angela Martin", "item": "cat food"},
    {"full_name": "Oscar Martinez", "item": "calculator"},
    {"full_name": "Phyllis Lapin", "item": "cut flowers"},
    {"full_name": "Kelly Kapoor", "item": "People magazine"},
    {"full_name": "Toby Flenderson", "item": "files"},
    {"full_name": "Creed Bratton", "item": "mung beans"},
    {"full_name": "Darryl Philbin", "item": "forklift"},
]
"""
for character in office:
    for k, v in character.items():
        if k == "full_name":
            fullname = v.split(" ")
            lastname = fullname[1]
            firstname = fullname[0]
            newfullnmae = lastname, firstname
        if k == "item":
            personalItem = v
    print(f"{lastname:10}, {firstname:10} {personalItem:<20}")
    """

longestfullname = 0

for character in office:
    for k, v in character.items():
        if k == "full_name":
            fullname = v.split(" ")
            lastname = fullname[1]
            firstname = fullname[0]
            newfullname = f"{lastname}, {firstname}"
            if len(newfullname) > longestfullname:
                longestfullname = len(newfullname)

        if k == "item":
            personalItem = v

    print(f"{newfullname:{longestfullname+1}}  {personalItem:<20}")