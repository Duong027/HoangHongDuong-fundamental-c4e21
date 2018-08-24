items = ['T-Shirt','Sweater']
while True:
    
    ask = input('Welcome to our shop, what do you want (C, R, U, D)?').upper() #control lower upper case

    if ask == 'R': #Read_doc du lieu trong list
        print('Our item: ',end ="")
        print(*items,sep =",")

    elif ask == 'C': #Create_tao them du lieu moi trong list

        nhap = input('Enter new item ')
        items.append(nhap)
        print('Our item: ',end ="")
        print(*items,sep =",")

    elif ask == 'U': #Update them du lieu trong list

        vitri_update = int(input('Update position '))
        
        if vitri_update <= len(items): #check out of range
            sanpham = input('New item? ')
            items[vitri_update - 1] = sanpham
            print('Our item: ',end ="")
            print(*items,sep =",")

        else:
            print('Select position again')

    elif ask == 'D': #Xoa du lieu trong list
        vitri_xoa = int(input('Delete position '))
        
        if vitri_xoa <= len(items): #check out of range
            items.pop(vitri_xoa - 1)
            print('Our item: ',end ="")
            print(*items,sep =",")

        else:
            print('Select position again')
    
    else:
        print('There are only 4 choices, pick again ')