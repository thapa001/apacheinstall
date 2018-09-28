# apacheinstall
yum -y install httpd
systemct1 enable httpd
systemctl start  httpd
yum -y install mod_ssl
systemctl restart httpd

