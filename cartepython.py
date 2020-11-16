#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Oct 31 15:30:43 2020

@author: mperaud
"""

# =============================================================================
# Necessary libraries
# =============================================================================
import matplotlib.pyplot as plt
from mpl_toolkits.basemap import Basemap
from geopy.geocoders import Nominatim
from matplotlib.patches import Polygon
import numpy as np


# =============================================================================
# Map creation : Europe
#To define center and four corners of the map GPS coordinates, use
#https://boundingbox.klokantech.com/
#
#color codes in https://web-color.aliasdmc.fr/couleur-web-lightskyblue-rgb-hsl-hexa.html#couleurs-blanc
# =============================================================================
m= Basemap(resolution='l',#low resolution
            projection='merc',#mercator
            lat_0=44.86, lon_0=9.17,#map center coordinates
            llcrnrlon =-20.38, llcrnrlat =28.97, urcrnrlon = 41.27, urcrnrlat = 59.11)
            #four corners of the map coordinates



#plt.annotate("Marianne",m(44.86,9.17),fontsize =20)

# =============================================================================
# Stations coordinates in dataframe (later on)
# =============================================================================

#Latitude de Hamburg Finkenwerder
latxfw =	53.529481
#Longitude de Hamburg Finkenwerder
longxfw =	9.863512

#Latitude de Toulouse
lattls = 43.636541
#longitude de Toulouse
longtls =1.389942


# =============================================================================
# gcline from Toulouse to Finkenwerder
# =============================================================================
## line from Toulouse to Finkenwerder with an arrow at the end
gclineback, = m.drawgreatcircle(longtls,lattls,longxfw,latxfw,color='b')
path = gclineback.get_path() # get path from the great circle 

head = m(longxfw,latxfw)    # get location of arrow's head (at Finkenwerder) 
tail = path.vertices[round(-len(path)/6)] # get location of arrow's tail 

#draw annotation with arrow in 'red' color 
#blank text is specified, because we need the arrow only 
#adjust facecolor and other arrow properties as needed 
plt.annotate('', 
      xy=(head[0], head[1]), 
      xycoords='data', 
      xytext=(tail[0], tail[1]), 
      textcoords='data', 
      size=22, 
      arrowprops=dict(headwidth=10, 
          headlength=15,  
          facecolor="b", 
          edgecolor="none",  
          connectionstyle="arc3, rad=0.001")) 

# =============================================================================
# gclineforth from Finkenwerder to Toulouse
# =============================================================================
## line from Finkenwerder to Toulouse with an arrow at the end
gclineforth, = m.drawgreatcircle(longxfw,latxfw,longtls,lattls,color='g')
path = gclineforth.get_path() # get path from the great circle 

head = m(longtls,lattls)    # get location of arrow's head (at Toulouse) 
tail = path.vertices[round(-len(path)/6)] # get location of arrow's tail 

#draw annotation with arrow in 'green' color 
#blank text is specified, because we need the arrow only 
#adjust facecolor and other arrow properties as needed 
plt.annotate('', 
      xy=(head[0], head[1]), 
      xycoords='data', 
      xytext=(tail[0], tail[1]), 
      textcoords='data', 
      size=22, 
      arrowprops=dict(headwidth=10, 
          headlength=15,  
          facecolor="g", 
          edgecolor="none",  
          connectionstyle="arc3, rad=0.001")) 

# =============================================================================
#Final drawing 1 to 1 for one program
# =============================================================================

m.drawmapboundary(fill_color ='#b0C4DE')#draws the map

m.fillcontinents(color='#fffaf0',lake_color='#b0C4DE')#fill with colors defined above
m.drawcoastlines()
m.drawcountries()
gclineback
gclineforth

xtls, ytls = m(longtls, lattls)
xxfw,yxfw=m(longxfw,latxfw)
plt.annotate('Toulouse', xy=(xtls, ytls),  xycoords='data',
                xytext=(-30, -10), textcoords='offset points',
                color='g',
                #arrowprops=dict(arrowstyle="fancy", color='b')
                )
            
plt.annotate('Finkenwerder', xy=(xxfw, yxfw),  xycoords='data',
                xytext=(-45, 5), textcoords='offset points',
                color='b',
                #arrowprops=dict(arrowstyle="fancy", color='b')
            
                )               


plt.text(xxfw,round(yxfw/1.3), "40 FH\n22 jigs",fontsize=10,
                    ha='left',va='center',color='w',
                    bbox=dict(facecolor='b', alpha=1))

plt.text(xxfw,round(xtls/1.3), "40 FH\n22 fuselages",fontsize=10,
                    ha='left',va='center',color='w',
                    bbox=dict(facecolor='g', alpha=1))

plt.title("A330")
plt.show()


# =============================================================================
# Drawing
# ===================================================================




