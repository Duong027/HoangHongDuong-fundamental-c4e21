print('Hello, my name is Hiep and there are my ship size')
sizes = [5,7,300,90,24,50,75]

print(sizes)

max_size = max(sizes)
    
print("Now my biggest sheep has size",max_size, "let's shear it" )  
print(sizes)

print("After shearing here is my flock")

# Tim vi tri cua gia tri lon nhat_Dung ham index
index_change = sizes.index(max_size)
sizes[index_change] = 8
print(sizes)