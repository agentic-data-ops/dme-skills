# change user_mode current_mode


##### Function

The **change user_mode current_mode** command is used to switch a user view. This command is used when you want to switch from the user view to the developer or engineer view.

##### Format

**change user_mode current_mode** user_mode=?

##### Parameters

| Parameter | Description | Value |
|---|---|---|
| user_mode=? | View that you want to enter. | The value can be "developer" or "engineer", where: <br>"developer": developer view.<br>"engineer": engineer view.<br> If the error message (^) is displayed after entering "developer" or "engineer" and pressing "Tab" or "Enter", the switch to the enter view is not supported. |

##### Usage Guidelines

None

##### Example

Enter the developer view.

```text
admin:/>change user_mode current_mode user_mode=developer
DANGER: You are about to switch to the developer view. Commands in this view must be run under the guidance of R&D engineers. You can choose whether to run this command. If you run this command to switch to the developer view, it means that you know risks of running commands in the developer view. Device vendors are not responsible for any loss or damage caused to the user or others by running commands in the developer view.
1. Running the command in the developer view may cause system reset, restart, offline, service interruption, data loss, and data inconsistency.
2. Running the command in the developer view may cause the performance to decrease.
3. Running the command in the developer view to delete or remove configurations may have impact on the service and data.
4. Running the command in the developer view may cause system alarms.
Suggestion: Run this command under the guidance of R&D engineers.
Have you read danger alert message carefully?(y/n)y
Are you sure you really want to perform the operation?(y/n)y
developer:/>
```

Enter the engineer view.

```text
admin:/>change user_mode current_mode user_mode=engineer
engineer:/>
```

##### System Response

None
