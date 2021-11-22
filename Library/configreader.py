import configparser


def readdata(section,key):
    cfg = configparser.ConfigParser()
    cfg.read("C:/Softwares/Python/EndtoEndframework/Configurationfile/Nimconfig.cfg")
    return cfg.get(section,key)


print(readdata('details','URL'))










