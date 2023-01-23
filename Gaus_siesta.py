import csv
import pandas
from pandas import DataFrame
from pandas import read_csv
import os
import re

periodic_table = read_csv("Periodic Table of Elements.csv")
# print(periodic_table.head())


def convert_file_to_dataframe():
    replace_spaces()
    
# Read the input file into a DataFrame
    df = read_csv('example.csv',skiprows=[0], names=['ElementSymbol', 'X', 'Y', 'Z'])
    df.to_csv('Gaussian_input.csv', index=False)
    # Write the DataFrame to a CSV file
    print(df.head())


def replace_spaces():
    # Open the file for reading
    with open('example.xyz', 'r') as file:
        # Read the file into a string
        file_contents = file.read()

    # Replace all blank spaces with commas
    file_contents = file_contents.replace(' ', ',')

# Open the file for writing
    with open('example.csv', 'w') as file:
        # Write the modified string back to the file
        file.write(file_contents)
        
    with open('example.csv', 'r') as file:
        # Read the file into a string
        file_contents = file.read()

    # Replace multiple commas with a single comma
    file_contents = re.sub(r',+', ',', file_contents)

    # Open the file for writing
    with open('example.csv', 'w') as file:
        # Write the modified string back to the file
        file.write(file_contents)

        
if __name__=='__main__':
    convert_file_to_dataframe()
    


# file_input = read_csv('example.xyz',skiprows=[0], sep=' {10}')

# # Write the DataFrame to a CSV file
# file_input.to_csv('example.csv', index=False)

# print(file_input.shape)