# Set max open files limits for holberton user in limits.conf

exec { 'replace_hard_limit':
  command  => 'sed -i "s/nofile 5/nofile 1024/" /etc/security/limits.conf',
  provider => 'shell'
}
exec { 'replace_soft_limit':
  command  => 'sed -i "s/nofile 4/nofile 2048/" /etc/security/limits.conf',
  provider => 'shell'
}
