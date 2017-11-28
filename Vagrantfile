# -*- mode: ruby -*-
# vi: set ft=ruby :
#
# Install python and python-pip:
# sudo apt-get install software-properties-common
# sudo apt-add-repository universe
# sudo apt-get update
# sudo apt-get install python-pip
#
# Install MariaDB with columnstore:
# sudo apt-get -y install libboost-all-dev expect perl openssl file sudo libdbi-perl libreadline-dev libdbd-mysql-perl
# wget https://downloads.mariadb.com/ColumnStore/1.0.7/ubuntu/dists/xenial/main/binary_amd64/mariadb-columnstore-1.0.7-1-xenial.x86_64.deb.tar.gz
# tar zxf mariadb-columnstore-1.0.7-1-xenial.x86_64.deb.tar.gz
# sudo dpkg -i *.deb
# sudo /usr/local/mariadb/columnstore/bin/postConfigure
# Expose the mcsmysql client:
# alias mcsmysql='/usr/local/mariadb/columnstore/mysql/bin/mysql --defaults-file=/usr/local/mariadb/columnstore/mysql/my.cnf'


Vagrant.configure("2") do |config|

  config.vm.define "test_suite" do |test_suite|

    test_suite.vm.box = "ubuntu/xenial64"

    test_suite.vm.provider "virtualbox" do |vb|
      vb.gui = false
      vb.memory = "4096"
    end

  end

end
