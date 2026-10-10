# change dr_star general


##### Function

The **change dr_star general** command is used to modify the attributes of a DR Star trio.

##### Format

**change dr_star general** dr_star_id=? { swap_strategy=? \| swap_silent_time=? \| name=? }

##### Parameters

| Parameter | Description | Value |
|---|---|---|
| dr_star_id | DR Star trio ID. | To obtain the value, run "show dr_star general". |
| swap_strategy | Switchover policy. | The value can be "manual" or "automatic", where: <br>"manual": manual switchover.<br>"automatic": automatic switchover. |
| name | DR Star trio name. | The value contains 1 to 255 ASCII characters, including digits, letters, hyphens (-), underscores (_), and periods (.), and can only start with a digit or a letter. |
| swap_silent_time | Switchover silence time. | The value ranges from 0 to 30, expressed in minutes. |

##### Usage Guidelines

Run the "**change dr_star general** dr_star_id=? { swap_strategy=? \| swap_silent_time=? \| name=? }" command to modify the name, switchover policy, or switchover silence time of a DR Star trio.

##### Example

Modify the attributes of DR Star trio whose ID is "200bc79b99520000", including modifying the switchover policy to automatic and the silence time to one minute.

```text
admin:/>change dr_star general dr_star_id=200bc79b99520000 swap_strategy=automatic swap_silent_time=1
Command executed successfully.
```

##### System Response

None
