# %%
from dotenv import dotenv_values
import requests 

# %%
config_values = dotenv_values('.env')


# %%
TOKEN_API = config_values['CEP_ABERTO_API']
URL_CEP = config_values['CEP_ABERTO_URL_API']
headers = {'Authorization': f'Token token={TOKEN_API}'}

# %%
def search_by_cep(cep):
    diff_size_cep = 8 - len(str(cep))
    if diff_size_cep>0:
        cep = str(cep)+ "0"*diff_size_cep
    url = URL_CEP+"cep"
    payload = {'cep':cep}
    response = requests.get(url,headers=headers,params=payload)
    if response.status_code == 200:
        return response.json()
    else:
        print(response.status_code)
        print(response.json())
        return response