import netmiko

ip = '10.254.0.1'
username = 'cisco'
password = 'cisco'
device_type = 'cisco_ios'
port = '22' 

net_connect = netmiko.ConnectHandler(
    ip = ip,
    device_type = device_type,
    username = username,
    password = password, 
    port = port
 )
 
 show_ip_route = net_connect.send_command('show ip route') 
 print(show_ip_route)