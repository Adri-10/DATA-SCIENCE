# -*- coding: utf-8 -*-
"""
Created on Sat Aug 28 04:26:21 2021

@author: Adri Saha
"""
#Task 1

def determinant_2019160024(mat,n):
    det=0
    sign=1
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
            det=det+sign*(mat[0][x]*determinant_2019160024(a,n-1))
            sign=-1*sign
    return det
    

def inverse_adri(inverse,d,adj,r):
    for i in range(r):
        for j in range(r):
            inverse[i][j] = adj[i][j]/d        
    print("\nThe inverse Matrix is:")
    for i in range(r):
        for j in range(r):
            print(round(inverse[i][j],2),end = " ")
        print()
        
def transpose_adri(num,cofac,n):
    adjugate = [[0 for i in range(n)] for j in range(n)]
    inverse = [[0 for i in range(n)] for j in range(n)]
    for i in range(n):
        for j in range(n):
            adjugate[i][j]=cofac[j][i]
    det=determinant_2019160024(num,n)
    inverse_adri(inverse,det,adjugate,n)
    
    
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
            cofactor[x][y]=((-1)**(x+y))*determinant_2019160024(mat,n-1)
    transpose_adri(num,cofactor,n)

#main
#Adri Saha
#ID: 2019-1-60-024

print("Enter rowwise entries of the", 3, "x", 3, "Matrix:")
matrix=[]
for i in range(0,3): 
   matrix.append([int(j) for j in input().split()]) 

print('\nThe matrix is:')
for i in range(3): 
    for j in range(3): 
        print(matrix[i][j], end = " ") 
    print() 

d=determinant_2019160024(matrix,3)
if d==0:
    print("The determinant is", d ,"\nSo, inverse matrix cannot be calculated")
else:
    cofactor_adri(matrix,3)

