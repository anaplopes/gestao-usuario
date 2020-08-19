# -*- coding: utf-8 -*-
from sqlalchemy_filters import apply_filters, apply_sort
from db_connection import ConnectionDbService


class ExecutionDbService:
    """ Serviço responsável por solicitar sessão ao db_connection 
        e executar query. """

    def __init__(self):
        self.connection = ConnectionDbService()
        self.session = None

    def __enter__(self):
        self.session = self.connection.create_connection()
        return self.session

    def complete(self):
        self.connection.complete()

    def create_one(self, data):
        return self.session.add(data)

    def create_many(self, data):
        return self.session.add_all(data)

    def read_all(self, table):
        obj_model = eval(table)
        return self.session.query(obj_model).all()

    def filter_all(self, table, filter_spec, sort_spec=None):
        obj_model = eval(table)
        query = self.session.query(obj_model)
        filtered_query = apply_filters(query, filter_spec)
        if sort_spec:
            filtered_query = apply_sort(filtered_query, sort_spec)
        return filtered_query.all()

    def filter_first(self, table, filter_spec):
        obj_model = eval(table)
        query = self.session.query(obj_model)
        filtered_query = apply_filters(query, filter_spec)
        return filtered_query.first()

    def update(self, table, filter_spec, data):
        obj_model = eval(table)
        query = self.session.query(obj_model)
        filtered_query = apply_filters(query, filter_spec)
        return filtered_query.update(data)

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.connection.save_change()
