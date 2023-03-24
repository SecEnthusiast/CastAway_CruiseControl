import math
import random
import time

def calculate_hit_accuracy(distance, radar_cross_section, angle, speed):
    # Radar power (assumed)
    radar_power = 1000

    # Normalize the parameters to include them in the calculation
    distance_normalized = distance / 1000
    radar_cross_section_normalized = radar_cross_section / 10
    angle_normalized = abs(angle) / 90
    speed_normalized = speed / 1000

    # Calculate the accuracy based on the given parameters
    accuracy = radar_power / (distance_normalized * radar_cross_section_normalized * angle_normalized * speed_normalized)

    # Convert accuracy to percentage
    accuracy_percentage = accuracy * 100

    return accuracy_percentage

# Example: Calculate the hit accuracy of an AIM-120
distance = 5000  # Distance to the target in meters
radar_cross_section = 3  # Radar cross section of the target in square meters
angle = 45  # Angle between the radar and the target in degrees
speed = 800  # Speed of the target in km/h

while True:
    hit_accuracy = calculate_hit_accuracy(distance, radar_cross_section, angle, speed)
    print("Hit accuracy: {:.2f}%".format(hit_accuracy))
    time.sleep(5)  # Wait for 5 seconds before running the loop again
