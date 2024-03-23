#!/usr/bin/env bash
# Automating my Tasks using Puppet set up your client SSH configuration file

file { '/etc/ssh/ssh_config':
  ensure => present,
content  => "
    # SSH client configuration
    Host *
      IdentityFile ~/.ssh/school
      PasswordAuthentication no
  ",
}
