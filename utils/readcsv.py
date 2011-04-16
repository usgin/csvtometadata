import csv

def csv_to_dict_reader(csv_file_path):
    try:
        return csv.DictReader(open(csv_file_path))
    except IOError, ex:
        raise ex
    except Exception, ex:
        raise ex