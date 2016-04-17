#!/bin/bash

xsltproc svgproc.xsl $1 | bash massageia.sh
