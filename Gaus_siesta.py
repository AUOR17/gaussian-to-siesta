import csv
import pandas
from pandas import DataFrame
from pandas import read_csv
import numpy as np
import os
import re


# print(periodic_table.head())

# Function to convert the file xyz into dataframe or csv
def convert_file_to_dataframe():
    replace_spaces()
    
# Read the input file into a DataFrame
    df = read_csv('example.csv',skiprows=[0], names=['Symbol', 'X', 'Y', 'Z'])
    df.to_csv('Gaussian_input.csv', index=False)
    # Write the DataFrame to a CSV file
    # print(df.head())
    
 #Get the first block of the siesta input file   
def data_treatment():
    convert_file_to_dataframe()
    xyz = read_csv('Gaussian_input.csv')
    periodic_table = read_csv("Periodic Table of Elements.csv")
    siesta_file1 = xyz.merge(periodic_table,on='Symbol')
    siesta_filtered = siesta_file1[['Symbol', 'X', 'Y', 'Z', 'AtomicNumber']]
    chemical_elements =  siesta_filtered['Symbol'].value_counts()
    siesta_grouped = siesta_filtered.groupby('Symbol').first().reset_index()
    siesta_grouped['TabColumn'] = np.full(len(siesta_grouped), '\t')
    siesta_grouped['AtomIndentificator'] = [i+1 for i,row in enumerate(siesta_grouped.iterrows())]
    siesta_filtered['AtomIndentificator'] = [i+1 for i,row in enumerate(siesta_filtered.iterrows())]
    siesta_filtered['TabColumn'] = '\t'
    number_of_species =  siesta_grouped['Symbol'].nunique()
    number_of_atoms = siesta_filtered.shape[0]
    siesta_filtered.to_csv('Data to work.csv', index=False)
    output_file =convert_to_fdf_file()
    with open(output_file,'w') as file:
        file.write('*** Data Input***'+ '\n'+ '\n')
        file.write('SystemName'+ '\t' + '\t' + '\t' +  'Water_molecule'+ '\n')
        file.write('SystemLabel'+ '\t' + '\t' + '\t' +  'h20'+ '\n'+ '\n')
        file.write('NumberOfSpecies' + '\t' + '\t' + str(number_of_species)+ '\n')
        file.write('NumberOfAtoms' + '\t' + '\t' +  str(number_of_atoms)+ '\n'+ '\n')
        file.write('%block ChemicalSpeciesLabel'+ '\n')
        file.write(siesta_grouped[['AtomIndentificator','Symbol','AtomicNumber']].to_string(index=False,header=False).replace(',','\t\t')+'\n')
        file.write('%endblock ChemicalSpeciesLabel'+ '\n'+ '\n')
        file.write('AtomicCoordinatesFormat'+ '\t' + 'Ang' + '\n'+ '\n')
        file.write('%block AtomicCoordinatesAndAtomicSpecies' + '\n')
        file.write(siesta_filtered[['X','Y','Z','AtomIndentificator']].to_string(index=False,header=False).replace(',','\t\t\t')+'\n')
        file.write('%endblock AtomicCoordinatesAndAtomicSpecies' + '\n')
    # print(siesta_filtered.tail)
    print(siesta_filtered)

def convert_text():
    data_treatment()
    output_file =convert_to_fdf_file()
    with open(output_file, "r") as f:
        content = f.readlines()

    content = [line.replace(" ", "\t\t") for line in content]

    with open(output_file, "w") as f:
        f.writelines(content)

#change the name of "example.xyz" according to the name of the file to convert
def replace_spaces():
    # Open the file for reading
    file_name = read_file_xyz()
    with open(file_name, 'r') as file:
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
        
def read_file_xyz():
    extension = "xyz"
    filenames = []

    for filename in os.listdir():
        if filename.endswith(extension) :#and (filename != "requirements.txt" ):
            filenames.append(filename)

    result = filenames[0]
    return result
    # print(result)
    # print(type(result))
def convert_to_fdf_file():
    filename = read_file_xyz()
    file_require = ".fdf"
    base_name,file_extension = os.path.splitext(filename)
    output_name = base_name + file_require
    return output_name
    # print(output_name)
    # print(type(output_name))
    

        
if __name__=='__main__':
    # convert_text()
    data_treatment()
    # replace_spaces()
    # convert_to_fdf_file()
    # read_file_txt()
    # convert_file_to_dataframe()
    


# file_input = read_csv('example.xyz',skiprows=[0], sep=' {10}')

# # Write the DataFrame to a CSV file
# file_input.to_csv('example.csv', index=False)

# print(file_input.shape)