Python 3.13.1 (tags/v3.13.1:0671451, Dec  3 2024, 19:06:28) [MSC v.1942 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> 
========= RESTART: C:\Users\student\Ch_09_Data_Files\breezypythongui.py ========
>>> from breezypythongui import EasyFrame
>>> class TemperatureConverter(EasyFrame):
...     def __init__(self):
...         EasyFrame.__init__(self, title="Temperature Converter")
...         self.addLabel(text="Fahrenheit", row=0, column=0)
...         self.addLabel(text="Celsius", row=0, column=1)
...         self.fahrenheitField = self.addFloatField(value=32.0, row=1, column=0, precision=2)
...         self.celsiusField = self.addFloatField(value=0.0, row=1, column=1, precision=2)
...         self.addButton(text=">>>>", row=2, column=0, command=self.computeCelsius)
...         self.addButton(text="<<<<", row=2, column=1, command=self.computeFahrenheit)
...     def computeCelsius(self):
...         fahrenheit = self.fahrenheitField.getNumber()
...         celsius = (fahrenheit - 32) * 5 / 9
...         self.celsiusField.setNumber(celsius)
...     def computeFahrenheit(self):
...         celsius = self.celsiusField.getNumber()
...         fahrenheit = (celsius * 9 / 5) + 32
...         self.fahrenheitField.setNumber(fahrenheit)
... 
...         
>>> if __name__ == "__main__":
...     TemperatureConverter().mainloop()
... 
...     
