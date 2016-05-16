import numpy as np
import sys

CMATRIX = np.array([[1,0,0,0], [-3,3,0,0], [3,-6,3,0], [-1,3,-3,1]])
QMATRIX = np.array([[1,0,0],[-2,2,0],[1,-2,1]])
#estou fazendo em py pq octave n tem pass by reference

#plane é [[nx, ny],dist]
class path_clipper:
  def __init__(self, plane, outfunc):
    self.M([0,0])
    self.plane = plane
    self.outfunc = outfunc

  def M(self, args):
    self.isfirst = True
    self.currpoint = np.array(args)
    self.firstpoint = self.currpoint

  def m(self, args):
    self.M(self.currpoint + np.array(args))

  #def L(self, args):
  #  if self.isfirst and is_on_visible_side():
  #    self.outfunc("M {} {} ".format( self.currpoint[0], self.currpoint[1]) )
  #  self.outfunc("L {} {} ".format(args[0], args[1]) )

  def beginDraw(self):
    if (np.dot(self.currpoint, self.plane[0]) > 0):
      if self.isfirst:
        self.outfunc("M {} {} ".format( self.currpoint[0], self.currpoint[1]))
        self.isfirst = False
        return True
    else:
      return False
  
  def param_line_root(self, p0, p1):
    pd = p1 - p0
    poly = np.dot(self.plane[0], np.array([p0, pd]).T)
    poly[0] = poly[0] -self.plane[1]
    if poly[1] != 0:
      t = -1*(poly[0]/poly[1] )
      if t >0 and t < 1:
        return p0 + pd*t
      else:
        return None
    else:
      return None
  
  def preline(self, p1):
    p0 = self.currpoint
    drawing = self.beginDraw()
    p = self.param_line_root(p0, p1)
    if p is not None:
      if drawing:
        drawing = False
        self.outfunc("L {} {} ".format( p[0], p[1]))
      else:
        drawing = True
        if self.isfirst:
          self.outfunc("M {} {} ".format( p[0], p[1]))
        else:
          self.outfunc("L {} {} ".format( p[0], p[1]))
    return drawing
          
  def L(self, args):
    if self.preline(np.array(args)):
      self.outfunc("L {} {} ".format( args[0], args[1]))
  
  def z(self, args):
    self.preline(self.firstpoint)
    self.outfunc("z ")
  
  def Z(self, args):
    self.z(args)
    
  def l(self, args):
    self.L(np.array(args) + self.currpoint)
    
  def C(self, args):
    p0 = self.currpoint
    p1 = [args[0],args[1]]
    p2 = [args[2],args[3]]
    p3 = [args[4],args[5]]
    tailbez = np.mat([p0,p1,p2,p3])
    
    drawing = self.beginDraw()
    param_matrix = CMATRIX*cpoints
    for t in self.roots(param_matrix):
      p = poly.polyval(t, param_matrix)
      if drawing:
        drawing = False
        headbez, tailbez = splitbezier(cpoints, t)
        self.outfunc("C {} {} {} {} {} {}".format( tailbez[0], tailbez[1], tailbez[2], tailbez[3], tailbez[4], tailbez[5]))
      else:
        drawing = True
        if self.isfirst:
          self.outfunc("M {} {} ".format( p[0], p[1]))
        else:
          self.outfunc("L {} {} ".format( p[0], p[1]))
    if (drawing):
      self.outfunc("C {} {} {} {} {} {}".format( tailbez[0], tailbez[1], tailbez[2], tailbez[3], tailbez[4], tailbez[5]))
      
  
      
  #param_matrix é a matriz da funcao parametrica, 4elm de 2 cada, em termos absolutos
  def roots(self, param_matrix):
    poly = np.asarray(self.plane[0]*param_matrix)[0]
    poly[0] = poly[0] - self.plane[1]
    roots = sorted(poly.roots())
    return (t for t in roots if t > 0.0 and t < 1.0 and imag(t) == 0)
  
  def z(self, args):
    if not self.isfirst:
      outfile.write("z")
    
  def Z(self, args):
    self.z(args)

  
	
    

PATH_COMMAND = {
'm' : {"next":"l", "nargs":2},
'M' : {"next":"L", "nargs":2},
'l' : {"next":"l", "nargs":2},
'L' : {"next":"L", "nargs":2},
'z' : {"next":"m", "nargs":0},
'Z' : {"next":"M", "nargs":0}
}

def parse_d(d, sink):
  args = []
  nargs = 2
  currcommand = 'M'
  for tkn in d.split(" "):
    try:
      arg = float(tkn)
      args.append(arg)
      nargs = nargs - 1
    except ValueError:
      currcommand = tkn
      nargs = PATH_COMMAND[tkn]['nargs']
    if nargs == 0:
      getattr(sink, currcommand)(args)
      args = []
      currcommand = PATH_COMMAND[currcommand]['next']      
      nargs = PATH_COMMAND[currcommand]['nargs']
  

def parse_line():
  d = "m 0 0.5 l 1 0 z"
plane = [[1,-1], 0]

parse_d(d, path_clipper(plane, sys.stdout.write))
#main

#argumento tem arquivo com as retas


for l in sys.stdin:
  path_id, path_matrix, path_d = parse_path(l)



