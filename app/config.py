import os 


class Config: 
     """Set Flask configuration vars from .env file.""" 
     # General Config 
     SECRET_KEY = os.environ.get('SECRET_KEY') 
     
        # Database Config
        # the .replace() is for when you deploy to Heroku  
     SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL').replace('postgres://', 'postgresql://')
     SQLALCHEMY_ECHO = True # prints out the SQL queries that are run in the terminal
     SQLALCHEMY_TRACK_MODIFICATIONS = False  # silence the deprecation warning  