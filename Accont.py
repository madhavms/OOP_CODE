class Account:

    def __init__(self,CustomerID):
        self.ID = CustomerID
        self.total=0

    def deposit(self, amount):
        self.total = self.total + amount

        return "BALANCE AFTER DEPOSIT RS:"+" "+str(self.total)+"\n"

    def withdraw(self, amount):
        self.total-=amount
        if(self.total<0):
            self.total+=amount
            return "INSUFFICIENT BALANCE"

        else:
            return "BALANCE AFTER WITHDRAWAL RS:"+" "+str(self.total)+" "

    def balance(self):
        return "BALACNCE RS:"+" "+str(self.total)+"\n"


    def transfer(self,amount,ID):


        if(self.total<amount):
            self.total = self.total - amount


        else:
            self.total=self.total-amount
            ID.total = ID.total + amount


A=Account(1)
A.deposit(1000)
B=Account(2)
B.deposit(1000)
C=Account(3)
C.deposit(1000)
D=Account(4)
D.deposit(1000)

x=True
z=True
y=True
v=True
ls=[A,B,C,D]

while(v):

    while (x):

        b = input("ENTER USER 1=A,2=B,3=C,4=D:" + " "+"\n")
        if(b<5 and b>0):
            r=ls[b-1]
            break
        else:
            print"INVALID USER RE-ENTER"
            continue

    while (y):

        a = raw_input("ENTER YOUR CHOICE d=DEPOSIT t=TRANSFER b=BALANCE w=WITHDRAW q=QUIT:" + " "+"\n")

        if (a == 'd'):
            c = input("ENTER THE AMOUNT TO DESPOSIT:" + "\n")
            print r.deposit(c)
            continue

        elif (a == 't'):

            while (True):

                f = input("ENTER THE ID TO BE TRANSFERED:" + "\n")
                if (b < 5 and b>0):
                    r = ls[b - 1]
                    break
                else:
                    print "INVALID ID>>RE-ENTER THE ID:" + "\n"
                    continue

            while (z):

                e = input("ENTER THE AMOUNT TO TRANSFER:" + "\n")
                r.transfer(e, k)
                if (r.total < 0):
                    r.total = r.total + e
                    print "INSUFFICIENT BALANCE>>BALANCE=Rs:" + " " + str(r.total)+"\n"
                    continue
                else:
                    print "BALANCE AFTER WITHDRAWAL Rs:" + " " + str(r.total)+"\n"
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




















