from automation1.api.liebs.arcadeApi import ArcadeApi

api = ArcadeApi(user_id="U07B1MK6MAQ", save=True, debug=False)

# Start a new session
#api.start_session("My Arcade Session")

# Pause the session
#api.pause_session()

# Resume the session
#api.resume_session()

# Post a reply to the session thread
api.post_reply("Hello, Arcade!")

#print(api.get_latest_session_ts())