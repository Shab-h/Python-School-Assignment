
# coding: utf-8

# Before you turn this problem in, make sure everything runs as expected. First, **restart the kernel** (in the menubar, select Kernel$\rightarrow$Restart) and then **run all cells** (in the menubar, select Cell$\rightarrow$Run All).
# 
# Make sure you fill in any place that says `YOUR CODE HERE` or "YOUR ANSWER HERE", as well as your name and collaborators below:

# In[ ]:

NAME = "Shahab Hassan, Hassas20, 400085601, 11/15/17"
COLLABORATORS = ""


# ---

# # <center>Major Assignment 4 Version 2</center>
# -------------
# <b><center>ENGINEER 1D04</center><b>
# <b><center>Dr. Ashgar Bokhari</center><b>
# <b><center>McMaster University, Fall 2017</center><b>

# ## Background
# ----------------
# This assignment deals with interpreting a table of weather simulation data, to predict the daily weather. Say that when a weather simulation program runs, it creates a row of output in the form of a Python list:
# 
#     row = [hour, temperature, relHumidity, [cloudCover, cloudHeight], [windSpdLow, windSpdHigh]]
# 
# where `hour` is an integer between 0 and 23 representing hours past midnight, `temperature` is a float in Celsius, `relHumidity` and `cloudCover` are percents (floats) between 0 and 1, `cloudHeight` is an integer in metres, and both `windSpdLow` and `windSpdHigh` are floats in km/h.
# The simulation runs $n$ times, and returns the final result as a list of rows:
# 
#                                     data = [ row_1, row_2, ..., row_n ]
#                                     
# Your program will contain a set of functions that can be used to interpret this list of simulation rows.
#                                     
# Design, implement, and test a program that satisfies the requirements below.
# 
# -------------------
# ## Requirements
# 1. Implement the function `isTempBetween(row, minTemp, maxTemp)`, which takes ONE ROW of a weather simulation (`[hour, temp, etc.]`) and two floats `minTemp` and `maxTemp`, and returns `True` if `temperature` for that row is between `minTemp` and `maxTemp`, `False` otherwise.<br><br>
# 
# 2. Implement the function `isCloudCoverOver(row, percent)`, which takes ONE ROW of a weather simulation (`[hour, temp, etc.]`) and a float `percent`, and returns `True` if `cloudCover` for that row is above `percent`, `False` otherwise. <br><br>
# 
# 3.  Implement the function `isCloudHeightBetween(row, minHeight, maxHeight)`, which takes ONE ROW of a weather simulation (`[hour, temp, etc.]`) and two integers `minHeight` and `maxHeight`, and returns `True` if `cloudHeight` for that row is between `minHeight` and `maxHeight`, `False` otherwise. <br><br>
# 
# 4.  Implement the function `freezingRainChance(data)`, which takes a list of weather simulation rows (`[row1, row2, etc.]`), and returns the list `[chance, time]`. <br>`chance` is a float between 0 and 1 representing the chance that freezing rain will occur, and `time` is an integer defined as the range of time freezing rain could be present: <br><br>
# $$chance = \frac{Number\hspace{0.15cm}of\hspace{0.15cm}rows\hspace{0.15cm}in\hspace{0.15cm}data\hspace{0.15cm}that\hspace{0.15cm}indicate\hspace{0.15cm}freezing\hspace{0.15cm}rain }{Total\hspace{0.15cm}number\hspace{0.15cm}of\hspace{0.15cm}rows\hspace{0.15cm}in\hspace{0.15cm}data}$$ 
#  
#  
# $$\texttt{time} = \frac{\sum\texttt{hour}\hspace{0.15cm}of\hspace{0.15cm}each\hspace{0.15cm}row\hspace{0.15cm}in\hspace{0.15cm}data\hspace{0.15cm}that\hspace{0.15cm}indicates\hspace{0.15cm}freezing\hspace{0.15cm}rain}{Number\hspace{0.15cm}of\hspace{0.15cm}rows\hspace{0.15cm}in\hspace{0.15cm}data\hspace{0.15cm}that\hspace{0.15cm}indicate\hspace{0.15cm}freezing\hspace{0.15cm}rain}$$ <br><br>For our purposes, a row indicates freezing rain if `cloudCover` $>$ 0.9, `temperature` is between -10 and 0, and `cloudHeight` is between 1000 and 2000. 
# 
# `NOTE:` If no rows of `data` indicate freezing rain, then `time` should be equal to zero.
# 
# 5. The program requires very little besides the function definitions. There is no main().<br><br>
# 
# 6. Your name, MacID, student number, and the date are given in comments at the top of the first Python cell below.<br><br>
# 
# 7. Your answers to the design questions and test plan are given in the appropriate Markdown cells below.<br><br>
# 
# 8. Your program MUST have valid Python syntax and it must run without errors. Ensure that your program runs properly by running it before you submit.<br><br>
# 
# 9. You must sign out with a TA or IAI after you have submitted your lab at the submission station. Failure to do so could result in a mark of zero.
# ------------------
# ## Design and Implementation Instructions
# 
# 1. You may assume that inputs will be within a valid range and of the correct type, and that exception handling is not necessary.<br><br>
# 2. Follow the function syntax **EXACTLY** as given, including spelling, capitalization and the order of function paramaters.
# 
# ------------------

