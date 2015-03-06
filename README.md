# csvtometadata
Python module that can be used to convert CSV documents created using the USGIN metadata template into USGIN-profile XML metadata records.  
  
This CSV to USGIN-profile ISO XML also uses https://github.com/usgin/xmlvalidator as a tool to transform CSV files in the metadata content model (http://schemas.usgin.org/models/#Metadata). It takes each record from the spreadsheet (having field headings and data types as specified in the content model) and parses those to individual metadata records.  
  
The work flow for transforming metadata into a records in the USGIN catalog are as follows:  
1) Enter metadata into the Metadata Content Model, save as CSV.  
2) Clone this repository to desktop to run. Open the runcsvtoxml.py file in Notepad++ or another editer. Edit ONLY the csv_filepath and the output_folder_path and close. Double-click runcsvtoxml.py to run.  
3) Valid files will be dropped into the output/valid-xml folder. Move those files to a WAF.  
4) In a USGIN-profile GeoPortal or other catalog instance (https://github.com/usgin/usginspecs/blob/master/Setting%20up%20a%20USGIN%20ISO%2019115%20Profile%20for%20ESRI%20Geoportal.docx?raw=true) register the WAF as a new resource and harvest.  
