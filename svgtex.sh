#!/bin/bash

xsltproc extrai_d.xsl $1 | cut -d: -f2 | sed -r -f massage_matrix.sed #bash massageia.sh | python3 svg_preproc.py
