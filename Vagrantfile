# -*- mode: ruby -*-
# vi: set ft=ruby :
Vagrant.configure("2") do |config|
    config.vm.define "backend" do |h|
        h.vm.box = "centos/7"
        h.vm.network "private_network", ip: "192.168.98.10"
        h.vm.hostname = "backend"
        h.vm.define "backend"
        h.vm.provider :virtualbox do |vb|
            vb.name = "backend"
            vb.memory = 512
        end
        id_rsa_pub = File.read("#{Dir.home}/.ssh/id_rsa.pub")
        config.vm.provision "copy ssh public key", type: "shell",
          inline: "echo \"#{id_rsa_pub}\" >> /home/vagrant/.ssh/authorized_keys"
    end
end
