# Cloudmos

Now that we have our application dockerized, a manifest created, and $AKT in our wallet, it is time to begin the deployment process on chain! While it is possible to deploy with the Command Line Interface (CLI), there are interfaces that simplify this process. The first deploy tool to gain traction was [Tom Beynon's docker application](https://github.com/tombeynon/akash-deploy), and Space Potato made a [web-based deploy tool](https://github.com/spacepotahto/akash-deploy-ui), but the one that has dramatically led the market is [Cloudmos' deploy tool](https://cloudmos.io/cloud-deploy).&#x20;

**Deploy Your Manifest With Cloudmos**

1. First, download the [Cloudmos deploy tool](https://cloudmos.io/cloud-deploy).
2. Open the application and add an account by recovering from your seed phrase.
3. Enter your seed phrase from the Keplr Wallet extension from the "Create a Wallet" tutorial. The password is not your seed phrase, but a way to access the account through Cloudmos. This password is not related to data on chain.
4.  If you've already imported an account, the landing page will look like this. Sign in with your password.

    <figure><img src="../../.gitbook/assets/Screen Shot 2022-09-05 at 3.57.55 PM.png" alt=""><figcaption></figcaption></figure>

5\.  Click "Create Deployment"

<figure><img src="../../.gitbook/assets/Screen Shot 2022-09-05 at 4.00.09 PM.png" alt=""><figcaption></figcaption></figure>

6\. Select "Empty"

<figure><img src="../../.gitbook/assets/Screen Shot 2022-09-05 at 4.00.57 PM.png" alt=""><figcaption></figcaption></figure>

7\. Name your deployment "test" (this is also just app data and not stored on chain) and paste in the manifest from the "Deploy.yaml" tutorial. Click "Create Deployment". **Note:** Notice how we have removed the accept section. **Also**, don't forget to change the account\_name in the image section to your account!

<figure><img src="../../.gitbook/assets/Screen Shot 2022-09-05 at 4.05.03 PM.png" alt=""><figcaption></figcaption></figure>

8\. Click Deposit

<figure><img src="../../.gitbook/assets/Screen Shot 2022-09-05 at 4.07.51 PM.png" alt=""><figcaption></figcaption></figure>

9\. I choose low fees. Select "Approve".

<figure><img src="../../.gitbook/assets/Screen Shot 2022-09-05 at 4.08.16 PM.png" alt=""><figcaption></figcaption></figure>

10\. Choose a provider. I'll select palmito.duckdns.org.

<figure><img src="../../.gitbook/assets/Screen Shot 2022-09-05 at 4.09.17 PM.png" alt=""><figcaption></figcaption></figure>

11\. Create the lease (memo field optional).&#x20;

<figure><img src="../../.gitbook/assets/Screen Shot 2022-09-05 at 4.09.32 PM.png" alt=""><figcaption></figcaption></figure>

12\. Switch away from the "Logs" tab and click on the "Leases" tab

<figure><img src="../../.gitbook/assets/Screen Shot 2022-09-05 at 4.10.01 PM.png" alt=""><figcaption></figcaption></figure>



13\. Click the URI. Congrats! You've deployed a site on Akash!

<figure><img src="../../.gitbook/assets/Screen Shot 2022-09-05 at 4.15.15 PM.png" alt=""><figcaption></figcaption></figure>

