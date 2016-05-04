import numpy as np
import sys

'''def main(paths, clipgroups):
  for path_id, path_matrix, path_d in paths:
    for clipgroup in clipgroups:
      proj_matrix, plane1, plane2, plane3 = transform_clipgroup(path_matrix, clipgroup)
      res = [path_clip( path_clip(path_clip(path_d, plane1), plane2), plane3)]
      if len(res) > 0:
        ?

def genpathsfromstdin():
  

main(sys.stdin, uvfile)gs


for l in sys.stdin:
  a,b = l.split(" ")
  print(a + b)
'''
NEXT_STATE = {}
NEXT_STATE["m"] = "mx"
NEXT_STATE["l"] = "lx"
NEXT_STATE["M"] = "Mx"
NEXT_STATE["L"] = "Lx"
NEXT_STATE["z"] = "z"
NEXT_STATE["Z"] = "Z"

NEXT_STATE["mx"] = "my"
NEXT_STATE["my"] = "lx"
NEXT_STATE["lx"] = "ly"
NEXT_STATE["ly"] = "lx"
NEXT_STATE["Mx"] = "My"
NEXT_STATE["My"] = "Lx"
NEXT_STATE["Lx"] = "Ly"
NEXT_STATE["Ly"] = "Lx"


#seg = [s1, s0]
#clip_plane = [[N], R0N]
def seg_clip(s0, s1, n, r0n):
  den = np.dot((s1 - s0),n)
  if den != 0:
    t = (r0n - np.dot(s0,n))/den
    if t >0 and t < 1:
      if den < 0:
        yield s0
      yield (t*s1 + (1-t)*s0)
  if np.dot(s1,n) > r0n:
    yield s1
  
    
def path_clip(path_d, clip_plane):
  path_d = path_d
  clip_plane = clip_plane
  state = "M"
  currpoint = np.array([0,0])
  isfirst = True
  firstpoint = currpoint
  args = {}  
  for tkn in path_d:
    if tkn in NEXT_STATE:
      state = tkn
    else:
      args[state] = float(tkn)
    if state == "my":
      currpoint = currpoint + np.array([args["mx"],args["my"]]) 
    elif state == "My":
      currpoint = np.array([args["Mx"],args["My"]])
    elif state == "ly":
      s1 = currpoint + [args["lx"],args["ly"]]
      for s in seg_clip(currpoint, s1,  clip_plane[0], clip_plane[1]):
        if isfirst:
          yield "M"
          yield s[0]
          yield s[1]
          isfirst = False
        else:
          yield "L"
          yield s[0]
          yield s[1]
    state = NEXT_STATE[state]
  
d = "m 0 0.5 l 1 0".split(" ")
plane = [[-1,1], 0]
print ( list(path_clip(d, plane) ).join(" ") ) 

