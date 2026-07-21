# 📖 Chapter 1: Series
# A Series is a one-dimensional labeled array...
# Simple meaning:
# A Series is a single column of data with index numbers...


#Example:-
# import pandas as pd
# data=[10, 20, 30, 40, 50]
# s=pd.Series(data)
# print(s)# now we have a Series with index numbers (0, 1, 2, 3, 4) and corresponding values (10, 20, 30, 40, 50)...
#Series = Single column...
#DataFrame = Complete table (rows and columns)...

# Practice...
# Without running the code:
# a = pd.Series([50,60,70,80,90])
# print(a[1])
# print(a[4])
# What will be printed? 😊...

# Important Question
# What do you think this will print?
# a = pd.Series([50,60,70,80,90])
# print(a[-1])
# Options:
# A) 90
# B) Error
# C) 50
# Guess first. This is where Pandas behaves a little differently from normal Python lists 😊...
 #Ans is B) Error,becauese pandas tries to find the lable index -1,which is not avaible so pandas will throw
# an error,but in numpy the ans will be 90[-1]which is valid...

# 🚀 Pandas Go Go Go – Day 2
# Today we'll learn:
# Custom Index
# .loc[]
# .iloc[]
# Practice Questions...

# before we go ahead we already see that pandas make its own index form series but now this time we wil make our
# own index...

# import pandas as pd
# a=pd.Series([10,20,30,40],index=['a','b','c','d']) 
# print(a)# now series you know this time we used index parameter to create our own index for the series...

# Practice 1
# Predict the output:
# a = pd.Series([10,20,30], index=["X","Y","Z"])
# print(a)
# What will be displayed?...
#ans is x 10,y 20,z 30...

#.loc[]
# .loc[] means:
# Access data using INDEX LABELS.
# Example:...
# import pandas as pd
# abc = pd.Series([10, 20, 30, 40], index=['a', 'b', 'c', 'd'])
# print(abc.loc['b'])#now its target is b so ans is 20...

# .iloc[]
# .iloc[] means:
# Access data using POSITION...
#Example...
# import pandas as pd
# hkl=pd.Series([10, 20, 30, 40], index=['a', 'b', 'c', 'd'])
# print(hkl.iloc[2])#it is like a indexing method in python[Pandas]...
# print(hkl.iloc[-1])# now why we used -1 because iloc works like numpy positions...
#Remeber: .loc[] is used for index labels and .iloc[] is used for positions...

# 🎯 Practice Questions
# For this Series:
# a = pd.Series(
#     [50,60,70],
#     index=["P","Q","R"]
# )
# Answer without running code:
# Q1
# print(a["Q"])
# Q2
# print(a.loc["R"])
# Q3
# print(a.iloc[0])
# Q4
# print(a.iloc[-1])
# Give all 4 answers😎...

# Final Challenge 🏆
# Predict the output:
# a = pd.Series(
#     [100,200,300,400],
#     index=["A","B","C","D"]
# )
# print(a.loc["B"])
# print(a.iloc[2])
# print(a.iloc[-2])
# Give the 3 outputs in order...

# Tomorrow's Topic
# 🚀 Series Attributes
# shape
# size
# ndim
# dtype
# index
# values
# And of course, we'll do prediction questions before running code, just like today.
# You've been answering the practice questions correctly, which shows you're understanding the concepts rather than memorizing them.
# See you tomorrow! 👋...

# Pandas Go Go Go – Day 3: Series Attributes
# Today we'll learn:
# .shape
# .size
# .ndim
# .dtype
# .index
# .values...

# import pandas as pd
# pop=pd.Series([100,200,300,400])
# print(pop.shape)# it will give the shape of the series, which is (4,) because there are 4 elements in the series...
# print(pop.size)# it will give the size of the series, which is 4...
# print(pop.ndim)# it will give the number of dimensions of the series, which is 1...
# print(pop.dtype)# it will give the data type of the series, which is int64...
# print(pop.index)# it will give the index of the series, which is RangeIndex(start=0, stop=4, step=1)...
# print(pop.values)# it will give the values of the series as a numpy array ex output [100,200,300,400]...

# Day 4: Series Slicing
# Today we'll learn Slicing in Pandas Series.
# Since you've learned NumPy, this will feel familiar...


#  1️⃣ What is Slicing?
# Slicing means:
# Taking a portion of the data...

# Example:
# import pandas as pd
# a = pd.Series([10,20,30,40,50])
# print(a[1:4])
# Output:
# 1    20
# 2    30
# 3    40
# dtype: int64
# Understanding 1:4
# a[start:stop]
# Rule:
# Start = Included ✅
# Stop = Excluded ❌
# So:
# a[1:4]
# means:
# Take index 1
# Take index 2
# Take index 3
# Don't take index 4
# Result:
# 20
# 30
# 40
# 2️⃣ Same Rule as NumPy
# a = pd.Series([10,20,30,40,50])
# print(a[0:3])
# Output:
# 10
# 20
# 30
# Indexes taken:
# 0 ✅
# 1 ✅
# 2 ✅
# 3 ❌
# 3️⃣ From Beginning
# print(a[:3])
# Output:
# 10
# 20
# 30
# Meaning:
# Start from beginning
# Stop before index 3
# 4️⃣ Till End
# print(a[2:])
# Output:
# 30
# 40
# 50
# Meaning:
# Start at index 2
# Go till end
# 5️⃣ Entire Series
# print(a[:])
# Output:
# 10
# 20
# 30
# 40
# 50
# Everything is returned.
# 6️⃣ Negative Slicing
# print(a[-3:])
# Output:
# 30
# 40
# 50
# Explanation:
# -1 → 50
# -2 → 40
# -3 → 30
# Start from third-last element and go till the end...

