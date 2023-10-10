class Users:
    def __init__(self, name, email, dlnumber):
        self.name = name  
        self.email = email
        self.dlnumber = dlnumber
    def intro(self):
        print(f"Hi, my name is {self.name}, my email address is {self.email} and my driver's licence number is {self.dlnumber}")

caleb = Users("Caleb", "caleb.a.davis114@gmail.com", 292928343)
julia = Users("Julia", "juliadias@gmail.com", 4985673)
steven = Users(email="steventhekingsen@gmail.com",dlnumber=29304058,name="Steven")
julia.intro()
caleb.intro()
steven.intro()