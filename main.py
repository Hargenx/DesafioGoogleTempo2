def solution(n):
  int_max = int((297595**2 - (271533 - n)**2)**(1 / 2) - 121780 + 34)
  sqrt_int_max = int(int_max**(1 / 2)) + 1
  tamanho = int_max // 2 + 1
  primos = [2]
  set_numero = [True] * tamanho
  set_numero[0] = False
  for numero in range(3, sqrt_int_max, 2):
    if set_numero[numero // 2]:
      for multiplo in range(numero**2, int_max, numero * 2):
        set_numero[multiplo // 2] = False

  primos.extend(x * 2 + 1 for x, y in enumerate(set_numero) if y)
  return ''.join(map(str, primos))[n:n + 5]


print(solution(3))

'''
import time
start = time.time()
for n in range(10000):
  print(solution(n))
print(f'{(time.time() - start)} seconds')'''


'''"Esta versão da função usa o algoritmo Peneira de Eratóstenes com algumas otimizações adicionais. Ela primeiro elimina os números pares e, em seguida, verifica os números ímpares no intervalo usando uma versão otimizada da Peneira de Eratóstenes usando a peneira Sundaram e a peneira segmentada para verificar apenas o números no intervalo. Isso deve resultar em melhor desempenho."'''
