from volaratio import *
app = Renderer()
app.objects.append(Cube3D(app,pg.Color('red'),[1,0,0]))
app.objects.append(Cube3D(app,pg.Color('red'),[2,0,0]))
app.objects.append(Cube3D(app,pg.Color('red'),[3,0,0]))
app.run()
