# Ma tran 2*1
# Without numpy
x = [[1,2],[3,4]]
y = [1,0]

a = x[0][0]*y[0] + x[0][1]*y[1]
b = x[1][0]*y[0] + x[1][1]*y[1]

#i = 0
for j in range(len(x)):
    for i in range(len(y)-1):
        u = x[j][i]*y[i]+x[j][i+1]*y[i+1]
        print(u)

# Ma tran 2*2
x = [[1,2],[3,4]]
y = [[0,0],[1,0]]

x = [[1,2],[3,4]]
y = [[0,0],[1,0]]

for j in range(len(x)):
    for i in range(len(x[i])-1):
        u = x[j][i]*y[i][i] + x[j][i+1]*y[i][i+1]
        t = x[j][i]*y[i+1][i] + x[j][i+1]*y[i+1][i+1]
        print(u,t)

# Thuat toan nhan ma tran Wiki
x = [[1,2],[3,4]]
y = [[0,0],[1,0]]


for j in range(0,2):
    for j in range(0,2):
        sum = 0
        for k in range(0,2):
            sum = sum + x[i][k] * y[k][j]
        print(sum)