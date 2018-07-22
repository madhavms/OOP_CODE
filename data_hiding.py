class Customer:
    def selfphone(self,phone):
        self.phone = phone
        print phone

    def __init__(self,phone):
        self.phone=phone
        print self
        print __name__
custobj=Customer(94792729781)
