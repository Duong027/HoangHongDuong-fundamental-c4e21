print('Hello, my name is Hiep and there are my ship size')
sizes = [5,7,300,90,24,50,75]

print(sizes)

max_size = max(sizes)
    
print("Now my biggest sheep has size",max_size, "let's shear it" )  
print(sizes)

print("After shearing here is my flock")

index_change = sizes.index(max_size)

sizes[index_change] = 8

print(sizes)

print('One month has passed, now here is my flock')
#create a new list
new_sizes =[]

for size in sizes:
    size = size + 50
    new_sizes.append(size)
print(new_sizes)
