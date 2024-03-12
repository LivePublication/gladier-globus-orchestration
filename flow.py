"""
This file contains a single LivePublication Action Provider flow using Gladier & Globus interfaces. 
It serves as an experimental testbench for the LivePublication CLI.
"""
from logger_config import logger
import json

# Importing Gladier
from gladier import GladierBaseClient, generate_flow_definition
from pprint import pprint

# Import config variables
from config import DataStoreUUID, SourceFile, DestFile

def run_flow():
    """
    This function runs the LivePublication Action Provider flow using Gladier & Globus interfaces.
    """
    @staticmethod
    @generate_flow_definition
    class Example_Flow(GladierBaseClient):
        """
        Note the order of the tools - this defines the order of the flow.
        Also, note how this comment is included within the WEP as a comment.

        These components (here called tools) are disconnected descriptions of the 
        actions which gladier will stitch together into a flow.
        When instantiating the prospective provenance, these components could be
        used as the software components of each action.
        """
        gladier_tools = [
            "gladier_tools.globus.Transfer:FromSource",
            "gladier_tools.globus.Transfer:ToDestination"
        ]

    flow_input = {
        "input": {
            # Input vars for transfer 1 (FromSource)
            "from_source_transfer_source_endpoint_id": DataStoreUUID,
            "from_source_transfer_destination_endpoint_id": DataStoreUUID,
            "from_source_transfer_source_path": SourceFile,
            "from_source_transfer_destination_path": DestFile,
            "from_source_transfer_recursive": False,
            # Input vars for transfer 2 (ToDestination)
            "to_destination_transfer_source_endpoint_id": DataStoreUUID,
            "to_destination_transfer_destination_endpoint_id": DataStoreUUID,
            "to_destination_transfer_source_path": SourceFile,
            "to_destination_transfer_destination_path": DestFile,
            "to_destination_transfer_recursive": False
        }
    }

    example_flow_client = Example_Flow()
    logger.debug(json.dumps(example_flow_client.get_flow_definition(), indent=2))

    flow = example_flow_client.run_flow(
        flow_input=flow_input,
        label="Testing gladier transfers as aliases",
    )

    action_id = flow['action_id']
    example_flow_client.progress(action_id)
    pprint(flow.result(action_id))

run_flow()