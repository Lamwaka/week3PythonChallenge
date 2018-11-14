from datetime import datetime, date

date_of_birth = datetime.strptime(raw_input("type date (dd/mm/yy)"), "%d/%m/%y")

def calculate_age(born):
    today = date.today()
    return today.year - born.year - ((today.month, today.day) < (born.month, born.day))

age = calculate_age(date_of_birth)

if age >0 and age <18:
    print "you are a minor"
else:
    if age >=18 and age <=36:
        print "you are a youth"
    else:
        print "you are an elder"

input()
