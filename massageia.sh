#!/bin/bash

exponent='[eE][-+]?[0-9]+'
float='(([0-9]*\.[0-9]+|[0-9]+\.)('$exponent')?|[0-9]+'$exponent')'
number='[+-]?([0-9]+|'$float')'
#separa os numeros e remove caracteres inuteis
sed -r -e 's/'$number'/ & /g' -e 's/z/ z /g' -e 's/ *[(,)] */ /g' -e 's/   */ /g' | fold -s

#tee cut -d: -f3
#sed -r -n -e 's/,/ /' \
#-e 's/'$number'/& /gp'\
#-e 's/[mMzZlLvVhHcCsSQqTtaA]/& /'