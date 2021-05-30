# XmlGenerator - Excel to Xml converter tool. 
This tool will be useful when you want to generate the xml nodes with different properties. For each node only few properties will change and other remains the same.
In this case XmlGenerator will be helpful. We will define all xml properties file inside application.yaml file and provide the excel sheet which will all the values for those properties whose value will change.

Xml node properties can be control through application.yaml file.

# Update configuration file as per requirement
	Update the application.yaml file. There few sections need to be updated in application.yaml.
	1. Update the input file path and output file path under 'app-arguments'
	2. Update the output xml column name under 'xml.properties-names' and provide the default values for each under 'xml.default-values'.
	3. Update the fields information present under 'excel.fields'. These values will be fetched from excel document.
	
# How to Run the program
	java -jar xmlgenerator-0.0.1-SNAPSHOT.jar --spring.config.location=application.yaml

