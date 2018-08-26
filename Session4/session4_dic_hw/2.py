#Create a new dictionary called prices using {} format like the example above.
#Put these values in your prices dictionary:

prices = {
    "banana": 4,
    "apple": 2,
    "orange": 1.5,
    "pear": 3,
}

#Create another dictionary called stock using {}:

stocks = {
    "banana": 6,
    "apple": 0,
    "orange": 32,
    "pear": 15,
}

#Loop through each key in prices. For each key, print out the key along with its price and stock information

for k,v in prices.items():
    print(k,'\n''price:',v)
    if k in stocks:
        print('stock:',stocks[k])
    else:
        print('Check prices and stocks again!!!')

#Let's determine how much money you would make if you sold all of your food.
total = 0

# Calculate
for k,v in prices.items():
    if k in stocks:
        print('Money from',k,'is:',prices[k] * stocks[k])
        a = prices[k] * stocks[k]
        total += a
print('Total money is',total)

    
