print('Hello, my name is Hiep and there are my ship size')
sizes = [5,7,300,90,24,50,75]
print(sizes)
# Thang 1"

print("Month 1 :")
print('One month has passed, now here is my flock')
new_sizes =[]
for size in sizes:
    size = size + 50
    new_sizes.append(size)
print(new_sizes)
max_size = max(new_sizes)
print("Now my biggest sheep has size",max_size, "let's shear it" ) 
print("After shearing here is my flock")
index_change = new_sizes.index(max_size)
new_sizes[index_change] = 8
print(new_sizes)


# Lấy kết quả của tháng 1 và loop cho đến các tháng muốn tính tiếp
n = int(input('Ban muon tinh tiep bao nhieu thang '))
for i in range(2,n+1):  
    print('Month',i,":")
    sizes = new_sizes
    new_sizes = []
    print('One month has passed, now here is my flock')
    for size in sizes:
        size = size + 50
        new_sizes.append(size)
    print(new_sizes)
    max_size = max(new_sizes)
    print("Now my biggest sheep has size",max_size, "let's shear it" ) 
    print("After shearing here is my flock")
    index_change = new_sizes.index(max_size)
    new_sizes[index_change] = 8
    print(new_sizes)
