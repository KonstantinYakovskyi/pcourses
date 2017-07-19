import fnmatch

import cherrypy
from os import listdir
from os.path import isfile, join


class DirListener:
    @cherrypy.expose
    def index(self):
        return 'hi there. select /list or /txt_list'

    @cherrypy.expose
    def list(self, root):
        result = [f for f in listdir(root) if isfile(join(root, f))]
        return str(result)

h1 = DirListener()
if __name__ == '__main__':
    cherrypy.quickstart(h1)

