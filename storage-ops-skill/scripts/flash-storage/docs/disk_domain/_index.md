# disk_domain

Manage disk domains, including disk addition, domain creation, rekeying, and redundancy recovery.

Manage disk domains, including disk addition, domain creation, rekeying, and redundancy recovery.

| command | function |
|---|---|
| add disk_domain disk | add disks to a disk domain. |
| change disk_domain general | modify the properties of a disk domain, including the disk domain name, hot spare strategy, switch status of the LUN mapping table repair function, and similarity-based deduplication execution level. |
| change disk_domain rekey | manually update the AK according to the disk domain. |
| create disk_domain | create a disk domain. |
| delete disk_domain | delete a disk domain. |
| show bst configuration | check the BST switch status. |
| show disk_domain available_capacity | query the usable capacity of a specific RAID level in a disk domain. |
| show disk_domain general | query information about disk domains. |
| show disk_domain redundancy_recovery_task | query status of a redundancy recovery task in a disk domain. |
| show disk_domain task | query the status of a reconstruction or pre-copy task in a disk domain. |
| show disk_remove_task general | query the status of a capacity reduction task of a disk domain. |