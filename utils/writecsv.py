import csv, os

def new_csv_file(folder_path, filename, fieldnames):
    result = csv.DictWriter(open(os.path.join(folder_path, filename + '.csv'), 'w'), fieldnames)
    headers = dict()
    result.writerow(dict((field, field) for field in fieldnames))
    
    return result