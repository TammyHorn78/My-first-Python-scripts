height = float(input("Enter the height that the ball is dropped: "))
bounces = int(input("Enter the number of bounces for the ball: "))
distance = 0
for count in range(bounces):
    distance = height +  (height * 0.6)
print("The total distance traveled is", distance, "feet.")
