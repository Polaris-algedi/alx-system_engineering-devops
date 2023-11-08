# This Puppet manifest replaces 'phpp' with 'php' in /var/www/html/wp-settings.php
exec { 'replace_phpp_with_php':
  command => '/bin/sed -i "s/phpp/php/g" /var/www/html/wp-settings.php',
  onlyif  => '/bin/grep -q phpp /var/www/html/wp-settings.php',
  path    => ['/bin', '/usr/bin'],
}
