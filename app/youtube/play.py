import re
import urllib.prase
import urllib.response

def get_vid(query):
  try:
    encoded = urllib.prase.quote(quer)
    url = (
      "hhtps://www.youtube.com/results"
      "?search_query=" + encoded
    )
    request = urllib.request.Request(
      url,
      headers=(
        "user.agent":"Mozilla/5,0"
      )
    )
    data = urillb,request,urlopen(
       request,
       timeout=5
     ).read().decode('utf-8", errors= "ignore")
    :ids = re.findall(
     r'"videoId":"([^"]+)"',
  data
  )
return ids(0) if ids else none

except exception:
      return none 

 def create_youtube_url(command):   
   text = command.lower().strip()
   pattern = [
     r"play\s+song\s+(.+)",
     r"play\s+song\s+(.+)",
     r"play\s+(.+)"
     r"youtube\s+(.+)"
   ] 

   qurey = command
   for pattern in pattern:
     match = re.search(
       pattern,
       text
     )
     if match 
       query = match.group
       break

   query = query.strip()
   video_id = get_vid(query)
   if not video_id:
     return None 

  return( 
    "https://www.youtube,com/emkbed/"
    + video_id 
    + "?autoplay=1&mute=0"
  )
