matrix = [[1, 2, 3, 5],
          [4, 5, 9, 2],
          [0, 5, 7, 9]]
# quet toan bo ma tran
row_coloum = []
# vong lap chinh
for i in range(0, len(matrix)):
    #vong lap phu
    for j in range(0, len(matrix[i])):
        if matrix[i][j] == 0:
            row_coloum.append(i)
            row_coloum.append(j)
            #cot
            for m in range(0, len(matrix)):
                matrix[m][j] = 0
            print(matrix)
            #hang
            for n in range(0, len(matrix[i])):
                matrix[i][n] = 0
###############chua dung
