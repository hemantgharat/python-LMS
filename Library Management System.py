class Employee:
    def __init__(self,eid,name,designation,salary):
        self.eid=eid
        self.name=name
        self.designation=designation
        self.salary=salary

    def __str__(self):
        return "EMP. ID : "+str(self.eid)+"\nName : "+self.name+"\nDesignation : "+self.designation+"\nSalary : "+str(self.salary)+"\n"

class Books:
    def __init__(self,sn,name,author,publication):
        self.sn=sn
        self.name=name
        self.author=author
        self.publication=publication

    def __str__(self):
        return "Searial No. : "+str(self.sn)+"\nName : "+self.name+"\nAuthor : "+self.author+"\nPublicatiion : "+str(self.publication)+"\n"

def admin_menu():
    c='y'
    while(c=='y'):
        ch=int(input("\nEnter your choice:\n\n1.Add Employee\n2.Show All Emps\n3.Search emp\n4.Update Emp\n5.Delete Emp\n6.Add Book\n7.View Books\n8.Search Book\n9.Delete Book Record  :  "))
        if(ch==1):
            addEMP()
        elif ch==2:
            showEMP()
        elif ch==3:
            searchEMP()
        elif ch==4:
            updateEMP()
        elif ch==5:
            deleteEMP()
        elif ch==6:
            addBook()
        elif ch==7:
            ViewBooks()
        elif ch==8:
            searchBook()
        elif ch==9:
            deleteBook()
        c=input('\n\nPress y to continue?  : ')

def user_menu():
    c='y'
    while(c=='y'):
        ch=int(input("\nEnter your choice : \n\n1.View Books\n2.Search Book\n3.Issue Book\n4.Return Book  :  "))
        if(ch==1):
            ViewBooks()
        elif ch==2:
            searchBook()
        elif ch==3:
            issueBook()
        elif ch==4:
            returnBook()
        else:
            print("\nEnter correct choice...")
        c=input('\n\nPress y to continue?  : ')


def addEMP():
    n=int(input('\nEnter the No. of Employees : '))
    for i in range(0,n):
        with(open('Employee.txt','a')) as f:
            id=input('\nEnter the Employee Id : ')
            f.write(id+"\n")
            n=input("Enter the name:")
            f.write(n+"\n")
            d=input("Enter the Designation Employee : ")
            f.write(d+"\n")
            s=input("Enter the Salary of Employee : ")
            f.write(s+"\n")

def showEMP():
    print("\n============ Employee Information ==========\n")
    with(open('Employee.txt','r')) as f:
        for line in f:
            id=line.strip()
            n=f.readline().strip()
            ds=f.readline().strip()
            sal=f.readline().strip()
            e1=Employee(id,n,ds,sal)
            print(e1)

def searchEMP():
   
    with(open('Employee.txt','r')) as f:
        id1=input("Enter Employee ID No. for search:")
        found=0
        for line in f:
            id=line.strip()
            n=f.readline()
            ds=f.readline()
            sal=f.readline()
            e1=Employee(id,n,ds,sal)
            if(id1==e1.eid):
                print("\n============ Employee Information ==========\n")
                print(e1)
                found=1
        if found==0:
            print("\nEmployee not found....")

def updateEMP():
    with(open('Employee.txt','r')) as f:
        id1=input("Enter the Employee ID you want to update : ")
        found=0
        emp={}
        for line in f:
            id=line.strip()
            n=f.readline()
            ds=f.readline()
            sal=f.readline()
            e1=Employee(id,n,ds,sal)
            if(id1==e1.eid):
                print("============ Employee Information ==========")
                print(e1)
                ch1=int(input("What do you want to update:\n1.Name\n2.Designation\n3.Salary\n"))
                if(ch1==1):
                    e1.name=input("Enter name you want to Update:")
                elif ch1==2:
                    e1.designation=input("Enter Designation you want to Update:")
                else:
                    e1.salary=input('Enter Salary you want to Update')
                found=1
            emp[id]=e1
        if found==0:
            print("Employee not found")
    with(open('Employee.txt','w')) as f:
        for i in emp:
            f.write(str(emp[i].eid)+"\r\n")
            f.write(emp[i].name+"\r\n")
            f.write(emp[i].designation+"\r\n")
            f.write(str(emp[i].salary)+"\r\n")

