# fix typo in wordpress settings file
exec { 'Fix wordpress settings file':
  command => 'sed -i s/.phpp/.php/g /var/www/html/wp-settings.php',
}
