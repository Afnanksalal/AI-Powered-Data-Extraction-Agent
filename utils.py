import yaml

def load_config(config_file):
    """Loads configuration from a YAML file.

    Args:
        config_file (str): Path to the YAML configuration file.

    Returns:
        dict:  The loaded configuration as a dictionary, or None if an error occurs.
    """
    try:
        with open(config_file, "r") as f:
            config = yaml.safe_load(f)
            return config
    except FileNotFoundError:
        print(f"Config file not found: {config_file}")
        return None
    except Exception as e:
        print(f"Error loading config: {e}")
        return None