# ## isTempBetween(row, minTemp, maxTemp) - (2 Points)

# In[1]:

#This Function check if the temperature of the input row is between the min and max temperature, returns true if between, and false if not.
def isTempBetween (row, minTemp, maxTemp):
    
    temp = row[1]
    #This if statements check is the temperature is between the min and max temperatures.
    if temp > maxTemp:
        return False
    elif temp > minTemp:
        return True
    else: 
        return False


# In[2]:

data = [ [0, 1.5, 0.4, [0.3, 42], [5.1, 10.0] ], 
		[10, 1.4, 0.3, [0.2, 41], [6.2, 8.6] ],	
		[3, -5.1, 0.91, [0.83, 21], [107.1, 108.1] ],
		[12, -6.3, 0.94, [0.91, 30], [106.5, 109.4] ],
		[18, 20.5, 0.4, [0.3, 12000], [60.1, 162.4] ],
		[2, 20.4, 0.3, [0.2, 11000], [105.6, 118.7] ],
		[5, -9.2, 0.2, [0.93, 1001], [6.2, 6.3] ],
		[15, -2.4, 0.1, [0.95, 1981], [7.4, 8.5] ] ]

assert isTempBetween(data[0], 1.4, 1.6) == True
assert isTempBetween(data[1], 1.4, 3) == False
assert isTempBetween(data[7], -21, -5) == False
print("Tests Successful")


# ## isCloudCoverOver(row, percent) - (2 Points)

# In[3]:

#This Function checks if the could cover percent for the input row in above the percent, if above returns True, else returns False.
def isCloudCoverOver(row, percent):
    
    cloudCover = row[3][0]
    #This if statement check if the cloudCover is above the percent, and returns true if yes, and returns false if no.
    if cloudCover > percent:
        return True
    else:
        return False
    


# In[4]:

data = [ [0, 1.5, 0.4, [0.3, 42], [5.1, 10.0] ],
		[10, 1.4, 0.3, [0.2, 41], [6.2, 8.6] ],
		[3, -5.1, 0.91, [0.83, 21], [107.1, 108.1] ], 
		[12, -6.3, 0.94, [0.91, 30], [106.5, 109.4] ], 
		[18, 20.5, 0.4, [0.3, 12000], [60.1, 162.4] ], 
		[2, 20.4, 0.3, [0.2, 11000], [105.6, 118.7] ], 
		[5, -9.2, 0.2, [0.93, 1001], [6.2, 6.3] ], 
		[15, -2.4, 0.1, [0.95, 1981], [7.4, 8.5] ] ] 

