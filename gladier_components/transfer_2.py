from gladier import GladierBaseTool

# Data Store to FastText action provider definition
class transfer_2(GladierBaseTool):  
    flow_definition = {
      "Comment": "#TODO", 
      "StartAt": "transfer_2", 
      "States": {
        "transfer_2": {
          "End": True,
          "Type": "Action",
          "Comment": "#TDOO",
          "WaitTime": 600,
          "ActionUrl": "https://actions.automate.globus.org/transfer/transfer",
          "Parameters": {
            "source_endpoint_id.$": "#TODO", 
            "destination_endpoint_id.$": "#TODO",
            "transfer_items": [
              {
                "source_path.$": "#TODO", 
                "destination_path.$": "#TODO",
                "recursive": False, 
              }
            ]
          },
          "ResultPath": "$.transfer_2"
        }
      }
    }

    funcx_functions = [] 

    flow_input = {
        'transfer_sync_level': 'checksum'
    }

    required_input = {} # TODO

    #   required_input = {
    #   "endpoints": {
    #     "datastore_uuid",
    #     "fasttext_uuid"
    #   },
    #   "datastore_paths": {
    #     "data_path"
    #   },
    #   "fastText_paths": {
    #     "DS_FT_dest"
    #   }
    # }
  
