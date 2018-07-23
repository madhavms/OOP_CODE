class Account:

    def __init__(self,CustomerID):
        self.ID = CustomerID  #creates id for each object
        self.total=1000  #object.total=1000 ;deposits 1000 into each account

    def deposit(self, amount):

        self.total +=amount

        return "BALANCE AFTER DEPOSIT RS:"+" "+str(self.total)+"\n"

    def withdraw(self, amount):
        self.total-=amount
        if(self.total<0):
            self.total+=amount
            return "INSUFFICIENT BALANCE>>BALANCE Rs:"+" "+str(self.total)

        else:
            return "BALANCE AFTER WITHDRAWAL RS:"+" "+str(self.total)+" "

    def balance(self):
        return "BALACNCE RS:"+" "+str(self.total)+"\n"


    def transfer(self,amount,ID):


        if(self.total<amount):
            self.total-=amount


        else:
            self.total-=amount
            ID.total+=amount


A=Account(1)
B=Account(2)
C=Account(3)
D=Account(4)


x=True
z=True
y=True
v=True
ls=[A,B,C,D]
list=['A','B','C','D']

while(v):

    while (x):

        b = input("USER LOGIN : 1=A,2=B,3=C,4=D:" + " "+"\n")
        if(b<5 and b>0):
            r=ls[b-1] #object for selected User ID
            break
        else:
            print"INVALID USER RE-ENTER"
            continue

    while (y):

        a = raw_input("LOGGED IN AS USER:"+" "+list[b-1]+"--> "+
                      "ENTER YOUR CHOICE d=DEPOSIT t=TRANSFER b=BALANCE w=WITHDRAW q=LOGOUT:"
                      "" + " "+"\n")

        if (a == 'd'):
            c = input("ENTER THE AMOUNT TO DESPOSIT:" + "\n")
            print r.deposit(c)
            continue

        elif (a == 't'):

            while (True):

                f = input("ENTER THE ID TO TRANSFER AMOUNT:(ID !="+" "+str(b)+')'+ "\n")
                if (f < 5 and f>0 and f!=b):
                    k = ls[f - 1]  #object for ID to get transferred amount

                    break
                else:
                    print "INVALID ID>>RE-ENTER THE ID:" + "\n"
                    continue

            while (z):

                e = input("ENTER THE AMOUNT TO TRANSFER:" + "\n")
                r.transfer(e, k) #transfers amount e from object r to object k
                if (r.total < 0):
                    r.total+=e
                    print "INSUFFICIENT BALANCE>>BALANCE=Rs:" + " " + str(r.total)+"\n"
                    continue
                else:
                    print "BALANCE AFTER TRANSEFER Rs:" + " " + str(r.total)+"\n"
                    break

        elif (a == 'b'):
            print r.balance()
            continue
        elif (a == 'w'):
            v = input("ENTER AMOUNT TO WITHDRAW Rs:" + "\n")
            print r.withdraw(v)
            continue
        elif (a == 'q'):
            break

        else:
            print "Wrong Choice"+"\n"
            continue