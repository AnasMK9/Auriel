# Purpose
Client that listens to commands on slack channel and executes on local machine, meant to automate scanning targets for bug bounty programs and move it the cloud instead of locally, planning to run the tools in a containerized environment. Point of all this complication is to configure tools once, create a channel for each tool, have them store results somewhere (S3 instance? google drive? who knows?). also categorize results by target (when running multiple tools against one target).

# How?
Originally intended to running multiple instances of each tool on a virtual machine, ended up liking the idea of containerizing the tools and spawning them using a container as a service platform more. each tool will recieve commands through a specific channel, and will have a class configured to handle its options and spawn a container through gcp or some other cloud provider. A Router class will be responsible for to mapping the channels with the classes responsible to run the tools. idk if it's necessary yet but thought it's fancier and will improve scalability in the future to add as many tools and channels as needed.

# Running
~~current main branch is a big mess, last commit that actually executes is f38dd1be9b7fa39bde86733ceeba074bddc2b0d8~~

1- install requirements using 
```
pip install -r requirements.txt
```
2- create a .sh script that includes `export VARIABLE_NAME=xxxx` for each environment variable and execute before running python

3- run with `python -m auriel.app`

# Plans
- Test with six2dez/reconftw.git and anshumanbh/git-all-secrets
- Implement a way to start a passive scanner for subdomains, new git commits for watched organizations
- Get it to work
- Add logging with sentry
- Documentation/unit tests and all the inconvenient stuff?
if you have an experience developing something like this or interested in the project please feel free to contact me or submit a PR

### I Just discovered [axiom](https://github.com/pry0cc/axiom) and that handles the job of spinning up instances for scanning, figuring out how to make them work together if it didn't have some of the features I have in mind