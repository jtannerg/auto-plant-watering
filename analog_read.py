#analog inputs function

from gpiozero import MCP3008
from time import sleep

moisture_dc = MCP3008(channel = 0)
moisture_voltage = 3.3 * moisture_dc.value
print("measured moisture voltage is: ", moisture_voltage)
if (moisture_voltage > 2.3)
  print ("Wow your soil is very wet!")
elif (moisture_voltage < 1.3)
  print("Wow your soil if very dry!")
else 
  print("soil looks great")
  
depth_dc = MCP3008(channel = 1)
depth_voltage = 3.3 * depth_dc.value
print ("measured depth voltage is: " depth_voltage)
#if (depth_voltage > 2.3)
#  print ("Plenty of water!")
elif (depth_voltage < 1.)
  print("Need to add water to the resivor soon!")
else 
  print("water levels are good to go")
  
sleep(1.5)
