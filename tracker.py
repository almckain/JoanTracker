from openpyxl.utils import get_column_letter
from datetime import date
from openpyxl import Workbook, load_workbook

#Creating a list
listOfRooms = []

#Location of spreadsheet
wb = load_workbook("/Users/aaronmckain/Desktop/JoanTrackerProj/unitTracker.xlsx")
ws = wb.active

room_and_key = []

room_and_times = {

}

def print_list(list):
    for item in list:
        return item

#stores the cell letters in a list
for row in range(1,2): #rows 1-29
    for col in range(1, 46): #col 1-40
        room_and_key.append(get_column_letter(col))
    print("\n") 

room_locations = [] 
for val in room_and_key:
    room_locations.append(val)

#Stores rooms in list
for letter in room_locations: 
    for i in range(1,2):
        current_room = ws[letter + str(i)]
        room_and_times[current_room.value] = []

#Cycles through each cell
for cell in room_locations: 
    #temporary list that store the times from each room; clears after use
    temp_list = []
    for i in range(2,39):
        time = ws[cell + str(i)]
        #stores cell data in the temporary list if return is not null
        if(time.value != None):
            temp_list.append((time.value).date())
            
    temp_list.reverse()
    
    for time in temp_list:
        print(time)
    
    num_of_changes = len(temp_list)
    print(num_of_changes)

    #clears the list for the next room
    temp_list.clear()
    print("\n")

print(room_and_times)









