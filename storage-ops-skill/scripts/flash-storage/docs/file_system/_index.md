# file_system

Manage file systems, including creation, modification, cloning, and HyperCDP schedules.

| command | function |
|---|---|
| add hyper_cdp_schedule fs | add file systems to a HyperCDP schedule. |
| change file_system enabled | enable file system related functions, such as to enable checksum, to perform periodic snapshots, and to modify the Atime. |
| change file_system general | modify file system parameters such as the name, capacity, block size, and owning controller. |
| create file_system general | create a file system. |
| create fs_clone general | create a clone file system. |
| delete file_system general | delete file systems. |
| remove hyper_cdp_schedule fs | remove file systems from a HyperCDP schedule. |
| show file_system general | query details about file systems. |
| show file_system reduction_info | query capacity reduction information about a file system. |
| show fs_clone general | query information about a file system's child clone file system, including its ID, name, status, and associated parent file system snapshot name. |
| show hyper_cdp_schedule fs | query information about file systems in a HyperCDP schedule. |