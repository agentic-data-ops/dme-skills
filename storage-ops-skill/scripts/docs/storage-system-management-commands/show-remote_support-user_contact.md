# show remote_support user_contact


##### Function

The **show remote_support user_contact** command is used to query a user's contact information.

##### Format

**show remote_support user_contact**

##### Parameters

None

##### Usage Guidelines

This command is used to query a user's contact information. You can run the "change remote_support user_contact" command to change the information.

##### Example

Query a user's contact information.

```text
admin:/>show remote_support user_contact

Contact ID           : 0
First Name           : Feng
Last Name            : Wang
Email                : foo@bar.com
Country Calling Code : +86
Mobile               : 1234567
---------------------------
Contact ID           : 1
First Name           : Abc
Last Name            : Zhang
Email                : abc@bar.com
Country Calling Code : +86
Mobile               : 7654321
```

##### System Response

The following table describes the parameter meanings.

| Parameter            | Meaning                                   |
|----------------------|-------------------------------------------|
| Contact ID           | User contact ID.                          |
| First Name           | First name of the user contact.           |
| Last Name            | Last name of the user contact.            |
| Email                | Email address of the user contact.        |
| Country Calling Code | Country calling code of the user contact. |
| Mobile               | Mobile phone number of the user contact.  |