assert isCloudCoverOver(data[2], 0.2) == True
assert isCloudCoverOver(data[4], 0.5) == False
assert isCloudCoverOver(data[6], 0.93) == False
print("Tests Successful")


# ## isCloudHeightBetween(row, minHeight, maxHeight) - (2 Points)

# In[5]:

#This Function takes cloud height from the input row and return tru if between minHeight and maxHeight, false otherwise.
def isCloudHeightBetween(row, minHeight, maxHeight):
    
    cloudHeight = row[3][1]
    #This if statement returns true if cloudHeight is between minHeight and Maxheight, false otherwise.
    if cloudHeight > maxHeight:
        return False
    elif cloudHeight > minHeight:
        return True
    else: 
        return False
    


# In[6]:

data = [ [0, 1.5, 0.4, [0.3, 42], [5.1, 10.0] ], 
		[10, 1.4, 0.3, [0.2, 41], [6.2, 8.6] ],
		[3, -5.1, 0.91, [0.83, 21], [107.1, 108.1] ], 
		[12, -6.3, 0.94, [0.91, 30], [106.5, 109.4] ], 
		[18, 20.5, 0.4, [0.3, 12000], [60.1, 162.4] ], 
		[2, 20.4, 0.3, [0.2, 11000], [105.6, 118.7] ], 
		[5, -9.2, 0.2, [0.93, 1001], [6.2, 6.3] ], 
		[15, -2.4, 0.1, [0.95, 1981], [7.4, 8.5] ] ] 

assert isCloudHeightBetween(data[1], 24, 44) == True
assert isCloudHeightBetween(data[3], 30, 35) == False
assert isCloudHeightBetween(data[5], 0, 10999) == False
print("Tests Successful")


# ## freezingRainChance(data) - (4 Points)

# In[8]:

#This funtion checks all the rows that indicate freezing rain and returns a list conatining the probability of freezing rain, and the hours of freezing rain.
def freezingRainChance(data):
    
    dataLen = len(data)
    freezingRainRowNum = 0
    timeFreezing = 0
    tempVar = 0
    
    #Assigning the parameters for freezing rain
    percent = 0.9
    minTemp = -10
    maxTemp = 0
    minHeight = 1000
    maxHeight = 2000
    
    #This while Loop filters thruw the data and summs up the rows that indicate freezing rain and hours for the row which indicate freezing rain conditions.
    while tempVar < dataLen:
        if isCloudCoverOver(data[tempVar], percent) and isTempBetween (data[tempVar], minTemp, maxTemp) and isCloudHeightBetween(data[tempVar], minHeight, maxHeight):
            freezingRainRowNum += 1
            timeFreezing += data[tempVar][0]
        tempVar +=1
            
    chanceFreezRain = freezingRainRowNum / dataLen
   
    #This if statemtn set time equal to zero if there are noe data rows which indicate freezing rain conditions. else calculates the time hours of freezing rain 
    if freezingRainRowNum == 0:
        totalTime = 0
    else:
        totalTime = timeFreezing / freezingRainRowNum
    
    finalList = [chanceFreezRain , totalTime]
    return finalList 


# In[9]:

data = [ [0, 1.5, 0.4, [0.3, 42], [5.1, 10.0] ],
		[10, 1.4, 0.3, [0.2, 41], [6.2, 8.6] ],
		[3, -5.1, 0.91, [0.83, 21], [107.1, 108.1] ], 
		[12, -6.3, 0.94, [0.91, 30], [106.5, 109.4] ], 
		[18, 20.5, 0.4, [0.3, 12000], [60.1, 162.4] ], 
		[2, 20.4, 0.3, [0.2, 11000], [105.6, 118.7] ], 
		[5, -9.2, 0.2, [0.93, 1001], [6.2, 6.3] ], 
		[15, -2.4, 0.1, [0.95, 1981], [7.4, 8.5] ] ] 

