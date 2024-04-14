from math import tan, pi

### Inputs
t1, t2 = -44.2, -41  # Yaw
x1,x2=89.693,170.906 # x coords
z1,z2=27.925,-34.545 # z coords

# Minecraft inverts the z axis compared to normal cartesian coords
y1,y2=-z1,-z2

# Convert Minecraft's yaw to Cartesian slope
def slope(theta):
    x = -theta -90
    return tan(x*pi/180)
m1,m2=slope(t1), slope(t2)

# Answer
x = (m1 * x1 - m2*x2 + y2-y1) / (m1-m2)
y=-(m1*(x-x1)+y1) # Must invert the z coords back from cartesian to mc coords
print(x,y)

# Sanity check (should be identical to answer)
y=-(m2*(x-x2)+y2)
print(x,y)
