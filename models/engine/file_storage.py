#!/usr/bin/python3
"""This is the file storage class for AirBnB"""
import json
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
import shlex


class FileStorage:
<<<<<<< HEAD
        """This class serializes instances to a JSON file and
            deserializes JSON file to instances
                Attributes:
                        __file_path: path to the JSON file
                                __objects: objects will be stored
                                    """
                                        __file_path = "file.json"
                                            __objects = {}

                                                def all(self, cls=None):
                                                            """returns a dictionary
                                                                    Return:
                                                                                returns a dictionary of __object
                                                                                        """
                                                                                                dic = {}
                                                                                                        if cls:
                                                                                                                        dictionary = self.__objects
                                                                                                                                    for key in dictionary:
                                                                                                                                                        partition = key.replace('.', ' ')
                                                                                                                                                                        partition = shlex.split(partition)
                                                                                                                                                                                        if (partition[0] == cls.__name__):
                                                                                                                                                                                                                dic[key] = self.__objects[key]
                                                                                                                                                                                                                            return (dic)
                                                                                                                                                                                                                                else:
                                                                                                                                                                                                                                                return self.__objects

                                                                                                                                                                                                                                                def new(self, obj):
                                                                                                                                                                                                                                                            """sets __object to given obj
                                                                                                                                                                                                                                                                    Args:
                                                                                                                                                                                                                                                                                obj: given object
                                                                                                                                                                                                                                                                                        """
                                                                                                                                                                                                                                                                                                if obj:
                                                                                                                                                                                                                                                                                                                key = "{}.{}".format(type(obj).__name__, obj.id)
                                                                                                                                                                                                                                                                                                                            self.__objects[key] = obj

                                                                                                                                                                                                                                                                                                                                def save(self):
                                                                                                                                                                                                                                                                                                                                            """serialize the file path to JSON file path
                                                                                                                                                                                                                                                                                                                                                    """
                                                                                                                                                                                                                                                                                                                                                            my_dict = {}
                                                                                                                                                                                                                                                                                                                                                                    for key, value in self.__objects.items():
                                                                                                                                                                                                                                                                                                                                                                                    my_dict[key] = value.to_dict()
                                                                                                                                                                                                                                                                                                                                                                                            with open(self.__file_path, 'w', encoding="UTF-8") as f:
                                                                                                                                                                                                                                                                                                                                                                                                            json.dump(my_dict, f)

                                                                                                                                                                                                                                                                                                                                                                                                                def reload(self):
                                                                                                                                                                                                                                                                                                                                                                                                                            """serialize the file path to JSON file path
                                                                                                                                                                                                                                                                                                                                                                                                                                    """
                                                                                                                                                                                                                                                                                                                                                                                                                                            try:
                                                                                                                                                                                                                                                                                                                                                                                                                                                            with open(self.__file_path, 'r', encoding="UTF-8") as f:
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                for key, value in (json.load(f)).items():
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        value = eval(value["__class__"])(**value)
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            self.__objects[key] = value
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    except FileNotFoundError:
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    pass

                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    def delete(self, obj=None):
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                """ delete an existing element
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        """
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                if obj:
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                key = "{}.{}".format(type(obj).__name__, obj.id)
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            del self.__objects[key]

                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                def close(self):
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            """ calls reload()
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    """
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            self.reload()
=======
    """This class manages storage of hbnb models in JSON format"""
    __file_path = 'file.json'
    __objects = {}

    def all(self, cls=None):
        """
        Add a new public instance method: def delete(self, obj=None):
        to delete obj from __objects if it’s inside - if obj is
        equal to None, the method should not do anything
        Update the prototype of def all(self) to def all(self, cls=None) -
        that returns the list of objects of one type of class
        """
        empty_dic = {}
        empty_list = []
        print(self.__objects)
        if cls is not None:

            for key , value in self.__objects.items():
                #if cls.__name__ in key:
                if isinstance(self.__objects, cls):
                    empty_dic.append(cls)
                    #empty_dic[key] = value
        else:
            
                return empty_list[self.__objects]
            #return empty_dic
            
            #empty_var ={}
            #for key,value in  self.__objects.items():
             #   sep_list = key.split(".")
              #  if cls.__name__ == sep_list[0]:
               #     empty_var[key] = value



            #return [ if isinstance(Filestorage.__objects, cls)]
        """Returns a dictionary of models currently in storage"""
        # return FileStorage.__objects

    def new(self, obj):
        """Adds new object to storage dictionary"""
        self.all().update({obj.to_dict()['__class__'] + '.' + obj.id: obj})

    def save(self):
        """Saves storage dictionary to file"""
        with open(FileStorage.__file_path, 'w') as f:
            temp = {}
            temp.update(FileStorage.__objects)
            for key, val in temp.items():
                temp[key] = val.to_dict()
            json.dump(temp, f)

    def reload(self):
        """Loads storage dictionary from file"""
        from models.base_model import BaseModel
        from models.user import User
        from models.place import Place
        from models.state import State
        from models.city import City
        from models.amenity import Amenity
        from models.review import Review

        classes = {
            'BaseModel': BaseModel, 'User': User, 'Place': Place,
            'State': State, 'City': City, 'Amenity': Amenity,
            'Review': Review
        }
        try:
            temp = {}
            with open(FileStorage.__file_path, 'r') as f:
                temp = json.load(f)
                for key, val in temp.items():
                    self.all()[key] = classes[val['__class__']](**val)
        except FileNotFoundError:
            pass

    def delete(self, obj=None):
        """ This method deletes key from the __object{}"""
        if obj is None:
            return
        for key, value in FileStorage.__objects.items():
            """ compares id if its equal to key"""
            if obj.id == key:
                del FileStorage.__objects[key]
                return
>>>>>>> 974c10551096d58df52f4c3c81ddb1c83d397f2c
