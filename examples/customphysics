## CUSTOM FLOOR, GRAVITY AND ACCELERATION OF GRAVITY WITH COLLISION, MADE WITH VOLARATIO

from volaratio import *
import time
app = Renderer()

vert = np.array([(0,0,0,1),(0,0.2,0,1),(5,0.2,0,1),(5,0,0,1), 
                (0,0,5,1),(0,0.2,5,1),(5,0.2,5,1),(5,0,5,1)])   

face = np.array([(0,1,2,3),(4,5,6,7),(0,4,5,1),(2,3,7,6),(1,2,6,5),(0,3,7,4)])


x = Cube3D(app,pg.Color("red"),[2,3,2])
floor = CustomObject3D(app,pg.Color('red'),vert,face,[0,0,0])
app.objects.append(floor) # FLOOR
app.objects.append(x) # CUBE
global i
i = 0
z= 0.0001 # ACCELERATION STARTING POINT
def gravity():
    global i,z
    stopped = False
    while True:
        z+=0.00000098 # ACCELERATION

        # COLLISION
        if math.sqrt((x.pos[0] - floor.pos[0])**2 + (x.pos[1] - floor.pos[1])**2 + (x.pos[2] - floor.pos[2])**2) <= 2.844:
            stopped = True
        time.sleep(0.01)
        i-=z
        if stopped == False:
            x.translate([0,i,0]) # MOVE CUBE
        

app.addfunc(gravity)
app.run()
