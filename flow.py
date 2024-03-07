"""
This file contains a single LivePublication Action Provider flow using Gladier & Globus interfaces. 
It serves as an experimental testbench for the LivePublication CLI.
"""
from logger_config import logger
import json

# Importing Gladier
from gladier import GladierBaseClient, generate_flow_definition

def run_flow():
    """
    This function runs the LivePublication Action Provider flow using Gladier & Globus interfaces.
    """
    @staticmethod
    @generate_flow_definition
    class Example_Flow(GladierBaseClient):
        """
        Note the order of the tools - this defines the order of the flow.
        """
        gladier_tools = [
            'gladier_components.transfer_1.transfer_1',
            'gladier_components.LPAP.LPAP',
            'gladier_components.transfer_2.transfer_2'
        ]

    example_flow_client = Example_Flow()
    logger.debug(json.dumps(example_flow_client.get_flow_definition(), indent=2))
    

run_flow()