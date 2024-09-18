
def spiral_matrix_recursive(matrix):  
    result = []  
    spiral_layer(matrix, result)  
    return result  
  
def spiral_layer(matrix, result):  
    if not matrix:  
        return 0
    for i in range(len(matrix[0])):  
        result +=[matrix[0][i]]  
 
    for i in range(1, len(matrix)):  
        result +=[matrix[i][-1]]

    if len(matrix) > 1:  
        for i in range(len(matrix[0])-2, -1, -1):  
            result +=[matrix[-1][i]] 

    if len(matrix[0]) > 1:  
        for i in range(len(matrix)-2, 0, -1):  
            result += [matrix[i][0]]    

    spiral_layer([row[1:-1] for row in matrix[1:-1]], result)  
  
matrix = [[1, 2, 3, 4, 5, 6], [7, 8, 9, 10, 11, 12], [13, 14, 15, 16, 17, 18]]  
spiral = spiral_matrix_recursive(matrix)  
print(spiral)
                                    ##### method 2 #####
def spiral_matrix_pop(matrix):  
    result = []  
    m, n = len(matrix), len(matrix[0])  
    left, right, top, bottom = 0, n-1, 0, m-1  
  
    while left <= right and top <= bottom:    
        for i in range(left, right+1):  
            result.append(matrix[top][i])  
        top += 1  
  
        for i in range(top, bottom+1):  
            result.append(matrix[i][right])  
        right -= 1  

        if top <= bottom:  
            for i in range(right, left-1, -1):  
                result.append(matrix[bottom][i])  
            bottom -= 1  
  
        if left <= right:  
            for i in range(bottom, top-1, -1):  
                result.append(matrix[i][left])  
            left += 1  
  
    return result  
  
matrix = [[1, 2, 3, 4, 5, 6], [7, 8, 9, 10, 11, 12], [13, 14, 15, 16, 17, 18]] 
spiral = spiral_matrix_pop(matrix)  
print(spiral)   