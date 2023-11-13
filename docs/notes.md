# Installation

```
# Logged into the droplet as root
# Cloned repo into /var/www/EnerguruAI
git clone ${repo} /var/www/EnerguruAI

cd /var/www/EnerguruAI
# New droplet will not allow installation of global python libraries, and 
# therefore forcing us to install libraries through venv
apt install python3.11-venv

```

# Notes

Certificates are in `/root/ssl/` directory, and additional files are in `/etc/nginx/dhparam.pem` and in the `/etc/nginx/snippets` directory


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
 