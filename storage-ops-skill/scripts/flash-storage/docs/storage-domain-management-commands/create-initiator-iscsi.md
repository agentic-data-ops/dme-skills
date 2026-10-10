# create initiator iscsi


##### Function

The **create initiator iscsi** command is used to create Internet Small Computer System Interface (iSCSI) initiators. You can enable hosts to access storage resources of the storage system using created initiators.

##### Format

**create initiator iscsi** iscsi_iqn_name=? \[ alias=? \| chap_enabled=? \[ chap_user=? \] \[ discovery_chap_type=? normal_chap_type=? \] \| host_id=? \] \[ multipath_type=? \[ failover_mode=? \[ special_mode_type=? \] \] \[ path_type=? \] \] \*

##### Parameters

| Parameter | Description | Value |
|---|---|---|
| iscsi_iqn_name=? | IQN of an iSCSI initiator. | The value contains 1 to 223 characters (32 < ASCII code < 127) and must start with a letter or a digit. |
| alias=? | Alias of an initiator. | The value contains 1 to 31 characters including digits, letters, underscores (_), periods (.) and hyphens (-). |
| chap_enabled=? | Whether or not to enable the CHAP function for iSCSI initiators. | The value can be "yes" or "no", where: <br>"yes": CHAP authentication will be enabled.<br>"no": CHAP authentication will be disabled.<br> The default value is "no". |
| chap_user=? | Name of a CHAP user. This parameter is required when chap_enabled=? is set to "yes". | The value contains 4 to 223 characters (32 < ASCII code < 127) and must start with a letter or a digit. |
| discovery_chap_type=? | CHAP type during the iSCSI Discover phase. When "chap_enabled=?" is set to "yes", this parameter is optional. | The value can be: 1."none". 2."single". 3."double". |
| normal_chap_type =? | CHAP type during the iSCSI Discover phase. When "chap_enabled=?" is set to "yes", this parameter is optional. | The value can be: 1."none". 2."single". 3."double". |
| host_id=? | ID of a host. | To obtain the value, run "show host general". |
| multipath_type=? | Multipathing mode. | The value can be "default" or "third-party", where: <br>default: Huawei multipathing software is used.<br>third-party: Third-party multipathing software is used.<br> The default value is "default". |
| failover_mode=? | Failover mode of the initiator. | The value can be "old_alua", "common_alua", "no_alua", or "special_mode", where: <br>old_alua: ALUA of an earlier version.<br>common_alua: common ALUA.<br>no_alua: ALUA not used.<br>special_mode: special mode.<br> The default value is "common_alua". |
| path_type=? | Path type of the initiator. | The value can be "non-optimized" or "optimized", where: <br>optimized: optimized path.<br>non-optimized: non-optimized path.<br> The default value is "optimized". |
| special_mode_type=? | Special mode type of the initiator. | The value can be "mode0", "mode1", "mode2", and "mode3", where: <br>mode0: special mode 0.<br>mode1: special mode 1.<br>mode2: special mode 2.<br>mode3: special mode 3. |

##### Usage Guidelines

-   Running this command with chap_enabled=? set to "yes" will prompt you to type CHAP passwords in interaction mode. The passwords are subject to the following conditions:
-   Each password is case sensitive and contains 12 to 16 characters.
-   Each password must be a combination of at least three of the following items:
-   Lowercase characters
-   Uppercase characters
-   Numbers
-   Special characters and the following: \` \~ ! @ \# $ % ^ & \* ( ) - \_ = + \\ \| \[ { } \] ; : ' " , \< . \> / ?
-   Each password must be different from a user name that is either in its normal or reverse order.
-   When "chap_enabled=?" is set to "yes" and parameters "discovery_chap_type" and "normal_chap_type" are not configured, "normal_chap_type =?" is set to "single" by default.
-   Running this command with parameters "discovery_chap_type" and "normal_chap_type" not set to "double" and parameter "chap_user" selected will prompt you to type the password for the target to authenticate the initiator in interaction mode.
-   Running this command with parameters "discovery_chap_type" and "normal_chap_type" set to "double" and parameter "chap_user" selected will prompt you to type the user name (the user name setting follows the rules of "chap_user" setting) and password for the initiator to authenticate the target and those for the target to authenticate the initiator in interaction mode.

##### Example

Create the iSCSI initiator whose IQN is "iqn.01".

```text
admin:/>create initiator iscsi iscsi_iqn_name=iqn.01
Command executed successfully.
```

##### System Response

None
