package com.tools.models;

import java.util.ArrayList;
import java.util.List;
import java.util.Map;

import javax.xml.bind.annotation.XmlElement;
import javax.xml.bind.annotation.XmlRootElement;
import javax.xml.bind.annotation.adapters.XmlJavaTypeAdapter;

import com.tools.adaptor.MapAdapter;

@XmlRootElement(name="root")
public class Output {
	List<Map<String, String>> outPutData = new ArrayList<>();

	@XmlJavaTypeAdapter(MapAdapter.class)
	@XmlElement(name="root_sub_node")
	public List<Map<String, String>> getOutPutData() {
		return outPutData;
	}

	public void setOutPutData(List<Map<String, String>> outPutData) {
		this.outPutData = outPutData;
	}
	
}
