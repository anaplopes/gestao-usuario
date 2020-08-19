# -*- coding: utf-8 -*-
from flask.views import MethodView
from services.worker_user import WorkerUserService
from flask import Blueprint


bp_user = Blueprint('user', __name__, url_prefix='/api')
class User(MethodView):
    
    def __init__(self):
        self.worker = WorkerUserService()

    def get(self, id=None):
        if id is None:
            return self.worker.list()   
        else:
            return self.worker.read(id=id)
                     

    def post(self):
        return self.worker.create()
    
    
    def put(self, id):
        return self.worker.update(id=id)


    def delete(self, id):
        return self.worker.delete(id=id)

view = User.as_view('user')
bp_user.add_url_rule('/user', view_func=view, methods=['GET'])
bp_user.add_url_rule('/user/<id>', view_func=view, methods=['GET', 'PUT', 'DELETE'])
bp_user.add_url_rule('/user/create', view_func=view, methods=['POST'])
