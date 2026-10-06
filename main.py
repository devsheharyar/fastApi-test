from fastapi import FastAPI
app = FastAPI()
@app.get("/")
def home():
        return {"message": "Hello, World!"}
@app.get("/name")
def main():
        return {"message":"Pakistan"}
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