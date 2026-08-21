## v0.7.0
- **Feature:** Add support for managing BGP filters and BGP filter rules on gateways (new API methods and models)
- **Feature:** Add new optional field `inbound_filter_id` to `BGPTunnelConfig`
- **Feature:** Add new optional field `network_config` (`NetworkConfig`) to `Gateway`, `GatewayResponse`, `CreateGatewayPayload` and `UpdateGatewayPayload`
- **Feature:** Add `sha2_512` as allowed value for `integrity_algorithms` in `Phase`
- **Improvement:** Add `RESOURCE_IN_USE` as allowed value for `reason` in `ApiErrorDetail`

## v0.6.0
- **Chore:** Bump minimum Python version to 3.10
- **Chore:** Update dependencies

## v0.5.0
- **Fix:** Flag `local_asn` field as required for `BGPGatewayConfig`
- **Feature:** Add `error_message` field to `GatewayStatusResponse`
- **Improvement:** Add description that `RoutingType` can only be set at the creation

## v0.4.0
- **Feature:** Add new optional attribute `labels` to `CreateGatewayConnectionPayload` and `UpdateGatewayConnectionPayload`

## v0.3.0
- **Breaking Change:** switch from `v1beta` version to `v1` version of the API

## v0.2.0
- **Feature:** regenerate with openapi-generator v7.22.0

## v0.1.0
- Initial publication of STACKIT Python SDK module for STACKIT VPN service
