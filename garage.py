from enum import Enum
import os
import platform
import ast

class Actions(Enum):
    EXIT =1
    DISPLAY = 2
    ADD = 3
    DELETE = 4
    FIND = 5
    SAVE = 6
    LOAD = 7

cars= []

FILE_NAME= 'garage.txt'


def menu():
    for act in Actions: print(f"{act.value} - {act.name}")
    return input ("your selection: ")

def displaycars():
    for index, car in enumerate(cars):
        print(f"{index}: Model: {car['Model']},: Brand: {car['Brand']},: Color: {car['Color']}")

def clear_terminal():
    if platform.system()== 'Windows':
        os.system('cls')
    else:
        os.system('clear')

def addCar():
    cars.append({"Model": input("car model: "),"Brand": input("car brand: "),"Color": input("car color: ")})

def delete_cars():
    if not cars:
        print("garage is empty no cars to delete")
        return

    displaycars()
    try:
        index = int(input("Enter the index of the car you want to delete: "))
        print(f"Deleted car: {cars.pop(index)}")
    except (ValueError, IndexError):
        print("invalid index.")

def findcars():
    if not cars:
        print("garage is empty")
        return
    search_key = input("Search by (model/brand/color): ").strip().lower()
    search_value = input(f"Enter the {search_key}to search: ").strip().lower()

    found =[
        car for car in cars
        if car.get(search_key, "").lower() == search_value
    ]
    if found:
        print("Matching cars: ")
        for car in found:
            print(f"Model: {car['model']}, Brand: {car['brand']},: Color: {car['color']}")
        else:
            print("No matching cars found.")

def Save_cars():
    with open(FILE_NAME, 'w+') as f:

        f.write(str(cars))
        print("File written successfully")
    
    f.close()

def load_cars():
    global cars
    try:
        print("Loading...")
        with open(FILE_NAME, 'r') as f:
            cars = ast.literal_eval(f.read())
            displaycars()
    except FileNotFoundError:
        print("The file does not exist. ")

if __name__=="__main__":
    user_selection=""
    while True:
        user_selection= Actions(int(menu()))
        clear_terminal()
        if user_selection == Actions.EXIT : exit()
        if user_selection == Actions.DISPLAY : displaycars()
        if user_selection == Actions.ADD : addCar()
        if user_selection == Actions.DELETE : delete_cars()
        if user_selection == Actions.FIND : findcars()
        if user_selection == Actions.SAVE : Save_cars()
        if user_selection == Actions.LOAD : load_cars()
        else: print("u idiot choose from the menu")