# -*- coding: utf-8 -*-
"""
Created on Sun Aug 29 21:06:11 2021

@author: Adri Saha
"""
#Name: Adri Saha
#ID: 2019-1-60-024

#Task 1 module

#determinant
def determinant_2019_1_60_024(mat,n):
    det=0
    a=[[0 for i in range(n)] for j in range(n)]
    if n==1:
        return mat[0][0]
    else:
        det=0
        for x in range(n):
            p=0
            q=0
            for i in range(n):
                for j in range(n):
                    if i!=0 and j!=x:
                        a[p][q]=mat[i][j]
                        if q<(n-2):
                            q+=1
                        else:
                            q=0
                            p+=1
            sign=1
            det=det+sign*(mat[0][x]*determinant_2019_1_60_024(a,n-1))
            sign=(-1)*sign
    return det

#Inverse  
def inverse_adri(inverse,d,adj,r):
    for i in range(r):
        for j in range(r):
            inverse[i][j] = adj[i][j]/d        
    print("\nThe inverse Matrix is:")
    for i in range(r):
        for j in range(r):
            print(round(inverse[i][j],2),end = " ")
        print()

#Transpose        
def transpose_adri(num,cofac,n):
    adjugate = [[0 for i in range(n)] for j in range(n)]
    inverse = [[0 for i in range(n)] for j in range(n)]
    for i in range(n):
        for j in range(n):
            adjugate[i][j]=cofac[j][i]
    det=determinant_2019_1_60_024(num,n)
    inverse_adri(inverse,det,adjugate,n)
  
#Cofactor     
def cofactor_adri(num,n):
    mat=[[0 for i in range(n)] for j in range(n)]
    cofactor=[[0 for i in range(n)] for j in range(n)]
    for x in range(n):
        for y in range(n):
            l=0
            m=0
            for i in range(n):
                for j in range(n):
                    if i!=x and j!=y:
                        mat[l][m] = num[i][j]
                        if m<(n-2):
                            m+=1
                        else:
                            m=0
                            l+=1
            cofactor[x][y] = ((-1)**(x+y))*determinant_2019_1_60_024(mat,n-1)
    transpose_adri(num,cofactor,n)

#Task 2 Module
# Length
def count_Adri(x):
    count = 0
    for i in x:
        count+=1
    return count

# Sum
def summation_Adri(x):
    total = 0
    for i in x:
        total +=i
    return total

#Mean
def mean_Adri(x):
    return summation_Adri(x)/count_Adri(x)

#splits data into train and test sets
def train_test_split_Adri(x, y, split):
    size = int(count_Adri(x)-(count_Adri(x)*float(split)))
    x_train = x[:size] #train set
    y_train = y[:size]
    x_test = x[size:] #test set
    y_test = y[size:]
    
    return x_train, y_train, x_test, y_test

#covariance of x and y
def cov_Adri(x,y):
    m = mean_Adri(x)  
    x_list = list()
    y_list = list()
    product = list()
    for i in x:
        x_list.append(i-m)
    for i in y:
        y_list.append(i-m)
    for i,j in zip(x_list, y_list):
        product.append(i*j)
    #print("Module covariance : ",summation_Adri(product))
    return summation_Adri(product)/(count_Adri(x)-1)

#variance of x
def var_Adri(x):
    #print("Pandas Output for variance:", x.var())
    m = mean_Adri(x)
    x_list = list()
    for i in x:
        x_list.append((i-m)**2)
    #print("Module variance : ", summation_Adri(x_list))
    return summation_Adri(x_list)/(count_Adri(x)-1)

def a_value_Adri(x,y):
    return mean_Adri(y)-(b_value_Adri(x, y)*mean_Adri(x))

def b_value_Adri(x,y):
    return cov_Adri(x,y)/var_Adri(x)

# Y predict or Y hat
def y_pred_Adri(x,y):
    y_hat_list = list()
    a = a_value_Adri(x,y)
    b = b_value_Adri(x,y)
    for i in x:
        y_hat_list.append((b*i)+a)
    return y_hat_list

#R-squared
def r_squared_Adri(y,y_p):
    mn = mean_Adri(y)
    residual = list()
    Tot_sum = list()
    for i,j in zip(y, y_p):
        residual.append((i-j)**2)
        rss=summation_Adri(residual)
    for i in y:
        Tot_sum.append((i-mn)**2)
        tss=summation_Adri(Tot_sum)
    return 1-(rss/tss)

#MSE(Mean Squared Error)
def mse_Adri(y,y_p):
    error = list()
    for i,j in zip(y,y_p):
        error.append((i-j)**2)
    return (1/count_Adri(y))*summation_Adri(error)

#Absolute
def absolute_2019_1_60_024(series):    
    return ((series*series)**0.5);

#MAE(Mean Absolute Error)
def mae_Adri(y,y_p):
    error = list()
    for i,j in zip(y,y_p):
        error.append(absolute_2019_1_60_024(i-j))
    return (1/count_Adri(y))*summation_Adri(error)

#Task 3 Module
def dot_2019_1_60_024(v1,v2):
    result=[[summation_Adri(a*b for a,b in zip(X_row,Y_col)) for Y_col in zip(*v2)] 
            for X_row in v1]
    return result

def transpose_2019_1_60_024(matrix):
    rows = count_Adri(matrix)
    columns = count_Adri(matrix[0])
    trans_mat=[]
    for j in range(columns):
        row = []
        for i in range(rows):
           row.append(matrix[i][j])
        trans_mat.append(row)
    return trans_mat

def weights_2019_1_60_24(x,y):  
    import numpy as np
    tp=transpose_2019_1_60_024(x)
    dot1=dot_2019_1_60_024(tp,x)
    length= count_Adri(dot1)
    print("Length of matrix is: ", length)
    #det = determinant_adri(dot1,length)
    #det = np.linalg.det(x)
    inverse= np.linalg.inv(dot1)
    dot2= dot_2019_1_60_024(tp,y)
    weight= dot_2019_1_60_024(inverse,dot2)
    print("Weight :",weight)
    return weight

''' if det== 0:
        print("The determinant is", det ,"\nSo, inverse matrix cannot be calculated")
    else:
        inverse=cofactor_adri(dot1,length)'''
   
