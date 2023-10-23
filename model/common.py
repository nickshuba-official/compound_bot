import configparser


def open_config():
    config = configparser.ConfigParser()
    config.optionxform = str
    config_file = open(
        file=r".\config.ini",
        encoding="utf-8"
    )
    config.read_file(config_file)
    return config
