from csvtometadata import transformcsv
import os

csv_filepath = 'C:\\Data\\Metadata\\EGI_NGDS_PrelimGeothermalDataMetadata1.3.5_Task1709_20140206_EP_DL_done.csv'
output_folder_path = 'C:\\Data\\Metadata\\Data_To_Process\\output'

# Don't mess with anything else below here
#------------------------------------------------------------

def output_report(report, folder_path):
    report_path = os.path.join(folder_path, 'report.txt')
    f = open(report_path, 'w')
    f.write('\r\n'.join(report))
    f.close()
    
report = transformcsv(csv_filepath, output_folder_path)
output_report(report, output_folder_path)
