#!/bin/bash
echo "yaaaah hooooooo"
yum -y install httpd mod_ssl
systemctl enable httpd
systemctl start httpd
