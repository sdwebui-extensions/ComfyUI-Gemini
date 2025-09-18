import os
import sys
import __main__
import json

python = sys.executable


WEB_DIRECTORY = "js"


# create config
if not os.path.isfile(os.path.join(os.path.dirname(os.path.realpath(__file__)),"config.json")):
    config = {
        "GEMINI_API_KEY": "your key"
    }
    with open(os.path.join(os.path.dirname(os.path.realpath(__file__)),"config.json"), "w") as f:
        json.dump(config, f, indent=4)

#load config
with open(os.path.join(os.path.dirname(os.path.realpath(__file__)),"config.json"), "r") as f:
    config = json.load(f)


from .GeminiAPINode import NODE_CLASS_MAPPINGS, NODE_DISPLAY_NAME_MAPPINGS

# Combine the dictionaries
#NODE_CLASS_MAPPINGS = {**NODE_CLASS_MAPPINGS_G}

__all__ = ['NODE_CLASS_MAPPINGS', 'NODE_DISPLAY_NAME_MAPPINGS']
