# hyper_copy

Manage HyperCopy clone relationships and consistency groups for local data replication.

Manage HyperCopy clone relationships and consistency groups for local data replication.

| command | function |
|---|---|
| add clone_consistency_group clone | add clone pairs to a specified clone consistency group. Use this command if consistency management is required for clone pairs. |
| add hyper_copy_consistency_group hyper_copy | add HyperCopy pairs to a specified HyperCopy consistency group. Use this command if consistency management is required for HyperCopy pairs. |
| change clone general | modify clone pair settings. |
| change clone restore | start, stop, pause, and resume full or differential reverse synchronization of the clone pair. |
| change clone synchronize | start, stop, pause, and continue clone pair synchronization. |
| change clone_consistency_group general | modify clone consistency group settings. |
| change clone_consistency_group restore | set reverse synchronization parameters of a clone consistency group. |
| change clone_consistency_group synchronize | start, pause, continue, and stop member synchronization of a clone consistency group. |
| change hyper_copy general | modify HyperCopy pair settings. |
| change hyper_copy restore | start, stop, pause, and resume full or differential reverse synchronization of the HyperCopy pair. |
| change hyper_copy synchronize | start, stop, pause, and continue HyperCopy pair synchronization. |
| change hyper_copy_consistency_group general | modify HyperCopy consistency group settings. |
| change hyper_copy_consistency_group restore | set reverse synchronization parameters of a HyperCopy consistency group. |
| change hyper_copy_consistency_group synchronize | start, pause, continue, and stop member synchronization of a HyperCopy consistency group. |
| create clone general | create a clone pair. |
| create clone relation | create a clone pair. |
| create clone_consistency_group | create a clone consistency group. |
| create hyper_copy local | create a HyperCopy pair. |
| create hyper_copy_consistency_group | create a HyperCopy consistency group. |
| delete clone | delete a clone pair. |
| delete clone_consistency_group | delete a clone consistency group. |
| delete hyper_copy | delete a HyperCopy pair. |
| delete hyper_copy_consistency_group | delete a HyperCopy consistency group. |
| remove clone_consistency_group clone | remove clone pairs from a specified clone consistency group. Use this command if consistency management is not required for clone pairs. |
| remove hyper_copy_consistency_group hyper_copy | remove HyperCopy pairs from a specified HyperCopy consistency group. Use this command if consistency management is not required for HyperCopy pairs. |
| show clone general | query clone pair information. |
| show clone_consistency_group clone | query information about members in a clone consistency group. |
| show clone_consistency_group general | query the basic information about a clone consistency group. |
| show hyper_copy general | query HyperCopy pair information. |
| show hyper_copy_consistency_group general | query the basic information about a HyperCopy consistency group. |
| show hyper_copy_consistency_group hyper_copy | query information about members in a HyperCopy consistency group. |