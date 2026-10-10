# change remote_support user_contact


##### Function

The **change remote_support user_contact** command is used to set a user's contact information.

##### Format

**change remote_support user_contact** contact_id=? { first_name=? \| last_name=? \| email=? \| country_calling_code=? \| mobile=? } \*

##### Parameters

| Parameter            | Description                          | Value                                                                                                            |
|----------------------|--------------------------------------|------------------------------------------------------------------------------------------------------------------|
| contact_id           | User contact ID.                     | The value is an integer from 0 to 4. Press Ctrl+A to view the list of available contacts.                        |
| first_name           | First name of the contact.           | The value contains 1 to 63 characters including letters, digits, underscores (\_), hyphens (-), and periods (.). |
| last_name            | Last name of the contact.            | The value contains 1 to 63 characters including letters, digits, underscores (\_), hyphens (-), and periods (.). |
| email                | Email address of the contact.        | The value consists of 5 to 127 ASCII characters.                                                                 |
| country_calling_code | Country calling code of the contact. | The value contains 1 to 31 characters including digits and symbols (\* \# + - ( )).                              |
| mobile               | Mobile phone number of the contact.  | The value contains 1 to 31 characters including digits and symbols (\* \# + - ( )).                              |

##### Usage Guidelines

This command is used to set a user's contact information. A user's contact information can be queried by running the "show remote_support user_contact" command.

##### Example

Set a user's contact information.

```text
admin:/>change remote_support user_contact contact_id=0 first_name=Feng last_name=Wang email=foo@bar.com country_calling_code=+86 mobile=1234567
Command executed successfully.
```

##### System Response

None
