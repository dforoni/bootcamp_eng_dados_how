#%%
# Imports
import requests
import json

#%%
url = 'http://economia.awesomeapi.com.br/json/last/USD-BRL'
ret = requests.get(url)
# %%
if ret:    
    print(ret)
else: 
    print('falied')
# %%
dolar = json.loads(ret.text)['USDBRL']

# %%
#print(f" 20 dolares custam: {float(dolar['bid']) * 20} reais")

# %%
def cotacao(valor, moeda):
    url = f'http://economia.awesomeapi.com.br/json/last/{moeda}'
    ret = requests.get(url)
    dolar = json.loads(ret.text)[moeda.replace('-', '')]
    print(f" {valor} {moeda[:3]} hoje custam: {float(dolar['bid']) * valor} {moeda[4:]}")


# print(cotacao(20, 'USD-BRL'))

#%%
try:
    print(cotacao(20, 'USD-BRL'))
except Exception as e:
    pass

# %%
def multi_moedas(valor, moeda):   
    url = f'http://economia.awesomeapi.com.br/json/last/{moeda}'
    ret = requests.get(url)
    dolar = json.loads(ret.text)[moeda.replace('-', '')]
    print(f" {valor} {moeda[:3]} hoje custam: {float(dolar['bid']) * valor} {moeda[4:]}")          
       
# %%
list_coins = ['USD-BRL', 'EUR-BRL', 'BTC-BRL', 'JPY-BRL', 'RPL-BRL']
# print(multi_moedas(20, 'USD-BRL'))
# %%
def error_check(func):
    def inner_func(*args,**kargs):
        try:
            func(*args,**kargs)
        except:
            print(f"{func.__name__} falhou")
    return inner_func

@error_check
def multi_moedas(valor, moeda):   
    url = f'http://economia.awesomeapi.com.br/json/last/{moeda}'
    ret = requests.get(url)
    dolar = json.loads(ret.text)[moeda.replace('-', '')]
    print(f" {valor} {moeda[:3]} hoje custam: {float(dolar['bid']) * valor} {moeda[4:]}") 

#%%
# print(multi_moedas(20, 'USD-BRL'))
# print(multi_moedas(20, 'EUR-BRL'))
# print(multi_moedas(20, 'BTC-BRL'))
# print(multi_moedas(20, 'RPL-BRL'))
# print(multi_moedas(20, 'JPY-BRL'))

#55
import backoff
import random

@backoff.on_exception(backoff.expo, (ConnectionAbortedError, ConnectionRefusedError, TimeoutError), max_tries=2)
def test_fun(*args, **kargs):
    rnd = random.random()
    print(F"""
            RND: {rnd}
            args: {args if args else 'sem args'}
            kargs: {args if kargs else 'sem kargs'}
    """)
    if rnd <.2:
        raise ConnectionAbortedError('Conexao foi finalizada')
    elif rnd < .4:
        raise ConnectionRefusedError('Conexao foi recusada')
    elif rnd < .6:
        raise TimeoutError('Tempo de espera excedido')
    else:
        return 'Ok!'

# %%
# print(test_fun())

# %%
# print(test_fun(42))

# %%
# print(test_fun(42, 51, nome = 'Ola'))

# %% 
import logging

# %%
log = logging.getLogger()
log.setLevel(logging.DEBUG)
formatter = logging.Formatter(
    '%(asctime)s - %(name)s, - %(levelname)s - %(message)s')
ch = logging.StreamHandler()
ch.setFormatter(formatter)
log.addHandler(ch)

# %%

@backoff.on_exception(backoff.expo, (ConnectionAbortedError, ConnectionRefusedError, TimeoutError), max_tries=2)
def test_fun(*args, **kargs):
    rnd = random.random()
    log.debug(f" RND: {rnd}")
    log.info(f" args: {args if args else 'sem args'}")
    log.info(f"kargs: {args if kargs else 'sem kargs'}")

    if rnd <.2:
        log.error('Conexao foi finalizada')
        raise ConnectionAbortedError('Conexao foi finalizada')
    elif rnd < .4:
        log.error('Conexao foi recusada')
        raise ConnectionRefusedError('Conexao foi recusada')
    elif rnd < .6:
        log.error('Tempo de espera excedido')
        raise TimeoutError('Tempo de espera excedido')
    else:
        return 'Ok!'
# %%
print(test_fun())
