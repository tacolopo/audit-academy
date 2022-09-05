[Docker](https://docs.docker.com/get-started/overview/) is a platform that allows you to create deployable bundles of code. The packed code with computer instructions on how to run it are called images. The runnable instances of these images are referred to as containers. Docker is a powerful and technically complex tool, but it is very easy to develop with. If you've ever used a virtual operating system before, the concept will be familiar.

When you run an operating system in a virtual environment, with tools like [VirtualBox](https://www.virtualbox.org/), you are taking prebuilt code and using an application to run it. Docker does the same thing, but instead of virtualizing operating systems, it is used by developers for applications. Have you ever seen a github repository full of code, with an enticing readme page, but you didn't know how to actually run it? Docker solves this problem by providing a standard virtualization method through [Dockerfiles](https://docs.docker.com/develop/develop-images/dockerfile_best-practices/) and the [Docker Engine](https://docs.docker.com/engine/).

Installing Docker on Mac is as simple as downloading the [proper dmg file](https://docs.docker.com/desktop/install/mac-install/) based upon the computer chip you have. Installing on Linux is a bit more convoluted, with the full instructions [here](https://docs.docker.com/desktop/install/ubuntu/). The basic steps are to download the latest DEB package and then running the commands:
 ```
 sudo apt-get update
 sudo apt-get install ./docker-desktop-<version>-<arch>.deb
 ```
If you run into issues, try moving the DEB package into the home directory, and then rerunning the commands.
Now that Docker is installed, navigate to [Docker Hub](https://hub.docker.com/) and create an account. Create a new repository, give it a name of your choice (testrun here) and make sure it is public.


Next, launch the downloaded Docker Desktop App and sign in to the newly created Docker Hub account:

Next, we need to create the image of our application. Navigate to the directory of what you want to dockerize. In this example, we'll dockerize an instance of [poweredbyakash.com](https://poweredbyakash.com/) (folder called testrun in this example). First, you'll need to create a Dockerfile, and since this is a static website, we'll make our Dockerfile using Nginx. Create a new text file (Mac users can use TextEdit) and name it Dockerfile. Enter the following and save:
```
FROM nginx
COPY . /usr/share/nginx/html
```

Next open up your Terminal and navigate to your app's directory:
```
cd ~/Desktop/testrun
```
If you are using a Mac with an Apple Chip, I highly recommend changing the environment variable to build with the amd architecture, as it is widely supported on Akash. You can do that by running this command (Note: you'll need to do this each time you restart Docker):
```
export DOCKER_DEFAULT_PLATFORM=linux/amd64
```
Then, build the image with this command:
```
docker build -t testrun:1.0 .
```
This command calls the docker cli, instructs it to build an image, assigns it a name and tag with -t, and then we state the directory of where to build the image is our current directory with the period notation. You should now see the image in the Docker desktop application. 

Now we need to tag (associate) the image to our account.
```
docker tag testrun:1.0 accountname/testrun:1.0
```
This takes the image we built (testrun:1.0) and associates it with our repository on Docker Hub, which we gave the same name (not required), and gives it the correlated tag of 1.0. There should be no response on the CLI.

Finally, we need to push this image to Docker Hub. Run:
```
docker push accountname/testrun:1.0
```
You should now see the pushed image on your Docker Hub repository:
