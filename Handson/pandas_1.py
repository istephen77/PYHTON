# import pandas as pd
# import numpy as np
#
# ipl_data = {'Team': ['Riders', 'Riders', 'Devils', 'Devils', 'Kings',
#    'kings', 'Kings', 'Kings', 'Riders', 'Royals', 'Royals', 'Riders'],
#    'Rank': [1, 2, 2, 3, 3,4 ,1 ,1,2 , 4,1,2],
#    'Year': [2014,2015,2014,2015,2014,2015,2016,2017,2016,2014,2015,2017],
#    'Points':[876,789,863,673,741,812,756,788,694,701,804,690]}
#
# df = pd.DataFrame(ipl_data)
# print(df)

#Split data into groups
#There are multiple ways to split an on object like :  obj.groupby('key'), obj.groupby(['key1','key2']), obj.groupby(['key1','axis=1'])

# import pandas as pd
#
# ipl_data = {'Team': ['Riders', 'Riders', 'Devils', 'Devils', 'Kings',
#    'kings', 'Kings', 'Kings', 'Riders', 'Royals', 'Royals', 'Riders'],
#    'Rank': [1, 2, 2, 3, 3,4 ,1 ,1,2 , 4,1,2],
#    'Year': [2014,2015,2014,2015,2014,2015,2016,2017,2016,2014,2015,2017],
#    'Points':[876,789,863,673,741,812,756,788,694,701,804,690]}
#
# df = pd.DataFrame(ipl_data)
# print(df.groupby('Team'))    #Output - <pandas.core.groupby.generic.DataFrameGroupBy object at 0x000001F63F3E4FA0>
# print(df.groupby('Team').groups)  #For viewinf the contents of the group


# #Groupby with multiple columns
# import pandas as pd
#
# ipl_data = {'Team': ['Riders', 'Riders', 'Devils', 'Devils', 'Kings',
#    'kings', 'Kings', 'Kings', 'Riders', 'Royals', 'Royals', 'Riders'],
#    'Rank': [1, 2, 2, 3, 3,4 ,1 ,1,2 , 4,1,2],
#    'Year': [2014,2015,2014,2015,2014,2015,2016,2017,2016,2014,2015,2017],
#    'Points':[876,789,863,673,741,812,756,788,694,701,804,690]}
#
# df = pd.DataFrame(ipl_data)
# print(df.groupby(['Team','Year']).groups)


#Iterating through groups - with the groupby object in hand we can iterate through the objects similar to othertools.obj

# import pandas as pd
#
# ipl_data = {'Team': ['Riders', 'Riders', 'Devils', 'Devils', 'Kings',
#    'kings', 'Kings', 'Kings', 'Riders', 'Royals', 'Royals', 'Riders'],
#    'Rank': [1, 2, 2, 3, 3,4 ,1 ,1,2 , 4,1,2],
#    'Year': [2014,2015,2014,2015,2014,2015,2016,2017,2016,2014,2015,2017],
#    'Points':[876,789,863,673,741,812,756,788,694,701,804,690]}
#
# df = pd.DataFrame(ipl_data)
# #print(df)
# grouped = df.groupby('Team')
# for group, name in grouped:
#    print(name)
#    print(group)

#Select a group - using the get_group() method we can select a single group

# import pandas as pd
#
# ipl_data = {'Team': ['Riders', 'Riders', 'Devils', 'Devils', 'Kings',
#    'kings', 'Kings', 'Kings', 'Riders', 'Royals', 'Royals', 'Riders'],
#    'Rank': [1, 2, 2, 3, 3,4 ,1 ,1,2 , 4,1,2],
#    'Year': [2014,2015,2014,2015,2014,2015,2016,2017,2016,2014,2015,2017],
#    'Points':[876,789,863,673,741,812,756,788,694,701,804,690]}
#
# df  = pd.DataFrame(ipl_data)
# grouped = df.groupby('Year')
# print(grouped.get_group(2017))

#Agrregations - returns a single aggregated value for each groups. Once the groupby object is created several aggregation operation can be performed on the group data.

# import pandas as pd
# import numpy as np
#
# ipl_data = {'Team': ['Riders', 'Riders', 'Devils', 'Devils', 'Kings',
#    'kings', 'Kings', 'Kings', 'Riders', 'Royals', 'Royals', 'Riders'],
#    'Rank': [1, 2, 2, 3, 3,4 ,1 ,1,2 , 4,1,2],
#    'Year': [2014,2015,2014,2015,2014,2015,2016,2017,2016,2014,2015,2017],
#    'Points':[876,789,863,673,741,812,756,788,694,701,804,690]}
#
# df = pd.DataFrame(ipl_data)
# grouped = df.groupby('Year')
# print(grouped['Points'].agg(np.mean))

