# show initiator


##### Function

The **show initiator** command is used to query details on host initiators configured for the storage system.

##### Format

**show initiator** \[ host_id=? \| isfree=? \| initiator_type=? \[ wwn=? \| iscsi_iqn_name=? \] \] \*

**show initiator** \[ host_name=? \| isfree=? \| initiator_type=? \[ wwn=? \| iscsi_iqn_name=? \] \] \*

##### Parameters

| Parameter | Description | Value |
|---|---|---|
| host_id=? | ID of a host. | To obtain the value, run "show host general". |
| host_name=? | Host name. | To obtain the value, run "show host general". |
| isfree=? | Whether an initiator is in the free status. | The value can be "yes" or "no", where: <br>"yes": An initiator is free and can be added to a host.<br>"no": An initiator has been engaged by a host and cannot be added to another host. |
| initiator_type=? | Type of an initiator. | The value can be "iSCSI" or "FC", where: <br>"iSCSI": indicates initiators.<br>"FC": indicates Fibre Channel initiators. |
| wwn=? | World Wide Name (WWN) of a Fibre Channel initiator. This parameter is valid only when "initiator_type=?" is set to "FC". | To obtain the value, run "show initiator" without parameters. |
| iscsi_iqn_name=? | iSCSI qualified name (IQN) of an iSCSI initiator. This parameter is valid only when "initiator_type=?" is set to "iSCSI". | To obtain the value, run "show initiator" without parameters. |

##### Usage Guidelines

-   To query details on all host initiators, run "**show initiator**".
-   To query details on initiators for a specific host, run "**show initiator** host_id=?".
-   To query the information on free or engaged initiators, run "**show initiator** is_free=?".
-   To query details on a specific type of initiators, run "**show initiator** initiator_type=? \[ wwn=? \| iscsi_iqn_name=? \]" (You can query information about a specific initiator by WWN or IQN).

##### Example

Query information about all the host initiators.

```text
admin:/>show initiator
iSCSI IQN  Running Status  Free  Alias  Host ID  CHAP Enabled  CHAP User  Multipath Type  CHAP Target User  Discovery Chap Type  Normal Chap Type  Failover Mode  Path Type  Special Mode Type  Host IP  Host Name
---------  --------------  ----  -----  -------  ------------  ---------  --------------  ----------------  -------------------  ----------------  -------------  ---------  -----------------  -------  ---------
124214     Offline         No    --     0        No            --         Default         --                --                   --                --             --         --                          host0
```

Query information about the initiators of the host whose ID is "0".

```text
admin:/>show initiator host_id=0

iSCSI IQN  Running Status  Free  Alias  Host ID  CHAP Enabled  CHAP User  Multipath Type  CHAP Target User  Discovery Chap Type  Normal Chap Type  Failover Mode  Path Type  Special Mode Type  Host IP  Host Name
---------  --------------  ----  -----  -------  ------------  ---------  --------------  ----------------  -------------------  ----------------  -------------  ---------  -----------------  -------  ---------
124214     Offline         No    --     0        No            --         Default         --                --                   --                --             --         --                          host0
```

Query information about the initiators of the host whose name is "host1".

```text

admin:/>show initiator host_name=host1

iSCSI IQN  Running Status  Free  Alias  Host ID  CHAP Enabled  CHAP User  Multipath Type  CHAP Target User  Discovery Chap Type  Normal Chap Type  Failover Mode  Path Type  Special Mode Type  Host IP  Host Name
---------  --------------  ----  -----  -------  ------------  ---------  --------------  ----------------  -------------------  ----------------  -------------  ---------  -----------------  -------  ---------
124214     Offline         No    --     0        No            --         Default         --                --                   --                --             --         --                          host1

```

Query information about all the free initiators.

```text
admin:/>show initiator isfree=yes

iSCSI IQN         Running Status  Free  Alias  Host ID  CHAP Enabled  CHAP User  Multipath Type  CHAP Target User  Discovery Chap Type  Normal Chap Type  Failover Mode  Path Type  Special Mode Type  Host IP  Host Name
----------------  --------------  ----  -----  -------  ------------  ---------  --------------  ----------------  -------------------  ----------------  -------------  ---------  -----------------  -------  ---------
4578963215478122  Offline         Yes   --     --       No            --         Default         --                --                   --                --             --         --                          --
```

Query details on iSCSI initiators.

```text
admin:/>show initiator initiator_type=iSCSI
iSCSI IQN                                      Running Status  Free  Alias  Host ID  CHAP Enabled  CHAP User  Multipath Type  CHAP Target User  Discovery Chap Type  Normal Chap Type  Failover Mode  Path Type  Special Mode Type  Host IP  Host Name
---------------------------------------------  --------------  ----  -----  -------  ------------  ---------  --------------  ----------------  -------------------  ----------------  -------------  ---------  -----------------  -------  ---------
iqn.1996-04.de.suse12-sp3-client-8.46.123.172  Offline         Yes   --     --       No            --         Default         --                --                   --                --             --         --                          --
iqn.1996-04.de.suse12-sp3-client-8.46.123.174  Offline         Yes   --     --       No            --         Default         --                --                   --                --             --         --                          --
```

##### System Response

The following table describes the parameter meanings.

| Parameter | Meaning |
|---|---|
| WWN | WWN of a Fibre Channel initiator. |
| iSCSI IQN | IQN of an iSCSI initiator. |
| Running Status | Operating status of an initiator. |
| Free | Whether an initiator is free. |
| Alias | Initiator alias. |
| Host ID | Host ID. |
| CHAP Enabled | Whether CHAP authentication is enabled. |
| CHAP User | CHAP user name for the target to authenticate the initiator. |
| Multipath Type | Multipathing mode. <br>Default: Huawei multipathing software is used.<br>Third-party: Third-party multipathing software is used. |
| Host IP | Host IP address. |
| CHAP Target User | CHAP user name for the initiator to authenticate the target. |
| Discovery Chap Type | CHAP type during the "Discovery" phase. |
| Normal Chap Type | CHAP type during the "Normal" phase. |
| Noop In Interval | Interval of iSCSI targets sending keepalive packets to initiators. |
| Failover Mode | Failover mode of the initiator. <br>Old ALUA: ALUA of an earlier version.<br>Common ALUA: common ALUA.<br>No ALUA: ALUA not used.<br>Special Mode: special mode. |
| Path Type | Path type of the initiator. <br>Optimized: optimized path.<br>Non-optimized: non-optimized path. |
| Special Mode Type | Special mode type of the initiator. <br>Mode0: special mode 0.<br>Mode1: special mode 1.<br>Mode2: special mode 2.<br>Mode3: special mode 3. |
| Host Name | Name of a host. |