# # Practice Questions...
# Given:
# a = pd.Series([100,200,300,400,500])
# Index	Value
# 0	100
# 1	200
# 2	300
# 3	400
# 4	500
# Q1
# a[1:4]
# Indexes:
# 1 ✅
# 2 ✅
# 3 ✅
# 4 ❌
# Output:
# 200
# 300
# 400
# ✅ Correct
# Q2
# a[:2]
# Indexes:
# 0 ✅
# 1 ✅
# 2 ❌
# Output:
# 100
# 200
# ✅ Correct
# Q3
# a[3:]
# Output:
# 400
# 500
# ✅ Correct
# Q4
# a[-2:]
# Think:
# -1 → 500
# -2 → 400
# Start at 400 and go till the end.
# Output:
# 400
# 500
# ❌ Not 400 to 100
# ✅ Correct answer: 400, 500
# Memory Trick
# For negative indexes:
# 100  200  300  400  500
#  0    1    2    3    4
# -5   -4   -3   -2   -1
# So:
# a[-2:]
# means:
# Start at -2 (400)
# Go till end
# Result:
# 400
# 500
# 🎯 Challenge:
# a = pd.Series([10,20,30,40,50,60])
# Predict:
# Q1
# a[2:5]
# Q2
# a[:4]
# Q3
# a[-3:]
# Q4
# a[1:]
# Answer all 4 without running the code. 😎📊
# 30 to 50,10 to 40,40 to 60,20 to end
# 🎉 Excellent! All 4 are correct.
# Given:
# a = pd.Series([10,20,30,40,50,60])
# Index	Value
# 0	10
# 1	20
# 2	30
# 3	40
# 4	50
# 5	60
# Q1
# a[2:5]
# Indexes taken:
# 2 ✅
# 3 ✅
# 4 ✅
# 5 ❌
# Output:
# 30
# 40
# 50
# ✅ Correct
# Q2
# a[:4]
# Output:
# 10
# 20
# 30
# 40
# ✅ Correct
# Q3
# a[-3:]
# Negative positions:
# -3 → 40
# -2 → 50
# -1 → 60
# Output:
# 40
# 50
# 60
# ✅ Correct
# Q4
# a[1:]
# Start at index 1 and go till end:
# 20
# 30
# 40
# 50
# 60
# ✅ Correct
# One Important Thing
# Since you know NumPy, remember:
# a[start:stop]
# Rule is still:
# Start Included ✅
# Stop Excluded ❌
# This rule appears everywhere:
# Python lists
# NumPy arrays
# Pandas Series
# Later in DataFrames too
# So if you master this once, it helps everywhere.
# 🏆 Today's score: 4/4.
# You're picking up Pandas quickly because the NumPy foundation is helping.
# Before we finish today's lesson, one quick question:
# a = pd.Series([10,20,30,40,50])
# print(a[-4:-1])
# What values will be returned? 🤔📊
# 20 to  40
# 🔥 Correct!
# Given:
# a = pd.Series([10,20,30,40,50])
# Negative positions:
#  10   20   30   40   50
#   0    1    2    3    4
#  -5   -4   -3   -2   -1
# Now:
# a[-4:-1]
# Means:
# Start at -4 ✅ (20)
# Take -3 ✅ (30)
# Take -2 ✅ (40)
# Stop before -1 ❌ (50)
# Output:
# 20
# 30
# 40
# ✅ Your answer "20 to 40" is correct.
# Today's Revision
# Series Slicing
# a[start:stop]
# Rule:
# Start Included ✅Stop Excluded ❌
# Examples:
# a[1:4]
# ➡️ Index 1, 2, 3
# a[:3]
# ➡️ Beginning to index 2
# a[2:]
# ➡️ Index 2 to end
# a[-3:]
# ➡️ Third last to end
# 🏆 At this point you've completed:
# ✅ Series Basics
# ✅ Indexes
# ✅ Custom Indexes
# ✅ [] Accessing
# ✅ .loc[]
# ✅ .iloc[]
# ✅ Series Attributes
# ✅ Series Slicing
# You're building a strong foundation before moving to DataFrames.
# Tomorrow, if you say "Pandas go go go", we'll continue with Series Operations (sum(), mean(), max(), min(), etc.) and more practice🚀📊...

#Pandas Go Go Go – Day 5: Series Operations...
#Today we will learn some operations on Series like sum(), mean(), max(), min(), etc...
# import pandas as pd
# nums=pd.Series(
#     [10,20,40,50])
# print(nums.sum())#sum of all digits...
# print(nums.mean())#sum of all /number of digits...
# print(nums.max())#maximum value...
# print(nums.min())#minimum value...
# print(nums.size)
# print(nums.count())

