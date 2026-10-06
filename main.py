from fastapi import FastAPI
from fastapi.responses import HTMLResponse

app = FastAPI()
posts = "name of the dictionary i have added"
@app.get("/")
def home():
        return {"message": "Hello, World!"}
@app.get("/name",response_class=HTMLResponse)
def main():
        return f"<h1>{posts}<h1>"
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