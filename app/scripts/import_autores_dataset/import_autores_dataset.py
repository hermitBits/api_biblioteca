import pandas as pd
import requests

class ImportAutoresDataSet:
    def __init__(self, file):
        self.file = file
    
    def action(self):
        df = pd.read_csv(self.file, sep=";")
                
        for index, row in df.iterrows():
            res = requests.post(
                "http://0.0.0.0:8085/autores/criar_autor/", 
                json={
                    "nome": row.autor.title().strip()
                }
            )
            print(index, res.text)
            print("----------")