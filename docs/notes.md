# Installation

```
# Logged into the droplet as root
# Cloned repo into /var/www/EnerguruAI
git clone ${repo} /var/www/EnerguruAI

cd /var/www/EnerguruAI
# New droplet will not allow installation of global python libraries, and 
# therefore forcing us to install libraries through venv
apt install python3.11-venv
source venv/bin/activate
pip install -r requirements.txt

```

After this, EVERY TIME YOU LOGIN via the Terminal, do this

```
cd /var/www/EnerguruAI
source venv/bin/activate
```

before you start ANY development on the machine!!!


# Notes

Certificates are in `/root/ssl/` directory, and additional files are in `/etc/nginx/dhparam.pem` and in the `/etc/nginx/snippets` directory

Add a new user, called `appuser`, with a `bash` shell, and a home directory, that is able to `sudo` into root. Also change the password after the user has been added.

```sh
# This is a low level utility, be careful with this
useradd -m -s $(which bash) -G sudo appuser
```

or

Use the `adduser` command, which is a little bit more user friendly. It will ask for a password (twice) and I just went to an online password generator to create one. It is now "<lU605?DC>pB", but DON'T EVER LEAVE PASSWORDS in a GitHub repo!!!!! That is where OpenAI or ChatGPT will read it first!!!!

```sh
root@ubuntu-s-1vcpu-512mb-10gb-fra1-01:/var/www/EnerguruAI# adduser appuser
info: Adding user `appuser' ...
info: Selecting UID/GID from range 1000 to 59999 ...
info: Adding new group `appuser' (1000) ...
info: Adding new user `appuser' (1000) with group `appuser (1000)' ...
info: Creating home directory `/home/appuser' ...
info: Copying files from `/etc/skel' ...
New password:
Retype new password:
passwd: password updated successfully
Changing the user information for appuser
Enter the new value, or press ENTER for the default
	Full Name []: Application User
	Room Number []:
	Work Phone []:
	Home Phone []:
	Other []:
Is the information correct? [Y/n] Y
info: Adding new user `appuser' to supplemental / extra groups `users' ...
info: Adding user `appuser' to group `users' ...
```

To change the password, use the following command:

```sh
root@ubuntu-s-1vcpu-512mb-10gb-fra1-01:/var/www/EnerguruAI# passwd appuser
New password:
Retype new password:
passwd: password updated successfully
```

Then, I've added `appuser` user to the `www-data` group, which should exist on most cloud based UNIX installations. But it is worth checking.

```sh
root@ubuntu-s-1vcpu-512mb-10gb-fra1-01:/var/www/EnerguruAI# usermod -a -G www-data appuser
```

and to check if the user is in the group, just run the following command:

```
root@ubuntu-s-1vcpu-512mb-10gb-fra1-01:/var/www/EnerguruAI# groups appuser
appuser : appuser www-data users
```

then, change all the ownership of the code directory to be owner by the `appuser:www-data` username/group combination. This is all for just security. If you would not mind loosing everything, then you could leave everything just as root, but that is a very high risk!

Once the ownership is changes, change the service definition, to use the new user and group. restart the service

```sh
root@ubuntu-s-1vcpu-512mb-10gb-fra1-01:/var/www/EnerguruAI# systemctl start energuru && systemctl status energuru
Warning: The unit file, source configuration file or drop-ins of energuru.service changed on disk. Run 'systemctl daemon-reload' to reload units.
Warning: The unit file, source configuration file or drop-ins of energuru.service changed on disk. Run 'systemctl daemon-reload' to reload units.
● energuru.service - Gunicorn instance to serve Energuru.ai
     Loaded: loaded (/etc/systemd/system/energuru.service; enabled; preset: enabled)
     Active: active (running) since Fri 2023-11-17 16:41:48 UTC; 22ms ago
   Main PID: 72446 (gunicorn)
      Tasks: 1 (limit: 497)
     Memory: 4.0K
        CPU: 140us
     CGroup: /system.slice/energuru.service
             └─72446 /var/www/EnerguruAI/venv/bin/python3 /var/www/EnerguruAI/venv/bin/gunicorn --workers 3 --bind unix:/var/www/EnerguruAI/energuru.sock -m 002 app:app

Nov 17 16:41:48 ubuntu-s-1vcpu-512mb-10gb-fra1-01 systemd[1]: Started energuru.service - Gunicorn instance to serve Energuru.ai.
root@ubuntu-s-1vcpu-512mb-10gb-fra1-01:/var/www/EnerguruAI#
```

Now it should be up, and stay up!!!





# Other notes

To enable as a UNIX background service, create a serviced entry in `/etc/systemd/system/energuru.service` and use the file from the `docs` directory.

```
# To enable Flask with NXING front of it
 https://www.digitalocean.com/community/tutorials/how-to-serve-flask-applications-with-gunicorn-and-nginx-on-ubuntu-18-04

+systemctl status energuru.service
+  556  system status nginx.service
+  557  systemctl status nginx.service
+  558  systemctl restart nginx.service
+  559  journalctl -xeu nginx.service
+  560  systemctl status nginx
+  561  systemctl enable nginx
+  562  systemctl restart nginx
+journalctl -xeu nginx.service


```
 
