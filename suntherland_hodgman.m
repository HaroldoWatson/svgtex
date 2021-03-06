1;
echo off all;
global prevpoint = [0,0];
global subpoint = [0,0];
global path_continuous = 0;

NEXT_STATE.m = "mx"
NEXT_STATE.l = "lx"
NEXT_STATE.M = "Mx"
NEXT_STATE.L = "Lx"
NEXT_STATE.z = "z"
NEXT_STATE.Z = "Z"

NEXT_STATE.mx = "my"
NEXT_STATE.my = "lx"
NEXT_STATE.lx = "ly"
NEXT_STATE.ly = "lx"
NEXT_STATE.Mx = "My"
NEXT_STATE.My = "Lx"
NEXT_STATE.Lx = "Ly"
NEXT_STATE.Ly = "Lx"

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

function path_l(line, args)
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



STATE_FUNCS.ly = @path_l

while(1)
  in = fgetl(stdin);
  if length(in) < 2
    break;
  endif
  
  inarr = strsplit(in,':');
  pathid = inarr{1};
  pathd = strsplit(inarr{2});
  pathmtx = [eval(inarr{3}); 0 0 1];
  prevpoint = [0,0];
  

  
  for dtoken = pathd
    if isfield(NEXT_STATE, dtoken)
      state = getfield(NEXT_STATE,dtoken);
    else
      setfield(args, state, str2double(dtoken)); 
    endif
    if isfield(STATE_FUNCS, state)
      getfield(STATE_FUNCS,state)(args);
    endif
    state = getfield(NEXT_STATE,state);
  endfor
endwhile



