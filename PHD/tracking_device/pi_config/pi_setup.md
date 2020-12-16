## setup

1. Update system

```bash
sudo apt-get update
```

2. set ssh

In the SD card containing pi OS:
	- Look for the boot partition
	- create a file named ssh
	- OS will auto enable ssh

3. set passwordless SSH acccess

```bash
# create the keys in the 'main' pc
ssh-keygen

# share public key into pi
ssh-copy-id <USERNAME>@<IP-ADDRESS>
```

