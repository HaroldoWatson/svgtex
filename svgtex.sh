#!/bin/bash

paths_f='paths.txt'
matrices_f='matrices.txt'
viewbox=$(xsltproc extrai_viewbox.xsl $1)
#xsltproc extrai_d.xsl $1  | cut -d: -f2 | sed -r -f massage_matrix.sed | octave -q -f process_matrix.m "$viewbox"
xsltproc extrai_d.xsl $1 | tee "$paths_f" | cut -d: -f2 | sed -r -f massage_matrix.sed | octave -q -f process_matrix.m "$viewbox" > "$matrices_f"
cut -d: -f1,3 < "$paths_f" | bash massage_d.sh | paste -d: - "$matrices_f" | python3 intersect.py
