# Integrate With Cloudmos

[Cloudmos](https://cloudmos.io/) (formerly Akashlytics) is currently the largest deployment vehicle for users of Akash. If you want your signature to be seen by users, integrating with Cloudmos is extremely beneficial.&#x20;

The Cloudmos deploy tool currently uses a .json file to pull auditor information. The official page is [here](https://github.com/maxmaxlabs/cloudmos-deploy/blob/master/auditors.json). We recommend forking the repository, adding your signature, and then making a PR.

The formatting is standard json with square brackets encompassing each item denoted in curly brackets:

```
[ 
  { 
    "id": "moultrie-audits-bronze", 
    "name": "Moultrie Audits Bronze", 
    "address": "akash18qa2a2ltfyvkyj0ggj3hkvuj6twzyumuaru9s4", 
    "website": "https://www.moultrieaudits.com/" 
  }, 
  { 
    "id": "moultrie-audits-silver", 
    "name": "Moultrie Audits Silver", 
    "address": "akash17fqxak4kprh2rlatjlv9w04s9ugl7mn32ckut3", 
    "website": "https://www.moultrieaudits.com/" 
  }, 
  { 
    "id": "akash-network",
    "name": "Akash Network", 
    "address": "akash1365yvmc4s7awdyj3n2sav7xfx76adc6dnmlx63",
    "website": "https://akash.network" 
  }
] 
```

Add a comma to the last listed item's curly bracket, then add a new item with your auditor's id and name (you can make this up, it is not on-chain information), your wallet address associated with the auditing account, and then your website for contact purposes:

```
  },
  { 
    "id": "your-auditor-name",
    "name": "Your Auditor Name", 
    "address": "your_akt_auditor_address",
    "website": "https://your_auditor_website" 
  }
```

Once the PR is made and Cloudmos is updated, your signature will be integrated. Super easy!
