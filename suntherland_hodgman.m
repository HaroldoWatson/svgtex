1;
echo off all;
global prevpoint = [0,0];
global subpoint = [0,0];
global path_continuous = 0;

function path_M(args)
  global path_continuous
  global subpoint
  global prevpoint
 
  path_continuous = 0
  subpoint = args
  prevpoint = subpoint
endfunction

function path_m(args)
  path_M(args)
endfunction

function path_L(line, args)
  s0 = prevpoint
  sd = args(1:2)
  den = sd*line.N
  
  if (den != 0)
    num = line.r0N - (s0*line.N)
    t = num/den
    if (t > 0 && t < 1)
      x = sd*t
      if (den > 0)
        if (path_continuous)
          printf("l %f %f ", x(1), x(2))
        else
          printf("m %f %f ", x(1), x(2))
        endif
        printf("l %f %f ", sd(1), sd(2))
      else
        printf("l %f %f ", x(1), x(2))
      endif
    endif
  endif
endfunction

pathsegs.m.nargs = 2
pathsegs.m.f = @path_m
args = argv()
line_in = eval(args{1})


while(1)
  global prevpoint;
  in = fgetl(stdin);
  if length(in) < 2
    break;
  endif
  
  inarr = strsplit(in,':');
  pathid = str2double(inarr{1});
  pathd = strsplit(inarr{2});
  pathmtx = [eval(inarr{3}); 0 0 1];
  prevpoint = [0,0];
  
  nargs = 2
  argi = 1
  currfunc = @path_m
  args = [0 0 0 0 0 0]
  
  for dtoken = pathd
    if isfield(pathsegs, dtoken)
      seg = getfield(pathsegs,dtoken)
      nargs = seg.nargs
      currfunc = seg.f
    else
      args(argi) = str2double(dtoken)
      argi = argi + 1
    endif
    if (argi > nargs)
      currfunc(args)
      argi = 1
    endif
  endfor
endwhile
