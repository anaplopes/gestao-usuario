# -*- coding: utf-8 -*-
from db_connection import ConnectionDbService


class ExecutionDbService:
    """ Serviço responsável por solicitar sessão,
        executar query e solicitar o salvamento dos dados. """

    def __init__(self):
        self.connection = ConnectionDbService()
        self.session = None

    def __enter__(self):
        self.session = self.connection.create_connection()
        return self.session

    def complete(self):
        self.connection.complete()

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.connection.save_change()
