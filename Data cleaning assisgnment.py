#Data Cleaning Assignment
import pandas as pd
import numpy as np
df = pd.DataFrame({'From_To': ['LoNDon_paris', 'MAdrid_miLAN', 'londON_StockhOlm','Budapest_PaRis', 'Brussels_londOn'],
                   'FlightNumber': [10045, np.nan, 10065, np.nan, 10085],
                   'RecentDelays': [[23, 47], [], [24, 43, 87], [13], [67, 32]],
                   'Airline': ['KLM(!)', '<Air France> (12)', '(British Airways. )','12. Air France', '"Swiss Air"']})

pd.pandas.set_option('display.max_columns',None)

'''1.Some values in the the FlightNumber column are missing. These numbers are 
meant to increase by 10 with each row so 10055 and 10075 need to be put in 
place. Fill in these missing numbers and make the column an integer column 
(instead of a float column)'''
#Solution
df['FlightNumber']=df['FlightNumber'].interpolate().astype('int32')
print(df)

'''2. The From_To column would be better as two separate columns! Split each 
string on the underscore delimiter _ to give a new temporary DataFrame with 
the correct values. Assign the correct column names to this temporary 
DataFrame.'''
#Solution
df_temp=df['From_To'].str.split('_',expand=True)
df_temp.columns=['From','To']
print(df_temp)

'''3. Notice how the capitalisation of the city names is all mixed up in this 
temporary DataFrame. Standardise the strings so that only the first letter 
is uppercase (e.g. "londON" should become "London".)''' 
#Solution
df_temp['From']=df_temp['From'].str.title()
df_temp['To']=df_temp['To'].str.title()
print(df_temp)

'''4.Delete the From_To column from df and attach the temporary DataFrame 
from the previous questions.'''
#Solution
df=df.drop('From_To',axis=1).join(df_temp)
print(df)

'''5. In the RecentDelays column, the values have been entered into the 
DataFrame as a list. We would like each first value in its own column, each second value in its own column, and so on. If there isn't an Nth value, the value 
should be NaN'''
#Solution
delays=pd.DataFrame(df['RecentDelays'].values.tolist())
delays.columns=['delay1','delay2','delay3']
print(delays)
df=df.drop('RecentDelays',axis=1).join(delays)
print(df)


































