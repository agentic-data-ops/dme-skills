# Flash Storage Topics

## Alarm Management and Notification Management Commands

When an alarm is generated on the storage system, the system automatically records the information on the alarm and sends the information to associated personnel

| command group | function |
|---|---|
| alarm | Manage alarms and event notifications, including notification receivers, SMTP servers, alarm masking, and event configuration. |
| event | Query and manage operation logs (event records). |

## Basic Operation Commands

Basic commands are used to execute basic command line interface (CLI) operations including querying the online help information on a command, viewing and modifying command CLI settings, checking and exporting command execution history, and exiting the CLI.

| command group | function |
|---|---|
| base | Perform basic CLI operations, including bond port routes, user password changes, CLI history, and system/task queries. |

## Container Management Commands

Container management commands are used for container deployment, management, and usage. The functions of this type of commands include activating, re-activating, deploying, starting, stopping, and querying the container service, adding and querying container nodes, as well as installing, querying, modifying, and deleting container applications.

| command group | function |
|---|---|
| container_application | Manage container applications, including deployment, configuration, and query. |
| container_node | Query container node information. |
| container_service | Manage container services, including activation, deployment, and configuration. |

## Data Protect Management Commands

Data protection management commands functionally covers complete data protection functions provided by the storage system. Those functions can improve data redundancy and reduce data loss risks.

| command group | function |
|---|---|
| consistency_group | Manage consistency groups for remote replication and disaster recovery, including creation, modification, splitting, and synchronization. |
| device_manager | Configure device manager settings, including cipher suites, web configuration, and REST message return types. |
| dr_star | Manage DR Star disaster recovery functionality, including creation, enabling/disabling, and member management. |
| fs_hyper_metro_domain | Manage file system HyperMetro domains for synchronous replication between file systems. |
| fs_snapshot | Manage file system snapshots and HyperCDP, including creation, restoration, and deletion. |
| hyper_copy | Manage HyperCopy clone relationships and consistency groups for local data replication. |
| hyper_metro_consistency_group | Manage HyperMetro consistency groups for synchronous remote replication. |
| hyper_metro_domain | Manage HyperMetro domains, including quorum servers and domain creation. |
| hyper_metro_pair | Manage HyperMetro pairs for synchronous replication between storage systems. |
| kmc | Manage the key management center (KMC) and key service, including key backup and testing. |
| kmm | Test system trust (key management module). |
| lun_snapshot | Manage LUN snapshots and HyperCDP (continuous data protection), including snapshots, consistency groups, and schedules. |
| quorum_server_for_server | Manage quorum servers used for HyperMetro arbitration. |
| quorum_server_link | Add quorum server links. |
| remote_device | Manage remote devices for remote replication, including link and white list configuration. |
| remote_replication | Manage remote replication relationships between storage systems. |
| snapshot_group | Manage snapshot consistency group membership. |
| vstore_pair | Manage vStore pairs for HyperMetro and remote replication between vStores. |

## Hardware Management Commands

Hardware management commands are used to query and modify hardware parameters. Hardware includes controllers, caches, power modules, interface modules, ports, fan modules, expansion modules, BBUs, engines, disk enclosures, hard disks, and DBs.

| command group | function |
|---|---|
| bbu | Query the status of the backup battery unit (BBU). |
| configuration_data | Export the device configuration data. |
| controller | Configure and query controller settings, such as service sessions and I/O information. |
| disk | Manage disk operations, including media scanning, precopy, routine tests, and SSD route switching. |
| dns_zone | Manage DNS zones, including creation, modification, and deletion. |
| enclosure | Manage enclosures and network planes, including port/route configuration and enclosure location/light control. |
| expansion_module | Query expansion module information. |
| failover_group | Manage failover groups for link failover, including bond, Ethernet, and VLAN port membership. |
| fan | Query cooling unit and fan status. |
| interface_module | Manage interface modules, including power on/off and configuration. |
| logical_port | Manage logical ports, including creation, routes, failover, and VLAN configuration. |
| port | Manage ports (FC, Ethernet, RoCE), bond ports, and IP/route configuration. |
| power_supply | Query power supply status. |
| running_data | Export running data for diagnostics. |
| support | Manage support and maintenance functions, including user modes, diagnostics, and protocol services. |
| vlan | Manage VLANs, including creation, modification, and deletion. |

## License Management Commands

License files are authority credentials for value-added functions such as snapshot, remote replication, clone, and SmartQoS. License management commands are used to import and query the license files.

| command group | function |
|---|---|
| license | Manage device licenses, including import, export, and query. |

## Storage Domain Management Commands

Storage space management commands functionally involve the entire process of configuring and using storage space. Those commands can create and manage storage pools, create LUNs in storage pools, create mapping views, map LUNs to hosts for utilization, and configure the commands used by the SmartQoS functions.

