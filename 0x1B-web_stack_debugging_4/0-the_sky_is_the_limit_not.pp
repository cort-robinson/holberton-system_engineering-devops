# remove ulimit for nginx service
file { '/etc/default/nginx':
  content => '',
} ->
exec { 'restart nginx service':
  command  => 'sudo service nginx restart',
  provider => 'shell',
}

