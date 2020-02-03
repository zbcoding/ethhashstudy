import dask
import dask.array as da
import dask.dataframe as ddata
import matplotlib.pyplot as plt 
import pandas as pd 
import numpy as np 


def main():
    
    dftable = ddata.read_csv((r"D:/Users/A/Documents/Code/python calc/EthereumNetworkHashRateGrowthRate.csv"))
    print(dftable)
    
    daskarray = ddata.compute(dftable) #makes pandas array

    print(daskarray)

    df = dftable

    df = df.rename(columns={'Date(UTC)':'Date-UTC','UnixTimeStamp':'UnixTime','Value':'HashValue'})
    print(df)

    type(df)
    
    print(df.groupby(df.UnixTime).HashValue.mean().compute())

    df = df.compute() 
    #Call .compute() when you want your result as a Pandas dataframe

    print(type(df))

   
    df['HashValue'].plot(kind = 'line')
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

