# NBA_API notes:

## Games

The structures that contain information about games are contain only the information about the **first team in the MATCHUP
string**, to get all information about a game both structures are needed, for example:

```json
[
  {
    "Team_ID": 1610612738,
    "Game_ID": "0022301186",
    "GAME_DATE": "APR 14, 2024",
    "MATCHUP": "BOS vs. WAS",
    "WL": "W",
    "W": 64,
    "L": 18,
    "W_PCT": 0.78,
    "MIN": 240,
    "FGM": 51,
    "FGA": 89,
    "FG_PCT": 0.573,
    "FG3M": 16,
    "FG3A": 32,
    "FG3_PCT": 0.5,
    "FTM": 14,
    "FTA": 21,
    "FT_PCT": 0.667,
    "OREB": 10,
    "DREB": 38,
    "REB": 48,
    "AST": 29,
    "STL": 10,
    "BLK": 15,
    "TOV": 14,
    "PF": 13,
    "PTS": 132
  },
  {
    "Team_ID": 1610612764,
    "Game_ID": "0022301186",
    "GAME_DATE": "APR 14, 2024",
    "MATCHUP": "WAS @ BOS",
    "WL": "L",
    "W": 15,
    "L": 67,
    "W_PCT": 0.183,
    "MIN": 240,
    "FGM": 49,
    "FGA": 103,
    "FG_PCT": 0.476,
    "FG3M": 14,
    "FG3A": 38,
    "FG3_PCT": 0.368,
    "FTM": 10,
    "FTA": 10,
    "FT_PCT": 1.0,
    "OREB": 8,
    "DREB": 28,
    "REB": 36,
    "AST": 33,
    "STL": 9,
    "BLK": 4,
    "TOV": 11,
    "PF": 16,
    "PTS": 122
  }
]
```

In the first record above the statistics refer to team BOS and the second record to team WAS.

The matchup string is formatted as follows:
 - `TEAM_A vs. TEAM_B` the house team is TEAM_A
 - `TEAM_B @ TEAM_A` the house team is TEAM_B (read @ as "at")