#Another way to see the size of each group is by applying the size function (Aggregatuon - provides summary statistics)

# import pandas as pd
# import numpy as np
#
# ipl_data = {'Team': ['Riders', 'Riders', 'Devils', 'Devils', 'Kings',
#    'kings', 'Kings', 'Kings', 'Riders', 'Royals', 'Royals', 'Riders'],
#    'Rank': [1, 2, 2, 3, 3,4 ,1 ,1,2 , 4,1,2],
#    'Year': [2014,2015,2014,2015,2014,2015,2016,2017,2016,2014,2015,2017],
#    'Points':[876,789,863,673,741,812,756,788,694,701,804,690]}
#
# df = pd.DataFrame(ipl_data)
# grouped = df.groupby('Team')
# print(grouped['Points'].agg(np.size))
# print("*******************")
# print(grouped.agg(np.size))

#Applying multiple aggregation function at once. With grouped series you can also pass a list or dict of functions to do aggregation with and generate DataFrame as output.

# import pandas as pd
# import numpy as np
#
# ipl_data = {'Team': ['Riders', 'Riders', 'Devils', 'Devils', 'Kings',
#    'kings', 'Kings', 'Kings', 'Riders', 'Royals', 'Royals', 'Riders'],
#    'Rank': [1, 2, 2, 3, 3,4 ,1 ,1,2 , 4,1,2],
#    'Year': [2014,2015,2014,2015,2014,2015,2016,2017,2016,2014,2015,2017],
#    'Points':[876,789,863,673,741,812,756,788,694,701,804,690]}
#
# df = pd.DataFrame(ipl_data)
# grouped = df.groupby('Team')
# print(grouped['Points'].agg([np.sum, np.std, np.mean]))

#Transformations - on a group or a column returns an object of the same size that is being grouped. Thus the transform should return a result that is the same size as that of the group chunk.

# import pandas as pd
# import numpy as np
#
# ipl_data = {'Team': ['Riders', 'Riders', 'Devils', 'Devils', 'Kings',
#    'kings', 'Kings', 'Kings', 'Riders', 'Royals', 'Royals', 'Riders'],
#    'Rank': [1, 2, 2, 3, 3,4 ,1 ,1,2 , 4,1,2],
#    'Year': [2014,2015,2014,2015,2014,2015,2016,2017,2016,2014,2015,2017],
#    'Points':[876,789,863,673,741,812,756,788,694,701,804,690]}
#
# df = pd.DataFrame(ipl_data)
# grouped = df.groupby('Team')
# score = lambda x : (x-x.mean())/x.std()*10
# print(grouped.transform(score))

#Filtration - Filtration filters the data on a defined criteria and returns the subset of the data. The filter()

# import pandas as pd
# import numpy as np
#
# ipl_data = {'Team': ['Riders', 'Riders', 'Devils', 'Devils', 'Kings',
#    'kings', 'Kings', 'Kings', 'Riders', 'Royals', 'Royals', 'Riders'],
#    'Rank': [1, 2, 2, 3, 3,4 ,1 ,1,2 , 4,1,2],
#    'Year': [2014,2015,2014,2015,2014,2015,2016,2017,2016,2014,2015,2017],
#    'Points':[876,789,863,673,741,812,756,788,694,701,804,690]}
#
# df = pd.DataFrame(ipl_data)
# print(df.groupby('Team').filter(lambda x : len(x) >=3))
#


#********************* 10 mins to Pandas ************

# import pandas as pd
# import numpy as np

#DataFrame - 2 dimensional, size mutable, potentially heterogeneous tabular data

#Object creation - Creating a 'Series' by passing a list of values, letting pandas create a default integer index
# s = pd.Series([13,42,34,45,np.nan,18,56])
# print(s)

#Creating a Dataframe by passing a numpy array with a datetime index and labeled column
# numpy.random.randn() creates an array of specified shape and fills it with random values as per the standard normal distribution. If positive arguments are provided then randn() generates an array of shape (d0, d1,... ) filled with random float sampled from univariate  normal distribution of mean 0 and variance 1. A single float randomly sampled from the distribution is returned if no argument is provided.
#Randomly constructing 1D array
# import numpy as np
# array = np.random.randn(5)
# print(array)

#Randmly constructing 2D array
# import numpy as np
# array = np.random.randn(4,5)
# print(array)

#Random constructing 3D array
# import numpy as np
# array = np.random.randn(2,2,2)
# print(array)


