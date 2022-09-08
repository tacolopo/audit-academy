Congrats on dockerizing your first application! Now that we have the prepackaged code bundle ready to go, it's time to shore up the Akash side of things. Before we actually get to deploying though, it's important to understand what the deploy.yaml file does, as it's the key part of the deployment process.

In Docker, the [compose file](https://docs.docker.com/compose/) allows you to use [yaml](https://yaml.org/) (easily readable language) to define the applications specifications. Things like [ports](https://www.cloudflare.com/learning/network-layer/what-is-a-computer-port/) and [dependencies](https://coderslegacy.com/what-are-dependencies-in-programming/) are in this file. Akash uses something very similar to Docker's compose files called a "manifest" (same thing as deploy.yaml). The manifest is where you will put in all the specifications for how you want you application to be configured, and it dually serves as the request/query to providers. So in addition to specifying things like what image you want to run, ports, and CPU/memory, you also include how much you are willing to pay. Let's take a look at an example:

# Note:

I've included in the accept field a domain that I own. Putting this domain in your manifest will not override my deployment. It also may not work, as providers allow one manifest with the same domain active at a time. I recommend removing this field before deploying, which I do in the "Cloudmos" tutorial in this intro section.
```
---
version: "2.0"

services:
  web:
    image: account_name/testrun:1.0
    expose:
      - port: 80
        as: 80
        accept:
          - poweredbyakash.com
          - www.poweredbyakash.com
        to:
          - global: true

profiles:
  compute:
    web:
      resources:
        cpu:
          units: 0.5
        memory:
          size: 512Mi
        storage:
          size: 512Mi
  placement:
    dcloud:
      pricing:
        web:
          denom: uakt
          amount: 100

deployment:
  web:
    dcloud:
      profile: web
      count: 1
```      
Now here's an annotated version to explain what we're looking at:
```
---
#Version is currently 2.0
version: "2.0"

services:
  web:
  #This is where you specify the Docker account and image you want to have hosted
    image: account_name/testrun:1.0
    expose:
    #These are the ports we're using. For a simple web app like this, 80 works well.
    #Note that there is currently no native support for 443 (https)
      - port: 80
        as: 80
        #This is where we list the domain we want to resolve. The Akash deployment
        #will return a uri (o7cks0qoe5f3db6sk67ogm1ir0.ingress.provider-0.prod.ams1.akash.pub/)
        #if you want to be able to enter in an actual domain name it needs to be
        #included here. Other actions are required which we'll discuss later. 
        accept:
          - poweredbyakash.com
          - www.poweredbyakash.com
        to:
          - global: true

profiles:
  compute:
    web:
    #Here we list how much resources we need from the provider to successfully run
    #our application. The more resources you need, the more expensive the deployment.
      resources:
        cpu:
          units: 0.5
        memory:
          size: 512Mi
        storage:
          size: 512Mi
  placement:
    dcloud:
      pricing:
      #uakt is a representation of 1 akt divided by 1 million. This is the max price 
      #per block, meaning every ~6 seconds, we are willing to pay the provider 
      #.0001 akt
        web:
          denom: uakt
          amount: 100

deployment:
  web:
  #Don't worry about this field as a beginner, but it maps the service to the 
  #deployment specifications. The count is how many instances are present on 
  #the infrastructure.
    dcloud:
      profile: web
      count: 1
 ```
There are tons of other thing you can include in this file, and we've left out some important fields for auditors. We'll come back to this file to update our deployment once we get into more auditing specific tasks. For the meantime, understanding the basics is sufficient. If you'd like to see ready-to-use templates for a bunch of applications, the [Awesome-Akash repository](https://github.com/ovrclk/awesome-akash) is a fantastic resource.
