from .db import db
from flask_login import UserMixin 
from werkzeug.security import generate_password_hash, check_password_hash




class User(db.Model, UserMixin):
        __tablename__ = 'users' # why is this coming back as an Undefinded Table error?
        def __repr__(self): 
                return f"<User {self.id} {self.username} {self.email} {self.created_at} {self.updated_at}>"
        
        id = db.Column(db.Integer, primary_key=True)
        username = db.Column(db.String(40), nullable=False, unique=True)
        email = db.Column(db.String(255), nullable=False, unique=True)
        hashed_password = db.Column(db.String(255), nullable=False)
       
        
         
          
           
            
        def __str__(self): 
                return f"<User {self.id} {self.username} {self.email} {self.created_at} {self.updated_at}>"
       
            

        @property
        def password(self):
            return self.hashed_password
    
        @password.setter
        def password(self, password):
            self.hashed_password = generate_password_hash(password)
            
        def check_password(self, password):
            return check_password_hash(self.hashed_password, password)
    
        def to_dict(self):
                return {
                        "id": self.id,
                        "username": self.username,
                        "email": self.email,
                        "created_at": self.created_at,
                        "updated_at": self.updated_at
                }
                
       