#Manipulation with randomly created array
# import numpy as np
# array = np.random.randn(2,2)
# print("1", array)
# print("2",array*3)

# import pandas as pd
# import numpy as np
# dates  = pd.date_range("20220418", periods=10)
# df = pd.DataFrame(np.random.randn(10,4), index=dates, columns=list("ABCD"))
# print(df)

#Creating Dataframe by passing a dictionary of objects that can be converetd into a series like structure:
#
# import pandas as pd
# import numpy as np
#
# df2 = pd.DataFrame(
#     {
#         "A": "1.0",
#         "B": pd.Timestamp("20220418"),
#         "C": pd.Series(1, index=list(range(4)), dtype="float32"),
#         "D": np.array([3]*4, dtype="int32"),
#         "E": pd.Categorical(["test","train","test","train"]),
#         "F": "foo",
#     }
# )
# print(df2)
# print(df2.dtypes)

#Viewing  data :

# import pandas as pd
# import numpy as np
#
# dates = pd.date_range("20220418", periods=10)
# df1 = pd.DataFrame(np.random.randn(10,4), index=dates, columns=list("ABCD"))
# print(df1.head())  #Prints top 5 rows of the dataset
# print(df1.tail())  #Prints last 5 rows of the dataset
# print(df1.index)  #Display index
# print(df1.columns)  #Display columns


# Dataframe.to_numpy() gives a Numpy representation of the underlying data. This can be an expensove operation if ur dataset have columns with differnt datatypes, which comes down to a fundamental difference between pandas and numpy. Numpy array have one dtype for the entire array while pandas have one dtype per column. When you call datatype.to_numpy() pandas will call the numpy dtype that can hold all dtypes into the frame. This may end up being an object which requires casting every value to a Python object.

# import pandas as pd
# import numpy as np
# dates = pd.date_range("20220418", periods=10)
# df = pd.DataFrame(np.random.randn(10,4), index=dates, columns=list("ABCD"))
#print(df.to_numpy())  #Returns an array with the same datatype.... to_numpty() doesn't include the index or column label in the output

#describe() shows a quick statistic summary of your data
#print(df.describe())

#Transposting your Data - Reverse the index and column label in x--y to y---> x axis
# print(df.T)
# #Sorting by an axis
# print(df.sort_index(axis=1, ascending=False))   #axis = 1 ---> Sorting of Dates, Ascending = False ---. Sortinf of column
# #Sorting by values
# print(df.sort_values(by = "B"))  #Sorting by a column index or values


#Selection : Optimized pandas data access methods --> .at, .iat, .loc, .iloc

#Getting - Selecting a single column which yields a series equivalent to df.A :

# import pandas as pd
# import numpy as np
# dates = pd.date_range("20220418", periods=10)
# df = pd.DataFrame(np.random.randn(10,4), index=dates, columns=list("ABCD"))
# print(df)
# print(df["A"])  #Selecting via '[]' slices the rows
# print(df[0:3])

#Selecting by Label - For getting a cross section by using a label
# print(df.loc[dates[0]])
# print(df.loc[:,["A","B"]])  #Selecting on a multi-axis by label
# print(df.loc["20220418" : "20220420", ["A","B"] ])   #Showing label slicing, both end points are included
# print(df.loc["20220419"], ["A","B"])  #Reduction in the dimension of the returned object
# print(df.loc[dates[0],"A"])  #For getting a scalar value
# print(df.at[dates[0], "A"])  ##For getting fast access to the above mentioned scalar value
#
# #Select by position : 1) Select the positions via passed integers
# print(df.iloc[3])
# print(df.iloc[3:5, 0:2])  #By integer slices, acting similar to NumPy/Python
# print(df.iloc[[1,2,4], [0,2]])  #By list of integer position location similar to Numpy/Python
# print(df.iloc[1:3, :]) #For slicing rows explicitly
# print(df.iloc[:, 1:2]) #For slicing columns explicitly
# print(df.iloc[1,1])  #For getting a value explicitly

#Boolean Indexing : 1) Using a single columns value to select a data
# print(df[df["A"] >0])

#Selecting values from a dataframe where a boolean condition is met
# print(df[df > 0])

#Using the isin() for filtering
# df2 = df.copy()
# df2["D"] = ["1","2","3","4","5","5","5","6","7","10"]
# print(df2[df2["D"].isin(["5","10"])])

