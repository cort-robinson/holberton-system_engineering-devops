# fix typo in wordpress settings file
exec { 'fix wordpress settings typo':
  command  => 'sed -i s/.phpp/.php/g /var/www/html/wp-settings.php',
  provider => 'shell',
}
