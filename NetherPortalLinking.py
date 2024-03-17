def nether_to_overworld(x,y,z):
    x *= 8
    z *= 8
    return (x,y,z)

def overworld_to_nether(x,y,z):
    x /= 8
    z /= 8
    return (round(x),y,round(z))

print(overworld_to_nether(-174, 61, -268))
