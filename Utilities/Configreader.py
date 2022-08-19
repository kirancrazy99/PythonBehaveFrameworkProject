from configparser import ConfigParser


def config_reader(head, element):
    config = ConfigParser()
    config.read(r"..\ConfigData\conf.ini")
    return config.get(head, element)





