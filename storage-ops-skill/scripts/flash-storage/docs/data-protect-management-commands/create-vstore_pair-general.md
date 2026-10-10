# create vstore_pair general


##### Function

The **create vstore_pair general** command is used to create a vStore pair.

##### Format

**create vstore_pair general** rep_type=? local_vstore_id=? remote_vstore_id=? domain_id=?

##### Parameters

| Parameter | Description | Value |
|---|---|---|
| rep_type=? | Type of a vStore pair. | The value is "hyper_metro", where: <br>""hyper_metro"": HyperMetro vStore pair. |
| local_vstore_id=? | ID of the local vStore. | You can run the "show vstore" command to obtain the value. |
| remote_vstore_id=? | ID of the remote vStore. | You can obtain the value of this parameter by running the "show vstore" command on the remote end. |
| domain_id=? | ID of a HyperMetro domain. | You can run the "show fs_hyper_metro_domain general" command to obtain the value. |

##### Usage Guidelines

None

##### Example

Create a vStore pair.

```text

admin:/>create vstore_pair general rep_type=hyper_metro local_vstore_id=1 remote_vstore_id=1 domain_id=9ce37477ca790100
CAUTION: You are about to create a NAS HyperMetro vStore pair for the vStore. This operation may interrupt services of the local non-HyperMetro file systems of the vStore.
Suggestion: Ensure that the HyperMetro relationship will be configured for all file systems of the vStore.
Do you wish to continue?(y/n)y
Command executed successfully.

```

##### System Response

None
