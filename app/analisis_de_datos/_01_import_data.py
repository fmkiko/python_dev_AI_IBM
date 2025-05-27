import pandas as pd
import numpy as np
import asyncio
from pyodide.http import pyfetch

async def download(url, filename):
    response = await pyfetch(url)
    if response.status == 200:
        with open(filename, "wb") as f:
            f.write(await response.bytes())

file_path = "https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-DA0101EN-Coursera/laptop_pricing_dataset_base.csv"
download(file_path, "laptops.csv")
#df = pd.read_csv("laptops.csv")

#Load the dataset to a pandas dataframe named 'df'
df = pd.read_csv("laptops.csv", header=None)
print(df.head())

#Add headers to the dataframe
headers = ["Manufacturer", "Category", "Screen", "GPU", "OS", "CPU_core", "Screen_Size_inch", "CPU_frequency", "RAM_GB", "Storage_GB_SSD", "Weight_kg", "Price"]
df.columns = headers
print(df.head(10))

#Replace '?' with 'NaN'
df.replace("?", np.nan, inplace = True)

#Print the data types of the dataframe columns
print(df.dtypes)

#Print the statistical description of the dataset, including that of 'object' data types
print(df.describe(include="all"))

#Print the summary information of the dataset.
print(df.info())

