from fastapi import FastAPI
app=FastAPI()
@app.get("/")
def home():
    return{"message": "hello world"}
@app.get("/about{item_id}")
def about(item_id:bool):
    return{"item_id":item_id}

@app.get("/search/")
def search_items(keyword:str,limit:int):
    return{'keyword':keyword,'limit':limit}

@app.get("/greet/{user_id}")
def greet(user_id:int,user_name:str,user_presence:bool):
    return{"user_id":user_id , "user_name":user_name,"user_presence":user_presence}

# nested dictionaries
@app.get("/nested")
def nested_dic():
    return{'name':'mariam','age':20,'qualifications':['matric','inter','bs']}