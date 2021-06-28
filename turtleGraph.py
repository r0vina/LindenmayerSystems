# -*- coding: utf-8 -*-
"""
Created on Tue Dec  1 18:34:44 2020

@author: Roneet
"""
import numpy as np

def turtleGraph(LindenmayerString,N):
    # TURTLEGRAPH Creates and returns an array of alternating length and angle
    # specifications. 
    # 
    # Usage: turtleCommands=turtleGraph(LindenmayerString,N) 
    # Takes a Lindenmayer string and the desired number of iterations(N) 
    # as arguments. Identifies the L-system in use and assigns appropriate 
    # angle and length specifications to the output array. The number of 
    # iterations are used for calculating the scaling for the line 
    # segments in the plot. The output is an array with alternating length
    # and angle specifications.
    # 
    # Author: Roneet V. Nagale, s204091@dtu.dk, 2020

    
    turtleCommands = []   
    
    #Starting character S identifies the string as a Koch Curve
    if LindenmayerString[0]=='S':
        for characterIndex in range(0, len(LindenmayerString)):
            
            # Treat all characters with even indexes (including 0) 
            # as length specification
            
            if characterIndex%2 == 0:
                lineSegmentLength = pow(1/3,N)
                turtleCommands.append(lineSegmentLength)
                
            #Treat all remaining characters as angle specifications.
            
            else:
                if(LindenmayerString[characterIndex])=='L':
                    angle=(1/3)*np.pi
                    turtleCommands.append(angle)
                elif(LindenmayerString[characterIndex])=='R':
                    angle=-(2/3)*np.pi
                    turtleCommands.append(angle)
    
    #Starting character A or B identifies the string as a Sierpinski Triangle
    elif LindenmayerString[0] == 'A' or LindenmayerString[0]=='B':
        
        for characterIndex in range(0, len(LindenmayerString)):
           #Treat all characters with even indexes (including 0) 
           #as length specification
           if characterIndex%2 == 0:
               lineSegmentLength = pow(1/2,N)
               turtleCommands.append(lineSegmentLength)
           #Treat all remaining characters as angle specifications.
           else:
               if(LindenmayerString[characterIndex])=='L':
                   angle=(1/3)*np.pi
                   turtleCommands.append(angle)
               elif(LindenmayerString[characterIndex])=='R':
                   angle=-(1/3)*np.pi
                   turtleCommands.append(angle)
    
    #Starting character F identifies the string as a Dragon Curve.                
    elif LindenmayerString[0] == 'F':
         for characterIndex in range(0, len(LindenmayerString)):
            #Treat character F as length specification. 
            if LindenmayerString[characterIndex] == 'F':
                lineSegmentLength = pow(1/2,N)
                turtleCommands.append(lineSegmentLength)
            #Treat all remaining characters as angle specifications.
            else:
                if(LindenmayerString[characterIndex])=='L':
                    angle=(1/2)*np.pi
                    angle2=(1/2)*np.pi
                    turtleCommands.append(angle)
                    turtleCommands.append(angle2)
                elif(LindenmayerString[characterIndex])=='R':
                    angle=-(1/2)*np.pi
                    angle2=-(1/2)*np.pi
                    turtleCommands.append(angle)
                    turtleCommands.append(angle2)
        
    return turtleCommands 