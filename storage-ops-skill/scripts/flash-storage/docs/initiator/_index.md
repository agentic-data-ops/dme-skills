# initiator

Manage initiators (FC, iSCSI, NVMe over RoCE), including creation, modification, and deletion.

| command | function |
|---|---|
| add host nvme_over_roce_initiator | add an NVMe over RoCE initiator to a host. |
| change initiator | modify the attributes associated with an initiator including the Challenge Handshake Authentication Protocol (CHAP) status, initiator alias, and multipathing mode. Also, it can be used to replace initiators. |
| change iscsi initiator_name | change the name of an iSCSI initiator configured for the storage system. |
| change iscsi initiator_name_v2 | change the name of an iSCSI initiator configured for the storage system. |
| change nvme_over_roce_initiator general | modify the attributes of an initiator, including its alias and NVMe qualified name (NQN), as well as replace an initiator. |
| create initiator fc | create Fibre Channel initiators. You can enable hosts to access storage resources of the storage system using created initiators. |
| create initiator iscsi | create Internet Small Computer System Interface (iSCSI) initiators. You can enable hosts to access storage resources of the storage system using created initiators. |
| create nvme_over_roce_initiator general | create an NVMe over RoCE initiator so that a host can access the storage system resources through the initiator. |
| delete initiator fc | delete Fibre Channel initiators. You can disable hosts from accessing the storage resources of the storage system by running this command. |
| delete initiator iscsi | delete Internet Small Computer Systems Interface (iSCSI) initiators. You can disable hosts from accessing the storage resources of the storage system by running this command. |
| delete nvme_over_roce_initiator general | delete an NVMe over RoCE initiator. After the deletion, the host can no longer access the storage system resources through the initiator. |
| remove host nvme_over_roce_initiator | remove an NVMe over RoCE initiator from a host. |
| show initiator | query details on host initiators configured for the storage system. |
| show iscsi initiator_name | query the names of iSCSI initiators configured for the storage system. |
| show iscsi initiator_name_v2 | query the names of iSCSI initiators configured for the storage system. |
| show nvme_over_roce_initiator general | query information about NVMe over RoCE initiators added to hosts in the storage system. |
| show port nvme_over_roce_initiator | view the NVMe qualified name (NQN) information about all NVMe over RoCE initiators that are mapped to a port. |