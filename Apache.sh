#!/bin/bash
yum -y install httpd mod_ssl
systemct1 enable httpd
systemctl start  httpd
sed -i 's/^/#/g' /etc/httpd/conf.d/welcome.conf
echo "<html><body><h1>>h1 there</h1></body</html>" > /var/www/html/index.html
