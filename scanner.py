"""
Photoacoustic Signal Scanner
----------------------------
This program was written at the Universidade Estadual do Norte Fluminense (UENF)
by me with, my friend Mila and my other friends of Photoacoustic laboratory.

If you want to use it, please remember of us.
"""

## Importing the libraries
from time import sleep, strftime
import matplotlib.pyplot as plt
from drawnow import drawnow
import numpy as np
import pyaudio
import visa


#funtion where the signals are calculated
def makeFig():
    #take the x and y values from a GPIB conected in the computer
    x, y = list(map(np.float, inst.query('SNAP?1,2').split(','))) 

	#take the power and temperature values
    power = np.float(inst.query('OAUX?3'))
    temp = round(float(inst.query('OAUX?1')), 3)

	#save the values in the file
    file.writelines("%e,%e,%e,%e\n" % (x, y,temp, power))

	#calculate the R-value
    R.append(np.sqrt(np.power(x, 2) + np.power(y, 2)))

	#plots the R-value
    plt.plot(R)
    plt.grid()


## Defining arrays to plot
R = [] #defining the R-values array


## Some informations
inst = visa.ResourceManager().open_resource(visa.ResourceManager().list_resources()[2]) #conect to the instrument lock-in
TEMP = round(float(inst.query("OAUX?1")), 3) #get the temperature value
TEMPFIM = 15*0.1 #define the final temperature value at the 15C


## Defining the file where the values where they will be saved
file_name = "N2O_Conc=10ppmv_Temp=-15a%.1f_data=%s.dat" % (TEMPFIM*10, strftime("%a_%d-%m-%Y_%Hh%Mmin%Ss")) #defining the name
file = open(file_name, 'w') #opening the file
file.writelines("x,y,temperature,power\n") #the label of the file


## Principal part of the program
if (TEMP - 0.005) <= TEMP < (TEMP + 0.005): #temperature range. It's needed to set a 0.005 value because of the temperature variation
    
    for T in np.arange(TEMP*10, TEMPFIM, 0.01):
        drawnow(makeFig) #get in the funtion drawnow
        inst.write("AUXV1,%.2f" % (T)) #set the value at 1 C
        sleep(2) #it waits 2 seconds


## Close the file
file.close()

## Stop and close the streams
stream.stop_stream()
stream.close()
pa.terminate()