#Setting : setting up a new column in an existing dataset
#
# s1 = pd.Series([1,2,3,4,5,6,7,8,9,10], index=pd.date_range("20220418", periods=10))
#print(s1)
# df["E"] = s1
# #print(df)
# df1 = df.at[dates[0], "A"] = 0  #Setting values by values
# df2 = df.iat[0,1] = 0  #Setting values by using positions
# df3 = df.loc[:,"D"] = np.array([5]*len(df)) #Setting value by using Numpy array
# print(df)

#OPERATIONS : 1) Performing a descriptive statistics

# print(df.mean())
# print(df.mean(1))  #Just changed the axis from default to 1

#Apply : Applying functions to the data
# print(df.apply(np.cumsum))

#numpy.cumsum(a, axis = none, dtype = none, out=none) ---> Returns the cumulative sum of all elements of a given axis.  a--> array like, axis--> int, axis along which the cumulative value is calculated, dtype - the datatype of the array returned, out--> alternative output of the array in which to place result
#import pandas as pd
# import numpy as np
# a = np.array([[1,2,3],[4,5,6]])
# print(a)
# print(np.cumsum(a))
# print(np.cumsum(a, dtype=float))

#APPLY  :Apply functions to the data

# print(df.apply(np.cumsum))
# print(df.apply(lambda x:x.max()- x.min()))

#String Methods : Series is equipped with a set of string processing methods in the str attribute which makes it easy to operate on each element of the array.
# import pandas as pd
# import numpy as np
# df = pd.Series(["A","B","V","D","X","C","D","D", np.nan])
# print(df.str.lower())

#pandas.Dataframe.astype() : Dataframe.astype(dtype, copy = true, errors = 'raise')..... dtype = data type or dict of column name, copy = boolean or default = true, errors - default raise (raise - allows exceptions to be raise and allow - supress exceptions)
#to_datetime - convert argument to datetime   to_timedelta - convert argument to time delta   to_numeric - convert argument to numeric type   numpy.ndarray.astype = cast a numpy array to a specific type

#application of pandas.Dataframe.astype is to caste into different type of datatype

#Create a dataframe
# import pandas as pd
# import numpy as np
# d = {"col1":[1,2,3,4,5],"col2":[6,7,8,9,10]}
# df = pd.DataFrame(d)
# print(df)

#cast all columns to int32
# print(df.astype('int32').dtypes)
# print(df.astype({'col2': 'int32'}).dtypes)

#Create a series
# ser = pd.Series([1,2], [3,4], dtype= 'int32')
# print(ser)
# print(ser.astype('int64'))
# print(ser.astype('category'))

#Convert to ordered categorical type with custom ordering

# from pandas.api.types import CategoricalDtype
# cat_dtypes = CategoricalDtype(
#     categories=[22,21], ordered=True
# )
# print(ser.astype(cat_dtypes))

#Using copy = False changing and updating the data
# s1 = pd.Series([21,2])
# s2 = s1.astype('int64', copy=False)
# s2[1] = 22
# print(s2)

#Create a Series of dates
# date = pd.Series(pd.date_range("20220419", periods=6))
# print(date)

#Categoricals : Pandas can include the categorical data into dataframe

# import pandas as pd
# import numpy as np
# df = pd.DataFrame({
#     "id":[1,2,3,4,5,6,7,8,9,10], "raw_grades" : ["a","b","b","c","a","d","d","a","b","c"]
# })
# print(df)

#Converting the dataframe into categoricals
# from pandas.api.types import CategoricalDtype
# df["grades"] = df["raw_grades"].astype('category')
# print(df["grades"])
#
# #Rename the categories into more meaningful names (assigning to Series.cat.categories() in it's place)
# df["grades"].cat.categories = ["very good","good","very bad", "bad"]
# df["grades"] = df["grades"].cat.set_categories(
#     ["very good","bad","good","medium good"]
# )
# print(df["grades"])
#
# #Sorting is per order in the categories, not lexical order
# print(df.sort_values(by="grades"))
#
# #Grouping by categorical column also shows the empty category
# print(df.groupby("grades").size())



#***************************** APRIL 6 ********************************

# import pandas as pd
# import numpy as np
#print(pd.Series.__doc__)  #To get the details about the documentation of specific method/command/variable. "Series is a 1-D data-type in pandas".
# data = pd.Series(['python','java','c++','javascript'])
# print(data)

#ATTRIBUTES  ----> means kind of a variable----> attributes doesn't contains any type of braces
# print(data.index)  #Info about the start and end index
# print(data.dtypes) #Gives info about the data-type (object, int32, int64, float32 etc.)
# print(data.shape) #Gives info about (rows, columns)
# print(data.size)  #gives info about the number of values
# print(data.empty)  #returns boolean result stating whether the dataframe is empty or not
# print(data.ndim)   #gives info about the dimensions of the data-frame (1D,2D etc.)
# print(data.hasnans)  #hasnans -- has nan (not a number) values
# print(data.nbytes)

