package com.tools.config;

import org.springframework.boot.context.properties.ConfigurationProperties;
import org.springframework.context.annotation.Configuration;

import lombok.Data;

@Data
@Configuration
@ConfigurationProperties(prefix = "app-arguments")
public class ApplicationArguments {
	
	private String input;
	private String output;
}
