#!/usr/bin/sed -r -n -f
s/[(),]/ /g #cortando caracteres inuteis
s/(matrix|translate|scale|rotate|skewX|skewY)/ \1 /g #separando transforms
s/([a-zA-Z])([0-9])/ \1 \2/g #separando comandos
s/([^eE])([+-])/\1 \2/g #sinal, exceto de expoente, sempre no inicio
s/([eE][+-]?[0-9]+)/\1 /g #expoente sempre no final
s/([0-9]?\.[0-9]+)(\.[0-9])/\1 \2/g #separando pontos de nums diferentes
s/ \+/ /g #tirando + do inicio
s/( \.|^\.)/ 0./g #colocando zero em inicio de float
s/(\. |\.$)/.0 /g #colocando zero em fim de float
s/ +/ /g #comprimindo espacos
p