#INDEXING - loc, iloc, slicing(similar to python ot numpy), looping

# print(data.loc[0])
# print(data.iloc[0])
# print(data[3])
# print(data[2:5])
# print(data[0:2:5])
#
# for i in data:
#     print(i)

# WINDOWS FUNCTIONS :  rolling and expanding can be mostly seen in Time Series data
# import pandas as pd
# import numpy as np
# data = pd.Series([1,2,3,4,5,6,7,2,3,5,6,7,34])
# print(data)
# print(data.rolling(window=2).sum)  #window=2 (size of the  moving window) is adding up 2 index and generating a new column. Rolling function provides rolling window calculations.
# print(data.expanding(min_periods=2).sum)  # Cumulative calculation

# import pandas as pd
# import numpy as np
# data = pd.Series([2000,3000,3000,4000,2400,5000,2000,4000,3000], index=["Male","Female","Male","Female","Male","Male","Female","Female","Female","Male"])
# print(data)


#PlOTTING :
# import pandas as pd
# import numpy as np
# df = pd.DataFrame({'Name': {0: 'John', 1: 'Mike', 2: 'jesse', 3:'adola'},
#                    'Gender':{0:'male', 1:'male', 2:'female', 3:'female'},
#                    'Department':{0:'Sales', 1:'Marketing', 2:'Datascience', 3:'Python'},
#                    'Age': {0: 27, 1: 23, 2: 21, 3:25},
#                    'Salary':{0:1000, 1:2000, 2:3000, 3:2500}})
# print(df.plot('Department', 'Salary'))  #For plotting the data in a graph
# print(df.plot(x = 'Department', y = 'Age', kind = 'bar'))  #Bar graph
# print(df.plot(x = 'Department', y = 'Age', kind = 'scatter'))  #Scatter graph plotting

#TIME SERIES :
# import pandas as pd
# import numpy as np
# dates = pd.date_range("20220418", periods=5)
# df = pd.DataFrame({'Dates' : dates})
# df['Year'] = df['Dates'].dt.year
# df['Month'] = df['Dates'].dt.month
# df['Day'] = df['Dates'].dt.day
# df['Week'] = df['Dates'].dt.week
# print(df)

#DATAFRAME STYLING :
# import pandas as pd
# import numpy as np
# df = pd.DataFrame({'Name': {0: 'John', 1: 'Mike', 2: 'jesse', 3:'adola'},
#                    'Gender':{0:'male', 1:'male', 2:'female', 3:'female'},
#                    'Department':{0:'Sales', 1:'Marketing', 2:'Datascience', 3:'Datascience'},
#                    'Age': {0: 27, 1: 23, 2: 21, 3:25},
#                    'Salary':{0:1000, 1:2000, 2:3000, 3:2500}})
#
# print(df.style.highlight_max(color='lightblue'))
# print(df.style.highlight_min(color='red'))
# print(df.style.highlight_max(color='lightblue').highlight_min(color='red'))
# print(df.style.highlight_null(null_color='yellow'))
# print(df.style.background_gradient(cmap="gist_rainbow"))
# print(df.style.bar(color='red'))

#RESHAPING : 1) Melt  2) Pivot  3) Pivot table  4) Cross Tab  5) Cut  6) Stacking
#Melt :
# import pandas as pd
# import numpy as np
# df = pd.DataFrame({
#     'Name' : ["Stephen","Amr","Jerin","Vivek","Rahul"],
#     'Age' : [25,24,23,21,22],
#     'Salary' : [55000,35000,23000,32000,30000]
# })
# print(pd.melt(df))  #Dataframe from wide format to long format.
# print(pd.melt(df, id_vars='Name', value_vars=['Age']))


# id_varstuple, list, or ndarray, optional
# Column(s) to use as identifier variables.
#
# value_varstuple, list, or ndarray, optional
# Column(s) to unpivot. If not specified, uses all columns that are not set as id_vars.
#
# var_namescalar
# Name to use for the ‘variable’ column. If None it uses frame.columns.name or ‘variable’.
#
# value_namescalar, default ‘value’
# Name to use for the ‘value’ column.
#
# col_levelint or str, optional
# If columns are a MultiIndex then use this level to melt.
#
# ignore_indexbool, default True
# If True, original index is ignored. If False, the original index is retained. Index labels will be repeated as necessary.

