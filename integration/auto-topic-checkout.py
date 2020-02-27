# This script is used till now for test purposes and guideline, please handle it on your own ;)

import json 
git_user = "inegm"
filepath = 'reply.json'

with open(filepath) as fp:
  lines = fp.readlines()
  line_counter = 0

  for line in lines:
    # Update the counter
    line_counter += 1
    # parse x:
    json_per_line = json.loads(line)

    # If it's the last line skip it 
    if len(lines) == line_counter:
      continue
    # the result is a Python dictionary:
    print("cd " + json_per_line["project"])
    print("git fetch \"https://"+git_user+"@forge.vnet.valeo.com/gerrit/a/proj2000_imx8_failure_manager\" "+ json_per_line["currentPatchSet"]["ref"] +" && git checkout FETCH_HEAD")
    
 



