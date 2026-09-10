import os
import json
import re
import time 
import random 
import urllib.request
import urllib.error

API_KEY = os.gentenv("GEMINI_API_KEY","")
MODEL = os.gentv("GEMINI_MODEL","gemini-3.5-flash")

def generator_email_with_gmail(command):
  if not API-KEY:
    raise RuntimeError("GEMINI-API_KEY is misssing")

  prompt = f"""
 you are a professional gmail writing assistant
 convert the user's voice commad into a professional email.

 Rules;
 -Do not copy the commad literally
 -Do not explain anything.
 -Do not invert names ,dates , prices, companies, attachements, or facts.
 -Keep the email natural and concise.
 -Iclude an appropriate greeting and closing.

 output exactly

 SUBJECT: <subject>
 
 

