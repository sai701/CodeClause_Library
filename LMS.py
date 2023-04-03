def display():
    l=['a','b','c','d']
    print(l)
def borrow():
    a=input('Enter the book you want to borrow: ')
    if(a=='a' or a=='b' or a=='c' or a=='d'):
        print('You can borrow the book')
    else:
        print('Book Not Available')
def returni():
    print('Thanks for returning the book')

def start():
    print(" \n\tWelcome to Library ")
    print("\n")
    print("1.Display\n")
    print("2.Borrow\n")
    print("3.Return\n")
    print("4.Exit\n")
    try:
        ch=int(input('Choice: '))
        print()
        if(ch==1):
            display()
        elif(ch==2):
            borrow()
        elif(ch==3):
            returni()
        elif(ch==4):
            print('Thank You!Happy Learning')
        else:
            print('Invalid Input')
    except ValueError:
        print('Input again!!!')
start()