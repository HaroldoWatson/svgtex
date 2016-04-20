#!/bin/bash


viewbox=$(xsltproc extrai_viewbox.xsl $1)
xsltproc extrai_d.xsl $1  | cut -d: -f2 | sed -r -f massage_matrix.sed | octave -q -f process_matrix.m "$viewbox"
#xsltproc extrai_d.xsl $1 | tee paths | cut -d: -f2 | sed -r -f massage_matrix.sed | octave -q -f process_matrix.m "$viewbox" > matrices&
#cut -d: -f1,3 < paths | bash massage_d.sh | paste -d: - matrices | octave -q -f suntherland_hodgman.m bleu 
