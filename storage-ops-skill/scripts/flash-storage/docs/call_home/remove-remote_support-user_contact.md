# remove remote_support user_contact


##### Function

The **remove remote_support user_contact** command is used to delete the contacts of eSerivce.

##### Format

**remove remote_support user_contact** contact_id=?

##### Parameters

| Parameter  | Description      | Value                                                                                     |
|------------|------------------|-------------------------------------------------------------------------------------------|
| contact_id | User contact ID. | The value is an integer from 0 to 4. Press Ctrl+A to view the list of available contacts. |

##### Usage Guidelines

This command is used to delete the contacts of eService. You can query the added contacts of a storage system by running the "show remote_support user_contact" command.

##### Example

Delete the contacts of eService.

```text
admin:/>remove remote_support user_contact contact_id=0
CAUTION: You are about to delete a eService contact. The technical support center notifies users of the device health status through the contact information configured for the eService. If you delete all eService contacts, the technical support center cannot obtain the contact information.
Suggestion: Before performing this operation, ensure that the contact does not need to receive the device health notification provided by the eService. To receive the device health notification, reserve at least one contact.
Have you read warning message carefully?(y/n)y
Are you sure you really want to perform the operation?(y/n)y
Command executed successfully.
```

##### System Response

None
