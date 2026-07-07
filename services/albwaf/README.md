# stackit.albwaf
Generate a Web Application Firewall (WAF) to use with Application Load Balancers (ALB). The name of the WAF configuration is used in the listener of the ALB. This will activate the WAF for that ALB. An ALB with a WAF can have Managed Rule Set (MRS) and in addition can have Custom Rule Group (CRG). To create a WAF one first needs to create all the configurations that are referenced in the WAF configuration. Currently this only consists of a rule configuration, which is written in Seclang. Once all configurations are created and referenced in the WAF configuration it can be used with an ALB. Currently updating a WAF configuration will not update an existing ALB until the Load Balancer VMs are restarted.


This package is part of the STACKIT Python SDK. For additional information, please visit the [GitHub repository](https://github.com/stackitcloud/stackit-sdk-python) of the SDK.


## Installation & Usage
### pip install

```sh
pip install stackit-albwaf
```

Then import the package:
```python
import stackit.albwaf
```

## Getting Started

[Examples](https://github.com/stackitcloud/stackit-sdk-python/tree/main/examples) for the usage of the package can be found in the [GitHub repository](https://github.com/stackitcloud/stackit-sdk-python) of the SDK.