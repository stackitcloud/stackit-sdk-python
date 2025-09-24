## v0.6.0
- **Feature**: Add attribute `labels` to `LoadBalancer`, `CreateLoadBalancerPayload`, `UpdateLoadBalancerPayload` model classes
- **Feature**: Add attribute `waf_config_name` to `Listener` model class

## v0.5.0
- **Version**: Minimal version is now python 3.9

## v0.4.0
- **Feature:** Add new field `load_balancer_security_group` in `LoadBalancer`, `CreateLoadBalancerPayload` and `UpdateLoadBalancerPayload` Models

## v0.3.1
- **Internal:** Improve deserializing and error types

## v0.3.0 (2025-06-12)
- **Feature:** Add new fields `disable_target_security_group_assignment` and `target_security_group` in `LoadBalancer`, `CreateLoadBalancerPayload` and `UpdateLoadBalancerPayload` Models

## v0.2.1 (2025-06-02)
- **Improvement:** Adjusted `GetQuotaResponse` and `RESTResponseType` message

## v0.2.0 (2025-05-14)
- **Feature:** New field `Path` for `Rule`

## v0.1.2 (2025-05-09)
- **Feature:** Update user-agent header

## v0.1.1 (2025-05-05)
- **Feature:** Switch to beta2 API

## v0.1.0 (2025-03-18)
- **New**: Client for managing the ALB service
