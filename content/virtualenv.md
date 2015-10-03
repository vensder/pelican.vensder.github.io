Title: Virtualenv for Python in CentOS
Date: 2015-10-03 11:04
Category: python

Virtualenv for Python in CentOS
###############################

```log
Oct 02 22:28:35 Installed: python27-libs-2.7.3-6.2.el6.nux.x86_64
Oct 02 22:28:36 Installed: python27-2.7.3-6.2.el6.nux.x86_64
Oct 02 23:56:57 Installed: python-devel-2.6.6-64.el6.x86_64
Oct 02 23:56:58 Installed: python-virtualenv-1.10.1-1.el6.noarch
Oct 02 23:57:03 Installed: python-virtualenv-clone-0.2.4-1.el6.noarch
Oct 02 23:57:04 Installed: python-virtualenvwrapper-3.5-2.el6.noarch
```

```sh
mkdir ~/venv && cd ~/venv
virtualenv --no-site-packages <venv_name>
```

```sh
cd ~/work/<project_name>
mkdir venv && echo "Virtualenv directory" > venv/README
git add venv && echo "/venv/" >> .gitignore && git add -f .gitignore
virtualenv --no-site-packages --prompt="(<project_name>)" <venv_name>

```

```
source ~/venv/<venv_name>/bin/activate
```
```
deactivate
```
