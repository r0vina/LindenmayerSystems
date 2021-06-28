# -*- coding: utf-8 -*-
"""
Created on Thu Nov 19 14:49:04 2020

@author: Roneet
"""

import matplotlib.pyplot as plt
from LindIter import LindIter
from turtleGraph import turtleGraph
from turtleplot import turtlePlot

# MAIN SCRIPT Displays a menu and a submenu, accepts inputs from the user
# regarding the choice of the Lindenmayer system and the number of iterations.
# Lets the user display the chosen plot with the chosen number of iterations.
#
# Initialize blank variables for the choice of system and number of iterations.
# The system variable has to be filled to proceed with plot generation. 
#
# Author: Roneet V. Nagale, s204091@dtu.dk, 2020

#Initialize blank
System =""
N=0
fig, ax = plt.subplots() 
ax.set_xlabel('x-Axis')
ax.set_ylabel('y-Axis')
# Display a menu and wait for user input. The user can pick between choosing
# a L-system type, or displaying the plot provided a system has already been
# picked. 
while True:
    chosenOption=input("""Please pick an option
      1. Choose the type of Lindenmayer system and the number of iterations.
      2. Generate plots
      3. Quit
      """)
    
    # If the user chooses option 1, display a submenu with the available 
    # L-system types. 
    if chosenOption == '1':
    
        while True:
            chosenOption=input("""Please pick an option
                                   1. Koch curve
                                   2. Sierpinski triangle
                                   3. Dragon Curve
                                   4. Back to previous menu. 
                                   """)
            # When option 1 is picked, ask the user to enter the desired 
            # number of iterations.
            if chosenOption == "1":
                iterationInput =input("""Please enter the number of iterations.
                                      """)
                # Check if the input is actually an integer, and throw an
                # exception if it isn't, and wait for a new input.
                try:
                    int(iterationInput)
                except:
                    print("Invalid input! Please input an int.")
                
                # If the input is valid, assign the value of the input to N.
                # Also assign the string "Koch" to the variable System.
                else:   
                    System = "Koch"                          
                    N = int(iterationInput)
                    
                    # Set the title for the plot with the name of the L-system
                    # and the number of iterations. Also set the ranges for 
                    # x and y axes for the plot.
                    plt.title("Koch Curve. Iterations:"+str(N))
                    plt.xlim([0,1])
                    plt.ylim([-0.2,0.5])

                    input('Input accepted! Please select option 2.'\
                          'from the main menu to generate and display'\
                              ' your plot. Press enter to continue.')
                    break
                
            # When option 2 is picked, ask the user to enter the desired 
            # number of iterations.                         
            if chosenOption == "2":
                iterationInput =input("""Please enter the number of iterations.
                                      
                                      """)
                # Check the validity of the input.
                try:
                    int(iterationInput)
                except:
                    print("Invalid input! Please input an int.")
                # If the input is valid, assign System and N their respective 
                # values.
                else: 
                    System = "Sierpinski"
                    N = int(iterationInput)
                    
                    # Set the title for the plot with the L-system name and
                    # number of iterations. 
                    
                    plt.title("Sierpinski Triangle. Iterations:"+str(N))
                    
                    # In the case of the Sierpinski Triangle, check if the 
                    # number of iterations entered is positive or negative, 
                    # and accordingly set the ranges for the plot axes. This
                    # is due to how the triangle is constructed for even and 
                    # odd number of iterations. (*This might be due to
                    # erronous code in the turtlePlot function)
                    if N%2==0:
                        plt.xlim([0,1])
                        plt.ylim([0,1])
                    else:
                        plt.xlim([0,1])
                        plt.ylim([0,-1])

                    input('Input accepted! Please select option 2.'\
                          'from the main menu to generate and display'\
                              ' your plot. Press enter to continue.')
                    break
            # Check the validity of the input. 
            if chosenOption == "3":
                iterationInput =input("""Please enter the number of iterations.
                                      (Best results with 10+)
                                      """)
                try:
                    int(iterationInput)
                except:
                    print("Invalid input! Please input an int.")
                
                # If the input is valid, assign System and N their respective 
                # values.
                else: 
                    System = "Dragon Curve"
                    N = int(iterationInput)
                    plt.title("Dragon Curve. Iterations:"+str(N))
                    input('Input accepted! Please select option 2.'\
                          'from the main menu to generate and display'\
                              ' your plot. Press enter to continue.')
                    break
                
            if chosenOption == "4":
                break
    
    # If the user chooses to generate the plot, check if the System variable 
    # is assigned. If not, let the user know that the L-system hasn't been 
    # configured yet. 
    
    elif chosenOption == '2':
        
        # If the System variable is assigned, proceed with generating the plot.
         if System:
            # Get the Lindenmayer string by passing the L-system name and 
            # the number of iterations to the LindIter function.
            LindenmayerString = LindIter(System, N)
            
            # Convert the Lindenmaayer string to turtleCommands by passing it
            # to the turtleGraph function, along with the number of iterations.
            turtleCommands=turtleGraph(LindenmayerString,N)
            
            # Finally, pass the turtleCommands array to the turtlePlot function,
            # which generates and displays the plot.
            turtlePlot(turtleCommands)
          
         else:
             print("System not configured yet.")
             
    # If the user chooses to quit, break the loop and exit the script.         
    elif chosenOption == '3':
            input("Exiting. Press enter to quit")
            break
    # If the user's input does not match any of the allowed options, warn the
    # user and ask for an input again. 
    else:
        input("Invalid option! Press enter to try again.")




