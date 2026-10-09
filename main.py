from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from test import say_hi
from test import testFunction
templates = Jinja2Templates(directory="templates")
app = FastAPI()
posts = "name of the dictionary i have added"
@app.get("/")
def home():
        return {"message": "Hello, World!"}
@app.get("/name",response_class=HTMLResponse)
def main():
        value=say_hi("imran")
        return f"<h1>{value}<h1>"



@app.get("/html",include_in_schema=False)
def html_response(request: Request ):
        values=say_hi("New Html Page setup")
        val2=testFunction("from there on Pakistan zindabad")
        return templates.TemplateResponse(request, "home.html",{"valueshtml":values,"val2":val2})



@app.get("/area",response_class=HTMLResponse, include_in_schema=False)
def test():
        newPage=testFunction()
        return f"<h2>{newPage}<h2>"
       
       

# def the_decorator(func):
#      def wrapper():c
#         print("first Print")
#         func()
#         print("sencond Print")

#      return wrapper


# @the_decorator
# def hi():
#     print("hi")


# hi()