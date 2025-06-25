### Python Automation Project -- Data Cleaning and Analysis

""" ** It should ask for datasets path and NameError
** It should check number of duplicates and remove all the duplicates
** It should keep a copy of all the duplicates
** It should check for missing  values and remove all the rows with missing values
** if any column that is numeric it should replace null with mean else it should drop the column
** At the end it save the data as clean data and also return
** Duplicates records, clean_data """


#Importing necessary libraries
import pandas as pd
import numpy as np
import time
import openpyxl
import xlrd
import os
import random


def data_cleaning(data_path, data_name):

    print("Thank you for giving the details!")

    sec = random.randint(1,4)  # generating random number
    # print delay message
    print(f"Please wait for {sec} seconds! Checking the file path. ")
    time.sleep(sec)

    #Check if the path exists
    if not os.path.exists(data_path):
        print("Incorrect path! Try again with correct path!")
        return

    else:
        # checking the file type
        if data_path.endswith('.csv'):
            print('Dataset is in CSV format')
            data = pd.read_csv(data_path, encoding_errors='ignore')

        elif data_path.endswith('.xlsx'):
            print('Dataset is in Excel format')
            data = pd.read_excel(data_path)

        else: 
            print('Unkown file format. Please provide a CSV or Excel file.')
            return
        
    # print delay message
    sec = random.randint(1,4)
    print(f"Please wait for {sec} seconds! Checking total columns and rows ")
    time.sleep(sec)
        
    # Showing number of rows and columns
    print(f"Dataset has {data.shape[0]} rows and {data.shape[1]} columns.")

    # Start cleaning process

    # print delay message
    sec = random.randint(1,4)
    print(f"Please wait for {sec} seconds! Checking duplicates ")
    time.sleep(sec)

    #1. Check for duplicates
    duplicates = data.duplicated()
    total_duplicates = data.duplicated().sum()

    print(f"Datasets has total duplicates records: {total_duplicates}")

    #Saving the duplicate records
    if total_duplicates > 0:  
        duplicate_records = data[duplicates]
        duplicate_records.to_csv(f'{data_name}_duplicate_records.csv', index=False)

    # Removing duplicates from the original dataset
    df = data.drop_duplicates()

    # print delay message
    sec = random.randint(1,4)
    print(f"Please wait for {sec} seconds! Missing values ")
    time.sleep(sec)

    # Finding missing values
    missing_values = df.isnull().sum()
    total_missing_value = df.isnull().sum().sum()
    print(f"Total missing values in the dataset: {total_missing_value}")
    print(f"Missing values in each column: \n {missing_values}")


    #Dealing with missing values
    #filna -- for int and float columns, dropna -- for object columns

    columns = df.columns
    for column in columns:
        # If the column is numeric, fill NaN with the mean
        if df[column].dtype in [np.int64, np.float64]:
            df[column] = df[column].fillna(df[column].mean())
        else:
            # dropping all rows with missing values in non-numeric columns
            df.dropna(subset=[column], inplace=True)


    # Saving the cleaned data
    print("Data cleaning completed successfully \nNumber of rows after cleaning: ", df.shape[0], "\nNumber of columns after cleaning: ", df.shape[1])
    #saving the cleaned data to a CSV file
    df.to_csv(f'{data_name}Clean_data.csv', index=None)
    print(f"Congrats! Cleaned data saved as {data_name}_Clean_data.csv")


if __name__ == "__main__":

    print("Welcome to Data cleaning tools!")
    # asking path and file name
    data_path = input("Please enter dataset path : ")
    data_name = input("Please enter dataset name : ")

    #calling the function
    data_cleaning(data_path,data_name)