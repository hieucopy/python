import math
print('phuong trinh ax^2 +bx +c =0 ')
a=float(input('nhap gia tri a '))
b=float(input('nhap gia tri b '))
c=float(input('nhap gia tri c '))
delta= b**2-4*a*c
if delta<0: 
    print('phuong trinh vo nghiem')
else:
    x1=(-b-math.sqrt(delta))/(2*a)
    x2=(-b+math.sqrt(delta))/(2*a)
    if x1==x2:
        print('phuong trinh co nghiem kep x= ', x1)
    else :
        
        print ('x1={0},x2={1}'.format(x1,x2))
    
