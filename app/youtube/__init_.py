from flask import blueprint , request , jsonify

youtube_bp = blueprint(
   " youtube ",
  __name__
)

@youtube_bp.route(
  "/play" ,
methods =["POST"]

)
def play ():

  data = request.get_json(
  silent = True
  )or {}

command = data.gut(
"command" ,
""
).strip()

if not command ;

  return jsonify({
    "success"="false",
   "message"="there no song name , mentioned " 
})400