# In Pandas, size and count() are different.
# Example
# import pandas as pd
# a = pd.Series([10, 20, None, 40, 50])
# Series:
# 0    10
# 1    20
# 2    NaN
# 3    40
# 4    50
# 1. size
# print(a.size)
# Output:
# 5
# size counts all elements, including missing values (NaN).
# 2. count()
# print(a.count())
# Output:
# 4
# count() counts only non-missing values.
# It ignores:
# NaN
# None
# Easy comparison
# Method	Counts
# size	All elements
# count()	Only non-empty values
# For:
# [10, 20, NaN, 40, 50]
# size = 5
# count() = 4
# If there are no missing values
# a = pd.Series([10,20,30,40])
# Then:
# a.size
# ➡️ 4
# a.count()
# ➡️ 4
# Both are the same because nothing is missing...

# 🎯 Practice 1
# Without running code:
# a = pd.Series([100,200,300,400])
# Tell me:
# Q1
# a.sum()
# Q2
# a.mean()
# Q3
# a.max()
# Q4
# a.min()
# Q5
# a.count()
# Give all 5 answers😎📊...

# 🎯 Challenge 2
# a = pd.Series([10,20,30,40,50,60])
# Predict:
# Q1
# a.sum()
# Q2
# a.mean()
# Q3
# a.max()
# Q4
# a.min()
# Q5
# a.count()
# Try all 5. 😎📊
# Hint: First find the sum, then divide by the number of values for the mean...

# Mini Challenge 🏆
# Without running code:
# a = pd.Series([5,15,25,35,45])
# Tell me:
# a.sum()
# a.mean()
# a.max()
# a.min()
# a.count()...

# Your Progress So Far
# Series Basics          ✅
# Indexes                ✅
# Custom Indexes         ✅
# [] Accessing           ✅
# loc[]                  ✅
# iloc[]                 ✅
# Attributes             ✅
# Slicing                ✅
# Operations             ✅
# Filtering              ⏳ Next
# Missing Values         ⏳
# DataFrames             ⏳
# CSV Files              ⏳
# You've built a strong foundation. Because you've been 
# solving the practice questions correctly, I don't think you'll have trouble with filtering...

# See you tomorrow! 🚀📊👋...

# Day 6: Series Filtering (One of the Most Important Topics)
# Welcome back! 😄
# Today we'll learn Filtering.
# This topic is used everywhere:
# Data Analysis ✅
# Machine Learning ✅
# AI ✅
# Real-world datasets ✅
# What is Filtering?
# Filtering means:
# Show me only the data that satisfies a condition...
#Example...
# import pandas as pd
# klu=pd.Series([10,20,30,40,50])
# print(klu>30)# it will return all the values which are greater than 30...
# now ans will be like this:
# 0  False...
# 1  False...
# 2 False...
# 3 True...
# 4 True...
# dtype: bool...
 
#Explanation...
# now we have a series with 5 values and we applied a condition on it which is greater than 30,so the ans will be like this:
# 10>30? False
# 20>30? False
# 30>30? False
# 40>30? True
# 50>30? True
# another thing the number yo can see form 0 to 4 is index numbver of the series...
#Boolen means True or False...

# Example 2
# a = pd.Series([10,20,30,40,50])
# Find values greater than 25.
# a[a > 25]
# Output:
# 30
# 40
# 50
# Example 3
# Find values less than 30.
# a[a < 30]
# Output:
# 10
# 20
# Example 4
# Greater than or equal to
# a[a >= 30]
# Output:
# 30
# 40
# 50
# Example 5
# Less than or equal to
# a[a <= 20]
# Output:
# 10
# 20
# Example 6
# Equal to
# a[a == 40]
# Output:
# 40
# Notice:
# ==
# means compare.
# Not:
# =
# which means assignment.
# Example 7
# Not Equal
# a[a != 30]
# Output:
# 10
# 20
# 40
# 50
# Everything except 30.
# Comparison Operators
# Operator	Meaning
# >	Greater than
# <	Less than
# >=	Greater than or equal to
# <=	Less than or equal to
# ==	Equal to
# !=	Not equal to...

# 🎯 Practice 1
# a = pd.Series([15,25,35,45,55])
# Without running the code, tell me:
# Q1
# a[a > 30]
# Q2
# a[a < 40]
# Q3
# a[a >= 45]
# Q4
# a[a == 25]
# Q5
# a[a != 35]...

# 🎯 Challenge (Slightly Harder)
# Without running the code:
# a = pd.Series([12, 18, 25, 30, 42, 50])
# Predict:
# a[a > 25]
# a[a <= 30]
# a[a != 18]
# Most important question:
# What will this return?
# a > 25
# Not a[a > 25].
# Just:
# a > 25
# 👉 I especially want you to answer Question 4, because if you understand that, 
# you've truly understood filtering...

# one more thing its very important...
# import pandas as pd
# oppo=pd.Series([10,20,30,40])
# print(oppo>23)#1
# print(oppo[oppo>23])#2

