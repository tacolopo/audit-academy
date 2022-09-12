# Integrate With Awesome Akash

While Cloudmos is the primary hub for deploying on Akash, [Awesome Akash](https://github.com/ovrclk/awesome-akash) is the go to list for ready-to-deploy manifests for beginners and experience users alike.

Awesome Akash lists close to 100 deployment examples complete with readme and deploy.yaml files. As noted previously, the deploy.yaml files specify the user's desired configuration of the deployment. This is also where the user specifies if they want to see audited providers or not. So, just being integrated with Cloudmos is not enough, you also need to get your auditor on the tenant's radar.

Since it is the auditor's goal to seamlessly integrate into the user's experience, you want to minimize their effort to include you. Cloudmos automatically syncs with the Awesome Akash repository, and since many user's stick with the default configuration of these files, adding your auditor into these files is paramount. We recommend forking the repository, adding your signature, and then making a PR.

Here's an example of [Moultrie Audit's PR to Awesome Akash](https://github.com/ovrclk/awesome-akash/commit/b720cd57784f98eb471c5ec5f205ca68abe84fc2) for reference.

Let's take a look at the first folder on the Awesome Akash repo, CodiMD, and then open the [deploy.yaml file](https://github.com/ovrclk/awesome-akash/blob/master/CodiMD/deploy.yaml). You should see something similar to this:

```
---
version: "2.0"

services:
  db:
    image: postgres:11.6-alpine
    env:
      - POSTGRES_USER=codimd
      - POSTGRES_PASSWORD=change_password
      - POSTGRES_DB=codimd
    expose:
        - port: 3306
          as: 3306
        to: 
            - service: db
  codimd:
    image: hackmdio/hackmd:2.4.1
    env:
      - CMD_DB_URL=postgres://codimd:change_password@database/codimd
      - CMD_USECDN=false
    depends-on:
      - db
    expose: 
        - port: 3000
          as: 3000
        to:
            - global: true

profiles:
  compute:
      db:
        resources:
          cpu:
            units: 0.5
        memory:
            size: 512Mi
        storage:
            size: 512Mi
    codimd:
      resources:
        cpu:
          units: 0.5
        memory:
          size: 512Mi
        storage:
          size: 1Gi
  placement:
    westcoast:
      attributes:
        host: akash
      signedBy:
        anyOf:
          - "akash1365yvmc4s7awdyj3n2sav7xfx76adc6dnmlx63"
          - "akash18qa2a2ltfyvkyj0ggj3hkvuj6twzyumuaru9s4"
      pricing:
          db:
            denom: uakt
          amount: 10000
        codimd: 
          denom: uakt
          amount: 10000

deployment:
   db:
      westcoast: 
        profile: db
        count: 1
  codimd:
    westcoast:
      profile: codimd
      count: 1
```

The section we are interested in is the signedBy field. In Akash, adding an address to the anyOf section will include a search for providers signed by any of the listed addresses. You can think of this like the pipe ( | ) in programming. Providers only need to be signed by one of the listed signatures to populate to the user. Add your signature as such:

```
      signedBy:
        anyOf:
          - "akash1365yvmc4s7awdyj3n2sav7xfx76adc6dnmlx63"
          - "akash18qa2a2ltfyvkyj0ggj3hkvuj6twzyumuaru9s4"
          - "your_akt_auditor_address"
```

Once your PR gets approved, it will sync to Cloudmos, and you'll be integrated into the user's default deployment experience.
