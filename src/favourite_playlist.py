from playlist import Playlist

class FavouritePlaylist(Playlist):
    '''
    This represents the favourite playlist of the user. 
    '''

    def __init__(self, name, capacity):
       '''
       Parameters
       ----------
       name : str
       name of the playlist
       capacity : positive int
       maximum number of shows that can be stored in the playlist
    
       Raises
       ------
       TypeError
       when the given capacity is not an int
       ValueError
       when the given capacity is not positive
    
       Returns
       -------
       None.
    
       '''
       
       Playlist.__init__(self, name, capacity)
       
       
    def play_show(self, show_title = None):
     '''
     "play" a show with the given title in the playlist by printing out "Playing the show xxxx (yyyy)" and returning the corresponding show (type: Show)
     If show_title is not given, the show that has been added to the playlist first will be play

     Parameters
     ----------
     show_title : str, optional
         Show to play. It has to match the title perfectly (including case, spacing, etc)
         The default is None and the first show added to the playlist will be played.

     Raises
     ------
     IndexError
         when the playlist is empty
     KeyError
         when the given show is not in the playlist

     Returns
     -------
     show : Show
        title of the show and the type of show
        
    Prints
    -------
    str,
        Playing the show {title of the show} ({duration of the show})

     '''
     if show_title is None:
         try:
             show_title = list(self._shows)[0] # first show name in the playlist
         except IndexError:
             raise IndexError("No show is in the playlist.")
     try:
         show = self._shows[show_title]
     except KeyError:
         raise KeyError(f"The show {show_title} is not in the playlist.")

     play_str = f"Playing the show {show.get_title()} ({show.get_duration()})"
     print(play_str)
     return show


    
