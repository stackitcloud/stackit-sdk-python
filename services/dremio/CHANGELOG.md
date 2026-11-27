## v0.4.0
- **Breaking Change:** Switch from regional to global API server URL (region can't be set via `Configuration` / env-variable anymore).

## v0.3.0
- **Chore:** Bump minimum Python version to 3.11
- **Chore:** Support Python version 3.15
- **Chore:** Update dependencies

## v0.2.0

- **Feature:** Add `acl` field to models `CreateDremioInstancePayload`, `DremioResponse`, and `UpdateDremioInstancePayload`
- **Breaking Change:** `DremioResponse` now requires an `acl` field; constructing an instance without it will raise a validation error

## v0.1.0

- **New**: STACKIT Dremio module can be used to manage STACKIT Dremio instances and users.
