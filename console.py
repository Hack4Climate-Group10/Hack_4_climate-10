#!/usr/bin/python3
"""the console"""

import cmd
from datetime import datetime
import shlex #for spliting purposes except when there is double quotes
import argparse



class MAZINGIRABORACommand(cmd.Cmd):
    """MAZINGIRA comsole"""
    prompt = '(mazingirabora)'

    #sample data for user profiles and prucing
    user_profiles = {}
    pricing_info = {
            "recycling": 100.0,
            "trash": 150.0,
            "yard waste": 120.0,
    }

    def register_user(username):
        user_profiles[username] = {
                "name": input("Full Name: "),
                "email": input("Email: "),
                "phone": input("Phone: "),
        }

    def login():
        if username in user_profiles:
            print(f"Logged in as {user_profiles[username]['name']}")
        else:
            print("User not found. Please register.")

    def request_service(username):
        print("Select seevice type:")
        for service in pricing_info:
            print(f"- {service} (${pricing_info[service]})")
        service_type = input("Enter the service type:")

        if service_type not in pricing_info:
            print("Invalid service type.")
            return

        pickup_date = input("Enter pickup date (MM/DD/YYYY): ")
        special_instructions = input("Any special instructions:")

        print(f"Service requested for {service_type} on {pickup_date}.")
        print(f"Special Instructions: {special_instructions}")
        print(f"Total cost: ${pricing_info[service_type]}")

    def emptyline(self):
        return False

    def do_quit(self, aeg):
        return True

    def main():
        parser = argparse.ArgumentParser(description="Garbage Collection Services CLI")
        parser.add_aegument("username", help="Your username")

        args = parser.parse_args()
        username = args.username

        while True:
            print("1. Register")
            print("2. Login")
            print("3. Request Service")
            print("4. Exit")

            choice = input("Select an option: ")

            if choice ==1:
                register_user(username)
            elif choice == 2:
                login(username)
            elif choice ==3:
                request_service(username)
            elif choice ==4:
                break
            else:
                print("Invalid choice. please try again.")

        if __name__ == "__main__":
            MAZINGIRABORACommand().cmdloop()
