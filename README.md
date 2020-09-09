# gui-lyrics

Displays lyrics instantly or gives you options to choose from. Just enter artist and/or song title and hit ENTER.

## Dependencies
1. UI front-end is dearpygui. (Note: 32bit Python versions not supported.)

  To install:
`pip install dearpygui`

2. For scraping lyrics this app uses elmoiv's lyrics-api called azapi. 

  To install:
`pip install azapi`

## Bugs
1. dearpygui is an evolving framework. So any change in their syntax can break this app.
2. Window freeze when searching.

## To-Do:
  1. Test all possible combinations of artists and track titles and get fastest/seamless result.
  2. Re-write code to make it readable using context manager.
  3. Decrease stuttering/freezing while app searches.
  4. [FEATURE] Add album art of selected track.
  5. [FEATURE] Add a player with YT-DL?
  6. [FEATURE] Synchronised Lyrics?