#PIVOT : #The pivot() function is used to reshape a given dataframe organized by given index/column values. This function doesn't support data aggregation, multiple values will result in a MultiIndex in the columns.
#
# import pandas as pd
# import numpy as np
# df = pd.DataFrame({
#     'Name' : ["Stephen","Amr","Jerin","Vivek","Rahul"],
#     'Age' : [25,24,23,21,22],
#     'Salary' : [55000,35000,23000,32000,30000]
# })
# print(df.pivot("Name", "Age", "Salary"))

#PIVOT TABLE : The pivot_table() function is used to create a spreadsheet style pivot table as a DataFrame.

# import  pandas as pd
# import numpy as np
# df = pd.DataFrame({'Name' : {0:'Stephen', 1:'Shruti', 2:'Stefani', 3:'Aya', 4:'Trishita'},
#                    'Gender' : {0:'Male', 1:'Female', 2:'Female', 3:'Female', 4:'Female'},
#                    'Age': {0:25,1:25,2:21,3:20,4:24},
#                    'Salary' : {0:50000,1:60000,2:57000,3:70000,4:60000},
#                    'Department':{0:'Sales', 1:'Marketing', 2:'Datascience', 3:'Datascience'}
# })
# print(df.pivot_table(index=['Gender', 'Salary']))

#CROSS TAB : Compute a simple cross tabulation of two or more factors. By default computes a frequency table of the factors unless an array of values and an aggregation function are passed.

# import pandas as pd
# import numpy as np
# df = pd.DataFrame({'Name' : {0:'Stephen', 1:'Shruti', 2:'Stefani', 3:'Aya', 4:'Trishita'},
#                    'Gender' : {0:'Male', 1:'Female', 2:'Female', 3:'Female', 4:'Female'},
#                    'Age': {0:25,1:25,2:21,3:20,4:24},
#                    'Salary' : {0:50000,1:60000,2:57000,3:70000,4:60000},
#                    'Department':{0:'Sales', 1:'Marketing', 2:'Datascience', 3:'Datascience'}
# })
# print(pd.crosstab(df['Gender'], df['Department']))

#CUT : convert a continous column into a discrete or categorical column

# import pandas as pd
# import numpy as np
# df = pd.DataFrame({'Age' : np.random.randint(1,100,30)})
# df['bins'] = pd.cut(x = df['Age'], bins=[1,20,40,60,80,100],
#                     labels=['kids','young','adults','old','very old'])
# print(df)

#STACKING :

# import pandas as pd
# import numpy as np
# df_single_level = pd.DataFrame([[0,1], [2,3]], index=['Men', 'Women'], columns=['Sales', 'Marketing'])
# print(df_single_level)
# print(df_single_level.stack())
# print(df_single_level.unstack())

# import pandas as pd
# import  numpy as np
# multicol1 = pd.MultiIndex.from_tuples([('department', 'sales'),
#                                        ('department', 'marketing')])
# df_multi_level_cols1 = pd.DataFrame([[1, 2], [2, 4]],
#                                     index=['men', 'women'],
#                                     columns=multicol1)
# print(df_multi_level_cols1)
# print(df_multi_level_cols1.stack())
# print(df_multi_level_cols1.unstack())

#***********************************************PANDAS CHEATSHEET*************************************

# import pandas as pd
# import numpy as np
# df = pd.DataFrame({'a':[1,2,3], 'b':[4,5,6], 'c':[7,8,9]}, index= pd.MultiIndex.from_tuples(
#     [('d',1), ('d',2), ('e',2)], names=['n', 'v']))
# print(df)
# df1 = (pd.melt(df).rename(columns={'variables':'var', 'value':'val'}).query('val >=5'))  #Method Chaining
# print(df1)

#TIDY DATA : A FOUNDATION FOR WRANGLING IN PANDAS. 1) Each variable is saved in its own column. 2) Each observation is saved in its own row.
#Tidy data complements pandas vectorized operations. Pandas will automatically preserve observations as you manipulate variables . No other format works intuitively with pandas.


# import pandas as pd
# import numpy as np
# dates = pd.date_range("20220422", periods=6)
# df = pd.DataFrame(np.random.randn(6,4) ,index = dates, columns=list('ABCD'))
# df2 = df.copy()
# df2[df2 >0] = -df2
# print(df2)
# df1 = df.reindex(index = dates[0:4])

#MISSING DATA ---> df.dropna - to drop any row having missing data ----->  df.fillna - to fill any row having missing data -----> pd.isnan - To get the boolean mask where values are nan. Basically it returns true in the block of cells where value is nan



#**************************** NUMPY (NUMERICAL PYTHON)  ********************************

#Division or multiplication function is not supported on lists. For this we have to convert that lists into array

