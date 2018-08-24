print('Hello, my name is Hiep and there are my ship size')
sizes = [5,7,300,90,24,50,75]
print(sizes)

#Cách 1: Dùng built in function max
#max_size = max(sizes)
  
#print("Now my biggest sheep has size",max_size, "let's shear it" )  


# Cách 2: Tự viết code
# Assume max_value = 0
max_size = 0

for size in sizes:
    
    if size > max_size:
        
        max_size = size
 
print("Now my biggest sheep has size",max_size, "let's shear it" )  