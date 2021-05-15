'''
A commandline tool in Python to split a large tabular data file (.csv)
into smaler chunks based on the unique values in a particular column 
'''

# import packages from the python standart library
import os
from pathlib import Path
# import 3rd party packages, use pip or conda for installing
import pandas as pd
import fire

class One2Many():
    '''
    Split a large tabular data file (.csv) into smaler chunks 
    based on the unique values in a particular column 

    Usage:
    python one_to_many.py one2many --filepath '../path/to/data.csv' --colname 'name_to_split'
    '''
    def __init__(self):
        self.filepath = None
        self.data = None
        self.splitcolumn = None
        self.extension = None

    def read_file(self, filepath):
        '''
        Read file using pandas
        '''
        self.filepath = filepath
        self.extension = Path(filepath).suffix
        print(f'\n*********************************************\n')
        if self.extension not in ['.xlsx', '.xls', '.csv']:
            print(f'The program cannot deal with files with the extension {self.extension}')
            data = None
        elif self.extension in ['.xlsx', '.xls']:
            print('Processing an Excel file is not yet implemented. Try a .csv file.')
            data = None
        else:
            print(f'Loading the CSV file {Path(self.filepath).name}\n')
            data = pd.read_csv(self.filepath)
        self.data = data
        
    
    def extract_subsets(self, colname=None):
        '''
        Subset the dataset and save it to disk
        '''
        if colname is None:
            print(f'Column name to split on is not set.')
            return
        else:
            self.splitcolumn = colname

        outpath = Path(self.filepath).parents[0].resolve()
        
        for name in self.data[self.splitcolumn].unique():
            print(f'Computing {name} ...')
            subset = self.data.loc[self.data[self.splitcolumn] == name]
            fname = f'subset_{name.replace(" ", "_")}{self.extension}'
            filepath_subset = os.path.join(outpath, fname)
            subset.to_csv(filepath_subset, index=False)
            print(f'Saving file to {filepath_subset}\n')

    def one2many(self, filepath, colname):
        '''
        Main function
        '''
        self.read_file(filepath=filepath)
        if self.data is not None:
            self.extract_subsets(colname=colname)
        print(f'\n*********************************************\n')

if __name__ == '__main__':
    main = One2Many()  
    fire.Fire(main)
