# -*- coding: utf-8 -*-

import MySQLdb


class Connection_Factory(object):
    def get_connection(self):
        return MySQLdb.connect(host='localhost',
                               user='root',
                               passwd='',
                               db='alura')
