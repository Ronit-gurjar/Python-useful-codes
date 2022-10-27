'''Program for matrix multiplication of two matrices that are input taken from user.Developed by
@Ronit-gurjar on github. If you liked the code be sure to satr it on github'''
def matrixMaker(R,C,Temp):
    matrix = []
    if Temp==1:
        for i in range(R):		 
            a=[]
            for j in range(C):
                a.append(0)
            matrix.append(a)

    else:
    
        print("Enter the entries rowwise:")
        for i in range(R):		 
            a =[]
            for j in range(C):
                print("{",i,j,"}index:")
                ele = int(input(":"))
                a.append(ele)
            matrix.append(a)

    return matrix

print("enter rows and column for 1st matrix >>:")
R1 = int(input("rows:"))
C1 = int(input("columns:"))
A=matrixMaker(R1,C1,0)


print("enter rows and column for 2nd matrix >>:")
R2 = int(input("rows:"))
C2 = int(input("columns:"))
B=matrixMaker(R2,C2,0)

print("matrix 1:",A)
print("matrix 2:",B)

result = matrixMaker(C1,R2,1)
 
# iterating by row of A
for i in range(len(A)):
 
    # iterating by column by B
    for j in range(len(B[0])):
 
        # iterating by rows of B
        for k in range(len(B)):
            result[i][j] += A[i][k] * B[k][j]
 
for r in result:
    print(r)