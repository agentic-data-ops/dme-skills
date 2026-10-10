# Storage Performance Monitoring Management Commands

Storage performance management commands are used to enable or disable system performance statistical functions and the querying function for storage performance statistics. Those commands can configure and query the following items: status of the performance statisticsswitch, performance statistical policies, performance statistics on ports, LUNs, links, hard disks, storage pools, snapshots, remote replication tasks, and hosts, performance file dumping, and performance statistics export.

## performance

- change performance restore: configure the policies for dumping the performance statistics of the storage system.
- change performance retention_strategy: set the retention policy for performance data.
- change performance statistic_enabled: configure the performance statistics switch. Run this command to enable or disable the performance statistics function.
- change performance strategy: configure the policies of collecting system performance statistics.
- change performance threshold: change the thresholds of performance statistical object parameters.
- delete performance file: delete historical performance statistical files.
- export performance file: export historical performance statistics files.
- show performance bond_port: display the performance statistics on bonded ports. Use this command when you want to check the real-time performance statistics of bonded ports.
- show performance cifs_service: query performance statistics of a CIFS service. Running this command analyzes performance statistics of a CIFS service in real time.
- show performance consistency_group: query the performance statistics on a remote replication consistency group. Run this command to analyze the performance statistics on a remote replication consistency group in real time.
- show performance controller: query the performance statistics on a controller of the storage system. Run this command to analyze the performance statistics on a controller in real time.
- show performance disk: query the performance statistics of a disk. Running this command analyzes the performance statistics of a disk in real time.
- show performance disk_domain: query the performance statistics on a disk domain. Run this command to analyze the performance statistics on a disk domain in real time.
- show performance elink: query performance statistics of heterogeneous links. Running this command analyzes real-time performance statistics of heterogeneous links.
- show performance file: query historical performance statistics files.
- show performance file_system: query performance statistics of a file system.
- show performance host: query the performance statistics on a host. Run this command to analyze the performance statistics on a host in real time.
- show performance ip_port: query the performance statistics on a back-end port. Run this command to analyze the performance statistics on a port in real time.
- show performance link: query the performance statistics on a link. Run this command to analyze the performance statistics on a link in real time.
- show performance logical_port: query performance statistics of a logical port. Running this command analyzes performance statistics of a logical port in real time.
- show performance lun: query performance statistics on a logical unit number (LUN). Run this command to analyze the performance statistics on a LUN in real time.
- show performance lun_migration: query the performance statistics of a LUN migration task. Run this command to analyze the performance statistics of a LUN migration task in real time.
- show performance lun_priority: query the real-time performance statistics of LUNs with a specified I/O priority.
- show performance mode: query the performance statistical modes of the current system.
- show performance nfs_service: query performance statistics on an nfs_service. Run this command to analyze the performance statistics on an nfs_service in real time.
- show performance nfsv3: query the performance statistics for NFSv3. Run this command to analyze the performance statistics for NFSv3 in real time.
- show performance nfsv41: query the performance statistics of NFSv4. When you need to analyze the performance statistics of NFSv4 in real time, run this command.
- show performance port: query the performance statistics on a port. Run this command to analyze the performance statistics on a port in real time.
- show performance remote_device: query the real-time performance statistics on a remote device.
- show performance remote_replication: query the performance statistics of a remote replication pair. Run this command to analyze the performance statistics of a remote replication pair in real time.
- show performance restore: query the configuration policies for dumping performance statistics.
- show performance retention_strategy: query the retention policy for performance data.
- show performance smartqos_policy: query the performance statistics of SmartQoS policies.
- show performance smb2: query performance statistics of the SMB2 protocol. Running this command analyzes performance statistics of SMB2 in real time.
- show performance snapshot: query the performance statistics on a snapshot task. Run this command to analyze the performance statistics on a snapshot task in real time.
- show performance statistic_enabled: query the status of the performance statistics switch.
- show performance storage_pool: query the performance statistics on a storage pool. Run this command to analyze the performance statistics on a storage pool in real time.
- show performance strategy: query existing performance statistical policies for the storage system.
- show performance system: query the performance statistics of the storage system. Run this command to analyze the performance statistics of the system in real time.
- show performance threshold: query the thresholds of performance statistical object parameters.
