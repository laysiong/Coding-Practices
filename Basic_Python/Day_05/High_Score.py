Score = input().split()
highest_num = 0;

for n in range(0,len(Score)):
    Score[n] = int(Score[n]) 

for highest in Score:
    if highest> highest_num:
        highest_num  = highest
    else:
        highest_num = highest_num

print(f"The highest number is {highest_num}")
    