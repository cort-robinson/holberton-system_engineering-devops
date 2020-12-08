# kills a process named killmenow

exex { 'pkill killmenow':
  command => '/usr/bin/pkill -f /killmenow'
}
