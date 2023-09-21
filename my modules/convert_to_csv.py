from pathlib import Path
from pprint import pprint
import pandas as pd
import re 
import logging

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s') #Configure the logging

class Convert_xlfile_to_csv:
    def __init__(self):
        self.search_path = input("Insert your directory file by clicking ctrl + shift + V after copying it : ")
        self.logger = logging

    def create_cvs_file(self):
        csv_folder = Path(self.search_path) / 'csv folder'
        csv_folder.mkdir(exist_ok=True)
        xlfile_list = list(Path(self.search_path).rglob("*")) #To list every xlfile 

        for each_file in xlfile_list:
            if str(each_file).endswith(((".xlsx", "xls", ".xlsm", ".xlsb", ".xltx", ".xltm", ".xla", ".xlam", ".xll", ".ods"))):
                clean_file_name = re.sub(r"\.xlsx|\.xls|\.xlsm|\.xlsb|\.xltx|\.xltm|\.xla|\.xlam|\.xll|\.ods", '', str(each_file), flags=re.IGNORECASE)
                xfile_file = pd.ExcelFile(str(each_file))
                sheets = xfile_file.sheet_names
                for each_sheet in sheets:
                    sheet_data = xfile_file.parse(each_sheet)
                    csv_name = clean_file_name + '-' + each_sheet + '.csv'
                    sheet_data.to_csv(csv_folder / Path(csv_name).name,index=False)

        self.logger.info('Actions terminated successfully') #Print the message

if __name__ == '__main__':
    print("You are in this file")