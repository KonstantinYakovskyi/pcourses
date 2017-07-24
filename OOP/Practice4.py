import requests

HTTP = 'HTTP/1.0 301 Moved Permanently\r\nLocation: http://www.google.com/\r\nContent-Type: text/html; charset=UTF-8\r\nDate: Mon, 24 Jul 2017 16:26:03 GMT\r\nExpires: Wed, 23 Aug 2017 16:26:03 GMT\r\nCache-Control: public, max-age=2592000\r\nServer: gws\r\nContent-Length: 219\r\nX-XSS-Protection: 1; mode=block\r\nX-Frame-Options: SAMEORIGIN\r\n\r\n<HTML><HEAD><meta http-equiv="content-type" content="text/html;charset=utf-8">\n<TITLE>301 Moved</TITLE></HEAD><BODY>\n<H1>301 Moved</H1>\nThe document has moved\n<A HREF="http://www.google.com/">here</A>.\r\n</BODY></HTML>\r\n'


class HttpObject:
    def __init__(self, http, version=None, location=None, content_type=None):
        self.http = http
        self.version = version
        self.location = location
        self.content_type = content_type


def parse_http(http = ''):
    res = HttpObject(http)

    for element in http.splitlines():


    return res


if __name__ == '__main__':
    exit(h)

'HTTP/1.0 301 Moved Permanently\r\nLocation: http://www.google.com/\r\nContent-Type: text/html; charset=UTF-8\r\nDate: Mon, 24 Jul 2017 16:26:03 GMT'
