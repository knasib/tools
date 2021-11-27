import pandas
import src.yamlreader as yamlreader

df = pandas.read_excel(yamlreader.getProperties('app.input'))

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