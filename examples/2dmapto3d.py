## TURNING AN 2D 5x5 ARRAY INTO A MAP OF 3D CUBES USING VOLARATIO

from volaratio import *
app = Renderer()

x = np.random.choice([1,0], size=(5,5))

i = 0
order = [0,0]
WIDTH = 10
LENGTH = 10
pieces = 5
op = [LENGTH/pieces,WIDTH/pieces]
def handle(v):
    if v == 1:
        if order[0] >= WIDTH:
            order[1] += op[1]
            order[0] = 0
        app.objects.append(Cube3D(app,pg.Color("red"),[order[0],0,order[1]]))
        order[0] += op[0]
                
    else:
        if order[0] >= WIDTH:
            order[1] += op[1]
            order[0] = 0
        
        order[0] += op[0]


for i in x:
    for b in i:
        handle(b)
print(x)

app.run()