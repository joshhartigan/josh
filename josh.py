from __future__ import print_function

import getpass
import json
import os
import subprocess
import time

history = open(".josh_history", "a")

# Default Config
prompt = getpass.getuser() + " $ "
notFoundErr = "*** Command not found."


# Custom Config
if os.path.isfile(".joshrc"):
    joshrc = open(".joshrc")
    rc = json.load(joshrc)

    # Set Prompt
    if rc["prompt"]:
      prompt = \
        rc["prompt"].replace(
            "$NAME", getpass.getuser()
        ).replace(
            "$24HOUR", time.strftime("%H")
        ).replace(
            "$12HOUR", time.strftime("%I")
        ).replace(
            "$MINUTE", time.strftime("%M")
        ).replace(
            "$SECOND", time.strftime("%S")
        )

while True:
    command = raw_input(prompt)
    if command == "exit":
        break
    elif command.replace(" ","") != "":
        try:
            subprocess.call(command.split(" "))
        except Exception:
            print(notFoundErr)

    history.write(command)
