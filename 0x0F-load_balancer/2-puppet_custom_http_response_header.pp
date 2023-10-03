# Automate the task of creating a custom HTTP header response

exec { 'add X-Served-By header':
  command  => 'sudo apt-get -y update;
  sudo apt-get -y install nginx;
  sudo sed -i "/listen 80 default_server;/a add_header X-Served-By $HOSTNAME;" /etc/nginx/sites-available/default;
  sudo service nginx restart',
  provider => shell,
}
