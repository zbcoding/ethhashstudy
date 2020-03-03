import dask
import dask.array as da
import dask.dataframe as ddata
import matplotlib.pyplot as plt 
import pandas as pd 
import numpy as np 
from dask.distributed import Client



def main():
    
    client = Client(n_workers=1, threads_per_worker=4, processes=False, memory_limit='2GB')
    client

    dftable = ddata.read_csv((r"D:/Users/A/Documents/Code/python calc/EthereumNetworkHashRateGrowthRate.csv"))
    #print(type(dftable))
    #print(dftable)
    
    daskarray = ddata.compute(dftable) #makes pandas array

    #print(daskarray)

    df = dftable

    df = df.rename(columns={'Date(UTC)':'Date-UTC','UnixTimeStamp':'UnixTime','Value':'HashValue'})
    #print(df)
    print("Number of data columns is: {}" .format(len(df)) )

    dfc = df.compute(npartitions = 5)
    print(dfc.head())

    month_dict = {1: "Jan", 2:"Feb", 3:"Mar", 4:"Apr", 5:"May", 6:"Jun", 7:"Jul", 8:"Aug", 9:"Sep", 10:"Oct", 11:"Nov", 12:"Dec"}

    month_list = []

    #ex = "7/3/2012"
    #month_ex = ex[0]
    #print(type(month_ex)) 
    #print("the month number is: {}".format(ex[0]))
    #print(month_dict.get(ex[0]))

    print( month_dict.get(5))
    for date in dfc["Date-UTC"]:
        month_list.append(month_dict.get(int(date[0])))
    
    dfc['Month'] = month_list

    print(dfc.head())

    print("dfc type after adding month column", type(dfc))
    df = ddata.from_pandas(dfc, npartitions=5)
    print("df after using from_pandas on dfc pandas df", type(df))
    
    mean_HashValue_by_month = df.groupby('Month').HashValue.mean().compute()
    #group HashValue by month. TODO normalize with percent or trailing mean because 
    #grouping by month but over multiple years 

    print("Mean HashValue by Month {}".format(mean_HashValue_by_month))

    #for date in df.Date-UTC:



    #print(type(df))
    #print(df.HashValue.head())
    #print(df.groupby(df.UnixTime).HashValue.mean().compute())

    dfc = df.compute() 
    #Call .compute() when you want your result as a Pandas dataframe

    print(type(dfc))

    print(df.HashValue.mean().compute(npartitions = 5))
    dfc['HashValue'].plot(kind = 'line')
    plt.show()

    

#import numpy as np
#import dask.array as da
#x = np.arange(10)
#y = da.from_array(x, chunks=5)
#y.compute() #results in a dask array

#import numpy as np
#import dask.array as da
#
#x = np.arange(1000)  #arange is used to create array on values from 0 to 1000
#y = da.from_array(x, chunks=(100))  #converting numpy array to dask array
#
#y.mean().compute()  #computing mean of the array
#
#499.5


'''
# use gui to import a csv file
import tkinter as tk
from tkinter import filedialog
import pandas as pd

root= tk.Tk()

canvas1 = tk.Canvas(root, width = 300, height = 300, bg = 'lightsteelblue2', relief = 'raised')
canvas1.pack()

def getCSV ():
    global df
    
    import_file_path = filedialog.askopenfilename()
    df = pd.read_csv (import_file_path)
    print (df)
    
browseButton_CSV = tk.Button(text="      Import CSV File     ", command=getCSV, bg='green', fg='white', font=('helvetica', 12, 'bold'))
canvas1.create_window(150, 150, window=browseButton_CSV)

root.mainloop()'''
    

if __name__ == "__main__":
    main()

