import os 

# Get the full path of the current file
file_path = os.path.realpath(__file__)
localpath = os.path.dirname(file_path)
SourcePath = "/input/"
DestPath = "/output/"

transferfile = "testdata.txt"
SourceFile = os.path.join(SourcePath, transferfile)
DestFile = os.path.join(DestPath, transferfile)

# Config file for access creds
CLIENT_ID = ""
CLIENT_SECRET = ""
SCOPE_STRING = ""

DataStoreUUID = "b782400e-3e59-412c-8f73-56cd0782301f"

# Config for the LPAP flow
flow_config = {
  'input': {
    'endpoints': {
      'DS_1_uuid': '',
      'DS_2_uuid': '',
      'LPAP_uuid': ''
    },
    'directory_paths': {
      'DS_1': '',
      'DS_2': '',
      'LPAP_input': '',
      'LPAP_output': ''
    }
  }
}