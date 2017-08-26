HTTP = 'HTTP/1.0 301 Moved Permanently\r\nLocation: http://www.google.com/\r\nContent-Type: text/html; charset=UTF-8\r\nDate: Mon, 24 Jul 2017 16:26:03 GMT\r\nExpires: Wed, 23 Aug 2017 16:26:03 GMT\r\nCache-Control: public, max-age=2592000\r\nServer: gws\r\nContent-Length: 219\r\nX-XSS-Protection: 1; mode=block\r\nX-Frame-Options: SAMEORIGIN\r\n\r\n<HTML><HEAD><meta http-equiv="content-type" content="text/html;charset=utf-8">\n<TITLE>301 Moved</TITLE></HEAD><BODY>\n<H1>301 Moved</H1>\nThe document has moved\n<A HREF="http://www.google.com/">here</A>.\r\n</BODY></HTML>\r\n'
SPLITTER = '\r\n\r\n'


class HttpObject:
    def __init__(self, http, version=None, code=None, message=None, headers=None, body=None):
        self.http = http
        self.version = version
        self.code = code
        self.message = message
        self.headers = headers
        self.body = body


def parse_http_to_obj(http):
    http_obj = HttpObject(http)

    headers = (http.rsplit(SPLITTER, 1)[0]).splitlines()
    body = http.rsplit(SPLITTER, 1)[1]

    first_elem = headers[0]
    http_obj.version, http_obj.code, http_obj.message = first_elem.split(' ', 2)

    headers_dict = {}
    for element in headers[1:]:
        k, y = element.split(': ')
        headers_dict[k] = y

    http_obj.headers = headers_dict
    http_obj.body = body
    return http_obj


def parse_http(http):
    http_obj = parse_http_to_obj(http)

    print(http_obj.version)
    print(http_obj.code)
    print(http_obj.message)
    print(http_obj.headers)
    print(http_obj.body)


assert parse_http_to_obj(HTTP).version == 'HTTP/1.0'
assert parse_http_to_obj(HTTP).code == '301'
assert parse_http_to_obj(HTTP).message == 'Moved Permanently'
assert parse_http_to_obj(HTTP).headers == {'Location': 'http://www.google.com/', 'Content-Type': 'text/html; charset=UTF-8', 'Date': 'Mon, 24 Jul 2017 16:26:03 GMT', 'Expires': 'Wed, 23 Aug 2017 16:26:03 GMT', 'Cache-Control': 'public, max-age=2592000', 'Server': 'gws', 'Content-Length': '219', 'X-XSS-Protection': '1; mode=block', 'X-Frame-Options': 'SAMEORIGIN'}

if __name__ == '__main__':
    exit(parse_http(HTTP))
