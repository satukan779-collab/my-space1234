#What is NumPy?

# NumPy is a Python library used for:

# Fast calculations
# Arrays
# Mathematics
# AI/Data Science work

# Normally Python lists are slower for heavy calculations.
# NumPy arrays are much faster and powerful...

#Practice 1...
# import numpy as np 
# aqw = np.array([1,2,3,4,5])
# print(aqw)


# Why NumPy is Important in AI/Data Science

# Used in:

# Machine Learning
# AI
# Data Analysis
# Image Processing
# Mathematical operations

# Libraries like:

# Pandas
# TensorFlow
# Scikit-learn

# all depend heavily on NumPy internally...

#practice 2...
# import numpy as np
# marks=np.array([85,90,44,78,98])
# print(marks)

# Small Challenge 🔥

# Create a NumPy array storing:

# Your favorite 5 game names

# and print it.

# Quick Knowledge Check
# What is NumPy used for?
# What does np.array() do?
# Why do we write import numpy as np?
# Is NumPy array faster than normal Python list?

# Answer these first. Then we move to:

# NumPy Dimensions, Shape & Types

# import numpy as np
# games=np.array(["Free Fire","Sausage Man","Legneds of Neverland","Honor of Kings","Call of Duty"])
# print(games)
# #Numpy used for fast calculation used in data analytics,ai,Machine learning and image procesing...
# # np.array is used to store values in a fromat because normal python list is slower and not suitable for heavy calculation...
# # to import and use numpy library in our python code to use it inbuilt features and functions...
# # yes  


#NumPy Dimensions & Shape...
# 1D Array...
# import numpy as np
# uop=np.array([1,2,3,4,5])
# print(uop) # this is 1D array beacuse it has only one row and one column...


# 2D Array...
# import numpy as np
# mat=np.array([ 
#     [1,2,3],
#     [4,5,6]])
# print(mat) # this is 2D array because it has multiple rows and columns Used heavily in:
# Images
# AI datasets
# Cybersecurity logs...

# Shape of Array
# shape tells:
# rows
# columns...
# import numpy as np
# mat=np.array([ 
#     [1,2,3],
#     [4,5,6]])
# print(mat.shape)
# print(mat.ndim)#it tell the dimensions of the array...

# Mini Challenge 🔥
# Create a 2D NumPy array for:
# 3 students
# marks in 3 subjects
# Then print:
# The array
# Shape
# Number of dimensions...
# import numpy as  np
# marks=np.array([
#     ["raohn","sohan","Kohan"],
#     ["Science","Math","English"],
#     [45,65,67],
#     [87,65,32],
#     [34,56,67]
# ])
# print(marks)
# print(marks.shape)#tells you the number of rows and columns...
# print(marks.ndim)#means Number of Dimensions of the array.

#Indexing & Slicing in NumPy Arrays
# (very important for AI + cybersecurity data analysis)...
# 1D Array Indexing...
# import numpy as np

# arr = np.array([10,20,30,40])

# print(arr[3])#the index...

# 2D Array Indexing...
# import numpy as np
# mat=np.array([
#     [1,2,3],
#     [4,5,6]
# ])
# print(mat[1][2])#The first index is for the row and second index is for the column...

# Mini Challenge 🔥
# Create this array:
# [
#  [11,22,33],
#  [44,55,66]
# ]
# Then 
# print:
# 22
# 66
# 44
# using indexing only.
# import numpy as np
# lkj=np.array([
#     [11,22,33],
#     [44,55,66]
# ])
# print(lkj[0][1])  # 22
# print(lkj[1][2])  # 66
# print(lkj[1][0])  # 44

#NumPy Slicing (: operator)...

#1D Array Slicing...
# import numpy as np
# helio=np.array([10,20,90,211])
# print(helio[1:])#This mETHOD is called Slicing, slicing means taking the part from a array of your choice... here start index is included but end index is excluded...
# print(helio[:3])#This will print the elements from index 0 to 2 (excluding 3)...
# print(helio[2:])#This will print the elements from index 2 to the end of the array...
#print(arr[-2:])#This will print the last two elements of the array...-2 is start adn we can see we have not given any end point so python automatically print last two numbers...
 
#2D Array Slicing...
# import numpy as np
# mat=np.array([
#     [1,2,3],
#     [4,5,6],
#     [7,8,9]
# ])
# #print(mat[2])#This will print the third row of the mat array...
# print(mat[0:,2])#This will print the third column of the mat array...(,The comma , is used in 2D (or higher-dimensional) NumPy arrays to separate row and column indexing)...

#Practice 1...
# import numpy as np
# x = np.array([5,10,15,20,25,30])
# print(x[2:5])# Ans 15,20,25

# import numpy as np

# y = np.array([
#     [10,20],
#     [30,40],
#     [50,60]
# ])

# print(y[:,0])#Ans10,30,50...
# #Small Challenge 🔥
# Create this array:
# [
#  [11,22,33],
#  [44,55,66],
#  [77,88,99]
# ]
# Then print:
# First row.
# Last row.
# Second column.
# The subarray:
# [[55,66],
#  [88,99]]
# using slicing only...

# import numpy as np
# arr=np.array([
#     [11,22,33],
#     [44,55,66],
#     [77,88,99]
# ])
# print(arr[0])#first row
# print(arr[2])#last row
# print(arr[:,1])#second column
# print(arr[1:,1:])#the subarray...

# Mini Test (No Coding)
# Answer these quickly:
# What does arr[:2] return?row 
# What does arr[-1] return?last row
# What does arr[:,0] return?column 
# What is the difference between:
# arr[1]shows row
# and
# arr[:,1]shows column
#arr[rows, columns] numpy slicing...

