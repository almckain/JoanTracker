from webbrowser import get
from openpyxl.utils import get_column_letter
from datetime import date, datetime, timedelta
from openpyxl import Workbook, load_workbook

#Creating a list
listOfRooms = []

#Location of spreadsheet
wb = load_workbook("/Users/aaronmckain/Desktop/JoanTrackerProj/unitTracker.xlsx")
ws = wb.active

room_locations = []

room_and_averages = {

}

def calculate_sum(num_of_times):
    sum_of_days = timedelta(days=0)
    
    for i in range(0, len(num_of_times) - 1):
        difference = num_of_times[i] - (num_of_times[i + 1])
        sum_of_days = sum_of_days + difference
        
        x = num_of_times[i]
        y = num_of_times[i + 1]
        #print(f"\t\t{difference} = {x} - {y}")
    average = sum_of_days / len(num_of_times)
    #print(average)
    return average
        



#stores the cell letters in a list
for row in range(1,2): #rows 1-2
    for col in range(1, 46): #col 1-40
        room_locations.append(get_column_letter(col))
        print("\nStoring column " + get_column_letter(col) + " in the list room_locations")
        print("The list currently contains the following letters: ")
        for i in room_locations:
            print(i, end = " ")
        print("\n") 

for cell in room_locations:
    room = ws[cell + str(1)]
    print(room.value)

#Cycles through each cell
for cell in room_locations:
    #print("We are currently in cell " + cell) <><><><><><<><><><><><><><><><><><><><><><><><><><><><><><><><<
    #temporary list that store the times from each room; clears after use
    list_of_times = []
    for i in range(2,39):
        time = ws[cell + str(i)]
        #stores cell data in the temporary list if return is not null
        if(time.value != None):
            list_of_times.append((time.value).date())
        
    #Makes the temporary list sorted from earliest to latest      
    list_of_times.reverse()
   #for i in list_of_times: <><><><><><<><><><><><><><><><><><><><><><><><><><><><><><><><<
        #print(i) <><><><><><<><><><><><><><><><><><><><><><><><><><><><><><><><<
    
    
    #Calls calculate average
    average_change = calculate_sum(list_of_times)
    print("The average days between changes is " + str(average_change))

    for i in room_and_averages:
        room_and_averages[i] = average_change
        #print(room_and_averages[i])

    #clears the list for the next room
    list_of_times.clear()
    print("\n")

print(room_and_averages)



