# Tipps for Apache2 Webserver
Apache HTTP Server is the leading open source web server. On Ubuntu and Debian, the package is named "apache2" (on Redhat distributions, it is named "httpd").

## Configuration
`/var/www/html` contains a standard website `index.html`, which you can reach via ip `127.0.0.1`. On Ubuntu, the apache configuration under `/etc/apache2` follows a very special scheme. In this folder, you find the main configuration `apache2.conf`. Additionally, there are subfolders with the extension `-available`, containing the available configuration files for further virtual hosts, modules, etc. To make a configuration active in apache2, you must create a link from a file in an `-available` folder into the corresponding `-enabled` folder. Ideally, you use one of the special commands like `a2ensite` for this.

### Example to setup a webpage
Taken from [techrepublic.com](https://www.techrepublic.com/article/how-to-use-the-apache-web-server-to-install-and-configure-a-website/)
```bash
cd /var/www/html #go to the folder where you want to create your project
sudo mkdir test #create a project folder
sudo chown $USER:$USER test #if in /var/www/html, you might want to change the new project folder to another owner than root
chmod 755 test #you might want to change the read-write permissions too
cd test
touch index.html #create an index.html file inside. See below for an example
cd /etc/apache2/sites-available
touch test.conf #create a configuration for your site. See below for an example
sudo a2ensite test.conf #enable test.conf
sudo systemctl reload apache2 #reload the configuration files into the server
```
A simple index.html could look like:
```html
<!DOCTYPE html>
<html>
<body>
<h1>Hello, TechRepublic!</h1>
<p>How are you doing?</p>
</body>
</html>
```

A simple test.conf could look like:
```txt
<VirtualHost *:80>
    ServerAdmin admin@example.com
    ServerName example.com
    ServerAlias www.example.com
    DocumentRoot /var/www/html/test
    ErrorLog ${APACHE_LOG_DIR}/error.log
    CustomLog ${APACHE_LOG_DIR}/access.log combined
</VirtualHost>
```