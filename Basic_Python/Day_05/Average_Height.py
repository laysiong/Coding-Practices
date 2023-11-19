height = input().split()
total = 0
number = len(height)

for n in range(0,len(height)):
    height[n] = int(height[n]) 

for test in height:
    total += int(test)

average_height = total/len(height)

print(f"Total height: {total} \n Average height: {average_height}\n Total number of student:{number}")
