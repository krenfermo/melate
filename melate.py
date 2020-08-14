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

from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    #https://www.pronosticos.gob.mx/Documentos/Historicos/Melate.csv
    melate_df = baja_csv()
    primera=[]
    for col in melate_df.columns: 
        primera.append(melate_df[col].value_counts().idxmax())
        #print("R", melate_df[col].value_counts().idxmax())
     

    concatenated = pd.concat([melate_df["R1"], melate_df["R2"],melate_df["R3"], melate_df["R4"],melate_df["R5"], melate_df["R6"], melate_df["R7"]])
    segunda=[]
    segunda.append(primera)
    segunda.append("mas comun de todos: "+str(concatenated.value_counts().idxmax()))
    #print()
    #print("mas comun de todos",concatenated.value_counts().idxmax())
    #print()
    segunda.append(melate_df.value_counts()[:1].index.tolist()[0])
    #print(melate_df.value_counts()[:1].index.tolist())
    df = pd.DataFrame (concatenated)
    segunda.append(df.value_counts()[:7].index.tolist())
    #print(df.value_counts()[:7].index.tolist())

    #print (segunda)
    return str(segunda)

if __name__ == "__main__":
    app.run(debug=True,port=8000, host='0.0.0.0') 


