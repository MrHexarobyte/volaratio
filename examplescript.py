from main import *
app = SoftwareRender()
app.objects.append(Cube3D(app,pg.Color('red'),[1.0,0,0]))
app.objects.append(Cube3D(app,pg.Color('red'),[3,0,0]))
app.objects.append(Cube3D(app,pg.Color('red'),[4,0,0]))
app.objects.append(Cube3D(app,pg.Color('red'),[5,0,0]))
app.objects.append(Cube3D(app,pg.Color('red'),[6,0,0]))
app.objects.append(Cube3D(app,pg.Color('red'),[6,0,1]))
app.objects.append(Cube3D(app,pg.Color('red'),[6,0,2]))
app.objects.append(Cube3D(app,pg.Color('red'),[6,0,3]))
app.objects.append(Cube3D(app,pg.Color('red'),[6,0,4]))
app.objects.append(Cube3D(app,pg.Color('red'),[6,0,5]))
app.objects.append(Cube3D(app,pg.Color('red'),[6,0,6]))
app.run()