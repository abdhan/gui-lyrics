from dearpygui.dearpygui import *
import azapi

api = azapi.AZlyrics('google', accuracy=0.5)

set_main_window_size(850,800)
set_main_window_title("API Test")

##NEED TO add clear lyrics
def mainCallback(sender, data):
    if get_table_selections("songlisttable"):
        add_text("", parent="lyrics")
        index = get_table_selections("songlisttable")
        urls = get_data("songs")
        url = urls[index[0][0]]
        add_text(api.getLyrics(url), parent="lyrics")
        set_table_selection("songlisttable", row=index[0][0], column=index[0][1], value=False)

def searchHandler(sender, data):
    clear_table("songlisttable")
    if get_value("artist") and get_value("title"):
        api.artist = get_value("artist")
        api.title = get_value("title")
        try:
            add_text(api.getLyrics(), parent="lyrics")
        except:
            add_text("Try another Search term", parent="lyrics")
        songs = api.getSongs()
        set_value("songlist", songs)
        urls = []
        for song in songs:
            add_row("songlisttable", [song, api.artist, songs[song]['album'], songs[song]['year']])
            urls.append(songs[song]['url'])
        add_data("songs", urls)
    elif not get_value("artist") and get_value("title"):
        api.title = get_value("title")
        try:
            add_text(api.getLyrics(), parent="lyrics")
        except:
            add_text("Try another Search term", parent="lyrics")

add_text("Type Search term and click Search! \nEnter Artist/Title for better results. \nEnter only Artist to get songs \nEnter only title to get a relevant lyrics")
add_separator()
add_group("search")
add_input_text("artist", width=240)
add_same_line()
add_input_text("title", callback=searchHandler, on_enter=True, width=250)
end()

add_group("lyricsgroup")
add_child("search_results", width=650)
set_style_child_rounding(1.0)
add_table("songlisttable", headers=["song", "artist", "album", "year"])
end()
add_same_line()
add_child("lyrics", width=650)
add_text("Lyrics show up here!", wrap=50)
end()
end()

set_render_callback(mainCallback, "MainWindow")
start_dearpygui()
