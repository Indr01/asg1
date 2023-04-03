import math
for i in range(0, 346, 15):
    angle = math.radians(i)
    sine = round(math.sin(angle), 4)
    cosine = round(math.cos(angle), 4)
    print(f"angle {i} degrees:\tsin = {sine}\tcos = {cosine}")