# Now understand both gives different ans...
#1 you know the ans i dont need to explain it...
#2 in this this technique is called Boolean Indexing or Boolean Filtering,one of the most used trick in pandas
# even pandas got this trick from numpy,this trich gives order 
# that dont show me the checklist show me the actuall numbers...

#Outputs...
# #1... 0 false
#       1 False
#       2 true
#       3 True
#    dtype: bool

#2...  2  30
#        3  40
#  dtype: int64

# in both you can see the output difference #1 shows boolen but in 2 shows the actuall numbers...

# 🏆 Your Homework Question (Think Before Tomorrow)
# Without running the code, tell me what this returns:
# a = pd.Series([10,20,30,40,50])
# a[a >= 20]
# Two questions:
# What is the Boolean Series produced by a >= 20?
# What is the final filtered output of a[a >= 20]?
# If you can answer both, then you've truly mastered Pandas filtering🚀📊...

# 🏆 I'm Really Happy With Your Progress
# Do you remember a few days ago when we started with:
# pd.Series([10,20,30])
# Now look what you can do:
# ✅ Create Series
# ✅ Understand indexes
# ✅ Use custom indexes
# ✅ Use []
# ✅ Use .loc[] and .iloc[]
# ✅ Understand attributes (shape, size, ndim, dtype, index, values)
# ✅ Slice Series
# ✅ Perform operations (sum, mean, max, min, count)
# ✅ Filter data using Boolean conditions
# That's a big jump in just a few sessions.
# 📅 Tomorrow's Plan (1 Hour)
# We'll continue with multiple conditions, such as:
# a[(a > 20) & (a < 50)]
# a[(a == 10) | (a == 50)]
# You'll learn:
# & (AND)
# | (OR)
# ~ (NOT)
# These are used constantly in real-world Pandas code.
# ⭐ Your Current Progress
# Series Basics           ✅
# Indexes                 ✅
# Custom Indexes          ✅
# []                      ✅
# .loc[]                  ✅
# .iloc[]                 ✅
# Series Attributes       ✅
# Series Slicing          ✅
# Series Operations       ✅
# Single Condition Filter ✅
# Multiple Conditions     ⏳ Next
# DataFrames              ⏳ After Series
# You're following the lessons consistently, and it's showing. Keep this pace, and when we start DataFrames, 
# you'll find them much easier because all these Series concepts carry over...

# 🚀 Pandas Go Go Go – Day 7: Multiple Conditions (AND, OR, NOT)
# Welcome back! 😄
# Yesterday you mastered single-condition filtering.
# Today we'll learn:
# ✅ & (AND)
# ✅ | (OR)
# ✅ ~ (NOT)
# These are used all the time in data analysis...

# 1️⃣ AND (&)
# Suppose we have:
# import pandas as pd
# a = pd.Series([10,20,30,40,50,60])
# Now we want values:
# Greater than 20
# Less than 50
# Both conditions must be true.
# a[(a > 20) & (a < 50)]
# Step 1
# a > 20
# Result:
# 0    False
# 1    False
# 2    True
# 3    True
# 4    True
# 5    True
# Step 2
# a < 50
# Result:
# 0    True
# 1    True
# 2    True
# 3    True
# 4    False
# 5    False
# Step 3
# Now Pandas compares both:
# Value	>20	<50	AND (&)
# 10	F	T	F
# 20	F	T	F
# 30	T	T	T
# 40	T	T	T
# 50	T	F	F
# 60	T	F	F
# Only where both are True:
# 30
# 40
# Important Rule
# Notice the brackets:
# (a > 20)
# (a < 50)
# Then:
# (a > 20) & (a < 50)
# Always put each condition inside parentheses...


# 2️⃣ OR (|)
# Suppose we want:
# Value is 10
# OR value is 60
# a[(a == 10) | (a == 60)]
# Result:
# 10
# 60
# Only one condition needs to be True.
# Example:
# Value	==10	==60	OR
# 10	T	F	T
# 20	F	F	F
# 30	F	F	F
# 40	F	F	F
# 50	F	F	F
# 60	F	T	T
# Output:
# 10
# 60
# 3️⃣ NOT (~)
# NOT means:
# Reverse True and False.
# Example:
# a[~(a > 30)]
# First:
# a > 30
# Result:
# False
# False
# False
# True
# True
# True
# Now ~ reverses it:
# True
# True
# True
# False
# False
# False
# Output:
# 10
# 20
# 30


# Memory Tricks
# & (AND)
# Both conditions must be true.
# True  & True  = True
# True  & False = False
# False & True  = False
# False & False = False
# | (OR)
# At least one must be true.
# True  | True  = True
# True  | False = True
# False | True  = True
# False | False = False
# ~ (NOT)
# Reverse it.
# True  → False
# False → True...

#solve this a easy challenge...
# import pandas as pd
# a = pd.Series([5,10,15,20,25,30])
# print(a[(a>10) & (a<30)])
# print(a[(a == 5) |  (a == 30)])
# print((a > 10) & (a < 30))
#find by your self no ans will be provided...

#🎯 One Last Challenge...
# import pandas as pd
# a = pd.Series([2,4,6,8,10])
# print(a[(a >= 4) & (a <= 8)])
#print(a[~(a == 6)])
# print(a[(a==6)])
#What is the Boolean Series for:
#print(a >= 8)

