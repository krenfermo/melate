import pandas as pd
import requests

def baja_csv():
    req = requests.get("https://www.pronosticos.gob.mx/Documentos/Historicos/Melate.csv")
    url_content = req.content
    csv_file = open('melate.csv', 'wb')

    csv_file.write(url_content)
    csv_file.close()
    
    data=pd.read_csv("melate.csv")
    data.drop(["NPRODUCTO", "CONCURSO","BOLSA","FECHA"], axis = 1, inplace = True) 
    return data



#https://www.pronosticos.gob.mx/Documentos/Historicos/Melate.csv
melate_df = baja_csv()

for col in melate_df.columns: 
    print("R", melate_df[col].value_counts().idxmax())
 

concatenated = pd.concat([melate_df["R1"], melate_df["R2"],melate_df["R3"], melate_df["R4"],melate_df["R5"], melate_df["R6"], melate_df["R7"]])


print()
print("mas comun de todos",concatenated.value_counts().idxmax())
print()
print(melate_df.value_counts()[:1].index.tolist())
df = pd.DataFrame (concatenated)
print(df.value_counts()[:7].index.tolist())


