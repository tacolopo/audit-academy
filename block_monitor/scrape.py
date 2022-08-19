import requests, re

if 0:
    import ssl
    #Ignore SSL certificate errors
    ctx = ssl.create_default_context()
    ctx.check_hostname = False
    ctx.verify_mode = ssl.CERT_NONE

url = '#address to get tx details'
response = requests.get(url).text

matches = re.findall(r'''memo["']: ?["'](.*?)["'],''', response)
print(len(matches))

for e in matches:
    print(e)
