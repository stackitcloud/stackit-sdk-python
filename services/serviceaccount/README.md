# stackit.serviceaccount
API to manage Service Accounts and their Access Tokens.

### System for Cross-domain Identity Management (SCIM)
Service Account Service offers SCIM APIs to query state. The SCIM protocol was created as standard for
 automating the exchange of user identity information between identity domains, or IT systems. Service accounts
 are be handled as indentites similar to SCIM users. A custom SCIM schema has been created: `/ServiceAccounts`

#### Syntax
##### Attribute operators
| OPERATOR | DESCRIPTION              |
|----------|--------------------------|
| eq       | equal                    |
| ne       | not equal                |
| co       | contains                 |
| sw       | starts with              |
| ew       | ends with                |

##### Logical operators
| OPERATOR | DESCRIPTION              |
|----------|--------------------------|
| and      | logical \"and\"            |
| or       | logical \"or\"             |

##### Grouping operators
| OPERATOR | DESCRIPTION              |
|----------|--------------------------|
| ()       | precending grouping      |

##### Example
```
filter=email eq \"my-service-account-aBc2defg@sa.stackit.cloud\"
filter=email ne \"my-service-account-aBc2defg@sa.stackit.cloud\"
filter=email co \"my-service-account\"
filter=name sw \"my\"
filter=name ew \"account\"
filter=email co \"my-service-account\" and name sw \"my\"
filter=email co \"my-service-account\" and (name sw \"my\" or name ew \"account\")
```

#### Sorting

> Sorting is optional

| PARAMETER | DESCRIPTION                          |
|-----------|--------------------------------------|
| sortBy    | attribute response is ordered by     |
| sortOrder | 'ASCENDING' (default) or 'DESCENDING'|

#### Pagination

| PARAMETER    | DESCRIPTION                                  |
|--------------|----------------------------------------------|
| startIndex   | index of first query result, default: 1      |
| count        | maximum number of query results, default: 100|


This package is part of the STACKIT Python SDK. For additional information, please visit the [GitHub repository](https://github.com/stackitcloud/stackit-sdk-python) of the SDK.


## Installation & Usage
### pip install

```sh
pip install stackit-serviceaccount
```

Then import the package:
```python
import stackit.serviceaccount
```

## Getting Started

[Examples](https://github.com/stackitcloud/stackit-sdk-python/tree/main/examples) for the usage of the package can be found in the [GitHub repository](https://github.com/stackitcloud/stackit-sdk-python) of the SDK.