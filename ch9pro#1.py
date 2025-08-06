Python 3.13.1 (tags/v3.13.1:0671451, Dec  3 2024, 19:06:28) [MSC v.1942 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> 
========= RESTART: C:\Users\student\Ch_09_Data_Files\breezypythongui.py ========
>>> from breezypythongui import EasyFrame
>>> class TaxCalculator(EasyFrame):
...     def __init__(self):
...          EasyFrame.__init__(self, title="Tax Calculator")
...          self.addLabel(text="Gross Income:", row=0, column=0)
...          self.incomeField = self.addFloatField(value=0.0, row=0, column=1)
...          self.addLabel(text="Number of Dependents:", row=1, column=0)
...          self.dependentsField = self.addIntegerField(value=0, row=1, column=1)
...          self.addLabel(text="Tax Owed:", row=2, column=0)
...          self.taxField = self.addFloatField(value=0.0, row=2, column=1, state="readonly")
...          self.addButton(text="Calculate", row=3, column=0, columnspan=2, command=self.calculateTax)
...     def calculateTax(self):
...         TAX_RATE = 0.15
...         DEPENDENT_DEDUCTION = 2000.0
...         STANDARD_DEDUCTION = 8000.0
...         income = self.incomeField.getNumber()
...         dependents = self.dependentsField.getNumber()
...         taxableIncome = income - STANDARD_DEDUCTION - (DEPENDENT_DEDUCTION * dependents)
...         taxableIncome = max(0, taxableIncome)
...         tax = taxableIncome * TAX_RATE
...         self.taxField.setNumber(tax)
... 
...         
>>> if __name__ == "__main__":
...     TaxCalculator().mainloop()
... 
...     

