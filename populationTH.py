numOrganisms = float(input("Enter thr number of organisms: "))
growthRate = float(input("Enter the rate of growth: "))
rateHours = int(input("ERnter the number of hours to hit growth rate: "))
population = 0

for count in range(rateHours):
    population = (numOrganisms * growthRate) + population

print("After", rateHours, "the population count is", population, "organisms.")
