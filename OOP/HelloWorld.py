"""
http://docs.cherrypy.org/en/latest/tutorials.html
https://github.com/koder-ua/python-classes/blob/master/slides/pdf/FF_tasks_simple.pdf
"""

import cherrypy


class HelloWorld(object):
    @cherrypy.expose
    def index(self):
        return 'Hi there from HelloWorld!'

    @cherrypy.expose
    def sum(self, x, y):
        return x + y

    @cherrypy.expose
    def b(self):
        pass


class HelloWorld2(HelloWorld):
    @cherrypy.expose
    def index(self):
        return 'Hi there from HelloWorld2'

h1 = HelloWorld()
h2 = HelloWorld2()

h1.b = h2

if __name__ == '__main__':
    cherrypy.quickstart(h1)

# At home