# import pandas as pd
# import numpy as np
# speed_arr = np.array([10,15,20,25])
# dist_arr = np.array([.30,.40,.50,.45])
# result = speed_arr/dist_arr
# print(result)

# import pandas as pd
# import numpy as np
# a = np.array([10])  #Scalar - single value
# print(a)
# b = np.array([1,2,3,4,5,6,7,np.nan])  #Vector - A list of values or linear array
# print(b)
# c = np.array([[1,2,3],[4,5,6],[7,8,9]]) #Matrices - 3D array
# print(c)
#Array
#print(help(np.array))
# d = np.array([1.0,2.0,3.0], dtype='complex')  #To create complex number's array
# print(d)
# print(d.ndim)  #To know the dimension of the array

#Attr
# e = np.array([[2,3,4],[4,5,6],[3,4,5]])
# print(e)
# print(e.shape)  #Returns the number of rows and columns of the matrices
# print(e.size) #Returns the size or the number of digits/elements in the array
# print(e.dtype) #Returns the datatype
# print(e.ndim)  #Returns the dimension of the array
# print(e.itemsize) #Returns the itemsize of the array or the count of the unique element in the array

#Accessing - 2D array
# f = np.array([[1,2,3,4], [2,3,4,5], [3,4,5,6]])
# print(f)
# print(f[1:,2])
# print(f[1:3, 1])

#Accessing - 3D array
# a1 = np.array([[[1,2,3],[2,3,4],[3,4,5]], [[4,5,6],[5,6,7],[6,7,8]]])
# print(a1)
# print(a1[1,:2,1:3])
# print(a1[0,1,1:3])
# print(a1[:,:,1:2])
# print(a1[1,0:2,1:3])
# print(a1[1,0:2,0:3])
# print(a1.ndim)

#ARRANGE - Return evenly spaced values within a given interval. Values are generated within the half-open interval [start, stop) (in other words, the interval including start but excluding stop). For integer arguments the function is equivalent to the Python built-in range function, but returns an ndarray rather than a list.

# print(np.arange(10))  #Returns the 'n-1', where n is given as input in arrange()
# print(np.arange(20,0,-2))  #Here (start, end-stepcount , step count)
# print(np.arange(0,25,5))
# print(np.arange(0,40,dtype = 'float')) #The step count is 1 by default

#ZEROS - Return a new array of given shape and type, filled with zeros.
# print(np.zeros(10))  #Returns n number of elements in the array. 'n' is passed as a parameter inside zeros(). The dtype pf zeros() is 'float64' by default.
# print(np.zeros((5,5), dtype='int'))

#ONES - Return a new array of given shape and type, filled with ones.
# print(np.ones(10))  #Returns a list of 'n' elements in the list and it's dtype is 'float64' by default
# print(np.ones((2,3), dtype= int))

#Linespace- Returns evenly spaced numbers over a specified intervals. Returns num evenly spaced samples, calculated over the interval part. The endpoints of the sample can be optionally excluded.

# print(np.arange(1,10))  #(start, end-1)
# print(np.linspace(10,100, num=10, retstep=False, endpoint=False))  #start - starting value, stop - end value (num+1), endpoint - if true then stop is the last sample else its not included, retstep - If true return sample, step where step is the spacing between samples
# print(np.linspace(10,100, num=10, retstep=True, endpoint=True))
# print(np.linspace(1,100, num=10, retstep=True, endpoint=False))

#RANDOM - Random values in a given shape.

# print(np.random.randn(5,5))    # randn - Normally distributed values. (STANDARD NORMAL DITSRIBUTION)
# print(np.random.rand(4,5)) #rand - Uniformly distributed values  (UNIFORM NORMAL DISTRIBUTION [0,1) )
# print(np.random.random_integers(5)) #Random integers of type np.int_ between low and high, inclusive. Return random integers of type np.int_ from the “discrete uniform” distribution in the closed interval [low, high]. If high is None (the default), then results are from [1, low]. The np.int_ type translates to the C long integer type and its precision is platform dependent. This function has been deprecated. Use randint instead.
# print(np.random.randint(2,15, size=(5,5)))

"""rand                 Uniformly distributed values.
    randn                Normally distributed values.
    ranf                 Uniformly distributed floating point numbers.
    random_integers      Uniformly distributed integers in a given range.
                         (deprecated, use ``integers(..., closed=True)`` instead)
    random_sample        Alias for `random_sample`
    randint              Uniformly distributed integers in a given range
    seed                 Seed the legacy random number generator."""

