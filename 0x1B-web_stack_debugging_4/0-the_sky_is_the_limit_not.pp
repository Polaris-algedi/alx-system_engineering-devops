# Increase max open files in /etc/default/nginx
file { '/etc/default/nginx':
  ensure  => file,
  content => inline_template("<%= File.read('/etc/default/nginx').gsub(/^ULIMIT=.+$/, 'ULIMIT=\"-n 10000\"') %>"),
}

# Restart Nginx if the file was changed
exec { 'restart_nginx':
  command     => 'service nginx restart',
  refreshonly => true,
  subscribe   => File['/etc/default/nginx'],
  provider    => 'shell',
}
