# Alberto Islas 
# Compute the elements of a given row of pascal's triangle


def pascal(row):
    init = [0,1,0]
    result = init

    for i in range(row):
        result = []
        result.append(0)
        for j in range(len(init)-1):
            result.append(init[j]+ init[j+1])
        result.append(0)

        init = result
    
    result = result[1:-1]
    return result


print(pascal(10))

            
            




