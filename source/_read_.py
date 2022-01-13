import json
import pandas as pd

filename = "dataframe"

if __name__ == '__main__':
    try:
        with open(filename + '.json', 'r') as openfile:
            json_object = json.load(openfile)
    except Exception as e:
        print(f"Reading file unsuccessful.: {e}")
    print(f"The json file is ... \n{json_object}")
    df = pd.dataFrame(json_object)
    df.to_excel("dataframe.xlsx")
    
    
