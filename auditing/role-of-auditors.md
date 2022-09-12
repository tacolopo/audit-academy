# Role of auditors

Auditors on Akash exist to help users find reliable providers, aid in provider setup, and alert prominent users and providers about issues.&#x20;

**Help Users Find Reliable Providers**

When someone new goes to use Akash, they should be able to deploy their Manifest successfully. Deploying to a misconfigured provider and having the process fail will likely confuse someone coming from Web2 and cause them to exit the ecosystem. Say what you want about AWS and GCP, but they are very reliable and easy to use. If Akash, or any decentralized product, is going to seriously compete with Web2, it needs to work, on the first try. That's why we need to highlight reliable providers through the auditing and signatory process.&#x20;

**Aid in Provider Setup**

When you get approached for an audit, or go to audit a doxxed provider (someone who's identity is known or public), and things aren't working, it's your duty to report that. You should offer troubleshooting advice to the best of your ability, but notifying the provider is the most important thing. For example, if you see they didn't bid on a deployment of a static website, and have plenty of available resources, you should check to ensure their wallet has at least 5 $AKT. If their provider is inactive, you should ask if they ran the startup script. If you get errors accessing the deployment, you could ask about their general setup, perhaps their ports are misconfigured?

Another thing to consider is that as setting up a provider gets easier, you may be dealing with people who have low technical capabilities. In this case, the Praetor team may have walked them through the process, and you can always refer them back to the source about their setup.&#x20;

**Alert Prominent Users and Providers About Issues**

Sometimes providers go down, and important projects may exit Akash if their site/app is offline for extended periods of time. If you see a provider go down, you should check their active leases. If you know of an important project, perhaps monitor the deployment so you can alert them if something happens. Moultrie recently alerted [Craft Economy](http://crafteconomy.io/), an upcoming blockchain, about their website going down, and they were able to switch providers and redeploy. **** We also notified the Akash team that their website was allowing connections over http, and offered solutions about how to fix that.

For providers, other issues may exist outside of them failing. Moultrie recently alerted ThanosNode when their provider wasn't collecting funds from the escrow. This means that they were still hosting the application, even after the agreed to price would have exhausted the existing payment. This helps save providers money and improve their experience.

**Reputation v. Accessibility**

A final note to consider is that all auditors have to deal with the balancing Reputation and Accessibility. This is to say that if you audit someone and the provider performs poorly, whether unjustified or not, you will suffer reputational damage. This leads to pressure to increase audit standards, but then providers don't want to go through the trouble of dealing with you, and costs increase, decreasing the accessibility of your audits. There is no perfect middleground, but be aware of this, and accept imperfection. Moultrie introduced a tiered auditing structure to address this problem.
