import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

speed = int(input())
light_count = int(input())

# formule vitesse en m/s
# speed_ms = speed / 3.6
# v = d / t

distance = [ 0 for i in range(light_count) ]
duration = [ 0 for i in range(light_count) ]
for i in range(light_count):
    distance[i], duration[i] = [int(j) for j in input().split()]

# Write an answer using print
# To debug: print("Debug messages...", file=sys.stderr, flush=True)

# test des vitesses
for i in range(speed,0,-1):
    # test pour chaque feu
    for j in range(light_count):
        # temps pour arriver au feu "j"
        time_d = round(distance[j] / (i / 3.6), 3)

        # couleur du feu "j"
        # Un cycle complet dure 2* duration
        time_f = round(time_d % (2 * duration[j]), 3)
        # Vert si time_f < duration sinon rouge
        #Si rouge, la voiture ne passe pas
        if duration[j] <= time_f <= 2 * duration[j]:
            break
    else:
        answer = i
        break

print(answer)    
    
