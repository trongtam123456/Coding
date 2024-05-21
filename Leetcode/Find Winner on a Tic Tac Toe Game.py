# tao bang choi
bang  = [['', '', ''],
         ['', '', ''],
         ['', '', '']]
# ham kiem tra thang 
def kiemtra(bang):
    if (bang[0][0] == bang[1][1] == bang[2][2] != ''):
        return True
    if (bang[0][2] == bang[1][1] == bang[2][1] != ''):
        return True
    for i in range(0, 3):
        if (bang[i][0] == bang[i][1] == bang[i][2] != ''):
            return True
        if (bang[0][i] == bang[1][i] == bang[2][i] != ''):
            return True
    return False

#nhap du lieu tro choi 
for i in range(0, 9):
    if (i%2 == 0):
        print('CHON BUOC DI BEN A  ')
        hang = int(input("nhap buoc di vo day (hang) : "))
        cot = int(input("nhap buoc di vo day (cot) : "))
        if (bang[hang-1][cot-1] == 'X' or bang[hang-1][cot-1] == 'O'):
            print('cho nay da co chu')
            break
        else:
            bang[hang-1][cot-1] = 'X'
            for i in range(0, len(bang)):
                print(bang[i])
        

    else:
        print('CHON BUOC DI BEN B  ')
        hang = int(input("nhap buoc di vo day (hang) : "))
        cot = int(input("nhap buoc di vo day (cot) : "))
        if (bang[hang-1][cot-1] == 'X' or bang[hang-1][cot-1] == 'O'):
            print('cho nay da co chu')
            break
        else:
            bang[hang-1][cot-1]= 'O'
            for i in range(0, len(bang)):
                print(bang[i])
    if kiemtra(bang):
        print("YOU WIN")
        break

