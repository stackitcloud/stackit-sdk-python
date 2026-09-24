import os
import sys
import time
from uuid import UUID

from stackit.automation.api.default_api import DefaultApi
from stackit.automation.models.automation_schedule_trigger import (
    AutomationScheduleTrigger,
)
from stackit.automation.models.automation_triggers import AutomationTriggers
from stackit.automation.models.create_volume_automation_payload import (
    CreateVolumeAutomationPayload,
)
from stackit.automation.models.partial_update_volume_automation_payload import (
    PartialUpdateVolumeAutomationPayload,
)
from stackit.automation.models.volume_automation_input import VolumeAutomationInput
from stackit.core.configuration import Configuration


def main():
    # Credentials are read from the credentialsFile in
    # `~/.stackit/credentials.json` or the env
    # STACKIT_SERVICE_ACCOUNT_KEY_PATH / STACKIT_SERVICE_ACCOUNT_KEY
    config = Configuration()
    automation_api = DefaultApi(config)

    # the id of your STACKIT project, read from env var for this example
    project_id = os.getenv("PROJECT_ID")
    if not project_id:
        print("Environment variable 'PROJECT_ID' not found.", file=sys.stderr)
        return

    # the region which should be used to interact with the automation service
    region = "eu01"

    try:
        # ///////////////////////////////////////////////////////
        # //          V O L U M E   T E M P L A T E S          //
        # ///////////////////////////////////////////////////////

        # list all available volume templates
        list_templates = automation_api.list_volume_templates(project_id=project_id, region=region)
        print("Listing volume templates:")
        if list_templates.items:
            for template in list_templates.items:
                print(f"* Template ID: {template.id}")

        # if there is a next_page_token, fetch next page of results
        while list_templates.next_page_token:
            list_templates = automation_api.list_volume_templates(
                project_id=project_id,
                region=region,
                page_token=list_templates.next_page_token,
            )
            print("Listing next page of volume templates:")
            if list_templates.items:
                for template in list_templates.items:
                    print(f"* Template ID: {template.id}")

        if not list_templates.items:
            print("No volume templates found.")
            return

        # get one specific volume template
        template = automation_api.get_volume_template(
            project_id=project_id,
            region=region,
            template_id=str(list_templates.items[0].id),
        )
        print("\n\nFetched volume template:")
        print(f"* Template ID: {template.id}")
        print(f"* Template name: {template.name}")
        print(f"* Template description: {template.description}")

        # ///////////////////////////////////////////////////////
        # //         V O L U M E   A U T O M A T I O N         //
        # ///////////////////////////////////////////////////////

        # create a volume automation with a schedule trigger
        volume_automation = automation_api.create_volume_automation(
            project_id=project_id,
            region=region,
            create_volume_automation_payload=CreateVolumeAutomationPayload(
                description="Creates daily recovery points for all volumes with specified label",
                name="My Daily Volume Recovery Point Creation Automation",
                template_id=UUID(str(template.id)),
                input=VolumeAutomationInput(
                    kind="VolumeRecoveryPointManagement",
                    additional_properties={
                        "inheritVolumeLabels": True,
                        "recoveryPointLabels": {
                            "exampleLabelKey1": "exampleLabelValue1",
                        },
                        "snapshotRetentionPolicy": {
                            "kind": "count",
                            "value": 2,
                        },
                        "volumeLabelSelector": "myLabelkey1=myLabelValue,myLabelKey2=myOtherLabelValue",
                    },
                ),
                triggers=AutomationTriggers(
                    schedule=AutomationScheduleTrigger(
                        rrule="DTSTART;TZID=Europe/Sofia:20200803T023000\nRRULE:FREQ=DAILY;INTERVAL=1",
                    ),
                ),
            ),
        )
        print("\n\nCreated volume automation:")
        print(f"* Automation ID: {volume_automation.id}")
        print(f"* Automation name: {volume_automation.name}")
        print(f"* Automation description: {volume_automation.description}")

        # list all volume automations
        list_automations = automation_api.list_volume_automations(project_id=project_id, region=region)
        print("\n\nListing volume automations:")
        if list_automations.items:
            for automation in list_automations.items:
                print(f"* Automation ID: {automation.id}")

        # if there is a next_page_token, fetch next page of results
        while list_automations.next_page_token:
            list_automations = automation_api.list_volume_automations(
                project_id=project_id,
                region=region,
                page_token=list_automations.next_page_token,
            )
            print("\nListing next page of volume automations:")
            if list_automations.items:
                for automation in list_automations.items:
                    print(f"* Automation ID: {automation.id}")

        # update an automation
        updated_automation = automation_api.partial_update_volume_automation(
            project_id=project_id,
            region=region,
            automation_id=str(volume_automation.id),
            partial_update_volume_automation_payload=PartialUpdateVolumeAutomationPayload(
                description="Updated daily recovery points automation",
                name="Updated Daily Volume Recovery Point Creation Automation",
            ),
        )
        print("\n\nUpdated volume automation:")
        print(f"* Automation ID: {updated_automation.id}")
        print(f"* Automation name: {updated_automation.name}")
        print(f"* Automation description: {updated_automation.description}")

        # get one specific volume automation
        fetched_automation = automation_api.get_volume_automation(
            project_id=project_id,
            region=region,
            automation_id=str(volume_automation.id),
        )
        print("\n\nFetched updated volume template:")
        print(f"* Automation ID: {fetched_automation.id}")
        print(f"* Automation name: {fetched_automation.name}")
        print(f"* Automation description: {fetched_automation.description}")

        # ///////////////////////////////////////////////////////
        # //                E X E C U T I O N S                //
        # ///////////////////////////////////////////////////////

        # trigger an automation execution
        created_execution = automation_api.create_volume_execution(
            project_id=project_id,
            region=region,
            automation_id=str(volume_automation.id),
        )
        print("\n\nTriggered volume automation execution:")
        print(f"* Execution ID: {created_execution.id}")
        print(f"* Execution status: {created_execution.status}")

        # wait for the automation execution to complete
        while str(created_execution.status).upper() in ["PENDING", "RUNNING"]:
            print("* Waiting for automation execution to complete ...")
            time.sleep(2)
            created_execution = automation_api.get_volume_execution(
                project_id=project_id,
                region=region,
                automation_id=str(volume_automation.id),
                execution_id=str(created_execution.id),
            )
        print("* Automation execution completed")

        # list all executions of a specific volume automation
        list_executions = automation_api.list_volume_executions(
            project_id=project_id,
            region=region,
            automation_id=str(volume_automation.id),
        )
        print("\n\nListing executions of the volume automation:")
        if list_executions.items:
            for execution in list_executions.items:
                print(f"* Execution ID: {execution.id}")

        # ///////////////////////////////////////////////////////
        # //                  D E L E T I O N                  //
        # ///////////////////////////////////////////////////////

        # trigger deletion of the created volume automation
        print("\n\nDeleting created volume automation")
        automation_api.delete_volume_automation(
            project_id=project_id,
            region=region,
            automation_id=str(volume_automation.id),
        )
        print(f'* Successfully deleted automation with ID "{volume_automation.id}"')

    except Exception as e:
        print(f"Exception when calling AutomationApi: {e}", file=sys.stderr)


if __name__ == "__main__":
    main()
