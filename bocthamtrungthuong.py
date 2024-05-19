import random
thungPhieu=set()
while(1):
    print('2.them moi phieu boc tham')
    print('3.xoa phieu boc tham')
    print('4.quay so ngau nhien')
    print('1.ket thuc ')
    a=int(input('vui long chon chuc nang'))
    if a==1:
        break
    elif a==2:
        sdt=input('nhap so dien thoai ')
        thungPhieu.add(sdt)
    elif a==3:
        sdt=input('nhap so dien thoai muon xoa ')
        thungPhieu.discard(sdt)
    else :
        ngaunhien=random.randint(0,len(thungPhieu))
        print("nguoi trung thuong o vi tri thu", ngaunhien)
        print('co sdt la')
        print (thungPhieu)
            
    
