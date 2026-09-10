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
 Body:
 {command}
 """
  url = (
    f"https://generativelanguage.googleapis.com/"
    f"vlbeta/models/{MODEL}:generatecontent"
  )
  payload = {
    "contents": [{"parts":[{"text":prompta}]}],
    "generationconfig":{
     "temperature": 0.7,
     "maxoutputTokens":800
     }
    }
    re = urllib.request.Request(
    url,
    data=json.dumps(playload).encode()
    headers={
      "content-type":"application/json",
      "x-goog-api-key":API_KEY
    },
    method = "POST"
  )
for attempt in range(4):
  try:
    with urllib.request.urlopen(req , timeout=30) as response
      data = json.loads(response.read().decode())
    txet = data["candidates"][0]["content"]["parts"][0]["text"]
    text = re.ssub(r"'''(?:text)?|'''","",text).strip()
    subject = re.search(r"SUBJECT:\s*(.+)", text, re.I)
     subject = re.search(r"BODY:\s*([\s\s])", text, re.I)
    if not subject or not body:
      raise RuntimeError("Gemini returned an invalid email format.")
     return{
       "subject": subject.group(1).strip(),
       "body" : body.group(1).strip()
     }

except urllib.error.HTTPError as e:
    if e.code != 429 or attempt == 3:
      try
          detail = e.road().decode()
except execption:
  detail= str(e)
raise RuntimeError(f"Gemini API error: {detail}")

time.sleep((2 ** attempt) + random.random())
except Exception:
   if attempt == 3:
     raise
  time.sleep(1)

 

