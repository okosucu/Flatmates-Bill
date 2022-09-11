from flat import Bill, Flatmate
from reports import PdfReport

bill_amount = float(input('hey user enter a bill amount: ' + '\n'))
bill_period = input("now enter a period: "+ '\n')
flatmate1_name = input("enter the name of the first flatmate: " + '\n')
flatmate1_stays= int(input("enter the days where first flatmate stays: ") +'\n')

flatmate2_name = input("enter the name of the second flatmate: " + '\n')
flatmate2_stays= int(input("enter the days where second flatmate stays: ") +'\n')

bill = Bill(bill_amount, bill_period)
Mary = Flatmate(flatmate1_name, flatmate1_stays)
John = Flatmate(flatmate2_name, flatmate2_stays)

print(Mary.name + " pays " + str(Mary.pays(bill,John) ))
print(John.name + " pays " + str(John.pays(bill,Mary) ))

pdf_report = PdfReport("bill.pdf").generate(Mary, John, bill)