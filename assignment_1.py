# -*- coding: utf-8 -*-
"""assignment 1

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1AfoS8E5Q3pk9NsPRAitw8IktR0odAlft
"""

# 1.split this string 
s='Hi there sam!'
s=s.split()
print(s);

#2 Use.format()to print the following string 
planet="earth"
diameter=12742
print('the diameter of {} is {} kilometers'.format(planet,diameter))

#3 In this nest dictionary grab the word"hello"
d = {'k1':[1,2,3,{'tricky':['oh','man','inception',{'target':[1,2,3,'hello']}]}]}
print(d['k1'][3]["tricky"][3]['target'][3])

"""Numpy"""

#4.1 create an array of 10 zeros
import numpy as np
array=np.zeros(10)
print("An array of 10 zeros:")
print(array)

#4.2 create an array of 10 fives
import numpy as np 
array=np.ones(10)*5
print("An array of 10 fives:")
print(array)

#5 create an array of all even integers from 20 to 35
import numpy as np
array=np.arange(20,36,2)
print("Array of all the even integers from 20 to 35")
print(array)

#6. create a 3x3 matrix with values ranging from 0 to 8
import numpy as np
x =  np.arange(0, 9).reshape(3,3)
print(x)

#7 Concatenate a and b
import numpy as np
 
a = np.array([1, 2, 3])
print(a)
 
b = np.array([4, 5, 6])
print(b)
 
print('\n---Result of a and b---')
print(np.concatenate((a, b)))

"""Pandas"""

#8. create a dataframe with 3 rows and 2 columns
import pandas as pd
import numpy as np

exam_data  = {'name': ['jay', 'prem', 'param', 'James', 'Emily', 'Michael', 'Matthew', 'Laura', 'Kevin', 'Jonas'],
        'score': [12.5, 9, 16.5, np.nan, 9, 20, 14.5, np.nan, 8, 19]}
labels = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']

df = pd.DataFrame(exam_data , index=labels)
print("First three rows of the data frame:")
print(df.iloc[:3])

#9.Generate the series of datas from 1st han ,2023 to 10th feb,2023
import datetime
import pandas as pd
test_date = datetime.datetime.strptime("01-01-2023", "%d-%m-%Y")
K = 41
date_generated = pd.date_range(test_date, periods=K)
print(date_generated.strftime("%d-%m-%Y"))

#10. create 2D list to Dataframe
import pandas as pd
lists=[[1, 'aaa', 22],[2, 'bbb', 25], [3, 'ccc', 24]]
df=pd.DataFrame(lists)
print(df)