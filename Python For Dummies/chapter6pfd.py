import datetime as dt

class Member:

    free_days = 90

    def __init__(self, uname, fname) -> None:
        # Define attributes and give them values
        self.username = uname
        self.fullname = fname
        # Default date joined to today
        self.date_joined = dt.date.today()
        # Default set to active member
        self.is_active = True
        # Set an expiration date for free trial
        self.free_expires = dt.date.today() + dt.timedelta(days = Member.free_days)
        # Default secret code to empty
        self.secretcode = ''


    #A method to return a formantted string showing the date joined
    def show_date_joined(self):
        return f"{self.fullname} joined on {self.date_joined:%m/%d/%y}"
    
    #A method to actiavte or deactivate account
    def activate(self,yesno):
        self.is_active = yesno

    @classmethod
    def setfreedays(cls,days):
        cls.free_days = days

    @staticmethod
    def currenttime():
        now = dt.datetime.now()
        return f"{now:%I:%M %p}"
    

class Admin(Member):
    expiry_days = 365 * 100

    def __init__(self, uname, fname, secretcode) -> None:
        super().__init__(uname, fname)
        self.secretcode = secretcode
class User(Member):
    pass




new_guy = Member('Rambo', 'Rocco Moe')
wilbur = Member('wblomgren', 'Wilber Blomgren')

print(wilbur.show_date_joined())
print(wilbur.currenttime())

help(Admin)