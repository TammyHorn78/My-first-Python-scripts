"""
This program calculated the income tax of an individual after
receiving inputs of gross income and number of dependents.
"""

TAX_RATE = 0.20
STANDARD_DEDUCTION = 10000.0
DEPENDENT_DEDUCTION = 3000.0

grossIncome = float(input("Enter the gross income: "))
numDependents = int(input("Enter the number of dependents: "))

taxableIncome = grossIncome - STANDARD_DEDUCTION - \
                DEPENDENT_DEDUCTION * numDependents
incomeTax = float(taxableIncome * TAX_RATE)
round(incomeTax, 2)
print("The income tax is $")
print(incomeTax)



