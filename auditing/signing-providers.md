# Signing Providers

Once it comes time to actually sign providers, you'll need to use the CLI, as no interface exists for this process. Luckily, it is extremely simple with the use of our [script](../automated\_signing/sign\_from\_list.py):&#x20;

```
import os

lst = [
'akash1wxr49evm8hddnx9ujsdtd86gk46s7ejnccqfmy',
'akash19yyxp7la8pklaft3s0s2err85t8tyzlwqca0v3',
'akash1q7spv2cw06yszgfp4f9ed59lkka6ytn8g4tkjf',
]
account_name = input('Please enter your local auditor account name: ')

for item in lst:
	os.system(f'''
	AKASH_NET="https://raw.githubusercontent.com/ovrclk/net/master/mainnet";
	AKASH_VERSION="$(curl -s "$AKASH_NET/version.txt")";
	export AKASH_CHAIN_ID="$(curl -s "$AKASH_NET/chain-id.txt")";
	export AKASH_NODE="$(curl -s "$AKASH_NET/rpc-nodes.txt" | shuf -n 1)";
	akash tx audit attr create {item} --from {account_name} --fees 5000uakt -y;
''')
```

You can save this file to your working folder with the name sign\_from_\__list.py. Then open your terminal, cd into the directory where you saved the file, and run

```
python3 unsign_from_list.py
```

This will automatically iterate through all the provider addresses in the list and sign them with your auditor signature. You can then check the full list of audited providers with the command:

```
akash query audit list
```

You should now see the provider you signed along with your signature in the output similar to this:

```
- attributes:
  - key: host
    value: akash
  - key: organization
    value: d3akash.cloud
  - key: region
    value: eu-ch
  - key: tier
    value: community
  auditor: akash1nxq8gmsw2vlz3m68qvyvcf3kh6q269ajvqw6y0
  owner: akash1u5cdg7k3gl43mukca4aeultuz8x2j68mgwn28e
```

If the command fails, run the environment commands with it, e.g.:

```
import os

os.system('''
    AKASH_NET="https://raw.githubusercontent.com/ovrclk/net/master/mainnet";
    AKASH_VERSION="$(curl -s "$AKASH_NET/version.txt")";
    export AKASH_CHAIN_ID="$(curl -s "$AKASH_NET/chain-id.txt")";
    export AKASH_NODE="$(curl -s "$AKASH_NET/rpc-nodes.txt" | shuf -n 1)";
    akash query audit list;
''')
```
