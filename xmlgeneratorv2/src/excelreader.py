import pandas
import src.yamlreader as yamlreader

try:
    df = pandas.read_excel(yamlreader.getProperties('app.input'))
except FileNotFoundError:
    print(f"{yamlreader.getProperties('app.input')} does not exist. Update the application.yaml file with correct excel path.")
    raise Exception(f"{yamlreader.getProperties('app.input')} does not exist.")

def getCellValue(row, column):
    try:
        if pandas.isna(df[df.columns[column]].get(row)):
            print(f'Cell[{row+2}][{column}] is empty in Excel.')
        
        value = "" if pandas.isna(df[df.columns[column]].get(row)) else df[df.columns[column]].get(row)
    except IndexError:
         print(f'Number of key defined under `xml.keys` must not exceed number of columns in Excel. Kindly check the yaml configuration under `xml.keys`')   

    return value;

def getRow(row):
    return df.iloc[row]    

def getExcel():
    return df

def getSize():
    return len(df)    

#print (len(df))