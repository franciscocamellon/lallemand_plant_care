# -*- coding: utf-8 -*-
"""
/***************************************************************************
 RegisterLpcTeam
                                 A QGIS plugin
 Lallemand Plant Care
 Generated by Plugin Builder: http://g-sherman.github.io/Qgis-Plugin-Builder/
                              -------------------
        begin                : 2023-10-07
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
import datetime
import os

from qgis.PyQt import QtWidgets, uic

from ..factories.postgres_factory import PostgresFactory
from ...gui.lpc_team.ui_register import RegisterLpcTeamUiDialog


class RegisterLpcTeam(QtWidgets.QDialog, RegisterLpcTeamUiDialog):

    def __init__(self):
        """Constructor."""
        super(RegisterLpcTeam, self).__init__()
        self.setupUi(self)
        self.lpcTeamRegisterButtonBox.accepted.connect(self.register)
        self.lpcTeamRegisterButtonBox.rejected.connect(self.reject)

    def register(self):
        connection = PostgresFactory().open_connection_to_db('BD_GEOSTAT_LPC')
        firstName = self.lpcTeamFirstNameLineEdit.text()
        lastName = self.lpcTeamLastNameLineEdit.text()
        createDate = datetime.datetime.now()

        sql = "INSERT INTO geostatistics.lpc_team (first_name, last_name, create_date) VALUES (%s, %s, %s);"
        data = (firstName, lastName, createDate.strftime('%Y-%m-%d %H:%M:%S'))
        result = PostgresFactory().postSqlExecutor(connection, sql, data)
        self.handleButtonClick(result)

    def handleButtonClick(self, result):
        if result:
            self.accept()
