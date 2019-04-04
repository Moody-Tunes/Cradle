# Cradle
Infastructure definitions for MoodyTunes


## Getting Started

- Create a directory on your computer to hold the MoodyTunes repositories

`mdkir MoodyTunes && cd MoodyTunes`

- Clone this repository and the moodytunes repository

`git clone git@github.com:Moody-Tunes/cradle.git`
`git clone git@github.com:Moody-Tunes/moodytunes.git`

- Install [virtualbox](https://www.virtualbox.org/wiki/Downloads)
- Install [vagrant](https://www.vagrantup.com/downloads.html) and add to $PATH
- Install vagrant plugins
	- `vagrant plugin install vagrant-hostsupdater`
- Create and activate a python3 virtual environment: `python3 -m venv venv`
- Install dependencies: `(venv) pip install -r requirements.txt`
	- If you can't install ansible because of dependencies, you might need to install libffi-dev


## Installing and booting Virtual Machine

- Bring up virtual machine with Vagrant: `vagrant up mtdj`
	- This should download the Ubuntu 18.04 virtualbox (might take a while the first time) and provision the box with the needed site programs, dependencies, and tools needed to run MoodyTunes

- The site is available through the hostname `moodytunes.vm`.
	- This is accomplished by `vagrant-hostmanager` adding the IP address for the virtual machine to your /etc/hosts file

- Now you can ssh into your virtual machine through `vagrant ssh mtdj`
	- You can also you straight ssh by doing `ssh vagrant@moodytunes.vm` when prompted for a password enter the default Vagrant password (which is `vagrant`)


## Specifying Environment To Run Against

By default, vagrant will target the host defined in the inventory/local file. This will boot up a local instance of
mtdj, so if you're a developer you shouldn't have to worry about it. If you happen to be provisioning an instance outside of a local environment you can specify the inventory to use with the `-i` option to ansible.
