print('Hello, my name is Hiep and there are my ship size')
sizes = [5,7,300,90,24,50,75]
print(sizes)
max_size = max(sizes)
print("Now my biggest sheep has size",max_size, "let's shear it" ) 

print("After shearing here is my flock")
index_change = sizes.index(max_size)
sizes[index_change] = 8
print(sizes)

print('Month 1:')
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

n = int(input('Bạn muốn làm việc trong mấy tháng '))

for i in range(2,n+1):
    
    print('Month',i,":")
    sizes = new_sizes
    new_sizes = []
    print('One month has passed, now here is my flock')
    for size in sizes:
        size = size + 50
        new_sizes.append(size)
    print(new_sizes)
    
    ask = input('Ban da muon di du lich quanh the gioi khong?, Bạn chỉ được chọn Yes hoặc No ').upper() # control upper case
    if ask == 'NO':                         # Tiep tuc cao long cuu
        max_size = max(new_sizes)
        print("Now my biggest sheep has size",max_size, "let's shear it" ) 
        print("After shearing here is my flock")
        index_change = new_sizes.index(max_size)
        new_sizes[index_change] = 8
        print(new_sizes)      
    
    else:                                       # Tinh tien va dung lai
        sum_ships = 0
        for size in new_sizes:
            
            sum_ships = sum_ships + size
        money = sum_ships * 2
        print('My flock has size in total:',sum_ships)
        print("I would get",sum_ships,"* 2$ =",money,"$")
        break

