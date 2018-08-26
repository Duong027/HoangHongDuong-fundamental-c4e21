inventory = { 
    'gold' : 500, 
    'pouch' : ['flint', 'twine', 'gemstone'], 
    'backpack' : ['xylophone', 'dagger', 'bedroll', 'bread loaf'] 
} 

#Add a ​key​ to inventory called ​'pocket'​. 
# Set the value of 'pocket' to be a list consisting of the strings 'seashell', 'strange berry', and 'lint'.

#Cach1
#inventory['pocket'] = ['seashell','strange berry','lint']

# Cach 2: Dung ham update
inventory.update({'pocket': ['seashell','strange berry','lint']})
print(inventory)

#Then .remove('dagger') from the list of items stored under the 'backpack' key.

del (inventory['backpack'][1])
print(inventory)

#Add 50 to the number stored under the 'gold' key.
inventory['gold'] += 50
print(inventory)
