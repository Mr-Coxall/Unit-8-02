# Created by: Mr. Coxall
# Created on: Sep 2016
# Created for: ICS3U
# This main program will create a bicycle object

from bicycle import *

# create an instance of a bicycle
bike1 = Bicycle()
bike2 = Bicycle()

print(bike1.current_state())
bike1.speed_up(10)
print('Current speed: ' + str(bike1.speed))
bike1.gear = 4
print('Current gear: ' + str(bike1.gear))
bike1.cadence = 60
print('Current cadence: ' + str(bike1.cadence))
bike1.apply_brakes(3)
print(bike1.current_state())

print('')

print(bike2.current_state())
bike2.speed_up(40)
print('Current speed: ' + str(bike2.speed))
bike2.gear = 3
print('Current gear: ' + str(bike2.gear))
bike2.cadence = 45
print('Current cadence: ' + str(bike2.cadence))
bike2.apply_brakes(12)
print(bike2.current_state())
