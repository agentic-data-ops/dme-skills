# Storage System Management Commands

Storage system management commands are used to configure and query the storage system's running information. The command functions include setting iSCSI initiators and targets, modifying Simple Network Management Protocol (SNMP) settings, upgrading the storage system, querying and modifying the common system settings such as the time and name.

## audit_strategy

- change audit_log_strategy: modify the audit log strategy.
- show audit_log_strategy: query audit log strategy.

## call_home

- add remote_support user_contact: add the contacts of eService.
- change call_home authenticate: authenticate the Call Home service.
- change call_home general: set the Call Home service.
- change remote_support agreement: sign the letter of authorization.
- change remote_support general: configure basic information about eService.
- change remote_support user_contact: set a user's contact information.
- clear remote_support proxy_user_password: clear the user name and password of the eService proxy server.
- import remote_support agreement: upload the photo of a letter of authorization.
- import remote_support smtp_publickey: upload the public key of the CHS mail channel.
- remove remote_support user_contact: delete the contacts of eSerivce.
- show call_home general: query information about Call Home functions.
- show remote_support agreement: query the letter of authorization and its status.
- show remote_support general: query basic configuration information about eService.
- show remote_support technical_support_center: query information about the technical support center.
- show remote_support user_contact: query a user's contact information.
- test call_home service: test whether the Call Home service is normal.

## dns_server

- change dns_server general: modify information about the management DNS server of a disk array.
- remove dns_server general: remove a DNS server.
- show dns_server general: check the management DNS server in a disk array.
- test dns_server general: test the connectivity of a DNS server.

## isns

- change isns server_ip: set the IP address of the Internet Storage Name Service (iSNS) server.
- delete isns server_ip: delete the IP address of the Internet Storage Name Service (iSNS) server.
- show isns server_ip: query the IP address of the Internet Storage Name Service (iSNS) server.

## snmp

- add snmp cache: add an SNMP cache object. No cache object is added by default.
- add snmp usm: add a USM user.
- change snmp cache: change the interval of updating the cache data of an SNMP cache object.
- change snmp community: change the SNMP read-only community string and read-write community string. SNMPv1 and SNMPv2c use community strings for authentication purposes. Run this command if you need to change community strings for improved system security.
- change snmp port: set the port number of the SNMP service.
- change snmp safe_strategy: change the security policy of the SNMP service.
- change snmp usm: modify the configuration of a USM user.
- change snmp version: set the status of the SNMPv1 and SNMPv2c protocols and the switch status of the SNMP unique controller enclosure ID function.
- delete snmp usm: delete a USM user.
- remove snmp cache: remove an SNMP cache object.
- show snmp cache: show the current SNMP cache object.
- show snmp context_name: query the Simple Network Management Protocol (SNMP) context name of the storage system.
- show snmp engineid: query the SNMP controller enclosure ID of a controller.
- show snmp port: query the port number of the SNMP service.
- show snmp safe_strategy: query the security policy of the SNMP service.
- show snmp usm: query the configuration of the USM user.
- show snmp version: check the status of the SNMPv1 and SNMPv2c protocols as well as status of the SNMP unique controller enclosure ID switch.

## system

- add ntp_server general: add an NTP server for time synchronization.
- change cli: modify command line interface (CLI) settings. Use this command when you need to modify the CLI timeout period, capacity display mode, output paging mode, command execution confirmation switch, or performance statistics display mode.
- change nas_service active: activate the NAS feature service for the first time.
- change ntp_server config: configure the time synchronization function. Run this command if you want the storage system to synchronize its time with that of an NTP server.
- change system description: change the storage system's description.
- change system dns_load_balance: enable or disable the DNS load balancing function and configure the load balancing policy.
- change system location: change the geographical location of a storage system.
- change system media_scan: modify the settings of disk media scanning.
- change system name: change the storage system's name.
- change system ntp: configure the NTP. Run this command if you want the storage system to synchronize its time with that of an NTP server.
- change system server_port: modify port information of the system.
- change system time: change the storage system's time. If the storage system's time is incorrect, you can run this command to change it.
- change system timezone: change the time zone where the storage system resides in. If the displayed time zone is different from the actual local time zone, you can run this command to change the time zone.
- change system write_policy: set the write protection switch and the period for a controller to run before the write policy is switched to write protection.
- change user_session number: change the number of sessions supported by the system.
- delete container_image: delete an application image package imported by a user.
- delete helm_chart: delete an application chart package imported by a user.
- import container_image: import an application image software package.
- import helm_chart: import an application Helm chart package.
- poweroff system: power off the storage system. Running this command causes service interruption.
- reboot system: restart the storage system. Running this command causes service interruption.
- remove ntp_server general: delete an NTP server used for time synchronization.
- show bst enabled: display the global BST function.
- show container_image general: query information about application image packages imported by a user.
- show helm_chart general: query information about the application chart packages imported by a user.
- show ntp status: query the NTP status.
- show ntp_server general: query the time synchronization function settings.
- show system client_name: query the address information about a storage system maintenance terminal.
- show system dns_load_balance: query information about DNS load balancing.
- show system dst: query the daylight saving time (DST) settings of the storage system.
- show system manufactory: query the vendor and brand of the storage system.
- show system media_scan: query the disk media scanning information, including the running status and execution period.
- show system ntp: query the Network Time Protocol (NTP) settings.
- show system power_consumption: query system power consumption in real time.
- show system server_port: query the port information about a specific service.
- show system timezone: query the time zone where the storage system resides.
- show system write_policy: display the current cache write policy of the system.
- show user_session number: show the number of sessions supported by the system.

## target

- change iscsi target: modify information about the iSCSI link between two disk arrays.
- change iscsi target_name: change the name of the iSCSI target configured for the storage system.
- create iscsi target: create a target over iSCSI links. Run this command if the LUN copy or remote replication is to be configured between a storage system and a remote device over iSCSI links. (The command format with local_control_id is not recommended.)
- delete iscsi target: delete an iSCSI target.
- show iscsi target: query information about the target connected to iSCSI links.
- show iscsi target_name: query the name of the iSCSI target configured for the storage system.

## upgrade

- show upgrade package: query details of the upgrade package.
- show upgrade redundant_link: query whether each controller has front-end redundant links.

## version

- show version all: query the version information on the storage system's controllers, expansion modules, and BBUs.
