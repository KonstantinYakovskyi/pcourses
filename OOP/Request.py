import requests


class Request:
    def getjson(self):
        r = requests.get(r'http://localhost:8080/list?root=D/test')
        print(r)

h1 = Request()
h1.getjson()

if __name__ == '__main__':
    exit(h1)