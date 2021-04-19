
def rotate1(matrix):
    new_matrix = []

    counter = 0
    while counter != len(matrix):
        aux_matrix = []
        print('entro while')
        for i in range(len(matrix)):
            print('entro first for')
            index = len(matrix)-1-i
            for j in range(len(matrix[index])):
                print('entro second for')
                aux_matrix.append(matrix[index][j+counter])
                break
        
        new_matrix.append(aux_matrix)
            
        counter = counter + 1
        print(counter)
    
    return new_matrix

        


print(rotate1([[0,1,2],[3,4,5],[6,7,8]]))
