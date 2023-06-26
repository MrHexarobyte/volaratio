## CUSTOM OBJECT USING CUSTOM VERTICES AND FACES -- HALF BLOCK/SLAB MADE WITH VOLARATIO

from volaratio import *
app = Renderer()

vert = np.array([(0,0,0,1),(0,0.5,0,1),(1,0.5,0,1),(1,0,0,1), 
                (0,0,1,1),(0,0.5,1,1),(1,0.5,1,1),(1,0,1,1)])   

face = np.array([(0,1,2,3),(4,5,6,7),(0,4,5,1),(2,3,7,6),(1,2,6,5),(0,3,7,4)])



app.objects.append(CustomObject3D(app,pg.Color('red'),vert,face,[0,0,0]))

app.run()

