import logging
from datetime import datetime
import pytz
from typing import Dict

# Set up logging
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

# File handler for logging to a file
file_handler = logging.FileHandler('orchestration_logic.log')
file_handler.setLevel(logging.DEBUG)
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
file_handler.setFormatter(formatter)
logger.addHandler(file_handler)

# Stream handler for logging to the console
stream_handler = logging.StreamHandler()
stream_handler.setLevel(logging.INFO)  # Set this to logging.INFO to only show info logs on the console
stream_handler.setFormatter(formatter)
logger.addHandler(stream_handler)

def extract_flow_info(status: Dict) -> str:
    code = status['details'].get('code', 'Unknown')
    description = status['details'].get('description', 'No description available')
    state_name = status['details'].get('state_name', 'Unknown state')
    start_time = status.get('start_time')

    if start_time:
        start_time_obj = datetime.strptime(start_time, '%Y-%m-%dT%H:%M:%S.%f%z')
        start_time_formatted = start_time_obj.strftime('%Y-%m-%d %H:%M:%S %z')
        time_elapsed = datetime.now(pytz.utc) - start_time_obj  # Use pytz.utc for timezone
        time_elapsed_str = str(time_elapsed).split('.')[0]  # Remove microseconds
    else:
        start_time_formatted = 'No start time available'
        time_elapsed_str = 'N/A'

    action_status = status['details'].get('action_statuses', [])
    action_info = ''
    
    if action_status:
        action = action_status[-1]  
        action_info = f"Action: {action.get('status', 'Unknown status')}, "
        action_details = action.get('details', {})
        # action_info += f"Type: {action_details.get('type', 'Unknown type')}, "
        # action_info += f"Label: {action_details.get('label', 'No label')}, "
        action_info += f"Status: {action_details.get('status', 'No status')}"

    log_entry = f"Code: {code}, Description: {description}, State: {state_name}, Start Time: {start_time_formatted}, Time Elapsed: {time_elapsed_str}, {action_info}"
    return log_entry