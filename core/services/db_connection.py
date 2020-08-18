# -*- coding: utf-8 -*-
import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


class ConnectionDbService:  
    """ Serviço responsável por cria uma conexão com o database,
        disponibilizar sessões,
        salvar alterações e fechar tudo ao termino do processo. """

    def __init__(self):
        self.url_engine = os.getenv('CONNECTION_URL', '')
        self.engine = None
        self._session = None
        self._complete = False

    def complete(self):
        self._complete = True

    def create_connection(self):
        self.engine = create_engine(self.url_engine, convert_unicode=True)
        session = sessionmaker(bind=self.engine, expire_on_commit=False)
        self._session = session()
        return self._session

    def save_change(self):
        try:
            if self._complete:
                self._session.commit()
            else:
                self._session.rollback()
        except Exception as e:
            self._session.rollback()
            raise Exception(e)
        finally:
            self._session.close()
            self.engine.dispose()
