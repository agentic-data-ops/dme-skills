# change initiator


##### Function

The **change initiator** command is used to modify the attributes associated with an initiator including the Challenge Handshake Authentication Protocol (CHAP) status, initiator alias, and multipathing mode. Also, it can be used to replace initiators.

##### Format

**change initiator** initiator_type=? \[ wwn=? \] \[ iscsi_iqn_name=? \] \[ new_wwn=? \] \[ new_iscsi_iqn_name=? \] \[ alias=? \] \[ chap_enabled=? \] \[ discovery_chap_type=? \] \[ normal_chap_type=? \] \[ chap_user=? \] \[ chap_target_user=? \] \[ multipath_type=? \[ failover_mode=? \[ special_mode_type=? \] \] \[ path_type=? \] \]

##### Parameters

| Parameter | Description | Value |
|---|---|---|
| initiator_type=? | Type of an initiator. | The value can be "iSCSI" or "FC", where: <br>"iSCSI": indicates Internet Small Computer System Interface (iSCSI) initiators.<br>"FC": indicates Fibre Channel initiators. |
| wwn=? | World Wide Name (WWN) of a Fibre Channel initiator. | To obtain the value, run "show initiator". |
| iscsi_iqn_name=? | iSCSI qualified name (IQN) of an iSCSI initiator. | To obtain the value, run "show initiator". |
| chap_enabled=? | Whether or not to enable the CHAP function for iSCSI initiators. | The value can be "yes" or "no", where: <br>"yes": CHAP authentication will be enabled.<br>"no": CHAP authentication will be disabled. |
| discovery_chap_type=? | CHAP type during the iSCSI Discover phase. When "chap_enabled=?" is set to "yes", this parameter is optional. | The value can be "none", "single", or "double". |
| normal_chap_type=? | CHAP type during the iSCSI Normal phase. When "chap_enabled=?" is set to "yes", this parameter is optional. | The value can be "none", "single", or "double". |
| chap_user=? | Name of a CHAP user. This parameter is required when chap_enabled=? is set to "yes". | The value contains 4 to 223 characters (32 < ASCII code < 127) and must start with a letter or a digit. |
| chap_target_user=? | CHAP user name for the initiator to authenticate the target. When "chap_enabled=?" is set to "yes", this parameter is optional. | The value contains 4 to 223 characters (32 < ASCII code < 127) and must start with a letter or a digit. |
| alias=? | Alias of an initiator. | The value contains 1 to 31 characters including digits, letters, underscores (_), periods (.) and hyphens (-). |
| multipath_type=? | Multipathing mode. | The value can be "default" or "third-party", where: <br>default: Huawei multipathing software is used.<br>third-party: Third-party multipathing software is used.<br> The default value is "default". |
| failover_mode=? | Failover mode of the initiator. | The value can be "old_alua", "common_alua", "no_alua", or "special_mode", where: <br>old_alua: ALUA of an earlier version.<br>common_alua: common ALUA.<br>no_alua: ALUA not used.<br>special_mode: special mode.<br> The default value is "common_alua". |
| path_type=? | Path type of the initiator. | The value can be "non-optimized" or "optimized", where: <br>optimized: optimized path.<br>non-optimized: non-optimized path.<br> The default value is "optimized". |
| special_mode_type=? | Special mode type of the initiator. | The value can be "mode0", "mode1", "mode2", and "mode3", where: <br>mode0: special mode 0.<br>mode1: special mode 1.<br>mode2: special mode 2.<br>mode3: special mode 3. |
| new_wwn=? | WWN of an updated Fibre Channel initiator. | It is a hexadecimal value that contains 16 characters comprised of uppercase letters A to F, lowercase letters a to f, or digits 0 to 9, but cannot all be 0, F, or f. |
| new_iscsi_iqn_name=? | IQN of an updated iSCSI initiator. | The value contains 1 to 223 characters (32 < ASCII code < 127) and must start with a letter or a digit. |

##### Usage Guidelines