#Ranf - numpy.random.ranf() is one of the function for doing random sampling in numpy. It returns an array of specified shape and fills it with random floats in the half-open interval [0.0, 1.0).
# print(np.random.ranf((3,3,3))) #----> parameter should be an inetger or tuple of ints

#Seed - Reseed a legacy MT19937 BitGenerator  ---> random.seed(self, seed=None)

# # random module is imported
# import random
#
# for i in range(5):
#     # Any number can be used in place of '0'.
#     random.seed(0)
#
#     # Generated random number will be between 1 to 1000.
#     print(random.randint(1, 1000))

#RESHAPE -

# import pandas as pd
# import numpy as np
# a = np.random.rand(5,5)
# print(a)
# print(a.shape)
# print(a.ndim)
# print(a.size)
# d = a.reshape(25,)
# print(d)
# print(d.ndim)


#RESIZE -
import numpy as np

# a = np.arange(10)
# print(a)
# print(np.resize(a, (2,2,2,4)))

# FLATTEN AND RAVEL -
# What is the difference between flatten() and ravel()?
# There are 2 popular ways to implement flattening. That is using the flatten() method
# and the other using the ravel() method.

# The difference between ravel and flatten is, the new array created using ravel is
# actually a reference to the parent array.
# So, any changes to the new array will affect the parent as well.
# But is memory efficient since it does not create a copy.

# c = np.array([[[1, 2, 3, 4],
#                [5, 6, 7, 8],
#                [9, 10, 11, 12]],
#
#               [[11, 12, 13, 14],
#                [5, 6, 7, 8],
#                [9, 10, 11, 12]]
#               ])
#
# print(c.flatten())
# print(c.ravel())

#TRANSPOSE - shifts the rows to columns axis
# d = np.array([[1,2,3,4],
#               [5,6,7,8],
#               [9,10,11,12]])
# print(d)
# print(np.transpose(d))


#EYE  - k>0 diagonal above main diagnol and vice versa
# z = np.eye(4,5,k=1)   #k>0 diagnal above the main diagnol
# print(z)

#Full - fills the rows and colums with similar value
# print(np.full((2,2),4))

#STACK - function is used to join a sequence of same dimension arrays along a new axis.The axis parameter specifies the index of the new axis in the dimensions of the result. For example, if axis=0 it will be the first dimension and if axis=-1 it will be the last dimension

# a = np.array([[1,2,3,4],
#               [5,6,7,8],
#               [9,10,11,12]])
#
#
# b = np.array([[11,12,13,14],
#               [5,6,7,8],
#               [9,10,11,12]])
#
# c = np.stack((a,b))
# print(c)
# print(c.ndim)

# CONCATENATE - numpy.concatenate() function concatenate a sequence of arrays along an existing axis.

# a = np.array([[1,2,3,4],
#               [5,6,7,8],
#               [9,10,11,12]])
#
#
# b = np.array([[11,12,13,14],
#               [5,6,7,8],
#               [9,10,11,12]])
#
# print(np.concatenate((a,b), axis = 0))
# print(np.concatenate((a,b), axis = 1))

#VSTACK AND HSTACK -
"""vstack(tup)
    Stack arrays in sequence vertically (row wise).
    
    This is equivalent to concatenation along the first axis after 1-D arrays
    of shape `(N,)` have been reshaped to `(1,N)`. Rebuilds arrays divided by
    `vsplit`.
    
    This function makes most sense for arrays with up to 3 dimensions. For
    instance, for pixel-data with a height (first axis), width (second axis),
    and r/g/b channels (third axis). The functions `concatenate`, `stack` and
    `block` provide more general stacking and concatenation operations.
    
    Parameters
    ----------
    tup : sequence of ndarrays
        The arrays must have the same shape along all but the first axis.
        1-D arrays must have the same length.
    
    Returns
    -------
    stacked : ndarray
        The array formed by stacking the given arrays, will be at least 2-D.
    
    See Also
    --------
    concatenate : Join a sequence of arrays along an existing axis.
    stack : Join a sequence of arrays along a new axis.
    block : Assemble an nd-array from nested lists of blocks.
    hstack : Stack arrays in sequence horizontally (column wise).
    dstack : Stack arrays in sequence depth wise (along third axis).
    column_stack : Stack 1-D arrays as columns into a 2-D array.
    vsplit : Split an array into multiple sub-arrays vertically (row-wise)."""

# a = np.array([[1,2,3,4],
#               [5,6,7,8],
#               [9,10,11,12]])
#
#
# b = np.array([[11,12,13,14],
#               [5,6,7,8],
#               [9,10,11,12]])
#
# c = np.vstack((a,b))
# print(c)
# d = np.hstack((a,b))
# print(d)