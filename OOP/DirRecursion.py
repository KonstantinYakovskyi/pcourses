import cherrypy
from os import listdir
from os.path import isfile, join, isdir

def get_files(root):
    result = []
    items = listdir(root)
    for item in items:
        if isfile(join(root, item)):
            result.append(item + ', ')
        elif isdir(root):
            result += get_files(join(root, item))
    return result


class DirRecursion:
    @cherrypy.expose
    def index(self):
        return 'hi there. select /list or /txt_list'

    @cherrypy.expose
    def list(self, root):
        return get_files(root)

h1 = DirRecursion()
if __name__ == '__main__':
    cherrypy.quickstart(h1)

