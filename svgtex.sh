#!/bin/bash

#estou fazendo em bash porque eh tudo um prototipo, um teste

paths_f='paths.txt'
matrices_f='matrices.txt'
#viewbox=$(xsltproc extrai_viewbox.xsl $1)
#xsltproc extrai_d.xsl $1  | cut -d: -f2 | sed -r -f massage_matrix.sed | octave -q -f process_matrix.m "$viewbox"
#xsltproc extrai_d.xsl $1 | tee "$paths_f" | cut -d: -f2 | sed -r -f massage_matrix.sed | octave -q -f process_matrix.m "$viewbox" > "$matrices_f"
#cut -d: -f1,3 < "$paths_f" | bash massage_d.sh | paste -d: - "$matrices_f" | python3 intersect.py

#triangulos visiveis
trifile=triangulos.txt 

#triangulos UV
uvfile=uv.txt

IFS=":"
xsltproc extrai_d.xsl $1 | 

{
while read pathid pathtransf pathd
do
pathtransf=$(sed -r -f massage_matrix.sed <<< $pathtransf)
pathd=$(bash massage_d.sh <<< $pathd)

cat $2 | tri2planes $pathtransf | while read groupid nx0 ny0 rn0 nx1 ny1 rn1 nx2 ny2 rn2
do
echo $pathd | intersect $nx0 $ny0 $rn0 | intersect $nx1 $ny1 $rn1 | intersect $nx2 $nx2 $rn2 | { 
while read newd
echo $pathid $newd 
}

done
done
}


