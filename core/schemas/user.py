from manager import marsh


class UserSchema(marsh.Schema):
    """ Definição de schema de usuários """
    
    class Meta:
        fields = ('uuid', 'username', 'password', 'name', 'email', 'create_on')
        
        
        
user = UserSchema()
users = UserSchema(many=True)
