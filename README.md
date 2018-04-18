# noid-api

RESTful API for creating and managing NOID (Nice Opaque Identifier), the persistent and opaque identifier scheme created by John Kunze, California Digital Library.  For more information on NOID see the [UCOP documentation](https://confluence.ucop.edu/display/Curation/NOID).


# Contributing to noid-api

* Check out the latest master to make sure the feature hasn't been implemented or the bug hasn't been fixed yet
* Check out the issue tracker to make sure someone already hasn't requested it and/or contributed it
* Fork the project
* Start a feature/bugfix branch
* Commit and push until you are happy with your contribution
* Make sure to add tests

# Usage

| Method | URI | Action |
|------- | --- | ------ |
| GET | /noid/api/v1.0/identifier | Retrieve list of identifiers
| GET | /noid/api/v1.0/identifier/[identifier] | Retrieve identifier metadata
| POST | /noid/api/v1.0/identifier | Mint identifier
| PUT | /noid/api/v1.0/identifier/[identifier] | Update identifier metadata
| DELETE | /noid/api/v1.0/identifier/[identifier] | Delete identifier
| GET | /noid/api/v1.0/user/ | Retrieve list of user IDs
| GET | /noid/api/v1.0/user/[userid] | Retrieve user profile
| POST | /noid/api/v1.0/user/[userid] | Create user
| DELETE | /noid/api/v1.0/identifier/[userid] | Delete user
