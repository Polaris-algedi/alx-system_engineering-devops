# Set up SSH client configuration with puppet to
# connect to a server without typing a password
file{'/etc/ssh/ssh_config':
  ensure  => 'present',
  content => '248550-web-01
    HostName 100.26.177.153
    User ubuntu
    IdentityFile ~/.ssh/school
    PasswordAuthentication no',
}
