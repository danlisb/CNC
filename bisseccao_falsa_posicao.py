# Implementação do Método da Bissecção e da Falsa Posição

f = lambda x: x**10 - 1

# f(x).f(a) > 0 = atualiza a
# f(x).f(a) < 0 = atualiza b

def biseccao(f, a, b, n):
  lista_b = []

  k = 0;
  while k < n:
    x = (a + b) / 2
    lista_b.append(x)

    if (f(x) * f(a) < 0):
      b = x
    else:
      a = x

    k = k + 1
    
  print(lista_b)
  return x;

def falsaposicao(f, a, b, n):
  lista_fp = []

  k = 0;
  while k < n:
    x = (a * f(b) - b * f(a)) / (f(b) - f(a))
    lista_fp.append(x)

    if (f(x) * f(a) < 0):
      b = x
    else:
      a = x

    k = k + 1
    
  print(lista_fp)
  return x;

print(f"Resultado final: {biseccao(f, 0, 1.3, 5)}\n")
print(f"Resultado final: {falsaposicao(f, 0, 1.3, 5)}\n")
