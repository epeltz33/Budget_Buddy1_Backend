import os 


class Config(): 
     
     
     SECRET_KEY = os.environ.get('SECRET_KEY') 
     SQLALCHEMY_TRACK_MODIFICATIONS = False 
        
        # the .replace() is for when you deploy to Heroku  
     SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL').replace('postgres://', 'postgresql://')
     SQLALCHEMY_ECHO = True # prints out the SQL queries that are run in the terminal
  
     