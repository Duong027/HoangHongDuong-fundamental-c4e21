def is_inside(l1,l2):
    return l2[0]<l1[0] and l2[1]<l1[1]

check = is_inside([200, 120], [140, 60, 100, 200])

if check == False:
    print('Check your function again')
else:
    print('Correct')
