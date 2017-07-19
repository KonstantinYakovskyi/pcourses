# https://stackoverflow.com/questions/3207219/how-do-i-list-all-files-of-a-directory
import fnmatch

import cherrypy
from os import listdir
from os.path import isfile, join


class DirListener:
    def __init__(self, root):
        self.root = root

    def index(self):
        return 'hi there. select /list or /txt_list'

    def list(self):
        result = [f for f in listdir(self.root) if isfile(join(self.root, f))]
        return str(result)


class TxtListener(DirListener):
    def txt_list(self):
        lst = self.list()
        res = [file for file in lst if fnmatch.fnmatch(file, '*.txt')]
        return res


h1 = DirListener()

if __name__ == '__main__':
    cherrypy.quickstart(expose)

