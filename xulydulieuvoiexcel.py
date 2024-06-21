file =open('data.csv',mode='r',encoding ="utf-8-sig")
file_new=open('data_new',mode='w',encoding='utf-8-sig')
header= file.readline()
header=header.strip()+';điểm trng bình'
file_new.write(header+';học lực\n')
while(1):
    row=file.readline()
    row=row.strip()
    row_list=row.split(';')
    if (len(row_list)<=1):
        break
    diem_toan=float(row_list[2])
    diem_van=float(row_list[3])
    diem_tb=diem_toan/2+diem_van/2
    diem_tb=round(diem_tb,2)
    row_list.append(str(diem_tb))
    s=';'.join(row_list)
    if diem_tb>=8:
        s=s+';gioi'
    elif diem_tb>=6.5:
        s=s+';kha'
    else:
        s=s+';dot'
    s=s+'\n'
    file_new.write(s)

