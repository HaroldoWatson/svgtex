1;
global M = eye(3);

function matrix(a,b,c,d,e,f)
  global M;
  M = M * [a c e; b d f; 0 0 1];
endfunction;

function translate(tx,ty)
  if nargin < 2
    ty = 0
  endif
  matrix(1,0,0,1,tx,ty)
endfunction

function scale(sx,sy)
  if nargin < 2
    sy = sx
  endif
  matrix(sx, 0,0,sy,0,0)
endfunction

function rotate(a,cx,cy)
  c = cos(a*pi/180)
  s = sin(a*pi/180)
  if nargin < 3
    matrix(c, s, -s, c, 0,0)
  else
    translate(cx,cy)
    rotate(a)
    translate(-cx,-cy)
  endif
endfunction

function skewX(a)
  matrix(1,0,tan(a*pi/180),1,0,0)
endfunction

function skewY(a)
  matrix(1,tan(a*pi/180),0,1,0,0)
endfunction

while(1)
  global M;
  a = fgetl(stdin);
  if length(a) < 2
    break;
  endif
  eval(a);
  printf('%f %f %f %f %f %f\n', M(1,1),M(2,1),M(1,2),M(2,2),M(1,3),M(2,3))
  M = eye(3);
endwhile