| command group | function |
|---|---|
| GUARANTEED_CAPACITY_INFO | Configure and query the effective capacity (guaranteed capacity) information. |
| TGT | Manage device mappings (host LUN IDs) and mapping switch settings. |
| cifs_service | Configure and query CIFS file sharing services and connections. |
| disk_destroy_data | Destroy data on disks (disk erase). |
| disk_domain | Manage disk domains, including disk addition, domain creation, rekeying, and redundancy recovery. |
| file_system | Manage file systems, including creation, modification, cloning, and HyperCDP schedules. |
| host | Manage hosts and their initiators, including creation, modification, and mapping queries. |
| host_group | Manage host groups, including adding or removing hosts and querying mappings. |
| initiator | Manage initiators (FC, iSCSI, NVMe over RoCE), including creation, modification, and deletion. |
| lun | Manage LUNs and LUN consistency groups, including creation, modification, deletion, and LUN takeover. |
| lun_group | Manage LUN groups, including adding or removing LUNs and querying mappings. |
| mapping_view | Manage mapping views by associating host groups, LUN groups, and port groups. |
| ndmp_service | Manage the NDMP service for tape backup, including configuration, users, and service restart. |
| nfs_service | Configure and query NFS service settings. |
| port_group | Manage port groups, including adding or removing ports and querying mappings. |
| qos | Manage SmartQoS policy minimum guaranteed resources. |
| quota | Manage file system quotas, including creation, modification, and deletion. |
| quota_tree | Manage quota trees (directories) for file system quotas. |
| remote_resource | Query remote LUN resources and their link status. |
| resource_user | Manage resource users and identity mapping (Unix/Windows users, groups, and identity mapping rules). |
| share | Manage CIFS/NFS shares and share permissions, including home directory rules. |
| share_permission | Manage NFS share permissions. |
| smart_cache | Manage SmartCache pools and partitions for SSD caching acceleration. |
| smart_migration | Manage LUN migration for relocating data between storage pools. |
| smart_qos | Manage SmartQoS policies for service quality control. |
| smartqos | Manage SmartQoS policy attachments to hosts and file systems. |
| space | Manage storage space and protection groups, including the recycle bin. |
| storage_pool | Manage storage pools, including creation, disk addition, and modification. |
| vstore | Manage vStores for multi-tenant storage, including creation and view configuration. |

## Storage Performance Monitoring Management Commands

Storage performance management commands are used to enable or disable system performance statistical functions and the querying function for storage performance statistics. Those commands can configure and query the following items: status of the performance statisticsswitch, performance statistical policies, performance statistics on ports, LUNs, links, hard disks, storage pools, snapshots, remote replication tasks, and hosts, performance file dumping, and performance statistics export.

| command group | function |
|---|---|
| performance | Query and manage performance statistics, including thresholds, retention strategies, and per-object performance data. |

## Storage System Management Commands

Storage system management commands are used to configure and query the storage system's running information. The command functions include setting iSCSI initiators and targets, modifying Simple Network Management Protocol (SNMP) settings, upgrading the storage system, querying and modifying the common system settings such as the time and name.

| command group | function |
|---|---|
| audit_strategy | Configure and query the audit log strategy. |
| call_home | Manage Call Home and remote support services, including user contacts and support agreements. |
| dns_server | Configure and query DNS server settings. |
| isns | Manage iSNS server settings. |
| snmp | Manage SNMP settings, including communities, users, versions, and ports. |
| system | Manage system-level settings, including time, NTP, name, description, containers, and power control. |
| target | Manage iSCSI targets, including creation, modification, and name configuration. |
| upgrade | Query upgrade packages and redundant links. |
| version | Query the device version information. |

## Storage System Security Management Commands

The storage system provides multiple storage security functions including the access authentication for Lightweight Directory Application Protocol (LDAP) domains and the whitelist mechanism. This prevents unauthorized access to the storage system for improved system security.

| command group | function |
|---|---|
| certificate | Manage device certificates and certificate revocation lists (CRLs), including import, export, and automatic update. |
| certificate_management | Configure and query the CA server used for certificate management. |
| domain | Manage authentication domains (AD, LDAP, NIS), including configuration, monitoring, and testing. |
| ldap | Manage LDAP authentication configuration. |
| security_rule | Manage security rules and NAS security settings. |

## User Management Commands

User management commands are used to create or delete users, change or initialize user passwords, force users to go offline, and query user information.

| command group | function |
|---|---|
| role | Manage user roles and their permissions. |
| safe_strategy | Manage password and security policies, including weak password management. |
| ssh | Manage SSH host keys, including deletion and import. |
| sso | Configure and query SSO (single sign-on) settings. |
| user | Manage device users, including creation, lock/unlock, and RADIUS authentication. |
| user_mode | Manage user mode switching (enabled state). |
