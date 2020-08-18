# -*- coding: utf-8 -*-
import sys
import json
import traceback
from datetime import datetime
from flask.views import MethodView
from flask import Blueprint, jsonify, request
from werkzeug.security import generate_password_hash
from ..services.worker_user import WorkerUserService


bp_user = Blueprint('user', __name__, url_prefix='/api')
class User(MethodView):
    
    def __init__(self):
        self.worker = WorkerUserService()


    def get(self, id=None):
        try:
            if id is None:
                response = self.worker.list()
            else:
                response = self.worker.read(id=id)
            return jsonify({'output': response['output']}), response['statusCode']
            
        except Exception:
            return jsonify({
                'output': {
                    'data': [],
                    'error': traceback.format_exc(),
                    'isValid': False
                }
            }), 500


    def post(self):
        try:
            payload = request.get_json()
            username = request.json['username']
            password = request.json['password']
            name = request.json['name']
            email = request.json['email']
            pass_hash = generate_password_hash(password)
            response = self.worker.create(payload=payload)
            return jsonify({'output': response['output']}), response['statusCode']
            
        except Exception:
            return jsonify({
                'output': {
                    'data': [],
                    'error': traceback.format_exc(),
                    'isValid': False
                }
            }), 500


    def put(self, id):
        try:
            payload = request.get_json()
            response = self.worker.update(id=id, payload=payload)
            return jsonify({'output': response['output']}), response['statusCode']
            
        except Exception:
            return jsonify({
                'output': {
                    'data': [],
                    'error': traceback.format_exc(),
                    'isValid': False
                }
            }), 500
        
        
    def delete(self, id):
        try:
            response = self.worker.delete(id=id)
            return jsonify({'output': response['output']}), response['statusCode']
            
        except Exception:
            return jsonify({
                'output': {
                    'data': [],
                    'error': traceback.format_exc(),
                    'isValid': False
                }
            }), 500


view = News.as_view('user')
bp_news.add_url_rule('/user', view_func=view, methods=['GET'])
bp_news.add_url_rule('/user/<id>', view_func=view, methods=['GET', 'PUT', 'DELETE'])
bp_news.add_url_rule('/user/create', view_func=view, methods=['POST'])
