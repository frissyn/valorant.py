Endpoints
=========

``valorant.py``, as of ``v0.5.0``, covers 4 endpoints:

-  **ACCOUNT-V1**
-  **VAL-CONTENT-V1**
-  **VAL-RANKED-V1**
-  **VAL-STATUS-V1**
-  **VAL-MATCH-V1** (Unimplemented)

ACCOUNT-V1
----------

+----------------------------------+----------------------------------+
| Method                           | Description                      |
+==================================+==================================+
| ``get_user_by_puuid(puuid)``     | Get an ``AccountDTO`` by a given |
|                                  | user PUUID.                      |
+----------------------------------+----------------------------------+
| ``get                            | Get an ``AccountDTO`` by a given |
| _user_by_name(name, delim="#")`` | name split by a delimeter.       |
+----------------------------------+----------------------------------+

VAL-CONTENT-V1
--------------

======================= ============================================
Method                  Description
======================= ============================================
``get_acts()``          Get a ``ContentList`` of Acts.
``get_characters()``    Get a ``ContentList`` of Agents.
``get_charms()``        Get a ``ContentList`` of Gun Buddies.
``get_charm_levels()``  Get a ``ContentList`` of Gun Buddy Levels
``get_chromas()``       Get a ``ContentList`` of Weapon Chromas.
``get_current_act()``   Get an ``ActDTO`` of the current act.
``get_equips()``        Get a ``ContentList`` of equipable items.
``get_maps()``          Get a ``ContentList`` of Maps.
``get_skins()``         Get a ``ContentList`` of Weapon Skins.
``get_skin_levels()``   Get a ``ContentList`` of Weapon Skin Levels.
``get_game_modes()``    Get a ``ContentList`` of Game Modes.
``get_sprays()``        Get a ``ContentList`` of Sprays.
``get_spray_levels()``  Get a ``ContentList`` of Spray Levels.
``get_player_cards()``  Get a ``ContentList`` of Player Cards.
``get_player_titles()`` Get a ``ContentList`` of Player Titles.
======================= ============================================

VAL-RANKED-V1
-------------

+----------------------------------+----------------------------------+
| Method                           | Description                      |
+==================================+==================================+
| ``get_leaderboa                  | Get a ``LeaderboardDTO`` with a  |
| rd(size=100, page=0, actID="")`` | list of players from the given   |
|                                  | values. The ``page`` attribute   |
|                                  | auto-calcs the index offest.     |
|                                  | ActID defaults to the current    |
|                                  | act ID.                          |
+----------------------------------+----------------------------------+

VAL-STATUS-V1
-------------

+---------------------------+-----------------------------------------+
| Method                    | Description                             |
+===========================+=========================================+
| ``get_platform_status()`` | Get a ``PlatformStatusDTO`` with the    |
|                           | current Platform Status.                |
+---------------------------+-----------------------------------------+