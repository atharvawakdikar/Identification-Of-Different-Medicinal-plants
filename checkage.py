import datetime
class person():
    def __init__(self, name, dob):
        self.name=name
        self.dob=dob
    def check(self):
        today=datetime.date.today()
        age=today.year-self.dob.year
        if today< datetime.date(today.year, self.dob.month, self.dob.day):
            age-=1
        if age>=18:
            print(self.name, " , Congratulation! You are eligible to vote.")
        else:
            print(self.name, " , Sorry! You are not eligible to vote")
p=person("Aryan", datetime.date(2012, 2, 14))
p.check()
