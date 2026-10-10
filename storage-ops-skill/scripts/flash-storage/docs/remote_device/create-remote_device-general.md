# create remote_device general


##### Function

The **create remote_device general** command is used to create remote devices. You must create a remote device by running this command before you can effortlessly perform remote replication tasks between the storage system and remote device.

##### Format

**create remote_device general** array_type=? remote_user=? { link_type=? { link_id=? \| local_eth_logical_port=? \| remote_ip=? } } { local_rep_port_group_id=? \| local_rep_port_group_name=? } { remote_rep_port_group_name=? \| remote_rep_port_group_id=? }

##### Parameters

| Parameter | Description | Value |
|---|---|---|
| array_type=? | Type of a remote device. | The value can be: <br>"replication": The remote device is from Huawei. |
| remote_user=? | User name for logging in to the remote device. | The value consists of 5 to 32 ASCII characters, including digits, letters, and underscores (_), and must start with a letter. To create a required remote device administrator, run the "create user" command on the remote device. |
| link_type=? | Link type. | The value can be: <br>"FC": The remote device and the local device connect to each other through Fibre Channel links.<br>"IP": The remote device and the local device connect to each other through IP links. |
| link_id=? | ID of a Fibre Channel link. This parameter is valid only when link_type=? is set to "FC". | To obtain the value, run "show remote_device link". |
| local_eth_logical_port=? | Name of a logical port. This parameter is valid only when link_type=? is set to "IP". | To obtain the value, run "show logical_port general". |
| remote_ip=? | IP address of a remote device. This parameter is valid only when link_type=? is set to "IP". | - |
| local_rep_port_group_name=? | Name of a local replication port group. | To obtain the value, run "show rep_port_group general". |
| remote_rep_port_group_name=? | Name of a remote replication port group. | To obtain the value, run "show rep_port_group general". |
| local_rep_port_group_id=? | ID of a local replication port group. | To obtain the value, run "show rep_port_group general". |
| remote_rep_port_group_id=? | ID of a remote replication port group. | To obtain the value, run "show rep_port_group general". |

##### Usage Guidelines

Description of accounts used for communication authentication between remote devices:

-   You need to create an authentication account on remote devices rather than local devices.
-   The authentication account must be a remote device administrator. Run the "create user" command to create one and set the role ID to 12.

##### Example

Create a remote device from Huawei, where the local replication port group ID is "1", the remote replication port group ID is "1", and the user name for logging in to the remote device is "huawei".

```text
admin:/>create remote_device general array_type=replication remote_user=huawei link_type=FC link_id=0 local_rep_port_group_id=1 remote_rep_port_group_id=1
WARNING: You are about to create a remote device.
Before performing this operation, ensure that the replication port group have been created and ports have been correctly selected. If no port is configured for the remote device, replication services cannot be configured for the remote device.
Suggestion: Configure the correct port for the remote device.
Have you read warning message carefully?(y/n)y
Are you sure you really want to perform the operation?(y/n)y
Password:**********
Command executed successfully.
```

##### System Response

None
