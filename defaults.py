__author__ = 'sp41mer'

import os

default_host = '0.0.0.0'
default_port = 80
default_document_root = os.path.dirname(__file__) + '/document_root'
DEF_WORKERS_COUNT = 2
DEF_NCPU = 2
content_types_list = {
    'html': 'text/html',
    'css': 'text/css',
    'js': 'application/javascript',
    'jpg': 'image/jpeg',
    'jpeg': 'image/jpeg',
    'png': 'image/png',
    'gif': 'image/gif',
    'swf': 'application/x-shockwave-flash',
    'txt': 'text/plain'
}
DEFAULT_CONTENT_TYPE = 'application/octet-stream'
server_answers_list = {
    200: 'OK',
    400: 'Bad request',
    403: 'Forbidden',
    404: 'Not Found',
    405: 'Method not allowed',
    500: 'Internal Server Error',
    502: 'Bad Gateway',
    504: 'Gateway Time-out'
}
name = 'superserver(net)'
separator = '\r\n'
index_page = 'index.html'
methods_list = ['GET', 'HEAD']
PORTION_TO_SEND = 4096

