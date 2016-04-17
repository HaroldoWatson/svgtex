{
  i = 0
  argi = 0
  while(i<NF){
    if ($i ~ /[0-9]/){
      args[argi] = $i
      argi = argi + 1
    }else{
      state = $i
    }
  }
}

function path_id(newid){
  id = newid
}