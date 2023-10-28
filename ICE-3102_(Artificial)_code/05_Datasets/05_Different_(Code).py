import pandas as pd
data= { 'Name': ['Jai','princi','Guarav', 'Anju','Ravi,Natasha','Riya'],
       'Age': [17,17,18,17,18,17,17],
       'Gender':['M',['F'],['N'],['M'],['M'],['F'],['F']],
         'Marks': [90,76, 'NaN', 74,65, 'NaN', 71]}

a=pd.DataFrame(data)

print(a,"/n")

b=pd.read_csv('1.car driving risk analysis.csv')
print("Read Dataset from csv file\n")
print(b)

import numpy as np
import statistics as stats 
import pandas as pd
data=pd.read_csv('dd.csv')
print('Dataset:\n', data)

mean=np.mean(data['num'])
print('Mean:',mean)

median=np.median(data['num'])
print('median:',median)

mode=stats.mode(data['gender'])
print('Mode:',mode)

varience=np.var(data['num'])
print('Variance:',varience)

std_dev=np.std(data['num'])
std_dev=round(std_dev,2)
print('Standard Deviation:', std_dev)



