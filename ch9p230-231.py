Python 3.13.1 (tags/v3.13.1:0671451, Dec  3 2024, 19:06:28) [MSC v.1942 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.

========= RESTART: C:\Users\student\Ch_09_Data_Files\breezypythongui.py ========
from breezypythongui import EasyFrame
class LayoutDemo(EasyFrame):
    def __init__(self):
       EasyFrame.__init__(self)
       self.addLabel(text = "(0, 0)", row = 0, column = 0, sticky = "NSEW")
       self.addLabel(text = "(0, 1)", row = 0, column = 1, sticky = "NSEW")
       self.addLabel(text = "(1, 0)", row = 1, column = 0, sticky = "NSEW")
       self.addLabel(text = "(1, 1)", row = 1, column = 1, sticky = "NSEW")

       
def main():
    LayoutDemo().mainloop()

    
if __name__ == "__main__":
    main()

    

========= RESTART: C:\Users\student\Ch_09_Data_Files\breezypythongui.py ========
from breezypythongui import EasyFrame
class LayoutDemo(EasyFrame):
...     def __init__(self):
...         EasyFrame.__init__(self)
...         self.addLabel(text = "(0, 0)", row = 0, column = 0, sticky = "NSEW")
...         self.addLabel(text = "(0, 0)", row = 0, column = 0, sticky = "NSEW")
...         self.addLabel(text = "(0, 0)", row = 0, column = 0, sticky = "NSEW")
... 
...         
>>> def main():
...     LayoutDemo().mainloop()
... 
>>> if __name__ == "__main__":
...     main()
... 
...     

========= RESTART: C:\Users\student\Ch_09_Data_Files\breezypythongui.py ========
>>> from breezypythongui import EasyFrame
>>> class LayoutDemo(EasyFrame):
...     def __init__(self):
...         EasyFrame.__init__(self)
...         self.addLabel(text = "(0, 0)", row = 0, column = 0, sticky = "NSEW")
...         self.addLabel(text = "(0, 1)", row = 0, column = 1, sticky = "NSEW")
...         self.addLabel(text = "(1, 0 and 1)", row = 1, column = 0, sticky = "NSEW", columnspan = 2)
... 
...         
>>> def main():
...     LayoutDemo().mainloop()
... 
...     
>>> if __name__ == "__main__":
...     main()
... 
...     
