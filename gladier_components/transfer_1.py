from gladier import GladierBaseTool

# Data Store to FastText action provider definition
class transfer_1(GladierBaseTool):  
    flow_definition = {
      "Comment": "#TODO", 
      "StartAt": "transfer_1", 
      "States": {
        "transfer_1": {
          "End": True,
          "Type": "Action",
          "Comment": "#TDOO",
          "WaitTime": 600,
          "ActionUrl": "https://actions.automate.globus.org/transfer/transfer",
          "Parameters": {
            "source_endpoint_id.$": "10", 
            "destination_endpoint_id.$": "10",
            "transfer_items": [
              {
                "source_path.$": "/example/path", 
                "destination_path.$": "/example/path",
                "recursive": False, 
              }
            ]
          },
          "ResultPath": "$.transfer_1"
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
  
