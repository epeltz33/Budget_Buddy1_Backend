# Why doesnt the api folder have an __init__.py file?
# Because it is not a package, it is a module (a folder with python files)
# all of the other folders have an __init__.py file because they are packages 
 # packages in python allow you to import modules from other folders in your project
 # Why does the api folder not need to be a package?
 # Because the api folder will contain all of the routes for your application
  # and  you will not need to import any of the routes from other folders in your project because
  # the routes will be in the same folder as the __init__.py file
# then why do all of the other folders need to be packages?
# Because you will need to import  all of the models from the models folder and the seed files
# from the seed folder in the __init__.py file
 