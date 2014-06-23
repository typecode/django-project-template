# -*- mode: ruby -*-
# vi: set ft=ruby :

VAGRANTFILE_API_VERSION = "2"

Vagrant.configure(VAGRANTFILE_API_VERSION) do |config|

    config.vm.box = "jdowning/trusty64"
    config.vm.box_check_update = false
    config.vm.network "forwarded_port", guest: 8000, host: 8000
    config.vm.network "private_network", ip: "192.168.33.10"

    config.vm.provider "virtualbox" do |vb|
        vb.gui = false
        vb.customize ["modifyvm", :id, "--memory", "1024"]
    end

    config.vm.synced_folder "salt/roots/", "/srv/salt/"

    config.vm.provision :salt do |salt|
        salt.minion_config = "salt/minion"
        salt.run_highstate = true
    end
end
