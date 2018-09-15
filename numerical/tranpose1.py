m = [[1,2],[3,4],[5,6]] 
new_list = []
new_list_1 = []
new_list_2 = []
for row in m:
    print(row)
for i in range(len(m)):
  
    for j in range(len(m[i])):
        
        new_list.append(m[i][j])
    
for num in new_list:
    if num %2 != 0:
        new_list_1.append(num)
    else:
        new_list_2.append(num)
print(new_list_1)
print(new_list_2)

