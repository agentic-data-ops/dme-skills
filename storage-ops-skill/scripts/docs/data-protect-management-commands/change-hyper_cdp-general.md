# change hyper_cdp general


##### Function

The **change hyper_cdp general** command is used to modify the name and restoration speed of a HyperCDP object.

##### Format

**change hyper_cdp general** cdp_id=? { name=? \| restore_speed=? }

##### Parameters

| Parameter | Description | Value |
|---|---|---|
| cdp_id=? | ID of a HyperCDP object. | The value is an integer ranging from 0 to 1999999.<br>To obtain the value, run "show hyper_cdp general". |
| name=? | New name of a HyperCDP object. | The value contains 1 to 31 characters including letters, digits, hyphens (-), underscores (_), and periods (.). |
| restore_speed=? | Restoration speed. | The value can be: <br>"Low": 0 to 5 MB/s.<br>"Middle": 10 to 20MB/s.<br>"High": 50 to 70 MB/s.<br>"Highest": The speed of a single engine reaches 1 GB/s when host services exist and 1.5 GB/s when no host services exist.<br> The default value is "Middle". |

##### Usage Guidelines

The new name of a HyperCDP object must be different from the names of all existing HyperCDP objects.

##### Example

Change the name of HyperCDP object "1" to "cdpName" and the restoration speed to "High".

```text
admin:/>change hyper_cdp general cdp_id=1 name=cdpName restore_speed=High
WARNING: You are about to modify the rate of restoring the HyperCDP object to "High" or "Highest". This operation may cause heavy service pressure and decrease the read/write performance of the host.
Suggestions: Perform this operation during off-peak hours.
Have you read warning message carefully?(y/n)y
Are you sure you really want to perform the operation?(y/n)y
Command executed successfully.
```

##### System Response

None
