#params rx,ry,nx,ny
#formato px py
NR==1 { rn = rx*nx + ry*ny}
NR>1 {
  pdn = ($1 - p0x)*nx + ($2 - p0y)*ny; 
  if (pdn != 0) print (rn - (p0x*nx + p0y*ny))/pdn
  
}
{p0x=$1; p0y=$2}