#!/bin/bash

xsltproc svgproc.xsl $1 | bash massageia.sh | python3 svg_preproc.py
