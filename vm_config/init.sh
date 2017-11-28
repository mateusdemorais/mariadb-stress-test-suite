sudo apt-get install -y python &&
sudo apt-get install software-properties-common &&
sudo apt-add-repository universe &&
sudo apt-get update &&
sudo apt-get install -y python-pip &&
sudo apt-get install -y virtualenv &&
sudo apt-get install -y libboost-all-dev expect perl openssl file sudo libdbi-perl libreadline-dev libdbd-mysql-perl &&
wget https://downloads.mariadb.com/ColumnStore/1.0.7/ubuntu/dists/xenial/main/binary_amd64/mariadb-columnstore-1.0.7-1-xenial.x86_64.deb.tar.gz &&
tar zxf mariadb-columnstore-1.0.7-1-xenial.x86_64.deb.tar.gz &&
sudo dpkg -i *.deb &&
sudo /usr/local/mariadb/columnstore/bin/postConfigure
