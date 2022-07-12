import json, sys, os

from util.plugins.utils import *

def fileExists():
  if os.path.isfile('defaults.json'):
    return True
  return False

def setup():
  if fileExists():
    return

  # use_defaults = str(input(f"{b}[{w}-{b}]{w} Do you want to set up defaults?: (Y/n): "))
  # if (use_defaults.lower() == "n" or use_defaults.lower() == "no"):
  #   return

  # while True:
    # token = str(input(f"{b}[{w}-{b}]{w} Enter Token: "))
    # webhook = str(input(f"{b}[{w}-{b}]{w} Enter Webhook: "))
    # valid_token = validateToken(token)
    # valid_webhook = validateWebhook(webhook)
    # valid = valid_token and valid_webhook
    # if valid:
    #   break
    # print(f"{b}[{r}-{b}]{w}" + "Invalid Token" if not valid_token else "Invalid Webhook" if not valid_webhook else "Error")

  # json_data = {
  #   "token": f"{token}",
  #   "webhook": ""
  # }

  # with open('defaults.json', 'w') as f:
  #   json.dump(json_data, f, indent=2)

  
