from fastapi import FastAPI, Header, HTTPException
import pandas as pd

#membuat object FastAPI()
app = FastAPI()

df = pd.read_csv("dataset.csv")

@app.get("/")
def getHome():
    return{
        "message": "selamat datang di home!"
    }

@app.get("/all-data/")
def getAllData():
    return df.to_dict(orient='records')

@app.get("/all-data/address/{address}")
def getAddress(address):
    #filtering
    filter_address = df[df['address'] == address]
    return filter_address.to_dict(orient='records')

@app.get("/all-data/name/{name}")
def getName(name):
    #filtering
    filter_name = df[df['name'] == name]
    return filter_name.to_dict(orient='records')
    #return filter_address.to_dict(orient='records') 

@app.get("/all-data/id/{id}")
def getId(id: int):
    #filtering
    #df[df['id'] == id]
    filter_id = df[df['id'] == id]
    return filter_id.to_dict(orient='records')
    #return filter_address.to_dict(orient='records') 

#menambahkan dictionary ke dataframe
@app.post("/new-data")
def newData(updateData: dict): #(parameter:tipe data)
    
    value_id = len(df.index) + 1
    df.loc[len(df.index)] = [value_id, updateData["name"], updateData["address"]] #["7", "ana", "banten"]

    return updateData

API_KEY = "batagor2024$_"
#membuat endpoint untuk penggunaan API Key

@app.get("/dokumennegara")
def readSecret(api_key:str = Header(None)):
    if api_key == None or api_key != API_KEY:
        raise HTTPException(status_code=401, detail="hayo, mau lihat apa")
    
        return {
            "message": "mau lihat apa"
        }
    return {
        "message": "kamu sedang memaca dokumen rahasia negara"
    }






#command shift P


"""
data = []

##membuat endpoint (URL) untuk home/halaman utama

@app.get("/")
def getHome():
    return{
        "message": "selamat datang di home!"
    }

@app.post("/new")
def newdata(add_data:dict): 
    # menyiapkan data yang akan ditambahkan
    value_id = len(data) + 1
    add_data["id"] = value_id
    #add_data["name"] = "Budi"
    #add_data["address"] = "Jakarta"
    #memassukkan dictionary ke dalam list
    data.append(add_data)
    return add_data

    

"""
#uvicorn API_test:app --reload
# add /docs in the end

