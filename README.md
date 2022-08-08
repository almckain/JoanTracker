# JoanTracker
<<------------------------------------------------->>

To run this file, please follow these steps.

STEP 1: Install pip
* This will be used to install other tools that are utilized in this project *
  1. Run the command "pip --version"
      This will be used to check if pip is installed. If nothing appears or an error occures. Continue with pip installation.
  2. Use the following command to download pip "curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py"
  
  3. Then run this command "python get-pip.py"
  
  4. Run "pip --version" to test if pip got installed

STEP 2: Install openpyxl
* This is used to interact with excel sheets with python *
  1. In the command line run "pip install openpyxl"
  
     If that command does not work try "pip3 install openpyxl"
    
     If that command does not work try "python -m pip install openpyxl"
    
     If that command does not work try "python3 -m pip install openpyxl"
     
  2. Run "pip3 show openpyxl"
  
     This will show the current version of openpyxl. If nothing show up, then openpyxl is not installed.
  
STEP 3: Install matplotlab
* Used to display data on a graph *
  1. In the command line run "python3 -m pip install -U matplotlib"
  
<<------------------------------------------------->>
<<------------------------------------------------->>

The purpose of this research was conducted to discover which rooms within the library were lacking adequate wifi signal strength. Rooms that were
lacking a wifi signal were victim to Joan units that would consume battery power quicker than others. This was due to the Joan unit losing connection
which would cause it to search for a new signal. Once library staff noticed this we began keeping track of when the Joan units needed changed. The graph 
is shown in figure 1. I wrote wrote this program to read through the data and compare the average amount of days between each unit change. This data was 
then represented on a graph. The graph can be seen in figure 2.


FIGURE (1)

<img width="428" alt="Joan_Graph" src="https://user-images.githubusercontent.com/100253301/183335920-03299c07-2007-47b2-ad19-084c17a3a915.png">

FIGURE (2)

<img width="807" alt="Data_Sheet" src="https://user-images.githubusercontent.com/100253301/183336284-7fafd6b0-55da-4110-9cc4-fd89843f0c87.png">

    
