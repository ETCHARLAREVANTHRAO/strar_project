from tkinter import *
import numpy as np

class Matrix:

    def matrix_additon(self):

        rows = row.get()
        cols = col.get()
        rows, cols = int(rows), int(cols)
        mat1, mat2 = arr1.get(), arr2.get()
        matrix1 = [int(i) for i in mat1.split()]
        matrix2 = [int(j) for j in mat2.split()]
        temp = []
        f_mat1 = np.resize(matrix1, (rows, cols))
        f_mat2 = np.resize(matrix2, (rows, cols))
        print("The Addition of Two matrixes are: ")
        print("Step 1: The Matrix 1 is taken")
        print(f_mat1)
        print("Step 2: The Matrix 2 is taken")
        print(f_mat2)
        print("Step 3: The Matrix 1 + Matrix is ")
        for i in range(2):
            a = []
            for j in range(2):
                y = str(f_mat1[i][j]) + '+' + str(f_mat2[i][j])
                a.append(y)
            temp.append(a)
        print(np.array(temp))
        print("Step 4: Final Result is : ")

        print(np.array(f_mat1) + np.array(f_mat2))


    def matrix_substraction(self):
        rows = row.get()
        cols = col.get()
        rows, cols = int(rows), int(cols)
        mat1, mat2 = arr1.get(), arr2.get()
        matrix1 = [int(i) for i in mat1.split()]
        matrix2 = [int(j) for j in mat2.split()]
        temp = []
        f_mat1 = np.resize(matrix1, (rows, cols))
        f_mat2 = np.resize(matrix2, (rows, cols))
        print("The Addition of Two matrixes are: ")
        print("Step 1: The Matrix 1 is taken")
        print(f_mat1)
        print("Step 2: The Matrix 2 is taken")
        print(f_mat2)
        print("Step 3: The Matrix 1 - Matrix is ")
        for i in range(2):
            a = []
            for j in range(2):
                y = str(f_mat1[i][j]) + '-' + str(f_mat2[i][j])
                a.append(y)
            temp.append(a)
        print(np.array(temp))
        print("Step 4: Final Result is : ")

        print(np.array(f_mat1) - np.array(f_mat2))


    def matrix_multiply(self):
        rows = row.get()
        cols = col.get()
        rows, cols = int(rows), int(cols)
        mat1, mat2 = arr1.get(), arr2.get()
        matrix1 = [int(i) for i in mat1.split()]
        matrix2 = [int(j) for j in mat2.split()]
        temp = []
        f_mat1 = np.resize(matrix1, (rows, cols))
        f_mat2 = np.resize(matrix2, (rows, cols))
        result = np.resize(temp, (rows, cols))
        for i in range(len(f_mat1)):
            for j in range(len(f_mat2[0])):
                for k in range(len(f_mat2)):
                    result[i][j] += f_mat1[i][k] * f_mat2[k][j]
        print("The multiplication of the matrix ", f_mat1, "and matrix ", f_mat2, "is: ")

        for r in result:
            print(r)


if __name__ == '__main__':
    root = Tk()
    row = StringVar()
    col = StringVar()
    arr1 = StringVar()
    arr2 = StringVar()
    obj = Matrix()
    Label(root, text="Rows").grid(row=0, column=0)
    text1 = Entry(root, textvariable=row, bd=5).grid(row=0, column=1)

    Label(root, text="Columns").grid(row=0, column=2)
    text2 = Entry(root, textvariable=col, bd=5).grid(row=0, column=3)

    Label(root, text="Matrix 1").grid(row=1, column=0)
    text3 = Entry(root, textvariable=arr1, bd=5).grid(row=1, column=1)

    Label(root, text="Matrix 2").grid(row=1, column=2)
    text4 = Entry(root, textvariable=arr2, bd=5).grid(row=1, column=3)

    Button(root, text="Add", bd=4,padx=20, fg="Orange", command=obj.matrix_additon).grid(row=2, column=0)
    Button(root, text= "Sub", bd=4, padx= 20, fg= "Orange", command= obj.matrix_substraction).grid(row=2, column=1)
    Button(root, text="Mul", bd=4, padx=20, fg="Orange", command=obj.matrix_multiply).grid(row=2, column=2)
    Button(root, text="Answer", bd=4,padx=20, fg="green", command=root.quit).grid(row=2, column=3)

    output = Text(root, width=100, height=20)
    root.mainloop()
