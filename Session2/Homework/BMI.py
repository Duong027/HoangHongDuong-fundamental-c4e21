height = int(input('Nhap chieu cao '))
weight = int(input('Nhap khoi luong '))
BMI = weight / (height/100 * height/100)
a = BMI
if a < 16:
    
    print('Severely underweight')

elif a < 18.5:
    
    print('Underweight')

elif a < 25:
    
    print('Normal')

elif a < 30:
    
    print('Overweight')

else:
    
    print('Obese')
