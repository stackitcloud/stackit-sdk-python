## v0.3.0

- **Breaking Change:** `list_provider_options` now returns a single `ProviderOptionsResponse` instead of `List[ProviderOptionsResponse]`, matching the endpoint's actual (non-array) response
- **Breaking Change:** Removal of `security_group` field from `RuleResponse` model
- **Breaking Change:** `type` field in `RuleResponse` model now validates against a fixed set of values (`ACL`, `PublicIP`, `SecurityRule`, `SecurityGroup`); previously any string was accepted
- **Feature:** Add `ref_id` and `stateful` fields to `RuleResponse` model
- **Feature:** Add `remote_security_group_id` and `stateful` fields to `CreateRulePayload` model

## v0.2.0

- **Chore:** Bump minimum Python version to 3.11 
- **Chore:** Support Python version 3.15
- **Chore:** Update dependencies

## v0.1.0

- **New**: STACKIT Unified Firewall (UFW) module
