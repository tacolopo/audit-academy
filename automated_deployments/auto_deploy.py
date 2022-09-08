import os

file = open('re.txt')
info = open('info.txt')

#Uncomment one of the below
# provider = input('Please enter provider address:')
# provider = 'akash1q7spv2cw06yszgfp4f9ed59lkka6ytn8g4tkjf'

#Configures environment, creates deployment, waits 10 seconds for bids, then exports the bid list
os.system('''
	AKASH_NET="https://raw.githubusercontent.com/ovrclk/net/master/mainnet";
	AKASH_VERSION="$(curl -s "$AKASH_NET/version.txt")";
	export AKASH_CHAIN_ID="$(curl -s "$AKASH_NET/chain-id.txt")";
	export AKASH_NODE="$(curl -s "$AKASH_NET/rpc-nodes.txt" | shuf -n 1)";
	akash tx deployment create deploy.yaml --from account_name --fees 5000uakt -y;
	sleep 10;
	akash query market bid list --owner your_wallet_address --state=open >> re.txt; 
''')

#grabs the dseq
for line in file:
	if line.startswith('      dseq:'):
		dseq = line.split(':')
		dseq = dseq[1].strip()
		dseq = dseq.replace('"', '')
    
#creates the lease, sends the manifest, and exports the lease-status data
os.system(f'''
	akash tx market lease create --dseq {dseq} --provider {provider} --from account_name --fees 30000uakt --gas auto -y;
	akash provider send-manifest deploy.yaml --dseq {dseq} --provider {provider} --from bronze;
	akash provider lease-status --dseq {dseq} --from bronze --provider {provider} >> info.txt;
''')

#displays the URI in the terminal
for goose in info:
	if 'ca.aksh.pw' in goose:
		print(goose)
