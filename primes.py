import numpy as np

def is_prime(n):
    '''
    Recebe um número e verifica
    se ele é primo
    '''
    if n == 2:
        return True
    
    if n < 2 or n % 2 == 0:
        return False
    
    for i in range(3, int(n**(0.5)) + 1, 2):
        if n % i == 0:
            return False
        
    return True
    
# Buscando os primos de 10.000 até
# 19.999
if 'primos.npy' not in glob('*.npy'):
    primes = []
    a = 10000
    for i in range(5000):
        if is_prime(a + 2 * i + 1):
            primes.append(a + 2 * i + 1)

    primes = np.array(primes)
    with open('primos.npy', 'wb') as f:
        np.save(f, primos)

else:
    primes = np.load('primos.npy')
