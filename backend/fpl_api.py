import requests
import time

def get_live_fpl_team_stats(email, password):
    # 1. Initialize a Session to automatically handle authentication cookies
    session = requests.Session()
    
    # 2. Log the user in
    login_url = "https://users.premierleague.com/accounts/login/"
    payload = {
        "login": email,
        "password": password,
        "app": "plfpl-web",
        "redirect_uri": "https://fantasy.premierleague.com/a/login"
    }
    # The session catches the sessionid and pl_profile cookies here
    session.post(login_url, data=payload)
    
    # 3. Extract Manager ID
    me_url = "https://fantasy.premierleague.com/api/me/"
    me_data = session.get(me_url).json()
    manager_id = me_data["player"]["entry"]
    
    # 4. Extract Current Gameweek
    bootstrap_url = "https://fantasy.premierleague.com/api/bootstrap-static/"
    bootstrap_data = session.get(bootstrap_url).json()
    
    current_gw = 1
    for event in bootstrap_data["events"]:
        if event["is_current"]:
            current_gw = event["id"]
            break
            
    # 5. Extract the User's Active Roster IDs
    picks_url = f"https://fantasy.premierleague.com/api/entry/{manager_id}/event/{current_gw}/picks/"
    picks_data = session.get(picks_url).json()
    roster_ids = [pick["element"] for pick in picks_data["picks"]]
    
    # 6. Fetch Live League Data and Filter to Roster
    live_url = f"https://fantasy.premierleague.com/api/event/{current_gw}/live/"
    live_data = session.get(live_url).json()
    
    ai_context = []
    for element in live_data["elements"]:
        if element["id"] in roster_ids:
            stats = element["stats"]
            ai_context.append({
                "player_id": element["id"],
                "minutes": stats["minutes"],
                "goals": stats["goals_scored"],
                "assists": stats["assists"],
                "points": stats["total_points"]
            })
            
    return ai_context

# To stream data during a match, your team would run this in a loop
# time.sleep(60) between calls to avoid rate limiting.