# Only for help...
# ✅ Q1
# a[(a >= 4) & (a <= 8)]
# Output:
# 1    4
# 2    6
# 3    8
# dtype: int64
# ✅ Correct!
# ✅ Q2
# a[~(a == 6)]
# Output:
# 0     2
# 1     4
# 3     8
# 4    10
# dtype: int64
# ✅ Correct!
# ✅ Q3
# a >= 8
# Output:
# 0    False
# 1    False
# 2    False
# 3     True
# 4     True
# dtype: bool
# ✅ Correct!...

# 📈 Your Pandas Progress
# Series Basics           ✅
# Indexes                 ✅
# Custom Indexes          ✅
# []                      ✅
# .loc[]                  ✅
# .iloc[]                 ✅
# Series Attributes       ✅
# Series Slicing          ✅
# Series Operations       ✅
# Single Filtering        ✅
# Multiple Filtering      ✅
# You're doing really well. At this pace, you won't just know Pandas—you'll understand why it works.
# 🗓️ Tomorrow's Topic
# We'll learn some very useful Series methods:
# unique()
# nunique()
# value_counts()
# Example:
# a = pd.Series([10,20,20,30,30,30])
# print(a.unique())
# print(a.nunique())
# print(a.value_counts())
# These are extremely useful when analyzing real datasets...

# Day 8: unique(), nunique(), value_counts()
# Welcome back! 😄
# Today we'll learn three very useful functions that are used in almost every data analysis project...

# using unique() function...
# import pandas as pd
# a=pd.Series([10,20,10,30,40,40,30])
# print(a.unique())
#lets understand the function...
#in list you see there are many clone numbers or we can say duplicate,we dont want duplicate numbers we want
# original numbers so we used unique() which is function in pandas, his work is to remove duplicate numers from
# the list and give correct output...
# ans=[10,20,30,40] 

# 2️⃣ nunique()
# It returns the number of unique values.
# Using the same Series:
# print(a.nunique())
# Output:
# 4
# Because the unique values are:
# 10
# 20
# 30
# 40
# There are 4 unique values...

#lets understand this function with another example
# import pandas as pd
# b=pd.Series([10,20,10,20,30,30,40])
# # print(b.unique())
# print(b.nunique())
# now you know th e work of unique...
# but if we ask about nunique()this tells the totla number of original value not count duplicate...
# ex ([10,20,10,20,30,30,40]) the output will be >>> 4 now explain 10 20 30 40 duplicate vlaue not count...

# 3️⃣ value_counts()
# This tells us:
# How many times each value appears.
# Example:
# a = pd.Series([10,20,20,30,30,30,40])
# print(a.value_counts())
# Output:
# 30    3
# 20    2
# 10    1
# 40    1
# dtype: int64
# Meaning
# Value	Appears
# 30	3 times
# 20	2 times
# 10	1 time
# 40	1 time
# Notice:
# value_counts() automatically arranges the result from highest count to lowest count.
# Memory Tricks 🧠
# unique()
# Give me the different values.
# Example:
# 10 20 20 30 30 40
# ↓
# 10 20 30 40
# nunique()
# Count the different values.
# 10 20 30 40
# ↓
# 4
# value_counts()
# Count how many times each value occurs.
# 30 → 3
# 20 → 2
# 10 → 1
# 40 → 1...

# 🎯 Practice 1
# a = pd.Series([5,5,10,15,15,20,20,20])
# Without running the code, answer:
# Q1
# a.unique()
# Q2
# a.nunique()
# Q3
# a.count()
# Q4
# a.value_counts()
# Write it in Pandas format.
# Example:
# 20    3
# 15    2
# ...
# dtype: int64
# ⭐ Interview Tip
# Many beginners confuse:
# count()
# nunique()
# Remember:
# count()   = Total values
# nunique() = Different values only
# Your turn! 😎
# Answer all 4 questions. Take your time...

# ✅ Q1
# a.unique()
# You answered:
# 5 10 15 20
# ✅ Correct!
# Pandas output:
# array([ 5, 10, 15, 20])
# (When printed, it appears as a NumPy array.)
# ✅ Q2
# a.nunique()
# You answered:
# 4
# ✅ Correct!
# ✅ Q3
# a.count()
# You answered:
# 8
# ✅ Correct!
# There are 8 total values.
# ✅ Q4
# a.value_counts()
# You answered:
# 5=2,10=1,15=2,20=3
# ✅ Correct concept!
# Pandas prints it like this:
# 20    3
# 5     2
# 15    2
# 10    1
# dtype: int64
# ⚠️ Notice something important!
# Pandas sorts by count (highest to lowest).
# So:
# 20 appears 3 times → first
# 5 appears 2 times
# 15 appears 2 times
# 10 appears 1 time → last...

