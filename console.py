#!/usr/bin/python3
"""the console"""

import cmd
from datetime import datetime
import models
from models.user import User
from models.base_model import BaseModel
import shlex  # for spliting purposes except when there is double quotes
import argparse
import mysql.connector
import re

classes = {"User": User, "BaseModel": BaseModel}

class MAZINGIRABORACommand(cmd.Cmd):
    """MAZINGIRA comsole"""
    prompt = '(mazingirabora)'

    def do_EOF(self, arg):
        """exits console"""
        return True

    def emptyline(self):
        """overwrites an empty line"""
        return False

    def do_quit(self, arg):
        """quits command to the program"""
        return True

    def _key_value_parser(self, args):
        """creates dictionary from list of strings"""
        new_dict = {}
        for arg in args:
            if "=" in arg:
                kvp = arg.split('=', 1)
                key = kvp[0]
                value = kvp[1]
                if value[0] == value[-1] == '"':
                    value = shlex.split(value)[0]
                else:
                    try:
                        value = int(value)
                    except:
                        try:
                            value = float(value)
                        except:
                            continue
                new_dict[key] = value
        return new_dict

    def do_create(self, arg):
        """creates new class instance"""
        args = arg.split()
        if len(args) == 0:
            print("*class name missing*")
            return False
        if args[0] in classes:
            new_dict = self._key_value_parser(args[1:])
            instance = classes[args[0]](**new_dict)
        else:
            print("*class doesn't exist*")
            return False
        print(instance.id)
        instance.save()

    def do_show(self, arg):
        """ prints instances based on class and id"""
        args = shlex.split(arg)
        if len(args) == 0:
            print("*class name missing*")
            return False
        if args[0] in classes:
            if len(args) > 1:
                key = args[0] + "." + args[1]
                if key in models.storage.all():
                    print(models.storage.all()[key])
                else:
                    print("*no instance found*")
            else:
                print("*instance id missing*")
        else:
            print("*class doesn't exist*")

    # establish a mysql connection
    con = mysql.connector.connect(
            host="mysql_host",
            user="mysql_user",
            password="mysql_password",
            database="database_name"
    )
    cursor = conn.cursor()

    # create user table
    create_table_query = """
    CREATE TABLE IF NOT EXISTS users (
       id INT AUTO_INCREMENT PRIMARY KEY,
       first_name VARCHAR(255),
       last_name VARCHAR(255),
       email VARCHAR(255),
       phone VARCHAR(15),
       password VARCHAR(255)
    )
    """
    cursor.execute(create_table_query)
    conn.commit()

    def do_register():
        """collecting user information"""
        first_name = input("Enter your first name:")
        last_name = input("Entee your last name:")
        email = input("Enter valid email:")
        phone = input("Enter phone number:")
        password = input("Create password:")

        if not re.match(
    r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$",
     email):
            print("Invalid email. Enter valid email.")
            return
        if len(password) < 8:
            print("Password must be atleast 8 characters long.")
            return

        # insert user data into database
        insert_query = """
        INSERT INTO users (first_name, last_name, email, phone, pslassword)
        VALUES (%s, %s, %s, %s, %s)
        """
        user_data = (first_name, last_name, email, phone, password)
        cursor.execute(insert_query, user_data)
        conn.commit()

    print("Registration succesful.")

    do_register()
    conn.close()

    def do_update(self, args):
      """updating data set"""
      args = shlex.split(arg)
      integers = ["Amount_of_waste", "pick_up_date"]
      floats = ["type_of_waste", "location"]
      if len(args) == 0:
          print("*class name missing*")
      elif args[0] in classes:
          if len(args) > 1:
              k = args[0] + "." + args[1]
              if k in models.storage.all():
                  if len(args) > 2:
                      if len(args) > 3:
                          if args[0] == "Location":
                              if args[2] in integers:
                                  try:
                                      args[3] = int[args[3]]
                                  except:
                                      args[3] = 0.0
                                  setattr(
    models.storage.all()[k], args[2], args[3])
                                  models.storage.all()[k].save()
                              else:
                                  print("*value missing*")
                      else:
                          print("*attribute missing*")
              else:
                  print("*no instance found*")
      else:
          print("*instance id missing*")

if __name__ == '__main__':
    MAZINGIRABORACommand().cmdloop()






  

                    
