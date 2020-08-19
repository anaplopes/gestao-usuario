# -*- coding: utf-8 -*-
import json
import traceback
from models.user import UserModel
from flask import jsonify, request
from db_execution import ExecutionDbService
from schemas.user import user_schema, users_schema
from werkzeug.security import generate_password_hash


class WorkerUserService:
    """ Serviço responsável pela regra de negócio 
        e as requisições ao db_execution. """
    
    def __init__(self):
        self.db_execution = ExecutionDbService()
    
    
    def create(self):
        username = request.json['username']
        password = request.json['password']
        name = request.json['name']
        email = request.json['email']
        pass_hash = generate_password_hash(password)
        
        user = UserModel(username, pass_hash, name, email)
        try:
            self.db_execution.add(user)
            self.db_execution.complete()
            result = user_schema.dump(user)
            return jsonify({
                'output': {
                    'data': result.data,
                    'message': 'successfully created',
                    'error': None,
                    'isValid': True
                }
            }), 201

        except Exception:
            return jsonify({
                'output': {
                    'data': [],
                    'message': 'unable to create',
                    'error': traceback.format_exc(),
                    'isValid': False
                }
            }), 500

    
    def list(self):
        try:
            user = UserModel.query.filter_by(isActive=True).all()
            if user:
                result = users_schema.dump(user)
                return jsonify({
                    'output': {
                        'data': result.data,
                        'message': 'successfully fetched',
                        'error': None,
                        'isValid': True
                    }
                }), 200
            
            return jsonify({
                'output': {
                    'data': [],
                    'message': 'nothing found',
                    'error': None,
                    'isValid': False
                }
            }), 404

        except Exception:
            return jsonify({
                'output': {
                    'data': [],
                    'message': None,
                    'error': traceback.format_exc(),
                    'isValid': False
                }
            }), 500
    
    
    def read(self, id):
        try:
            user = UserModel.query.filter_by(uuid=id, isActive=True).first()
            if user:
                result = user_schema.dump(user)
                return jsonify({
                    'output': {
                        'data': result.data,
                        'message': 'successfully fetched',
                        'error': None,
                        'isValid': True
                    }
                }), 200
            
            return jsonify({
                'output': {
                    'data': [],
                    'message': "user don't exist",
                    'error': None,
                    'isValid': False
                }
            }), 404

        except Exception:
            return jsonify({
                'output': {
                    'data': [],
                    'message': None,
                    'error': traceback.format_exc(),
                    'isValid': False
                }
            }), 500
    
            
    def update(self, id):
        username = request.json['username']
        password = request.json['password']
        name = request.json['name']
        email = request.json['email']
        
        user = UserModel.query.filter_by(uuid=id, isActive=True).first()
        if not user:
            return jsonify({
                'output': {
                    'data': [],
                    'message': "user don't exist",
                    'error': None,
                    'isValid': False
                }
            }), 404
        
        pass_hash = generate_password_hash(password)
        try:
            user.username = username
            user.password = pass_hash
            user.name = name
            user.email = email
            self.db_execution.complete()
            result = user_schema.dump(user)
            return jsonify({
                'output': {
                    'data': result.data,
                    'message': 'successfully updated',
                    'error': None,
                    'isValid': True
                }
            }), 201

        except Exception:
            return jsonify({
                'output': {
                    'data': [],
                    'message': 'unable to update',
                    'error': traceback.format_exc(),
                    'isValid': False
                }
            }), 500
    
    
    def delete(self, id):
        user = UserModel.query.filter_by(uuid=id, isActive=True).first()
        if not user:
            return jsonify({
                'output': {
                    'data': [],
                    'message': "user don't exist",
                    'error': None,
                    'isValid': False
                }
            }), 404
        
        try:
            user.isActive = False
            self.db_execution.complete()
            result = user_schema.dump(user)
            return jsonify({
                'output': {
                    'data': result.data,
                    'message': 'successfully deleted',
                    'error': None,
                    'isValid': True
                }
            }), 200

        except Exception:
            return jsonify({
                'output': {
                    'data': [],
                    'message': 'unable to delete',
                    'error': traceback.format_exc(),
                    'isValid': False
                }
            }), 500
