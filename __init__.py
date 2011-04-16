from utils.validcsv import validate
from utils.readcsv import csv_to_dict_reader

def validatecsv(filepath):
    reader = csv_to_dict_reader(filepath)
    return validate(reader)