# -*- coding: utf-8 -*-
__author__ = 'sp41mer'
from conn_class import *
import socket
import errno
import argparse



def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('-host', type=str, help="Set host address (default is {})".format(default_host))
    parser.add_argument('-p', type=int, help="Set port (default is {})".format(default_port))
    parser.add_argument('-c', type=int, help="Set number of CPU (default is {})".format(DEF_NCPU))
    parser.add_argument('-r', type=str, help="Set root directory (default is {}".format(default_document_root))
    args = vars(parser.parse_args())

    host = args['host'] or default_host
    port = args['p'] or default_port
    cpu_count = args['c'] or DEF_NCPU
    document_root = args['r'] or default_document_root

    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    sock.bind((host, port))
    sock.listen(1024)

    forks = []
    for x in range(0, DEF_WORKERS_COUNT * cpu_count):
        pid = os.fork()
        forks.append(pid)
        if pid == 0:
            print 'Child PID:', os.getpid()
            while True:
                try:
                    client_connection, client_address = sock.accept()
                except IOError as e:
                    code, msg = e.args
                    if code == errno.EINTR:
                        continue
                    else:
                        raise
                http_connection = HttpConnection(client_connection, document_root)
                http_connection.do_response()
                client_connection.close()

    sock.close()

    for pid in forks:
        os.waitpid(pid, 0)

if __name__ == '__main__':
    main()