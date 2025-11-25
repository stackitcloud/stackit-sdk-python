## v0.4.0
- **Feature:** Add new enum class `PartitioningUpdateType`
- **Feature:** Add attributes `partition_by` and `partitioning` to `IntakeCatalogPatch` model class

## v0.3.0
- Validate `display_name` attribute regular expression using a field validator in model classes `CreateIntakePayload`, `CreateIntakeRunnerPayload` and `CreateIntakeUserPayload`
- Set minimum length (`12`) for `password` attribute in model class `CreateIntakeUserPayload`
- Set maximum length from `32` to `1024` for `table_name` attribute in `IntakeCatalog` and `IntakeCatalogPatch` model classes
 
## v0.2.1
- **Bugfix:** Prevent year 0 timestamp issue

## v0.2.0
- **Feature:** Add response `IntakeRunnerResponse` to `UpdateIntakeRunnerExecute` request
- **Feature:** Add response `IntakeUserResponse` to `UpdateIntakeUserExecute` request

## v0.1.2
- **Feature:** Add new field `partitioning` to `IntakeCatalog` model

## v0.1.1
- Mark attributes `max_message_size_ki_b` and `max_messages_per_hour` as optional (previously required) in `UpdateIntakeRunnerPayload` model

## v0.1.0
- **New**: STACKIT Intake module can be used to manage the STACKIT Intake. Manage your `IntakeRunners`, `Intakes` and `IntakeUsers`
