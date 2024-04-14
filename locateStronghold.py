from math import sin, cos, tan, pi
from typing import Tuple

def locateStronghold(x1: float, z1: float, yaw1: float, x2: float, z2: float, yaw2: float) -> Tuple[float]:

    # Define division by zero threshold
    dbz_threshold = 0.01

    # Function for converting minecraft yaw to cartesian angles
    def convertYawMcToCart(yaw_mc: float) -> float:
        return (-yaw_mc - 90) * pi/180
    
    # Convert MC coords to Cartesian
    z1, z2 = -z1, -z2 
    theta1, theta2 = convertYawMcToCart(yaw1), convertYawMcToCart(yaw2)

    # Calculate the rise and run of both lines
    dx1, dx2 = cos(theta1), cos(theta2)
    dz1, dz2 = sin(theta1), sin(theta2)

    # Notify user if the two positions are collinear (Calculations won't work if so)
    if ((theta1 - theta2) < dbz_threshold):
        raise ValueError("Please pick two positions that are NOT collinear with the Stronghold.")

    # Calculate the x coord
    x = ((dx1 * dx2 * (z2-z1)) - (dz2 * dx1 * x2) + (dz1 * dx2 * x1)) / (sin(theta1 - theta2))

    # Calculate the z coord
    if dx1 < dbz_threshold:
        z = tan(theta2) * (x - x2) + z2
    else:
        z = tan(theta1) * (x - x1) + z1

    # Convert from Cartesian back into MC coords
    z = -z

    # Round the numbers
    x = round(x)
    z = round(z)

    return (x, z)
