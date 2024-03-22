# install flask from pip3 using Puppet

class { 'python::pip': }

package { 'flask':
  ensure   => '2.1.0',
  provider => 'pip3',
  require  => Class['python::pip'],
}
