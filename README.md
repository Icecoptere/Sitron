# Sitron
C'est le Sitron trop bon

## Modules
To make sure we are using the same module versions, we should use a requirements.txt which contains all modules and
their versions, and makes it easier to install from one place to another

To generate it, best is to use pipreqs:

>pipreqs . --force

This will create a requirements.txt file which contains all modules.
We can then install the modules from this file using :

>pip3 install -r /path/to/requirements.txt



Another way to list all modules is (but it lists all modules installed in the env, and not just the ones you use)

>pip3 freeze > requirements_pip.txt