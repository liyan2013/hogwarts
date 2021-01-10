import yaml


def from_file(file):
    f = open(file, encoding='utf-8')
    return yaml.safe_load(f)
