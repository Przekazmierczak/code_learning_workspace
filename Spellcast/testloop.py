# x1, x2 = 0  
# for i in range(10):
#     globals()[f'x{i}'] = "elo"

# print(x1)
# print(x2)
# x = 0
# y = 0
# z = [1]
# globals()[f'location{z[0]}'] = [x, y]
# globals()[f'location{z[0]}'].append(x)
# print(location1)


list = [1, 2, 3, 4]
list2 = [[1, 2]]
list3 = list.copy()
list2.append(list3)
list.pop()
print(list2)