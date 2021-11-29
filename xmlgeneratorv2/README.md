# About Xml Generator
XmlGenerator tool developed using python which will generate xml based on application.yaml's keys. This tool uses a xml template which is defined under `xml.template` and it will replace all the tags defined under `xml.keys` with the value present under excel.

# Points to remember
1. Excel must have header
2. Number of key defined under `xml.keys` must not exceed number of columns in Excel
3. Excel column1 values will be replaced to the xml node mentioned in key1 inside xml.keys
       column1 mapped to key1, column2 mapped to key2 and so on... 

# Install Dependencies
XmlGenerator requires two python dependencies. Those are:
1. PyYAML : Read configuration from yaml file
2. Pandas : Read data from Excel

These dependencies can be installed using below pip commands.

#### Install PyYAML for reading yaml file
`pip install PyYAML`

#### Install pandas for reading data from excel
`pip install pandas`

`pip install openpyxl`



# How to Run
Once all dependencies are installed, perform below steps

1. Update the `input` and `output` keys in application.yaml
2. Nagivate inside the root directory in command promt.
3. Run the below command in CMD.

    Command: `python main.py`
