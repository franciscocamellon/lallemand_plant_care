# -*- coding: utf-8 -*-
"""
/***************************************************************************
 PostgresFactory
                                 A QGIS plugin
 Lallemand - Crop Analysis Environment
 Generated by Plugin Builder: http://g-sherman.github.io/Qgis-Plugin-Builder/
                             -------------------
        begin                : 2023-10-04
        git sha              : $Format:%H$
        copyright            : (C) 2023 by CamellOnCase
        email                : camelloncase@gmail.com
 ***************************************************************************/

/***************************************************************************
 *                                                                         *
 *   This program is free software; you can redistribute it and/or modify  *
 *   it under the terms of the GNU General Public License as published by  *
 *   the Free Software Foundation; either version 2 of the License, or     *
 *   (at your option) any later version.                                   *
 *                                                                         *
 ***************************************************************************/
"""
import os

import psycopg2
import logging
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT


class PostgresFactory:
    def __init__(self):
        super(PostgresFactory, self).__init__()
        logging.basicConfig(filename=os.path.join(os.path.dirname(__file__), 'postgres_log.log'), level=logging.ERROR)

    @staticmethod
    def open_connection_to_db(database_name):
        conn = psycopg2.connect(
            database=database_name,
            user='postgres',
            password='postgres',
            host='127.0.0.1',
            port='5432'
        )

        conn.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)
        conn.autocommit = True
        return conn

    def getSqlExecutor(self, connection, sql):
        try:
            with connection.cursor() as curs:
                curs.execute(sql)
                result = curs.fetchall()
                curs.close()
            connection.close()
            return result
        except psycopg2.Error as e:
            error_message = f"Error executing SQL: {e}"
            logging.error(error_message)
            self.close_connection(connection)
            return error_message

    def postSqlExecutor(self, connection, sql, data=None):
        try:
            with connection.cursor() as curs:
                if data:
                    curs.execute(sql, data)
                else:
                    curs.execute(sql)
                curs.close()
            connection.close()
            return True
        except psycopg2.Error as e:
            error_message = f"Error executing SQL: {e}"
            logging.error(error_message)
            self.close_connection(connection)
            return False, error_message

    @staticmethod
    def close_connection(connection):
        connection.close()
