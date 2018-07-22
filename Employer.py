class Employer:



    def get(self,First_name,Last_name,Salary):
        self.First_name=First_name
        self.Last_name=Last_name
        self.Salary=Salary

    def __init__(self):
        self.First_name=None
        self.Last_name=None
        self.Salary=None

    def set(self):
        email=self.First_name+"."+self.Last_name+"@inapp.com"
        print "The Autogernerated EmailId is:"+" "+email


r=Employer()

user=r.get(
    raw_input('Enter First Name:'),
    (raw_input('Enter Last Name:')),
    int(raw_input('Enter Salary:')),
)
r.set()