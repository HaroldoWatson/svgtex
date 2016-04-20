1;
echo off all;
global prevpoint = [0,0];
global subpoint = [0,0];
global path_continuous = 0;

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
  prevpoint = [0,0]  ;
 argv()
endwhile
