s/([a-z]) +\(/\1(/g #removendo espaco entre nome da funcao e parentese
s/\)[, ]*/)\n/g #removendo virgulas entre funcoes e colocando quebra
s/([+.0-9]) +([+.0-9])/\1,\2/g #removendo espacos entre argumentos
s/

