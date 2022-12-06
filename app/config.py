import os 


class Config: 
      
      SECRET_KEY = os.environ.get('SECRET_KEY')
      SQLALCHEMY_DATABASE_URI = os.environ.get(' SQLALCHEMY_DATABASE_URI ') or'postgresql://ericpeltzman:Theboys36@localhost:5432/python_project'
      SQLALCHEMY_TRACK_MODIFICATIONS = False
      SQLALCHEMY_ECHO = True  
     