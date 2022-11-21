import os 


class Config(): 
      SECRET_KEY =  os.environ.get('SECRET_KEY') or 'you-will-never-guess'
      SQLALCHEMY_TRACK_MODIFICATIONS = False
      
      SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or 'postgresql://my_projectsTheboys36@localhost:5432/budget_buddy1'
      SQLALCHEMY_ECHO = True 