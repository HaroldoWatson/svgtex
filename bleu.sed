#exponent [eE][-+]?[0-9]+
#float (([0-9]?\.[0-9]+|[0-9]+\.)($exponent)?|[0-9]+<[^>]+>)
#number: [-+]?([0-9]+|float)
s/([eE][-+]?[0-9]+)/<\1>/g #englobando expoentes
s/(([0-9]?\.[0-9]+|[0-9]+\.)(<[^>]+>)?|[0-9]+<[^>]+>)/<\1>/g #englobando expoentes
p