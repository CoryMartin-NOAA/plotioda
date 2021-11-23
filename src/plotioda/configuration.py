import yaml

def get_config(yamlfile):
    """
    Args:
        yamlfile: path to YAML file
    """
    with open(yamlfile, 'r') as file:
        config = yaml.load(file, Loader=yaml.FullLoader)
    
    return config