# 🎯 Quick Challenge (One Last)
# a = pd.Series([1,2,2,3,3,3,4,4,4,4])
# Predict:
# Q1
# a.unique()
# Q2
# a.nunique()
# Q3
# a.count()
# Q4
# a.value_counts()
# 📈 Your Progress
# You've now completed almost the entire Series section.
# Series Basics            ✅
# Indexes                  ✅
# loc / iloc               ✅
# Attributes               ✅
# Slicing                  ✅
# Operations               ✅
# Single Filtering         ✅
# Multiple Filtering       ✅
# unique()                 ✅
# nunique()                ✅
# value_counts()           ✅
# We're getting very close to finishing Series. After a couple more topics and a revision test,'
# we'll move on to DataFrames, which are the heart of Pandas...

# 📅 Next Topic (Tomorrow)
# We'll learn Missing Values, one of the most important real-world topics.
# Example:
# a = pd.Series([10,20,None,40,None])
# You'll learn:
# isnull()
# notnull()
# dropna()
# fillna()
# These are used constantly because real datasets almost always contain missing data...

# Pandas Go Go Go – Day 9: Missing Values (NaN)
# Welcome back! 😄
# Today we'll learn one of the most important topics in Pandas.
# In real life, data is often incomplete.
# Example:
# Name	Marks
# Ram	90
# Shyam	❌ Missing
# Mohan	80
# Ravi	❌ Missing
# Pandas represents missing values as NaN (Not a Number)...

# 1️⃣ Creating a Series with Missing Values
# import pandas as pd

# a = pd.Series([10, 20, None, 40, None])
# print(a)

# Output:

# 0    10.0
# 1    20.0
# 2     NaN
# 3    40.0
# 4     NaN
# dtype: float64
# 🤔 Why float64?

# Notice the integers became:

# 10.0
# 20.0
# 40.0

# Because NaN is stored as a floating-point value, Pandas converts the whole Series to float64.

# 2️⃣ isnull()

# This tells us which values are missing.

# a.isnull()

# Output:

# 0    False
# 1    False
# 2     True
# 3    False
# 4     True
# dtype: bool

# Meaning:

# False → Value exists ✅
# True → Value is missing ❌
# 3️⃣ notnull()

# The opposite of isnull().

# a.notnull()

# Output:

# 0     True
# 1     True
# 2    False
# 3     True
# 4    False
# dtype: bool

# Meaning:

# True → Value exists ✅
# False → Missing value ❌
# 4️⃣ dropna()

# This removes missing values.

# a.dropna()

# Output:

# 0    10.0
# 1    20.0
# 3    40.0
# dtype: float64

# Notice:

# The NaN values are gone.
# The original indexes (0, 1, 3) remain.
# 5️⃣ fillna()

# Instead of removing missing values, we can replace them.

# Example:

# a.fillna(0)

# Output:

# 0    10.0
# 1    20.0
# 2     0.0
# 3    40.0
# 4     0.0
# dtype: float64

# Or:

# a.fillna(100)

# Output:

# 0     10.0
# 1     20.0
# 2    100.0
# 3     40.0
# 4    100.0
# dtype: float64
# 🧠 Memory Trick
# Function	Meaning
# isnull()	Is this value missing?
# notnull()	Is this value present?
# dropna()	Remove missing values
# fillna(x)	Replace missing values with x...

# Given:

# a = pd.Series([5, None, 15, None, 25])

# The Series looks like:

# 0     5.0
# 1     NaN
# 2    15.0
# 3     NaN
# 4    25.0
# dtype: float64
# ✅ Q1
# a.isnull()

# You answered:

# false true false true false

# ✅ Correct!

# Pandas output:

# 0    False
# 1     True
# 2    False
# 3     True
# 4    False
# dtype: bool
# ✅ Q2
# a.notnull()

# You answered:

# true false true false true

# ✅ Correct!

# Pandas output:

# 0     True
# 1    False
# 2     True
# 3    False
# 4     True
# dtype: bool
# ✅ Q3
# a.dropna()

# You answered:

# 0 5 2 15 4 25

# ✅ Correct! (Good observation that the original indexes remain.)

# Pandas output:

# 0     5.0
# 2    15.0
# 4    25.0
# dtype: float64
# ✅ Q4
# a.fillna(0)

# You answered:

# nan values to 0 value means they will get value 0

# ✅ Correct concept!

# Pandas output:

# 0     5.0
# 1     0.0
# 2    15.0
# 3     0.0
# 4    25.0
# dtype: float64
# 🏆 Score: 4/4

# Excellent! You understood all four functions.

# 🎉 Congratulations!

# You have now completed the Series section of our course.

# ✅ Series Basics
# ✅ Default & Custom Indexes
# ✅ [] Accessing
# ✅ .loc[]
# ✅ .iloc[]
# ✅ Attributes
# ✅ Slicing
# ✅ Operations
# ✅ Single Filtering
# ✅ Multiple Filtering
# ✅ unique()
# ✅ nunique()
# ✅ value_counts()
# ✅ Missing Values
# 📅 What Next?

# I recommend that our next session be a Series Revision Test. It will include:

# Predict the output
# Find the mistake
# MCQs
# Short coding questions

# If you do well on that, then start DataFrames, which are the most important part of Pandas...

# Pandas Series Revision Test (Part 1)

# Time: ~1 hour
# Rules:

# ❌ Don't run the code.
# 🧠 Think first, then answer.
# 📝 Write answers in Pandas format where appropriate.

