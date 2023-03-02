#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Feb 24 14:09:28 2023

@author: polina
"""
import copy
import math
from random import randint

class Matrix:
    def __init__(self, n, m, data=None, fill=None):
        self.matrix = [[fill for j in range(m)] for i in range(n)]
        if data != None: self.matrix = data
        self.rows = n
        self.cols = m
        self.size = (n, m)

    def get_readable_matrix_string(self, matrix):
        strings = []
        for row in matrix:
            strings.append(str(row))
        return '\n'.join(strings)  

    def __str__(self):
        return self.get_readable_matrix_string(self.matrix)
    
    def __len__(self):
        return len(self.matrix)

    def __getitem__(self, item):
        return self.matrix[item]
    
    def __setitem__(self, index, value):
        self.matrix[index] = value
    
    def __setitems__(self, value):
        self.matrix = value

    def __getElement__(self, i, j):
        return self.matrix[i-1][j-1]
    
    def __contains__(self, elem):
        for row in self.matrix:
            for element in row:
                if element == elem: return True
                else: pass
        return False
    
    def random(self, fr=-2, to=7):
        for row in self.matrix:
            for i in range(self.cols):
                row[i] = randint(fr, to)

    def get_transposed(self):
        result = Matrix(self.cols, self.rows, fill=0)
        if self.cols > 1:
            for i in range(self.rows):
                for j in range(self.cols):
                    result[j][i]=self.matrix[i][j]
        else:
            for i in range(self.rows):
                result[0][i] = self.matrix[i]
        return result
    
    def __transpose__(self):
        self.m = self.get_transposed(self.m)

    
    def __mul__(self, other):
        result = Matrix(self.rows, other.cols, fill=0)
        if isinstance(other, Matrix):
            for i in range(self.rows):
                for j in range(other.cols):
                    for k in range(other.rows):
                        result[i][j] += self.matrix[i][k] * other[k][j]
            return result
#            return self.get_readable_matrix_string(self.multiply(other))
        return self.get_readable_matrix_string([[num*other for num in row] for row in self.matrix])
    
    def __add__(self, other):
        result = Matrix(self.rows, self.cols, fill=0)
		#adds the corresponding elements of two matrices
        if isinstance(other, Matrix):
            for i in range(self.rows):
                for j in range(self.cols):
                    result.matrix[i][j] = self.matrix[i][j] + other.matrix[i][j]

		#adds a scalar to every element of A
        elif isinstance(other, (int, float)):
           
            for i in range(self.rows):
                for j in range(self.cols):
                    result[i][j] = self.matrix[i][j] + other
    
    def __subtract__(self, other):
        result = Matrix(self.rows, self.cols, fill=0)
		#subtracts the corresponding elements of two matrices
        if isinstance(other, Matrix):
            for i in range(self.rows):
                for j in range(self.cols):
                    result.A[i][j] = self.A[i][j] - other.A[i][j]

		#subtracts a scalar from every element of A
        elif isinstance(other, (int, float)):
           
            for i in range(self.rows):
                for j in range(self.cols):
                    result[i][j] = self.A[i][j] - other

        return result
    
    def concat(a, b):
        if a.cols == 1: a = Matrix(len(a), 1, [[i] for i in a])
        if b.cols == 1: b = Matrix(len(b), 1, [[i] for i in b])
        if a.rows != b.rows:
            raise AttributeError("can't concatenate matrices with different row number")
        result = Matrix(a.rows, a.cols + b.cols)
        for i in range(a.cols):
            for j in range(a.rows):
                result[j][i] = a[j][i]
        for i in range(b.cols):
            for j in range(b.rows):
                result[j][i + a.cols] = b[j][i]
        return result
    
    def concat_rows(a, b):
        if a.cols == 1: a = Matrix(len(a), 1, [[i] for i in a])
        if b.cols == 1: b = Matrix(len(b), 1, [[i] for i in b])
        if a.cols != b.cols:
            raise AttributeError("can't concatenate matrices with different row number")
        result = Matrix(a.rows + b.rows, a.cols)
        for i in range(a.rows):
            for j in range(a.cols):
                result[i][j] = a[i][j]
        for i in range(b.rows):
            for j in range(b.cols):
                result[i+a.rows][j] = b[i][j]
        return result

    def get_inversed(self):
        if self.is_square():
            result = Matrix(self.rows, self.cols)
        
        else: raise AttributeError(f"""Can't inverse matrix as it is not square ({self.rows}x{self.cols})""")
        
    def is_square(self):
        return self.cols == self.rows
    
    #def det(self):
        
    def eye(n, element=1):
        result = Matrix(n, n, fill=0)
        for i in range(n):
            result[i][i] = element
        return result
    
    #def find_LU(self):
        
    def diag_prod(self):
        if self.is_square():
            return math.prod([self.matrix[i][i] for i in range(self.rows)])
        else: print("Matrix is not square ({self.rows}x{self.cols})")
    
    def swap_rows(self, i, j):
        self.matrix[i], self.matrix[j] = self.matrix[j], self.matrix[i]
        
    def forward_elimination(self, b):
        P = Matrix.eye(self.rows)
#        .
        for i in range(0, self.rows):
            
            max_el_index = i
            while(max_el_index < self.rows and self.matrix[max_el_index][i] == 0):
                max_el_index += 1
            if(max_el_index == self.rows):
                continue
            if(max_el_index != i):
                self.swap_rows(i, max_el_index)
                P.swap_rows(i, max_el_index)

            for j in range(i+1, self.rows):     
                for k in range(0, self.rows):
                    self.matrix[j][k] = (self.matrix[i][i]*self.matrix[j][k]) - (self.matrix[j][i]*self.matrix[i][k])
      
#     
#    def back_substitution(self, b):
#        result = Matrix(b.rows, 1)
#        if not isinstance(b, Matrix):
#            raise AttributeError("unsupported parameter type '{}' for parameter b, b has to be Matrix".format(type(b)))
#
#        if self.rows != self.cols:
#            raise AttributeError("only square matrices are supported for lu decomposition")
#
#        for i in range(self.rows - 1, -1, -1):
#            if abs(self.matrix[i][i]) < self.EPS:
#               raise AttributeError("Matrix is singular")
#            result[i] /= self.matrix[i][i]
#            for j in range(0, i):
#                result[j] -= self.matrix[j][i] * b[i]

a = Matrix(3, 3, data=[[1, 2, 3], [1, 1, 0], [0, 1, 1]])
print(a)
c = Matrix(3, 1, data=[1, 1, 1])
print(c)
c.transpose()
print(c)
