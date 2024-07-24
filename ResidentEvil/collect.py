# %%
import requests

url = "https://www.residentevildatabase.com/personagens/ada-wong/"

resp = requests.get(url)
# %%

resp.status_code

# %%

resp.text
# %%
