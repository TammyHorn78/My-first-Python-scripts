hourlyWage = float(input("Enter employees hourly wage: "))
regularHours = float(input("Enter regular hours worked: "))
otHours = float(input("Enter overtime hours worked: "))

employeepay = (hourlyWage * regularHours) + ((hourlyWage * 1.5) * otHours)

print("The employees weekly pay is $" + str(employeepay))
