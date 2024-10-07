import os
import yaml

def get_apikey():
    """
    Reads API key from a configuration file.

    This function opens a configuration file named "apikeys.yml", reads the API key for OpenAI

    Returns:
    api_key (str): The OpenAI API key.
    """
    
    script_dir = ""
    file_path = os.path.join(script_dir, "myapikeys.yml")
    # correct filepath later
    
    with open(file_path, 'r') as yamlfile:
        loaded_yamlfile = yaml.safe_load(yamlfile)
        API_KEY = loaded_yamlfile['openai']['api_key']
    
    return API_KEY
# apikeys.yml
if __name__ == "__main__":
    print("API_KEY", get_apikey())