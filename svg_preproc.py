import sys
import itertools as IT
import functools as FT
import re

#definicao de matriz (spec)
# a c e 
# b d f
# 0 0 1
#
# aqui: [(a,b,0),(c,d,0),(e,f,1)]

int_regex = re.compile('[-+]?[0-9]')
number_regex = re.compile('[-+]?[0-9]*\.?[0-9]+([eE][-+]?[0-9]+)?')
unit_regex = re.compile('('+number_regex.pattern+')\s*(px|pt|pc|mm|cm|in)?')

unit_dict = {'px':1.0, 'pt':1.25, 'pc':15.0, 'mm':3.54, 'cm':35.4, 'in':90.0}
indentity = [(1,0,0),(0,1,0),(0,0,1)]

element_defaults = {
    'svg': {'width': 1, 'height': 1, 'viewbox': ''}
}

def unit_val(strin): 
  m = unit_regex.match(strin)
  g = m and m.group(1,3) or [0,None]
  return (float(g[0]) or 0) * (g[1] in unit_dict and unit_dict[g[1]] or 1)

def vector_esc(v,k):
  return [vn*k for vn in v]

def vector_sum(v1,v2):
  return [v1k + v2k for v1k,v2k in zip(v1,v2)]

def matrix_vector(m,v):
  return ft.reduce(vector_sum, (vector_esc(mk,vk) for mk,vk in zip(m,v) ))

def matrix_mul(m,n):
  return [matrix_vector(m,v) for v in n]

def viewbox_parse(vb):
  return [x!=None and float(x) or y for x,y in it.zip_longest((m.group(0) for m in number_regex.finditer(vb) ), [0.0,0.0,1.0,1.0] )]

def viewbox_matrix(vb):
  return [(1/vb[2], 0, 0 ), (0, 1/vb[3], 0) , (-vb[0]/vb[2], -vb[1]/vb[3], 1)]
  
'''
def elm_proc_svg(element, matrix):
  attr = {'width': 1, 'height': 1, 'viewbox': false}
  for k,v in element.attrib.items(): attr[k.lower()] = v;
  m = [1.f/unit_val(attr['width']),0,0, 1.f/unit_val(attr['height']), 0,0]
  return matrix_mul(m, viewbox_matrix(attr['viewbox']))

elm_proc_funcs = {'svg': elm_proc_svg}

matrix = [1,0,0,1,0,0];
'''

currpoint = [0,0] #ponto atual
subpoint = [0,0] #inicio do subpath atual
currmatrix = [1, 0, 0, 1, 0, 0]
path_id = None

def path_M(x,y):
  printf("M %f %f ",x,y)
  currpoint = subpoint = [x,y]
  return tkn_funs['L']

def path_m(x,y):
  return path_M(x+currpoint[0], y+currpoint[1])

def path_L(x,y):
  printf("L %f %f ",x,y)
  currpoint = [x,y]
  return tkn_funs['L']

def path_id(val):
  path_id = val
  currpoint = [0,0] #ponto atual
  subpoint = [0,0] #inicio do subpath atual
  currmatrix = [1, 0, 0, 1, 0, 0]
  return tkn_funs['id']  
  
tkn_funs = {'M': lambda x: lambda y: path_M(x,y),
            'm': lambda x: lambda y: path_m(x,y),
            'L': lambda x: lambda y: path_L(x,y),
            'id': lambda i: path_id(i)}

currfun = tkn_funs['id']

#it = (tkn for tkn in ' '.split(l) for l in sys.stdin)

def tokenize(path_linha_it):
  return IT.chain.from_iterable(l.split() for l in path_linha_it)

#generator de paths a partir dos tokens
def pathitize(token_it):
  currpath = None
  currfunc = None
  vb_matrix = [1,0,0,1,0,0]
  path = {'id':0, 'd':[], 'matrix':[1,0,0,1,0,0]}

  for t in token_it:
    currfunc = tkn_funs[t]()
    try:
      n = float(t)
      path['d'].append(n)
    except ValueError:
      if (t == 'viewBox'):
        viewbox = [float(f) for f in IT.islice(token_it, 4)]
        


def suntherland_hodgman(path, uvtri):
  virt_uvtri = matrix_mul(path.inv_matrix, uvtri)
  linea, lineb, linec = lines_from_tri(virt_uvtri)]
  for p in cut_path(cut_path(cut_path(path.d, linea), lineb) linec ):
    yield p

#dis gon be good
path_linha_it = (l for l in sys.stdin)
token_it = tokenize(path_linha_it)
path_it = pathitize(token_it)
#uvtri_linha_it = (l for l in uvfile)
#uvtri_lista = uvtri_listize(uvtri_linha_it)
#final_paths = ((suntherland_hodgman(path, uvtri) for uvtri in uvtri_lista) for path in path_it)
#output_paths(final_paths)

for t in token_it:
    print(t)

