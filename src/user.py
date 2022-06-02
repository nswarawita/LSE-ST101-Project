from datetime import date
from playlist import Playlist
from show import Show
from favourite_playlist import FavouritePlaylist


class User:
    '''
    User represents users of a streaming service
    '''
    
    def __init__(self, date_of_birth, month_of_birth, year_of_birth):
        '''
        Parameters
        ----------
        date_of_birth : int
            Birth date of the user 
        birth_month : int
            Birth date of the user 
        birth_year : int
            Birth date of the user .

        Returns
        -------
        None.

        '''
        if not isinstance(date_of_birth, int):
            raise TypeError(f"Date of birth needs to be an integer, but {type(date_of_birth)} is given.")
        if date_of_birth <= 0 or date_of_birth > 31:
            raise ValueError(f"Date of birth has to be an integer from 1 to 31, but {date_of_birth} is given.")
        if not isinstance(month_of_birth, int):
            raise TypeError(f"Month of birth needs to be an integer, but {type(month_of_birth)} is given.")
        if month_of_birth <= 0 or month_of_birth > 12:
            raise ValueError(f"Month of birth has to be an integer from 1 to 12, but {month_of_birth} is given.")        
        if not isinstance(year_of_birth, int):
            raise TypeError(f"Year of birth needs to be an integer, but {type(year_of_birth)} is given.")
        date_today = date.today()
        if year_of_birth < 1900 or year_of_birth > date_today.year:
            raise ValueError(f"Year of birth is expected to be greater than 1900, but {year_of_birth} is given.")
        self._birthday = date(year_of_birth, month_of_birth, date_of_birth)
        self._history = {}
        self._watch_later_playlist = Playlist("watch_later_playlist", 1000) #this is an arbitary value
        self._favourites_playlist = FavouritePlaylist("favourite_playlist", 1000) #this is an arbitary value
     
        
    def add_show_to_watch_later(self, show):
        '''
        Adds a show to the watch_later playlist. The title of the show is unique

        Parameters
        ----------
        show : an instance of Show
            show to add to the watch_later playlist
        
        Returns
        -------
        None.

        '''
        if not isinstance(show, Show):
            raise TypeError(f"{show} needs to be an instance of Show, but {type(show)} is given.")

        self._watch_later_playlist.add_show(show) 
    
    
    def remove_show_from_watch_later(self, show_title):
        '''
        Remove a show corresponding to the given show_title from the watch_later playlist

        Parameters
        ----------
        show_title : str
            title of the show to remove. It has to match the title perfectly (including case, spacing, etc)

        Raises
        ------
        KeyError
            if the corresponding show is not available from the playlist

        Returns
        -------
        None.
        '''
        if not isinstance(show_title, str):
            raise TypeError(f"{show_title} needs to be a str, but {type(show_title)} is given.")

        self._watch_later_playlist.remove_show(show_title) 
        
        
    def play_show_from_watch_later(self, show_title = None):
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
           description about what show was played and the duration of the show
           
       Prints
        -------
        str,
            Playing the show {title of the show} ({duration of the show})

        '''
        if show_title is None:
            try:
                show_title = list(self._watch_later_playlist._shows)[0] # first show name in the playlist
                show = show_title
            except IndexError:
                raise IndexError("No show is in the playlist.")
        try:
            show = self._watch_later_playlist._shows[show_title]
        except KeyError:
            raise KeyError(f"The show {show_title} is not in the playlist.")

        self._history[show.get_title()] = show # Add the show to history 
        self.remove_show_from_watch_later(show_title) # delete the show from the watch_later playlist

        play_str = f"Playing the show {show.get_title()} ({show.get_duration()})"
        print(play_str)
        return show
    
    
    def get_all_shows_in_watch_later(self):
        '''
        returns all the shows in the watch_later playlist

        Prints
        ------
        show : Show
            shows available in the watch later playlist

        '''
        self._watch_later_playlist.get_all_shows()
        

    def add_show_to_favourites(self, show):
        '''
        Adds a show to the favourites playlist. The title of the show is unique

        Parameters
        ----------
        show : an instance of Show
            show to add to the favourite playlist
        
        Returns
        -------
        None.

        '''
        if not isinstance(show, Show):
            raise TypeError(f"{show} needs to be an instance of Show, but {type(show)} is given.")

        self._favourites_playlist.add_show(show) 
    
    
    def remove_show_from_favourites(self, show_title):
        '''
        Remove a show corresponding to the given show_title from the favourite playlist

        Parameters
        ----------
        show_title : str
            title of the show to remove. It has to match the title perfectly (including case, spacing, etc)

        Raises
        ------
        KeyError
            if the corresponding show is not available from the playlist

        Returns
        -------
        None.
        '''
        if not isinstance(show_title, str):
            raise TypeError(f"{show_title} needs to be a str, but {type(show_title)} is given.")

        self._favourites_playlist.remove_show(show_title) 
    
       
    def play_show_from_favourites(self, show_title = None):
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
           ## description about what show was played and the duration of the show

        '''
        if show_title is None:
            try:
                show_title = list(self._favourites_playlist._shows)[0] # first show name in the playlist
                show = show_title
            except IndexError:
                raise IndexError("No show is in the playlist.")
        try:
            show = self._favourites_playlist._shows[show_title]
        except KeyError:
            raise KeyError(f"The show {show_title} is not in the playlist.")

        self._history[show.get_title()] = show # Add the show to history ????????????????????? 
        if show_title in self._watch_later_playlist._shows:
            self.remove_show_from_watch_later(show_title) # Remove the show from watch later ????????????????????? 
    
        play_str = f"Playing the show {show.get_title()} ({show.get_duration()})"
        print(play_str)
        return show
    
    
    def get_all_shows_in_favourites(self):
        '''
        returns a generator for the shows

        Prints
        ------
        show : Show
            Show available in the watch later playlist

        '''
        self._favourites_playlist.get_all_shows()
    
      
    def get_history(self):
        '''
        Prints all the shows in history

        Prints
        ------
        show : Show
            Show available from the streaming service
        '''
        for show in self._history.values():
            print(show)


    def clear_history(self):
        '''
        Removes all the shows in history

        Returns
        -------
        None.

        '''       
        if len(self._history) > 0:
            try:
                self._history.clear()
                clear_str = "History has been cleared"
                print(clear_str)
            except IndexError:
                raise IndexError("History is empty")
        
        
    def age_of_user(self):
        '''
        Calculates the age of the user

        Returns
        -------
        int, The age of the user

        '''
        current_date = date.today()
        age = current_date.year - self._birthday.year
        return age
        
