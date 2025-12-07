import numpy as n
import requests as r
print("Hello Buddy, this is my new project")
print("Numpy")
print(n.abs(-2))
resp = r.get('https://jsonplaceholder.typicode.com/todos/1')
print(resp.json())