data2 = [[5, -29.7, 0.81, [0.1, 756],[4.6, 99.0] ], 
         [20, -5.6, 0.7, [0.93, 1200],[11.2, 81.8] ], 
         [23, -1.7, 0.94, [0.23, 857],[123.6, 148.9] ], 
         [8, -30.1, 0.97, [0.84, 45],[29.1, 80.0] ], 
         [1, 25.0, 0.81, [0.1, 12001],[101.6, 150.9] ] ] 

data3 = [[1, 25.0, 0.81, [0.1, 12001],[101.6, 150.9] ]]

assert freezingRainChance(data) == [0.25, 10.0]
assert freezingRainChance(data2) == [0.2, 20.0]
assert freezingRainChance(data3) == [0, 0]
print("Tests Successful")


# ## Code Legibility (3 Points)
# ----------
# Your code will be marked on commenting and code legibility.<br\>
# The mark breakdown is as follows:<br\>
# 1 mark for using appropriate variable names that indicate what is being stored in that variable<br\>
# 1 mark for leaving comments on major parts of your code such as where you read the file or calculate a summation<br\>
# 1 mark for general legibility. The TA's should be able to understand your code without spending hours reading it. For example do not put your code in one very long line as this is hard for someone else reading your code to understand
# 
# <h6>Ignore the empty cell below. You do NOT need to type anything in it </h6>

# YOUR ANSWER HERE

# ## Design Question (4 Points)
# -------------------
# 1. What is the difference between `elif` and `else`? 
# 2. How could your `freezingRainChance` function use `Try-Except` to improve the robustness of your program? You do not actually need to implement any `Try-Except` blocks.
# 3. If your code has 3 `else` statements in it, what is the minimum number of `if` statements that your code would need? Explain your answer.
# 4. Does your `freezingRainChance` function work if the input `data` is empty? Why or Why not?
# 
# Enter your answers into the Markdown cell below.

# Q1. 
# Elif takes in a paramter which must equal tru for the block of code to run, while else is the last resort wich runs without any parametrs.
# 
# Q2. 
# You can use Try-except in the FreezingRainChance() funtion by replacing lines (26-29), the if statment of total time hours of freezing rain and replacing it with Try-Except to except division by zero and return zero.
# 
# Q3.
# You would need 3 if statements, because the else statent always comes at the end of and if staments. however and if statment dosent always need an else statment
# 
# Q4.
# In my specific funtion it wouldnt work, infact it would return a zero division error on line (23), to solve this problem I could use a try-except or an if estatement to prevent the zero division. 

# ## Testing Plan (3 Points)
# ---------------
# Produce a test plan in the Markdown cell below, in the following form:
# 
# `Test i for function j
# Input: inputs for function j
# Expected Output: expected output for function j
# Actual Output: actual output for function j
# Result: Pass/Fail
# `
# 
# Note: The actual output should be what the program produces, even if your output does not match the expected output.
# 
# You must have $NO$ $LESS$ $THAN$ $3$ $TEST$ $CASES$. Have at least 1 case where your program does not output an error. For the other cases, we encourage you to try and find test cases where your program would output an error (not mandatory, just recommended). That is, where the expected output is an error.

# `Test 1 for freezingRainChance(data)
# Input: ([])
# Expected Output: Zero Division Error (line 23)
# Actual Output: ZeroDivisionError: division by zero
# Result: Pass
# `
# 
# `Test 2 for isTempBetween (row, minTemp, maxTemp)
# Input: ([],0,0)
# Expected Output: list index out of range
# Actual Output: IndexError: list index out of range
# Result: Pass
# `
# 
# `Test 3 for isTempBetween (row, minTemp, maxTemp)
# Input: ([0, 1, 0, [0, 4], [5, 10] ] , 1000 ,1000)
# Expected Output: False
# Actual Output: False
# Result: Pass
# `
