# Automate the task of creating a custom HTTP header response

$config="events {}

http {

    server {
        listen 80 default_server;
        listen [::]:80 default_server;

	add_header X-Served-By $HOSTNAME;

        server_name purepolaris.tech;

        root /var/www/html/test;
        index index.html;

        location /redirect_me {
            return 301 https://www.youtube.com/watch?v=QH2-TGUlwu4;
        }
        
        error_page 404 /custom_404.html;
        location = /custom_404.html {
            internal;
        }
    }
}"

package { 'nginx':
  ensure => installed,
  before => File['/etc/nginx/nginx.conf'],
}


file { '/etc/nginx/nginx.conf':
  ensure  => present,
  content => $config,
  require => Package['nginx'],
  notify  => Service['nginx'],
}

service { 'nginx':
  ensure    => running,
  enable    => true,
  subscribe => File['/etc/nginx/nginx.conf'],
}
