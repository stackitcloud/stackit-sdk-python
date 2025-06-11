# stackit.auditlog
API Endpoints to retrieve recorded actions and resulting changes in the system.

### Audit Logging
Changes on organizations, folders and projects and respective cloud resources are logged and collected in the audit 
log.

### API Constraints
The audit log API allows to download messages from the last 90 days. The maximum duration that can be queried at 
once is 24 hours. Requests are rate limited - the current maximum is 1 request per second.

For more information, please visit [https://support.stackit.cloud/servicedesk](https://support.stackit.cloud/servicedesk)

This package is part of the STACKIT Python SDK. For additional information, please visit the [GitHub repository](https://github.com/stackitcloud/stackit-sdk-python) of the SDK.


## Installation & Usage
### pip install

```sh
pip install stackit-auditlog
```

Then import the package:
```python
import stackit.auditlog
```

## Getting Started

[Examples](https://github.com/stackitcloud/stackit-sdk-python/tree/main/examples) for the usage of the package can be found in the [GitHub repository](https://github.com/stackitcloud/stackit-sdk-python) of the SDK.