# There are 20 questions. We'll do them in 4 '
# 'rounds of 5 questions so it doesn't become overwhelming...

# 🟢 Round 1 – Basics & Attributes (5 Questions)
# Q1
# import pandas as pd

# a = pd.Series([100,200,300,400])

# Predict:

# a.shape
# Q2

# Using the same Series:

# a.size
# Q3

# Using the same Series:

# a.ndim
# Q4
# b = pd.Series(["Ram","Shyam","Mohan"])

# Predict:

# b.dtype
# Q5
# c = pd.Series(
#     [50,60,70],
#     index=["A","B","C"]
# )

# Predict:

# c.values
# 🏆 Scoring
# Each question = 2 marks
# Round 1 = 10 marks

#Ans...
# Q1
# a.shape

# Your answer:

# (4,)

# ✅ Correct (2/2)

# Q2
# a.size

# Your answer:

# 4

# ✅ Correct (2/2)

# Q3
# a.ndim

# Your answer:

# 1

# ✅ Correct (2/2)

# Q4
# b = pd.Series(["Ram","Shyam","Mohan"])

# b.dtype

# Your answer:#i think if you gaved 

# string

# ❌ Not quite.

# ✅ Correct answer:

# object

# Remember:

# Numbers → int64
# Decimal numbers → float64
# Text → object

# (In modern Pandas, there is also a
# dedicated "string" dtype, but 
# in the examples we've been 
# practicing, text Series
# typically have dtype 
# object. For our course 
# and revision, answer object.)

# Score: 0/2

# Q5
# c.values

# Your answer:

# [50 60 70]

# ✅ Correct (2/2)...

# 🚀 Round 2 – Indexing, loc[], iloc[], Slicing

# Given:
# import pandas as pd
# a = pd.Series([10,20,30,40,50], 
# index=["A","B","C","D","E"])
# Q6
# a["C"]
# Q7
# a.loc["D"]
# Q8
# a.iloc[1]
# Q9
# a[1:4]

# Write the values returned.

# Q10
# a[-2:]

# Write the values returned.

# 🎯 Try to get 10/10 in this round!🚀📊...

# Given:

# a = pd.Series([10,20,30,40,50], index=["A","B","C","D","E"])

# It looks like:

# Label	Value
# A	10
# B	20
# C	30
# D	40
# E	50
# ✅ Q6
# a["C"]

# Your answer:

# 30

# ✅ Correct (2/2)

# ✅ Q7
# a.loc["D"]

# Your answer:

# 40

# ✅ Correct (2/2)

# ✅ Q8
# a.iloc[1]

# Your answer:

# 20

# ✅ Correct (2/2)

# ✅ Q9
# a[1:4]

# Your answer:

# B    20
# C    30
# D    40

# ✅ Correct (2/2)

# Notice:

# Start = Included ✅
# Stop = Excluded ❌

# So indexes 1, 2, 3 are selected.

# ✅ Q10
# a[-2:]

# Your answer:

# D    40
# E    50

# ✅ Correct (2/2)

# 🏆 Round 2 Score
# Question	Marks
# Q6	✅ 2/2
# Q7	✅ 2/2
# Q8	✅ 2/2
# Q9	✅ 2/2
# Q10	✅ 2/2
# Total: 10/10 🌟
# 📊 Overall Score So Far
# Round 1: 8/10
# Round 2: 10/10

# Total: 18/20 (90%) 🎉

# You're right on track for your goal of 90%+.

# Next we'll do Round 3, which covers:

# sum()
# mean()
# max()
# min()
# count()
# Filtering with conditions

# You're doing a great job 
# predicting outputs without 
# running the code—that's exactly 
# the skill we want to build🚀📊...

# 🚀 Pandas Series Revision Test – Round 3

# Marks: 10 (2 marks each)

# This round covers:

# Operations
# Filtering

# Given:

# import pandas as pd

# a = pd.Series([10,20,30,40,50])
# Q11

# Predict:

# a.sum()
# Q12

# Predict:

# a.mean()
# Q13

# Predict:

# a[a > 25]

# Write the output in Pandas format.

# Q14

# Predict:

# a[(a >= 20) & (a < 50)]

# Write the output in Pandas format.

# Q15

# This is the most important question.

# Predict the Boolean Series:

# a > 30

# Write it in Pandas format.

# 🏆 Current Score
# ✅ Round 1: 8/10
# ✅ Round 2: 10/10

# Current Total: 18/20

# 🎯 Try to get 10/10 in this 
# round! If you do, you'll have 28/30,
# which is an outstanding score.

# Take your time and answer like this:

# Q11:
# Q12:
# Q13:
# Q14:
# Q15:

# 🚀 Go go go!...

# Let's check everything.

# Given:

# a = pd.Series([10,20,30,40,50])
# ✅ Q11
# a.sum()

# Your answer:

# 150

# ✅ Correct (2/2)

# ✅ Q12
# a.mean()

# Your answer:

# 30

# ✅ Correct (2/2)

# ✅ Q13
# a[a > 25]

# Your answer:

# 2    30
# 3    40
# 4    50
# dtype: int64

# ✅ Correct (2/2)

# ✅ Q14
# a[(a >= 20) & (a < 50)]

