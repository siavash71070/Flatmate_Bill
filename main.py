from flat import Bill, FlatMate
from reports import PdfReport

amount = float(input("Hey user; enter the bill amount: "))
period = input("What is the bill period? E.g. December 2023: ")
name1 = input("What is your name? ")
days_in_house1 = float(input(f"How many day did {name1} stay in the  house during of the bill period? "))
name2 = input("What is the name of the other flatmate? ")
days_in_house2 = float(input(f"How many day did {name2} stay in the  house during of the bill period? "))

the_bill = Bill(amount, period)
flatmate1 = FlatMate(name1, days_in_house1)
flatmate2 = FlatMate(name2, days_in_house2)

print(f"{flatmate1.name} Pays :", flatmate1.pays(the_bill, flatmate2))
print(f"{flatmate2.name} Pays :", flatmate2.pays(the_bill, flatmate1))

pdf_reporter = PdfReport(filename=f"{the_bill.period}.pdf")
pdf_reporter.generate(flatmate1, flatmate2, the_bill)
