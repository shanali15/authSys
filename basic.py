from tkinter import E
from turtle import end_poly
import requests
import bcrypt


# endpoint = "http://localhost:8000/api/"

# get_response = requests.get(endpoint)
# print(get_response.json())
pwd = '12345678'
bytePwd = pwd.encode('utf-8')  
mySalt = bcrypt.gensalt()
print(bytePwd,mySalt )
# Hash password
hash = bcrypt.hashpw(bytePwd, mySalt)
print(hash)
print(bcrypt.checkpw(bytePwd, hash))