from openpyxl.utils import get_column_letter
from datetime import date, datetime, timedelta
from openpyxl import Workbook, load_workbook

#Creating a list
listOfRooms = []

#Location of spreadsheet
wb = load_workbook("/Users/aaronmckain/Desktop/JoanTrackerProj/unitTracker.xlsx")
ws = wb.active

room_and_key = []

room_and_times = {

}

def calculate_sum(num_of_times):
    sum_of_days = timedelta(days=0)
    
    for i in range(0, len(num_of_times) - 1):
        difference = num_of_times[i] - (num_of_times[i + 1])
        sum_of_days = sum_of_days + difference
        
        #x = num_of_times[i]
        #y = num_of_times[i + 1]
        #print(f"{difference} = {x} - {y}")
    average = sum_of_days / len(num_of_times)
    return timedelta(average()
        

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
    
    #
    # Calculate average here
    # ##
    average_change = calculate_sum(temp_list)
    print(average_change)


    for time in temp_list:
        print(time)
    

    #clears the list for the next room
    temp_list.clear()
    print("\n")

print(room_and_times)

#
# passing in a list
# we need it to do the operations between 1 and the length of the list, MINUS ONE
# For every iteration, take the current index of the list and subtract the next index#
