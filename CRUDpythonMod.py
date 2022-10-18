from pymongo import MongoClient
from bson.objectid import ObjectId


class AnimalShelter(object):
    """ CRUD operations for Animal collection in MongoDB """

    def __init__(self, username, password):
        # Initializing the MongoClient. This helps to 
        # access the MongoDB databases and collections. 
#         username = "aacuser"
#         password = "aacpwd"
        self.client = MongoClient('mongodb://%s:%s@localhost:54567/AAC' % (username, password))
        #where xxxx is your unique port number
        self.database = self.client['AAC']
        

# Complete this create method to implement the C in CRUD.
    def create(self, data):      
        if data is not None and type(data) is dict: # data should be dictionary 
            insert_result = self.database.animals.insert_one(data)
            
            if insert_result is not None: #if successful insert
                return True
                
        else:
            raise Exception("Nothing to save, because data parameter is not of type dict or empty")

        return False #return false if unsuccessful insert

# Create method to implement the R in CRUD. 
    def read(self, data):
    
        if data is not None and type(data) is dict:# data should be dictionary 
            result = self.database.animals.find(data, {"_id": False})  

        else:
            raise Exception("Nothing to save, because data parameter is empty or not of type dict")
        if result is not None:  
            return result
        else:
            raise Exception("MongoDB could not find data entered")
    
    # U of CRUD function
    def update(self, data_find, update_param):
        
        if data_find is not None and type(data_find) is dict: 
            if update_param is not None and type(update_param) is dict:
                # data_find and update_param should be dictionary
                
                # Update the animal based on update_param
                self.database.animals.update_one(data_find, update_param)
                # Store updated animal in variable
                animal = self.database.animals.find_one(data_find)
                
            else:
                raise Exception("Nothing to save, because data to find parameter is empty or not of type dict")
      
        else:
            raise Exception("Nothing to save, because update parameter is empty or not of type dict")
        return animal
    
    # D of CRUD function
    def delete(self, data):
        
        if data is not None and type(data) is dict: # data should be dictionary 
        
            # Deleting data
            print("\nDeleting", data)
            print(self.database.animals.delete_one(data)) 
            print("\nSuccessfully deleted", data)
            
        else:
            raise Exception("Nothing to save, because data to find parameter is empty or not of type dict")
            