# NumPy Data Types (dtype)
# Under this topic, we'll learn:
# What is dtype?
# Integer (int)
# Float (float)
# String (str)
# Mixed data types
# Checking an array's data type:
# arr.dtype
# Converting data types:
# arr.astype()
# After dtype, we'll study:
# NumPy Mathematical Operations
# +
# -
# *
# /
# NumPy Functions
# sum()
# mean()
# max()
# min()...

#INTEGER ARRAY...
# import numpy as np
# arr=np.array([1])
# print(arr.dtype)#This will print the data type of the elements in the array...
# ans is int64, int menas integer and 64 means The number of bits used to store each integer bit is the smallest unit of computer memory
# it menas that each number uses 64 bit computer memory to store the value in integer...

#FLOAT ARRAY...
# import numpy as np
# arr = np.array([10.5,20.3,30.8])
# print(arr.dtype)# ans is float64, float means decimal numbers and 64 means The number of bits used to store each float value in the array...

# String ARRAY...
# import numpy as np
# arr = np.array(["Ram","Shyam","Mohan"])
# print(arr.dtype)
#<U5 this is ANS, lets break it down:...
# <U5 means is a NumPy data type for strings.< Means the byte order (how the computer stores data)....
# U means the Unicode string data type,It means the array stores text (characters)...
#5 Means the maximum length of a string is 5 characters...

#Mixed Data Type...
# import numpy as np
# arr = np.array([10,20,"Hello",40])
# print(arr)
# print(arr.dtype)
#ANS is <U21 now explanation...
#here are two print() statements because they print two different things.
#Output:
#['10' '20' 'Hello' '40']
#Notice that NumPy converts the numbers to strings because "Hello" is a string.
#or another <U... depending on the NumPy version)
#It means:
#< = byte order (ignore for CBSE).
#U = Unicode string.
#2Why did NumPy convert everything to strings?

#A NumPy array must have one common data type.
# Since "Hello" is a string, NumPy converts:
# 10  → "10"
# 20  → "20"
# 40  → "40"
# So the array becomes:
# ["10", "20", "Hello", "40"]

#Converting Data Type (astype())...
#conver to float...
# import numpy as np
# arr=np.array([10,20,30])
# print(arr.dtype)
# nrr=arr.astype(float)
# print(nrr)

#Convert it into Integer...
# import numpy as np
# arr = np.array([10.5,20.7,30.9])
# newarr = arr.astype(int)
# print(newarr)

#Practice 1...
# import numpy as np
# a = np.array([5,10,15])
# print(a.dtype)

#Practice 2...
# import numpy as np
# b = np.array([1.5,2.5,3.5])
# print(b.dtype)

#Practice 3...
# import numpy as np
# c = np.array([1,2,3])
# d = c.astype(float)
# print(d)
# print(d.dtype)


#Mini Challenge 🔥...
# Write a program that:
# Creates an integer array:
# [100,200,300,400]
# Prints its dtype.
# Converts it to float.
# Prints the new array.
# Prints the new dtype.

# Solution...
# import numpy as np
# cr=np.array([100,200,300,400])
# print(cr.dtype)
# mess=cr.astype(float)
# print(mess)
# print(mess.dtype)
#dtype means Data Type. It tells us what kind of data is stored in a NumPy array...

#NumPy Mathematical Operations
# We'll cover:
# + Addition
# - Subtraction
# * Multiplication
# / Division
# import numpy as np
# a=np.array([10,20,30])
# b=np.array([10,20,30])
# print(a+b)#Addition...
# print(a-b)#Subtraction...
# print(a*b)#Multiplication...
# print(a/b)#Division...Its ouput is in float,because [ / always performs floating-point division]...


# Mini Challenge 🔥...
# Write a program:
# a = [50,100,150]
# b = [10,20,30]
# Print:
# Addition
# Subtraction
# Multiplication
# Division

#solution...
# import numpy as np
# a=np.array([50,100,600])
# b=np.array([10,20,30])
# print(a+b)#ANs is [60,120,630]
# print(a-b)#ANs is [40,80,570]
# print(a*b)#ANs is [500,2000,18000]
# print(a/b)#ANs is [5.0,5.0,20.0]

# Today we'll learn the 4 most important NumPy functions for CBSE and practical programming...
# NumPy Functions
# We'll learn:
# sum()
# mean()
# max()
# min()

# import numpy as np
# marks = np.array([80, 90, 70, 60])
# print(marks.sum())#ANS 300,all values sum....
# print(marks.mean())#ANS 75.0,mean means average,Sum of values ÷ Number of values...
# print(marks.max())#ANS 90, finds the largest value in the array...
# print(marks.min())#ANS 60, finds the smallest value in the array...

#Practice 1...
# import numpy as np
# a = np.array([10,20,30,40,50])
# print(a.sum())#ANS 150
# print(a.mean())#ANS 30.0
# print(a.max())#ANS 50
# print(a.min())#ANS 10

# Mini Challenge 🔥...
# Write a program for:
# scores = [45, 67, 89, 76, 93]
# Convert it into a NumPy array and print:
# Total score
# Average score
# Highest score
# Lowest score

#Solution...
# import numpy as np
# scores=np.array([45,67,89,76,93])
# print(scores.sum())#ANS 360
# print(scores.mean())#ANS 72.0
# print(scores.max())#ANS 93
# print(scores.min())#ANS 45


# A Small Rule Sheet for You 📚

# For a 2D array:

# array[rows, columns]
# Expression	Meaning
# a[1]	Second row
# a[:,1]	Second column
# a[1:,0]	Column 0 from row 1 onwards
# a[0:2,:]	First two rows, all columns
# a[:2,:2]	First two rows and first two columns
# Memory Trick

# Think of it as:

# array[which rows?, which columns?]