package com.tools.config;

import java.util.List;

import org.springframework.boot.context.properties.ConfigurationProperties;
import org.springframework.context.annotation.Configuration;

import lombok.Builder;
import lombok.Data;

@Data
@Builder

@Configuration
@ConfigurationProperties(prefix = "excel")
public class ExcelConfig {

	private List<String> fields;
}
