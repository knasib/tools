import yaml

with open('resources/application.yaml') as yaml_file:
    yamlreader = yaml.safe_load(yaml_file)


def get_properties(key_str):
    yaml_crawler = yamlreader
    keys = key_str.split(".")

    for key in keys:
        yaml_crawler = yaml_crawler[key]
    return yaml_crawler