-   After CHAP authentication has been enabled, a host can access the storage system using the corresponding initiator only when the host's CHAP user name and password match with those for the storage system.
-   Upon successful update, a new initiator inherits complete features and mappings of the replaced initiator. For example, if an initiator has been allocated to a mapping view and been added to a specific host, the new initiator will be allocated to the same mapping view and also be added to the host upon successful update.
-   Running this command with chap_enabled=? set to "yes" will prompt you to type CHAP passwords in interaction mode. The passwords are subject to the following conditions:
-   Each password is case sensitive and contains 12 to 16 characters.
-   Each password must be a combination of at least three of the following items:
-   Lowercase characters;
-   Uppercase characters;
-   Numbers;
-   Special characters and the following: \` \~ ! @ \# $ % ^ & \* ( ) - \_ = + \\ \| \[ { } \] ; : ' " , \< . \> / ?;
-   Each password must be different from a user name that is either in its normal or reverse order.
-   If running this command displays "chap_enable=yes,discovery_chap_type=none,normal_chap_type=none", running this command will fail.
-   If running this command enables only unidirectional authentication, running this command with "chap_target_user" (user name for bidirectional authentication) selected will fail.
-   If running this command displays "discovery_chap_type=none,normal_chap_type=none", running this command with "chap_target_user/chap_user" selected will fail.

##### Example

Set the attributes of the Fibre Channel initiator whose WWN is "455856585f654578" as follows: Alias to "newfc" Multipathing mode to "third-party" Failover mode to "common_alua" Path type to "optimized".

```text
admin:/>change initiator initiator_type=FC wwn=455856585f654578 alias=newfc multipath_type=third-party failover_mode=common_alua path_type=optimized
DANGER: You are about to change the multipathing configuration of the initiator. This operation changes the host multipathing software's policy of managing paths of storage LUNs mapped to the host. If you do not configure the multipathing correctly, the host may have compatibility problems.
Suggestion: Before performing this operation, ensure that you know the correct configuration method clearly. In storage systems with one array or HyperMetro storage systems, all initiators mapped to the same physical host must have the same multipathing type and failover mode.
Have you read danger alert message carefully?(y/n)y
Are you sure you really want to perform the operation?(y/n)y
Command executed successfully.
```

Modify the attributes of an iSCSI initiator, where the IQN of the initiator is "iqn.01", CHAP authentication will be enabled, and the CHAP user name is "chapuser".

```text
admin:/>change initiator initiator_type=iSCSI iscsi_iqn_name=iqn.01 chap_enabled=yes chap_user=chapuser
CHAP user password:*************
Reenter password:*************
Command executed successfully.
```

Replace the Fibre Channel initiator whose WWN is "10000000c9b7bc72" with another Fibre Channel initiator whose WWN is "1234567890123456".

```text
admin:/>change initiator initiator_type=FC wwn=10000000c9b7bc72 new_wwn=1234567890123456
DANGER: You are about to modify the initiator identifier. This operation will remove and delete the specified offline initiator from the host.
Suggestion: Before performing this operation, ensure that you choose the offline initiator that has been added to the host.
Have you read danger alert message carefully?(y/n)y
Are you sure you really want to perform the operation?(y/n)y
Query old initiator.
Remove old initiator from host.
Delete old initiator.
Create or change new initiator.
Command executed successfully.
```

Modify the attributes of an iSCSI initiator, where the IQN of the initiator is "inq.1996-04.de.suse:01:ca9f3bcaf455", CHAP bidirectional authentication will be enabled, the initiator CHAP user name is "chapuser1", and the target CHAP user name is "chapuser2".

```text
admin:/>change initiator initiator_type=iSCSI iscsi_iqn_name=inq.1996-04.de.suse:01:ca9f3bcaf455 chap_enabled=yes normal_chap_type=double
CHAP target user:chapuser1
CHAP user password:*************
Reenter password:*************
CHAP target user:chapuer2
CHAP target user password:*************
Reenter password:*************
Command executed successfully.
```

##### System Response

None
