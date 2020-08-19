# -*- coding: utf-8 -*-
import sys
import json
import traceback
from models.user import User
from schemas.user import user_schema, users_schema
from db_execution import DbExecutionService
from flask import Blueprint, jsonify, request
from werkzeug.security import generate_password_hash


class WorkerUserService():
    """ Serviço responsável pela regra de negócio 
        e as requisições ao db_execution. """
    
    def __init__(self):
        self.db_exec = DbExecutionService()
    
    
    def create(self):
        username = request.json['username']
        password = request.json['password']
        name = request.json['name']
        email = request.json['email']
        pass_hash = generate_password_hash(password)
        user = Users(username, pass_hash, name, email)
        
        try:
            db_exec.create_one(data=user)
            result = user_schema.dump(user)
            return jsonify({
                'output': {
                    'data': result.data,
                    'message': 'user saved successfully',
                    'error': None,
                    'isValid': True
                }
            }), 201

        except Exception:
            return jsonify({
                'output': {
                    'data': [],
                    'error': traceback.format_exc(),
                    'isValid': False
                }
            }), 500
    
    # def create(self, payload):
    #     if not payload:
    #         return {
    #             'statusCode': 400,
    #             'output': {
    #                 'data': [],
    #                 'error': 'I was expecting a payload, but apparently on is missing',
    #                 'isValid': False
    #             }
    #         }
        
    #     payload['dt_publish'] = datetime.utcnow()
    #     self.db.create_one(payload)
    #     return {
    #         'statusCode': 201,
    #         'output': {
    #             'data': [],
    #             'message': 'User saved successfully',
    #             'error': None,
    #             'isValid': True
    #         }
    #     }


    # def list(self):
    #     users = self.db.read_all(table=User)
    #     return {
    #         'statusCode': 200,
    #         'output': {
    #             'data': users,
    #             'qtd_registro': len(news),
    #             'error': None,
    #             'isValid': True
    #         }
    #     }
    
    
    # def read(self, id):
    #     if not id:
    #         return {
    #             'statusCode': 400,
    #             'output': {
    #                 'data': [],
    #                 'error': 'I was expecting a id, but apparently on is missing',
    #                 'isValid': False
    #             }
    #         }
            
    #     news = self.db.find_one(collection='news', id=id, param={'isActive': True})
    #     if not news:
    #         return {
    #             'statusCode': 404,
    #             'output': {
    #                 'data': [],
    #                 'error': 'Id does not exist',
    #                 'isValid': False
    #             }
    #         }
            
    #     return {
    #         'statusCode': 200,
    #         'output': {
    #             'data': {
    #                 "_id": news['_id'],
    #                 "title": news['title'],
    #                 "content": news['content'],
    #                 "dt_publish": news['dt_publish']
    #             },
    #             'error': None,
    #             'isValid': True
    #         }
    #     }


    # def update(self, id, payload):
    #     if not id or not payload:
    #         return {
    #             'statusCode': 400,
    #             'output': {
    #                 'data': [],
    #                 'error': 'I was expecting a id and a payload, but apparently on (or both) is missing',
    #                 'isValid': False
    #             }
    #         }
        
    #     news = self.db.find_one(collection='news', id=id, param={'isActive': True})
    #     if not news:
    #         return {
    #             'statusCode': 404,
    #             'output': {
    #                 'data': [],
    #                 'error': 'Id does not exist',
    #                 'isValid': False
    #             }
    #         }
        
    #     self.db.update_one(collection='news', id=id, data=payload)
    #     return {
    #         'statusCode': 200,
    #         'output': {
    #             'data': [],
    #             'message': 'News updated successfully',
    #             'error': None,
    #             'isValid': True
    #         }
    #     }
    
        
    # def delete(self, id):
    #     if not id:
    #         return {
    #             'statusCode': 400,
    #             'output': {
    #                 'data': [],
    #                 'error': 'I was expecting a id, but apparently on is missing',
    #                 'isValid': False
    #             }
    #         }
            
    #     news = self.db.find_one(collection='news', id=id, param={'isActive': True})
    #     if not news:
    #         return {
    #             'statusCode': 404,
    #             'output': {
    #                 'data': [],
    #                 'error': 'Id does not exist',
    #                 'isValid': False
    #             }
    #         }
        
    #     self.db.update_one(collection='news', id=id, data={'isActive': False})
    #     return {
    #         'statusCode': 200,
    #         'output': {
    #             'data': [],
    #             'message': 'News successfully deleted',
    #             'error': None,
    #             'isValid': True
    #         }
    #     }
