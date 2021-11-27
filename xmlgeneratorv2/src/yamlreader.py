import yaml

with open('resources/application.yaml') as yamlfile:
  yamlreader = yaml.safe_load(yamlfile)

def getProperties(keystr):
  yamlCrawler = yamlreader
  keys = keystr.split(".")
    
  for key in keys:
      yamlCrawler = yamlCrawler[key]
  return yamlCrawler;   
