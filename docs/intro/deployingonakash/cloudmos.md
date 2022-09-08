Now that we have our application dockerized, a manifest created, and $AKT in our wallet, it is time to begin the deployment process on chain! While it is possible to deploy with the Command Line Interface (CLI), there are interfaces that simplify this process. The first deploy tool to gain traction was [Tom Beynon's docker application](https://github.com/tombeynon/akash-deploy), and Space Potato made a [web-based deploy tool](https://github.com/spacepotahto/akash-deploy-ui), but the one that has dramatically led the market is [Cloudmos' deploy tool](https://cloudmos.io/cloud-deploy). 

# Deploy Your Manifest With Cloudmos

1. First, download the [Cloudmos deploy tool](https://cloudmos.io/cloud-deploy).

2. Open the application and add an account by recovering from your seed phrase.

3. Enter your seed phrase from the Keplr Wallet extension from the "Create a Wallet" tutorial. The password is not your seed phrase, but a way to access the account through Cloudmos. This password is not related to data on chain.

4. If you've already imported an account, the landing page will look like this. Sign in with your password.

5.  Click "Create Deployment"

6. Select "Empty"

7. Name your deployment "test" (this is also just app data and not stored on chain) and paste in the manifest from the "Deploy.yaml" tutorial. Click "Create Deployment". **Note**: Notice how we have removed the accept section. **Also**, don't forget to change the account_name in the image section to your account!

8. Click Deposit

9. I choose low fees. Select "Approve".

10. Choose a provider. I'll select palmito.duckdns.org.

11. Create the lease (memo field optional). 

12. Switch away from the "Logs" tab and click on the "Leases" tab

13. Click the URI. Congrats! You've deployed a site on Akash!
