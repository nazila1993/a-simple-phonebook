import pickle as pk
contacts = []

feature = dict(
    fname = "first name",
    lname = "last name",
    phone = "phone NO",
    email = "Email address",
)
def add_():
    contacts.append(dict(
        fname = input("first name :"),
        lname = input("last name:"),
        phone = input("phone NO:"),
        email = input("Email address:"),
    ))
    save_()

def save_():
    with open("Desktop/contacts.pkl", "wb") as f:
        pk.dump(contacts,f)

def load_():
    global contacts
    try:
        with open("Desktop/contacts.pkl", "rb") as f:
            contacts = pk.load(f)
    except:
        contacts = []
def view_(l=None):#?
    if l == None:#?
        l = contacts#?
    if len(l) == 0:
        print("There is nothing to show")
        return
    print("NO  ", end='')
    for i in ("firstname", "lastname", "phone NO", "Email address"):
        print(i.upper().ljust(12), end='')
    print()

    for i,contact in enumerate(l):#?
        print(str(i+1).lower().ljust(4), end='') #?
        for i in contact.values():
            print(i.ljust(12), end='')
        print()
def delete_():
    x = find_(just_one=True)
    if x == None
    return
    if input("Are you sure?").lower().strip().startswith("y"):
        contacts.remove(x)
    save_()
    msg = f"\"{x.get('fname')} {x.get('lname')}\" has been removed!"
    print(msg)

def help_():
    help_str = '''
    HELP:
       a, add      to add a contact
       v, view     to view contacts
       f, find     to search a contact
       d, delete    to remove a contact
       h, help    to view help
       x, exit     to exit
    '''
    print(help_str)

    

def find_(just_one=False):
    x = input("who do you look for?").lower()
    result = []
    for c in contacts:
        values = [i.lower() for i in c.values()]
        if x in " ".join(values):
            result.append(c) # CHERA C?
    view_(result)
    if just_one:
        if len(result) > 1:
            idx = int(input("which one?")) -1
            return (result[idx])
        elif len(result == 1):
            return(result[0])
        else:
            return

    



def menu_():
    while True:
        dict(
            a=add_,     add=add_,
            h=help_,    help=help_,
            v=view_,    view=view_,
            x=exit,     exit=exit,
            f=find_,    find=find_,
            d=delete_,  delete=delete_,
            e=edit_,    edit=edit_,
        ).get(
            input("?").lower().strip(),
            lambda : print("wrong command!")
        )()

load_()
menu_()


   


      

    