# Your answer:

# 1    20
# 2    30
# 3    40
# dtype: int64

# ✅ Correct (2/2)

# ✅ Q15
# a > 30

# Your answer:

# 0    False
# 1    False
# 2    False
# 3     True
# 4     True
# dtype: bool

# ✅ Perfect! (2/2)

# 🏆 Round 3 Score
# Question	Marks
# Q11	✅ 2/2
# Q12	✅ 2/2
# Q13	✅ 2/2
# Q14	✅ 2/2
# Q15	✅ 2/2
# Total: 10/10 🌟🌟🌟
# 📊 Overall Score
# ✅ Round 1: 8/10
# ✅ Round 2: 10/10
# ✅ Round 3: 10/10
# Current Total: 28/30 (93.3%) 🥇

# Excellent work! You're 
# comfortably above our 90% goal.

# 🎯 Final Round (Round 4)

# This last round will test:

# unique()
# nunique()
# value_counts()
# isnull()
# fillna()

# If you do well here, we'll '
# 'officially complete the Series '
# 'Revision Test and then you're ready 
# to begin DataFrames in the next lesson.

# 🚀 One more round to go!...

# 😄 Let's go! Final Round! 🔥

# 🚀 Pandas Series Revision Test – Round 4 (Final)

# Marks: 10 (2 marks each)

# Given:

# import pandas as pd

# a = pd.Series([10,20,20,30,None,30,40])
# Q16

# Predict:

# a.unique()
# Q17

# Predict:

# a.nunique()
# Q18

# Predict:

# a.value_counts()

# Write it in Pandas format.

# Q19

# Predict:

# a.isnull()

# Write it in Pandas format.

# Q20

# Predict:

# a.fillna(0)

# Write it in Pandas format.

# 🎯 Target
# 36–40 marks → 🌟 Excellent
# 32–35 marks → 👍 Very Good
# Below 32 → Quick revision before DataFrames
# 📢 And yes...

# If you complete this round 
# successfully, then in the 
# next session (tomorrow)
# we'll officially start DataFrames. 🎉

# We'll begin from the absolute basics:

# What is a DataFrame?
# Difference between Series and DataFrame.
# Creating DataFrames.
# Rows and Columns.
# Accessing data.

# This is the biggest and most 
# exciting part of Pandas because
# it's what you'll use most in real projects...

# 🏆 Final Evaluation – 
# Pandas Series Revision Test

# Excellent effort! Let's check the final round.

# Given:

# a = pd.Series([10,20,20,30,None,30,40])
# ✅ Q16
# a.unique()

# Your answer:

# [10. 20. 30. nan 40.]

# ✅ Correct (2/2)

# Pandas returns the unique 
# values, including NaN.

# ✅ Q17
# a.nunique()

# Your answer:

# 4

# ✅ Correct (2/2)

# nunique() does not count NaN by default.

# Unique values are:

# 10
# 20
# 30
# 40

# Total = 4

# ✅ Q18
# a.value_counts()

# Your answer:

# 20.0    2
# 30.0    2
# 10.0    1
# 40.0    1
# Name: count, dtype: int64

# ✅ Correct (2/2)

# Excellent! (Depending on the 
#             Pandas version, you may 
#             or may not see 
#             the Name: count line, 
#             but your answer is 
#             perfectly acceptable.)

# ✅ Q19
# a.isnull()

# Your answer:

# 0    False
# 1    False
# 2    False
# 3    False
# 4     True
# 5    False
# 6    False
# dtype: bool

# ✅ Correct (2/2)

# ✅ Q20
# a.fillna(0)

# Your answer:

# 0    10.0
# 1    20.0
# 2    20.0
# 3    30.0
# 4     0.0
# 5    30.0
# 6    40.0
# dtype: float64

# ✅ Correct (2/2)

# #check and score by youself and give marks
# #  politely and give percentage also...

# 🎓 Series Course Status
# Series Basics            ✅
# Indexes                  ✅
# Custom Indexes           ✅
# []                       ✅
# .loc[]                   ✅
# .iloc[]                  ✅
# Attributes               ✅
# Slicing                  ✅
# Operations               ✅
# Single Filtering         ✅
# Multiple Filtering       ✅
# unique()                 ✅
# nunique()                ✅
# value_counts()           ✅
# Missing Values           ✅

# SERIES COMPLETED 🎉
# 📅 Tomorrow's Mission

# 🚀 Start DataFrames

# We'll begin with:

# What is a DataFrame?
# Difference between a Series and a DataFrame.
# Creating DataFrames from lists and dictionaries.
# Understanding rows and columns.
# Accessing data.
# 🌟 One thing I want to say

# I'm genuinely impressed by your progress.

# When we started Pandas, don't  mixed up:

# .shape and .size
# .loc[] and .iloc[]
# count() and nunique()

# Now you're correctly predicting:

# Boolean Series
# Filtering
# value_counts()
# Missing value functions
# Pandas-style output

# That improvement didn't 
# happen by luck—it happened 
# because you consistently
#  practiced instead of just reading.

# 🏁 Next Session

# Just type:

# Pandas go go go

# and we'll officially
# begin DataFrames, the most
# important part of Pandas...




     


