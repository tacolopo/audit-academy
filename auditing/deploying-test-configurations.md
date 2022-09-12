# Deploying Test Configurations

When auditing providers, it is important to pay attention to their stated capabilities. For example, some providers may state that they're chia-plot enabled, while others may advertise persistent storage. If they are advertising something, it is best to test it.

If they are no unique traits on the provider, it is still useful to test multiple types of deployments. Two common use-cases for Akash are website hosting and mining. Therefore, it's good to test a website, like we did with poweredbyakash.com, and a miner configuration, which you can do with [Monero](https://github.com/ovrclk/awesome-akash/blob/master/moneroocean/deploy.yaml) or [Pkt](https://github.com/ovrclk/awesome-akash/blob/master/pkt-miner/deploy.yaml).

Other good test configurations could include a collaborative site like [Mattermost](https://github.com/ovrclk/awesome-akash/blob/master/mattermost/deploy.yaml) or [Kanboard](https://github.com/ovrclk/awesome-akash/blob/master/kanboard/deploy.yaml), or if you want to support another decentralized project, you could run [IPFS](https://github.com/ovrclk/awesome-akash/tree/master/ipfs). All of these linked manifests are courtesy of the Awesome Akash repo.

When you test these deployments, there should be an element of randomness to what gets deployed to reduce bias and ensure a range of abilities exist on the provider. Manifests should vary, as well as their deployment time, within whatever time period you have specified for the length of the audit.

**Deployment Script**

****
