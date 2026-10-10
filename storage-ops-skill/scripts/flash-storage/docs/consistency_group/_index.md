# consistency_group

Manage consistency groups for remote replication and disaster recovery, including creation, modification, splitting, and synchronization.

| command | function |
|---|---|
| add consistency_group remote_replication | add a remote replication pair to a consistency group. |
| add consistency_group remote_replication_delay | add the remote replication into the consistency group after the initial synchronization of the remote replication is complete. |
| change consistency_group general | modify information about a consistency group. |
| change consistency_group mode | change the replication mode of the remote replication consistency group. |
| change consistency_group split | split consistency groups. |
| change consistency_group synchronize | synchronize appointed consistency groups. |
| create consistency_group asynchronization | create asynchronous consistency groups. |
| create consistency_group protect_group | create a remote replication consistency group for a protection group. |
| create consistency_group synchronization | create a synchronous consistency group. You can centrally manage multiple synchronous remote replication pairs by running this command. |
| create consistency_group verification_session | verify consistency groups. |
| delete consistency_group | delete consistency groups. |
| remove consistency_group remote_replication | delete remote replication pairs from a consistency group. |
| show consistency_group available_remote_replication | query for the remote replication tasks that can be added to a consistency group. |
| show consistency_group general | query details of consistency groups. |
| show consistency_group member | query details on members of a consistency group task. |
| swap consistency_group | implement primary/secondary switchover for existing remote replication tasks in a consistency group. |