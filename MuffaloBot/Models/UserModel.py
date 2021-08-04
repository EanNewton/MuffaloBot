#!/usr/bin/env python3
"""

"""


class PublicUser:
    def __init__(self, model: dict):
        self.steamid = model['steamid']
        self.community_visibility_state = model["community_visibility_state"]
        self.profile_state =
        self.persona_name =
        self.comment_permissions =
        self.profile_url =
        self.avatar =
        self.avatar_medium =
        self.avatar_full =
        self.last_logoff =
        self.persona_state =
        self.country_id =
        self.state_id =
        self.city_id =

    def hello(self):
        print('Hello, ', self.steamid)
