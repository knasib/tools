import pandas
from xmlgeneratorv2.src import yamlreader

try:
    df = pandas.read_excel(yamlreader.get_properties('app.input'))
except FileNotFoundError:
    print(
        f"{yamlreader.get_properties('app.input')} does not exist. Update the application.yaml file with correct "
        f"excel path.")
    exit(4)


def get_cell_value(row, column):
    try:
        if pandas.isna(df[df.columns[column]].get(row)):
            print(f'Cell[{row + 2}][{column}] is empty in Excel.')

        value = "" if pandas.isna(df[df.columns[column]].get(row)) else df[df.columns[column]].get(row)
    except IndexError:
        print(
            f'Number of key defined under `xml.keys` must not exceed number of columns in Excel. Kindly check the '
            f'yaml configuration under `xml.keys`')
    return value


def get_row(row):
    return df.iloc[row]


def get_excel():
    return df


def get_size():
    return len(df)
