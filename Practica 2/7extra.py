def es_primo(num):
    if num < 2:
        return False
    else:
        for i in range(2 , int(num**0.5)+1):
            if num % i == 0:
                return False
        return True
print(es_primo(7))

def es_primo1(num):
    if num < 2:
        return False
    else:
        # Iterar solo hasta la raíz cuadrada de num + 1
        # Usar num // 2 + 1 sería demasiado largo y no se mantendría preciso para números como 2.
        for i in range(2 , int(num**0.5) + 1):
            if num % i == 0:
                return False
        return True

print(es_primo1(72))  # Debería imprimir True
