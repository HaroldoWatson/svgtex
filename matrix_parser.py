import re

transformre = re.compile(r'(matrix|translate|scale|rotate|skewX|skewY)\s*,?\s*\(([^)]+)\)')


def parse_matrix(l):
  for m in transformre.finditer(l):
    transf = m.group(1)
    