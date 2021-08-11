import pickle as pk
contacts = []

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

def view_(l=None):# we use l=none because we want our function has 2 applications:1. view 2.delet or edit one contact
    # python aval function mikhune dore aval bad mire dakhele tavabe mikhune pas barae hamin inja agar b jae l = None > l=contacts bezarim barae ma list khali miare va error mikhorim vaghti dakhele tabe khund barae hamin dar dakhele tabe l = contacts gharar midim
    # l= None age chizi nagereft az tabe find biad bere to tabe va contacts neshun bede age chizi greft dar tabe find hamuno neshun bede
    if l == None:#?
        l = contacts#?
    if len(l) == 0:
        print("There is nothing to show")
        return
    print("NO  ", end='') # dorost kardan satr barae dorost neshun dadan contacts
    for i in ("firstname", "lastname", "phone NO", "Email address"): #titr k b sorate ofoghi hast
        print(i.upper().ljust(12), end='') #ljust = 12 yani har kodom b andaze 12 ta character ja bede
    print() # y khate khali chap kone

    for i,contact in enumerate(l): # dar inja i, contact 2 ta variable hastan k enumerate(l)index va value b sorate tuple b i va contact midahad
        print(str(i+1).ljust(4), end='')# inja str barae in estefade mishe chon method ljust() barae string has
        # ma az in halghe for mikhaym dar titrae k bala doros kardim hala value va index jaygozin konim az end '' estefade mikonim chon vaghti NO gozasht badesh bere fname lnam va.... bezare
        for i in contact.values():
            print(i.ljust(12), end='')#az contact.values() value haro poshte sare ham ba character 12 l barae titrasham tarif kardim mizare
        print() # mire khate bad va baz dobare NO jadid ba valuehash

def delete_():
    x = find_(just_one=True)
    if x == None:
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

    

def find_(just_one=False):# dobare mikhaym function find 2 ta kar anjam bede yki find kone , dovomi justone=true yk nafaro b ma bede k ma delete ya edit konim va to function delet edit azash estefade konim 
    x = input("who do you look for?").lower()
    result = []
    for c in contacts:
        values = [i.lower() for i in c.values()]
        if x in " ".join(values):
            result.append(c) # CHERA C? # chon c yk dictionary hast va email lname fname phone numbero baham mide to result
    view_(result) # b jae print result , resulto midim b tabe view_ k moratab behemun neshun bede
    if just_one:# vaghti bekhaym faghat ykio delete edit konim
        if len(result) > 1:
            idx = int(input("which one?")) -1
            return (result[idx]) # inja az return estefade mikonim chon dar tabe hastim va age begim print kon faghat print mikone va neshun mide
        elif len(result == 1):
            return(result[0])
        

    



def menu_():
    while True:
        dict(
            a=add_,     add=add_,
            h=help_,    help=help_,
            v=view_,    view=view_,
            x=exit,     exit=exit,
            f=find_,    find=find_,
            d=delete_,  delete=delete_,
            #e=edit_,    edit=edit_,
        ).get(
            input("?").lower().strip(),
            lambda : print("wrong command!") # we use get method in dictionary because of using wrong command instead of print None and we use lambda becuase we shod use gunction , we have () at the end
        )()

load_()
menu_()


   


      

    


