package com.tools;

import java.io.File;
import java.io.FileInputStream;
import java.io.IOException;
import java.util.Iterator;
import java.util.LinkedHashMap;
import java.util.Map;

import javax.xml.bind.JAXBContext;
import javax.xml.bind.JAXBException;
import javax.xml.bind.Marshaller;

import org.apache.poi.ss.usermodel.Cell;
import org.apache.poi.ss.usermodel.Row;
import org.apache.poi.xssf.usermodel.XSSFSheet;
import org.apache.poi.xssf.usermodel.XSSFWorkbook;
import org.springframework.boot.CommandLineRunner;
import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;

import com.tools.config.ApplicationArguments;
import com.tools.config.ExcelConfig;
import com.tools.config.XmlConfig;
import com.tools.models.Output;


@SpringBootApplication
public class XmlgeneratorApplication implements CommandLineRunner {
	
	private final XmlConfig xmlConfig;
	private final ExcelConfig excelConfig;
	private final ApplicationArguments arguments;
	
	public XmlgeneratorApplication(XmlConfig xmlConfig, ExcelConfig excelConfig, ApplicationArguments arguments) {
		super();
		this.xmlConfig = xmlConfig;
		this.excelConfig = excelConfig;
		this.arguments = arguments;
	}

	public static void main(String[] args) {
		SpringApplication.run(XmlgeneratorApplication.class, args);
	}

	@Override
	public void run(String... args) throws Exception {
		try {
			this.generateXml();
		} catch (Exception ex) {
			ex.printStackTrace();
			throw ex;
		}
	}
	
	private void generateXml() throws Exception {
		Output xml = this.getXmlData(this.arguments.getInput());
		this.writeObjectToXml(xml, this.arguments.getOutput());
		System.out.println("Xml generation completed. Avaiable at path :" 
					+ new File(this.arguments.getOutput()).getParent());
	}
	
	
	private Output getXmlData(String fileName) throws Exception {
		Output output = new Output();
		XSSFWorkbook workbook = null;
		try(FileInputStream file = new FileInputStream(new File(fileName))) {
			getXmlFromExcel(workbook, output, file);
		} finally {
            workbook = null;
		}
		return output;

	}

	private void getXmlFromExcel(XSSFWorkbook workbook, Output output, FileInputStream file) throws IOException {
		boolean header = true;
		workbook = new XSSFWorkbook(file);
		XSSFSheet sheet = workbook.getSheetAt(0);
		 
		//Skip the first row of the excel as it is header
		Iterator<Row> rowIterator = sheet.iterator();
		if(header) {
			rowIterator.next();
		}
		
		while (rowIterator.hasNext()) 
		{
		    Row row = rowIterator.next();
		    Iterator<Cell> cellIterator = row.cellIterator();
		    Map<String, String> xmlData = convertExcelRowToXMLNode(cellIterator);
		    output.getOutPutData().add(xmlData);
		}
	}

	private Map<String, String> convertExcelRowToXMLNode(Iterator<Cell> cellIterator) {
		Map<String, String> xmlData = new LinkedHashMap<String, String>();
		this.populateDefaultValues(xmlData);
        
        int cellPosition = 0;
		while(cellIterator.hasNext()) {
			if(this.excelConfig.getFields().size() > cellPosition) {
				String key = this.excelConfig.getFields().get(cellPosition);
				String value = cellIterator.next().getStringCellValue();
				if(value != null && value.trim().length() != 0) {
					xmlData.put(key, value);
				}
			} else {
				//Skip the extra columns present in excel
				cellIterator.next();
			}
            cellPosition++;
		}

		return xmlData;
	}
	
	private Map<String, String> populateDefaultValues(Map<String, String> map) {
		for(int index = 0; index < this.xmlConfig.getDefaultValues().size(); index++) {
			map.put(this.xmlConfig.getPropertiesNames().get(index), this.xmlConfig.getDefaultValues().get(index));
		}
		
		return map;
	}


	private void writeObjectToXml(Object object, String outputFile) throws JAXBException
	{
		File file = new File(outputFile);
		JAXBContext jaxbContext = JAXBContext.newInstance(Output.class);

		Marshaller marshaller = jaxbContext.createMarshaller();
		marshaller.setProperty(Marshaller.JAXB_FORMATTED_OUTPUT, true); 
		
		marshaller.marshal(object, file);
		//marshaller.marshal(object, System.out);
	}

}
