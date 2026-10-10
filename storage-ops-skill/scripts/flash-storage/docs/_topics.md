# Flash Storage Topics

## Alarm Management and Notification Management Commands

When an alarm is generated on the storage system, the system automatically records the information on the alarm and sends the information to associated personnel

- alarm
- event

## Basic Operation Commands

Basic commands are used to execute basic command line interface (CLI) operations including querying the online help information on a command, viewing and modifying command CLI settings, checking and exporting command execution history, and exiting the CLI.

- base

## Container Management Commands

Container management commands are used for container deployment, management, and usage. The functions of this type of commands include activating, re-activating, deploying, starting, stopping, and querying the container service, adding and querying container nodes, as well as installing, querying, modifying, and deleting container applications.

- container_application
- container_node
- container_service

## Data Protect Management Commands

Data protection management commands functionally covers complete data protection functions provided by the storage system. Those functions can improve data redundancy and reduce data loss risks.

- consistency_group
- device_manager
- dr_star
- fs_hyper_metro_domain
- fs_snapshot
- hyper_copy
- hyper_metro_consistency_group
- hyper_metro_domain
- hyper_metro_pair
- kmc
- kmm
- lun_snapshot
- quorum_server_for_server
- quorum_server_link
- remote_device
- remote_replication
- snapshot_group
- vstore_pair

## Hardware Management Commands

Hardware management commands are used to query and modify hardware parameters. Hardware includes controllers, caches, power modules, interface modules, ports, fan modules, expansion modules, BBUs, engines, disk enclosures, hard disks, and DBs.

- bbu
- configuration_data
- controller
- disk
- dns_zone
- enclosure
- expansion_module
- failover_group
- fan
- interface_module
- logical_port
- port
- power_supply
- running_data
- support
- vlan

## License Management Commands

License files are authority credentials for value-added functions such as snapshot, remote replication, clone, and SmartQoS. License management commands are used to import and query the license files.

- license

## Storage Domain Management Commands

Storage space management commands functionally involve the entire process of configuring and using storage space. Those commands can create and manage storage pools, create LUNs in storage pools, create mapping views, map LUNs to hosts for utilization, and configure the commands used by the SmartQoS functions.

- GUARANTEED_CAPACITY_INFO
- TGT
- cifs_service
- disk_destroy_data
- disk_domain
- file_system
- host
- host_group
- initiator
- lun
- lun_group
- mapping_view
- ndmp_service
- nfs_service
- port_group
- qos
- quota
- quota_tree
- remote_resource
- resource_user
- share
- share_permission
- smart_cache
- smart_migration
- smart_qos
- smartqos
- space
- storage_pool
- vstore

## Storage Performance Monitoring Management Commands

Storage performance management commands are used to enable or disable system performance statistical functions and the querying function for storage performance statistics. Those commands can configure and query the following items: status of the performance statisticsswitch, performance statistical policies, performance statistics on ports, LUNs, links, hard disks, storage pools, snapshots, remote replication tasks, and hosts, performance file dumping, and performance statistics export.

- performance

## Storage System Management Commands

Storage system management commands are used to configure and query the storage system's running information. The command functions include setting iSCSI initiators and targets, modifying Simple Network Management Protocol (SNMP) settings, upgrading the storage system, querying and modifying the common system settings such as the time and name.

- audit_strategy
- call_home
- dns_server
- isns
- snmp
- system
- target
- upgrade
- version

## Storage System Security Management Commands

The storage system provides multiple storage security functions including the access authentication for Lightweight Directory Application Protocol (LDAP) domains and the whitelist mechanism. This prevents unauthorized access to the storage system for improved system security.

- certificate
- certificate_management
- domain
- ldap
- security_rule

## User Management Commands

User management commands are used to create or delete users, change or initialize user passwords, force users to go offline, and query user information.

- role
- safe_strategy
- ssh
- sso
- user
- user_mode

## Acronyms and Abbreviations

|           |                                                    |
|-----------|----------------------------------------------------|
| **A**     |                                                    |
| **AD**    | Active Directory                                   |
| **ASCII** | American Standard Code for Information Interchange |
|           |                                                    |
| **C**     |                                                    |
| **CHAP**  | Challenge Handshake Authentication Protocol        |
| **CLI**   | Command-line Interface                             |
|           |                                                    |
| **D**     |                                                    |
| **DB**    | Database                                           |
|           |                                                    |
| **F**     |                                                    |
| **FC**    | Fiber Channel                                      |
| **FC-AL** | Fiber Channel Arbitrated Loop                      |
|           |                                                    |
| **G**     |                                                    |
| **GE**    | Gigabit Ethernet                                   |
| **GUI**   | Graphical User Interface                           |
|           |                                                    |
| **H**     |                                                    |
| **HBA**   | Host Bus Adapter                                   |
|           |                                                    |
| **I**     |                                                    |
| **IP**    | Internet Protocol                                  |
| **IOPS**  | Input/Output Operations Per Second                 |
| **IQN**   | iSCSI Qualified Name                               |
| **ISCSI** | Internet Small Computer Systems Interface          |
| **ISNS**  | Internet Storage Name Service                      |
|           |                                                    |
| **K**     |                                                    |
| **KVM**   | Keyboard, Video and Mouse                          |
|           |                                                    |
| **L**     |                                                    |
| **LAN**   | Local Area Network                                 |
| **LDAP**  | Lightweight Directory Access Protocol              |
| **LUN**   | Logical Unit Number                                |
|           |                                                    |
| **M**     |                                                    |
| **MAC**   | Medium Access Control                              |
|           |                                                    |
| **R**     |                                                    |
| **RAID**  | Redundant Array of Independent Disks               |
|           |                                                    |
| **S**     |                                                    |
| **SAN**   | Storage Area Network                               |
| **SAS**   | Serial Attached SCSI                               |
| **SCSI**  | Small Computer System Interface                    |
| **SFP**   | Small Form-Factor Pluggable                        |
| **SMTP**  | Simple Mail Transfer Protocol                      |
| **SMI-S** | Storage Management Interface Specification         |
| **SNMP**  | Simple Network Management Protocol                 |
| **SP**    | Server Pack                                        |
| **SSD**   | Solid State Drive                                  |
| **SVP**   | Service Processor                                  |
|           |                                                    |
| **U**     |                                                    |
| **USM**   | User-based Security Model                          |
|           |                                                    |
| **W**     |                                                    |
| **WORM**  | Write Once Read Many                               |
| **WWN**   | World-Wide Name                                    |

