import os
import yaml

def load_config(config_file):
    """Loads configuration from Koyeb environment variables if set, otherwise from a YAML file.

    Args:
        config_file (str): Path to the YAML configuration file.

    Returns:
        dict: The loaded configuration as a dictionary, or None if an error occurs.
    """
    config = {
        'serpapi_api_key': os.getenv('serpapi_api_key'),
        'groq_api_key': os.getenv('groq_api_key')
    }
    
    if None in config.values():
        try:
            with open(config_file, "r") as f:
                file_config = yaml.safe_load(f) or {}
                # Update only missing keys with file values
                config = {**file_config, **{k: v for k, v in config.items() if v is not None}}
        except FileNotFoundError:
            print(f"Config file not found: {config_file}")
            return None
        except Exception as e:
            print(f"Error loading config: {e}")
            return None
    
    return config
