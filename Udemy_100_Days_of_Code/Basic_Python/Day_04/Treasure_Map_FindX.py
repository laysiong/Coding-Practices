line1 = ['','','']
line2 = ['','','']
line3 = ['','','']
map = [line1,line2,line3]

print("Hiding your texsure! X marks the spot.")
position = input('Where do you want to put hte treasure?')
number = position.lower()
checklist = ['a','b','c']
x_coord= int(checklist.index(number[0]))
y_coord=int(number[1])-1

if y_coord > int(len(map[0]))+1 or  x_coord  > int(len(map[0])):
    print('Coord does not existed')
else:
    map[int(x_coord)][int(y_coord)]='X'
    print(f"{line1}\n{line2}\n{line3}")
# print(number)