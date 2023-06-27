from volaratio import *
app = Renderer()
app.objects.append(Cube3D(app,pg.Color('red'),[0,0,0]))
app.objects.append(Cube3D(app,pg.Color('blue'),[1,0,1]))
app.run()
