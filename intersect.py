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
def seg_clip(isfirst, op, s0, s1, n, r0n):
  s0n = np.dot(s0,n)
  if isfirst and s0n > 0:
    yield "M", s0
  den = np.dot((s1 - s0),n)
  if den != 0:
    t = (r0n - s0n)/den
    if t >0 and t < 1:
      yield "L", (t*s1 + (1-t)*s0)
  if op == 'Z':
    yield 'Z', 0
  else:
    if np.dot(s1,n) > r0n:
      yield op, s1
  

def path_clip(path_d, clip_plane):
  path_d = path_d
  clip_plane = clip_plane
  state = "M"
  currpoint = np.array([0,0])
  isfirst = True
  firstpoint = currpoint
  args = {}  
  for tkn in path_d:
    op = False
    if tkn in NEXT_STATE:
      state = tkn
    else:
      args[state] = float(tkn)
    if state == "my":
      op = "M"
      s1 = currpoint + np.array([args["mx"],args["my"]]) 
    elif state == "My":
      op = "M"
      s1 = np.array([args["Mx"],args["My"]])
    elif state == "ly":
      op = "L"
      s1 = currpoint + np.array([args["lx"],args["ly"]])
    elif state == "Ly":
      op = "L"
      s1 = np.array([args["Lx"],args["Ly"]])
    elif state == "z" or state == "Z":
      op = 'Z'

    if op == 'M':
      currpoint = s1
      isfirst = True
      firstpoint = s1
    elif op == 'L' or op == 'Z': 
      for opchar, p in seg_clip(isfirst, op, currpoint, s1, clip_plane[0], clip_plane[1]):
          yield opchar
          if opchar != 'Z':
            yield p[0]
            yield p[1]
      currpoint = s1
    state = NEXT_STATE[state]
  
d = "m 0 0.5 L 1 0 z".split(" ")
plane = [[1,-1], 0]

def parse_path():

for l in sys.stdin:
  path_id, path_d, path_matrix = parse_path(l)
