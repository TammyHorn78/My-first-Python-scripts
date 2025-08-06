Python 3.13.1 (tags/v3.13.1:0671451, Dec  3 2024, 19:06:28) [MSC v.1942 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> 
========= RESTART: C:\Users\student\Ch_09_Data_Files\breezypythongui.py ========
>>> from breezypythongui import EasyFrame
>>> class TextFieldDemo(EasyFrame):
...     def __init__(self):
...         EasyFrame.__init(self, title  = "Text Field Demo")
...         self.addLabel(text = "Input", row = 0, column = 0)
...         self.inputField = self.addTextField(text = "", row = 0, column = 1)
...         self.addLabel(text = "Output", row = 1, column = 0)
...         self.outputField = slef.addTextField(text = "", row = 1, column = 1, state = "readonly")
...         self.addButton(text = "Convert", row = 2, column = 0, columnspan = 2, command = self.convert)
...     def convert(self):
...         text = self.inputField.getText()
...         result = text.upper()
...         self.outputField.setText(result)
... 
...         
>>> def main():
...     TextFieldDemo().mainloop()
... 
...     
>>> if __name__ == "__main__":
...     main()
... 
...     
Traceback (most recent call last):
  File "<pyshell#19>", line 2, in <module>
    main()
  File "<pyshell#16>", line 2, in main
    TextFieldDemo().mainloop()
  File "<pyshell#13>", line 3, in __init__
    EasyFrame.__init(self, title  = "Text Field Demo")
AttributeError: type object 'EasyFrame' has no attribute '_TextFieldDemo__init'
>>> 
========================== RESTART: C:\Users\student\Ch_09_Data_Files\textfielddemo.py ==========================
