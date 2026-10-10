# system

| command | function |
|---|---|
| add ntp_server general | add an NTP server for time synchronization. |
| change cli | modify command line interface (CLI) settings. Use this command when you need to modify the CLI timeout period, capacity display mode, output paging mode, command execution confirmation switch, or performance statistics display mode. |
| change nas_service active | activate the NAS feature service for the first time. |
| change ntp_server config | configure the time synchronization function. Run this command if you want the storage system to synchronize its time with that of an NTP server. |
| change system description | change the storage system's description. |
| change system dns_load_balance | enable or disable the DNS load balancing function and configure the load balancing policy. |
| change system location | change the geographical location of a storage system. |
| change system media_scan | modify the settings of disk media scanning. |
| change system name | change the storage system's name. |
| change system ntp | configure the NTP. Run this command if you want the storage system to synchronize its time with that of an NTP server. |
| change system server_port | modify port information of the system. |
| change system time | change the storage system's time. If the storage system's time is incorrect, you can run this command to change it. |
| change system timezone | change the time zone where the storage system resides in. If the displayed time zone is different from the actual local time zone, you can run this command to change the time zone. |
| change system write_policy | set the write protection switch and the period for a controller to run before the write policy is switched to write protection. |
| change user_session number | change the number of sessions supported by the system. |
| delete container_image | delete an application image package imported by a user. |
| delete helm_chart | delete an application chart package imported by a user. |
| import container_image | import an application image software package. |
| import helm_chart | import an application Helm chart package. |
| poweroff system | power off the storage system. Running this command causes service interruption. |
| reboot system | restart the storage system. Running this command causes service interruption. |
| remove ntp_server general | delete an NTP server used for time synchronization. |
| show bst enabled | display the global BST function. |
| show container_image general | query information about application image packages imported by a user. |
| show helm_chart general | query information about the application chart packages imported by a user. |
| show ntp status | query the NTP status. |
| show ntp_server general | query the time synchronization function settings. |
| show system client_name | query the address information about a storage system maintenance terminal. |
| show system dns_load_balance | query information about DNS load balancing. |
| show system dst | query the daylight saving time (DST) settings of the storage system. |
| show system manufactory | query the vendor and brand of the storage system. |
| show system media_scan | query the disk media scanning information, including the running status and execution period. |
| show system ntp | query the Network Time Protocol (NTP) settings. |
| show system power_consumption | query system power consumption in real time. |
| show system server_port | query the port information about a specific service. |
| show system timezone | query the time zone where the storage system resides. |
| show system write_policy | display the current cache write policy of the system. |
| show user_session number | show the number of sessions supported by the system. |