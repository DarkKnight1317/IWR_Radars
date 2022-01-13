import os 
import pickle
import json 
import pandas as pd 

class Writer():
    def __init__(self, data, filename="Untitled"):
        self.data = data
        self.filename = filename

    def get_df(self):
        try:
            df = pd.DataFrame(self.data)
        except:
            print(f"file could not be converted to dataframe.  Data is of type: {type(self.data)}")
        return df

    def write_to_excel(self):
        name = self.filename + ".xlsx"
        df = self.get_df()
        try:
            df.to_excel(name)
        except Exception as e:
            print(f"File could not be written because: {e}")
        
    def write_to_text(self):
        try:
            writing_string = str(self.data)
        except:
            print(f"Could not convert data to string.  Data is of type: {type(self.data)}")
        name = self.filename + ".txt"
        try:
            with open(name) as filehandle:
                filehandle.write(writing_string, 'ab')
        except Exception as e:
            print(f"file could not be written because: {e}")

    def write_to_pickle(self):
        name = self.filename + ".pkl"
        try:
            with open(name, 'ab') as filehandle:
                pickle.dump(self.data, filehandle)
        except Exception as e:
            print(f"The file of type {type(self.data)} could not be dumped into pickle because: {e}")
    

class Reader():
    def __init__(self, filename, directory=os.getcwd()):
        self.filename  = filename
        self.directory = directory
        self.filetype  = self.filename.split(".")[-1]
        
    def read(self):
        if self.filetype == 'xlsx':
            self.read_excel()
        elif self.filetype == 'txt':
            self.read_text()
        elif self.filetype == 'pkl':
            self.read_pickle()
        else:
            print(f"Function to read filetype {self.filetype} not written.")

    def read_excel(self):
        try:
            data = pd.read_excel(self.filename)
            return data
        except Exception as e:
            print(f"{self.filename} could not be read because: {e}.")

    def read_text(self):
        try:
            with open(self.filename, 'r') as fhandle:
                data = fhandle.read()
            return data
        except Exception as e:
            print(f"{self.filename} could not be read because: {e}.")


    def read_pickle(self):
        try:
            with open(self.filename, 'rb') as filehandler:
                data = pickle.load(filehandler)
                return data
        except Exception as e:
            print(f"{self.filename} could not be read because: {e}.")        
        
    
    
if __name__ == "__main__":
    """
    __main__ for testing
    """

    readobj = Reader("test.txt")
    text = readobj.read()
    print(f"text is: {text}")
    # print(readobj.filetype)