import os 


class Config: 
      """Base configuration."""
      SECRET_KEY = os.environ.get('SECRET_KEY')
      SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL')
      SQLALCHEMY_TRACK_MODIFICATIONS = False
      SQLALCHEMY_ECHO = True  
     