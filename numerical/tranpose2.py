m = [[10,20,3],[2,40,-5],[3,-5,6]]
for row in m:
    print(row)
new_list = []
new_list_1 = []
new_list_2 = []
new_list_3 = []

print(range(len(m)))

for i in range(len(m)):
    print(m[i])
    for j in range(len(m[i])):
        print(m[i][j])
    
        new_list.append(m[i][j])

print(new_list)

new_list_1 = [new_list[0],new_list[3],new_list[6]]
new_list_2 = [new_list[1],new_list[4],new_list[7]]
new_list_3 = [new_list[2],new_list[5],new_list[8]]
print(new_list_1)
print(new_list_2)
print(new_list_3)

m_tran = [new_list_1,new_list_2,new_list_3]

if m == m_tran:
    print('m is a symmetric matrix')
else:
    print('m is not a symmetric matrix')