def deleteEMP():
    with(open('Employee.txt','r')) as f:
        id1=input("\nEnter the Empoyee ID you want to delete : ")
        found=0
        emp={}
        for line in f:
            id=line.strip()
            n=f.readline()
            ds=f.readline()
            sal=f.readline()
            e1=Employee(id,n,ds,sal)
            if(id1!=e1.eid):
                emp[id]=e1
            else:
                found=1
        if found==0:
            print("\nEmployee not found..")
    with(open('Employee.txt','w')) as f:
        for i in emp:
            f.write(str(emp[i].eid+"\n"))
            f.write(str(emp[i].name))
            f.write(str(emp[i].designation))
            f.write(str(emp[i].salary))

def deleteBook():
    with(open('Book.txt','r')) as f:
        sr1=input("\nEnter the Book serial no you want to delete record : ")
        found=0
        lms={}
        for line in f:
            sr=line.strip()
            n=f.readline()
            a=f.readline()
            p=f.readline()
            b1=Books(sr,n,a,p)
            if(sr1!=b1.sn):
                lms[sr]=b1
            else:
                found=1
        if found==0:
            print("\nBook not found..")
    with(open('Book.txt','w')) as f:
        for i in lms:
            f.write(str(lms[i].sn+"\n"))
            f.write(str(lms[i].name))
            f.write(str(lms[i].author))
            f.write(str(lms[i].publication))


def addBook():
    n=int(input('\nEnter the No. of Books you want to add : '))
    for i in range(0,n):
        with(open('Book.txt','a')) as f:
            sr=input('\nEnter the Book Serial No. : ')
            f.write(sr+"\n")
            nm=input("Enter the Book name:")
            f.write(nm+"\n")
            ar=input("Enter the Book Author : ")
            f.write(ar+"\n")
            pb=input("Enter the Book Pubication : ")
            f.write(pb+"\n")

            
def ViewBooks():
    print("\n\n============ Library Management System ==========\n\n")
    with(open('Book.txt','r')) as f:
        for line in f:
            sr=line.strip()
            n=f.readline().strip()
            a=f.readline().strip()
            p=f.readline().strip()
            b1=Books(sr,n,a,p)
            print(b1)

def searchBook():
   
    with(open('Book.txt','r')) as f:
        bn=input("\nEnter Book name for search : ")
        found=0
        for line in f:
            sr=line.strip()
            n=f.readline().strip()
            a=f.readline().strip()
            p=f.readline().strip()
            b1=Books(sr,n,a,p)
            if(bn==b1.name):
                print("\n\n============ Book Information ==========\n")
                print(b1)
                found=1
        if found==0:
            print("\nBook not found\n")

def issueBook():
    with(open('Book.txt','r')) as f:
        sr1=input("\nEnter the Book serial no you want to issue Book : ")
        found=0
        lms={}
        for line in f:
            sr=line.strip()
            n=f.readline()
            a=f.readline()
            p=f.readline()
            b1=Books(sr,n,a,p)
            if(sr1!=b1.sn):
                lms[sr]=b1
            else:
                found=1
        if found==0:
            print("\nBook not found..")
    with(open('Book.txt','w')) as f:
        for i in lms:
            f.write(str(lms[i].sn+"\n"))
            f.write(str(lms[i].name))
            f.write(str(lms[i].author))
            f.write(str(lms[i].publication))
    print("\n\nPlease use book Carefully...")

def returnBook():
        with(open('Book.txt','a')) as f:
            sr=input('\nEnter the Book Serial No. : ')
            f.write(sr+"\n")
            nm=input("Enter the Book name:")
            f.write(nm+"\n")
            ar=input("Enter the Book Author : ")
            f.write(ar+"\n")
            pb=input("Enter the Book Pubication : ")
            f.write(pb+"\n")
        print("\n\nThank You for returning the book...")



def LMS():
    ch=int(input("\nEnter your choice:\n\n1.Admin\n2.User  :  "))
    if(ch==1):
        uid=input("\nEnter Username : ")
        pwd=input("Enter Password : ")
        if(uid=="admin" and pwd == "1234"):
            print("\nLogin Successfull...")
            print("\n\n============ Library Management System ==========\n\n")
            admin_menu()
        else:
            print("Login Failed...")
    elif(ch==2):
        uid=input("\nEnter Username : ")
        pwd=input("Enter Password : ")
        if(uid=="user" and pwd == "0000"):
            print("\nLogin Successfull...")
            print("\n\n============ Library Management System ==========\n\n")
            user_menu()
        else:
            print("Login Failed...")
