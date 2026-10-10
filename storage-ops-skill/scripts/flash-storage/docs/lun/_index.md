# lun

| command | function |
|---|---|
| add lun_consistency_group lun | add a member LUN to a specified LUN consistency group. Use this command if consistency management is required for LUNs. |
| change lun | modify LUN settings, including the name and capacity. |
| change lun_clone split | start and stop splitting a clone pair or modify the split speed of a clone pair. |
| change lun_consistency_group general | modify the properties of a LUN consistency group. |
| change lun_takeover disable_switch_path | forbid the specified LUN's paths to be switched back to the source array and to allow the LUN to be used as the source LUN for online takeover. |
| change lun_takeover enhance_switch | set the enhanced masquerading switch of a specified LUN. |
| change lun_takeover finish_switch_path | confirm that the host paths of the specified LUN have been switched to the paths between the host and the target disk array. |
| change lun_workload_type general | modify the settings of an application type, including the name, I/O size, and so on. |
| change workload_type general | modify parameters of an application type, including "name", "io_size", and so on. |
| create lun | create LUNs. After creating a storage pool, you must divide its storage space into one or multiple LUNs so that resources can be more appropriately allocated to application servers. |
| create lun_clone general | create clones. You can create an identical and usable point-in-time duplicate for a data object by running this command. |
| create lun_consistency_group | create a LUN consistency group. |
| create lun_takeover general | create takeover LUNs. |
| create lun_workload_type general | create a workload type for LUNs. After creating a workload type, you can choose it when you are creating LUNs. Through this method the LUN space parameter can be reasonably set. |
| create workload_type general | create an application type for LUNs or for file systems. |
| delete lun | delete LUNs. |
| delete lun_consistency_group | delete a LUN consistency group. |
| delete lun_workload_type general | delete an application type. |
| delete workload_type general | delete an application type. |
| remove lun_consistency_group lun | remove a member LUN from a specified LUN consistency group. Use this command when consistency protection is not required for a specified LUN. |
| remove lun_takeover general | delete the information about a takeover LUN. |
| show disk_domain lun | query information about LUNs in a specified disk domain. |
| show hyper_cdp_schedule lun | query information about LUNs in a HyperCDP schedule. |
| show hyper_cdp_schedule lun_consistency_group | query information about LUN consistency groups in a HyperCDP schedule. |
| show lun general | query information about LUNs in the storage system. |
| show lun hyper_metro_pair | query information about LUNs for which HyperMetro is configured. |
| show lun lun_group | query information about the LUN group that is associated with a LUN. |
| show lun mapping_view | query information about a mapping view related to a specified LUN. |
| show lun protection | query protect information about the specified LUNs of the storage system. |
| show lun_clone available_lun | query the information about all LUNs that can serve as clone source LUNs. |
| show lun_clone general | query clone information. |
| show lun_consistency_group general | query information about LUN consistency groups in the storage system. |
| show lun_consistency_group lun | query information about LUNs in a LUN consistency group. |
| show lun_consistency_group snapshot_consistency_group | query information about snapshot consistency groups related to LUN consistency groups. |
| show lun_takeover general | query information about takeover LUNs of the storage system. |
| show lun_workload_type general | query information about application types in the storage system. |
| show protect_group lun | query information about LUNs in a protection group. |
| show workload_type general | query information about existing application types of the storage system. |