from datetime import date


class Show:
    '''
    Show represents a TV show / movie by storing and providing different information about the corresponding show
    '''
    _id_counter = 0
    def __init__(self, title, show_type, director, cast, release_year, rating, duration, listed_in, description):
        '''
        Parameters
        ----------
        title : str
            title of the show
        show_type : str
            whether the show is a TV show or a movie
        director: str
            the director of the movie or TV show
        cast: str
            the cast of the movie or TV show
        release_year : int
            the year that the movie was released
        rating : str
            parental guidelines rating
        duration : str
            length of the movie or the TV show
        listed_in : str
            genre of the show
        description : str
            description of the show

        Raises
        ------
        TypeError
            if the aspects of the show aren't of the required type
        ValueError
            if release_year is negative or greater than the currrent year

        Returns
        -------
        None.
        '''

        if not isinstance(title, str):
            raise TypeError(f"The title of the show needs to be a str, but {type(title)} is given.")
        if not isinstance(show_type, str):
            raise TypeError(f"The type of the show needs to be a str, but {type(show_type)} is given.")
        if type(director) == float:
            raise TypeError(f"The director of the show needs to be a str (or float if NaN), but {type(director)} is given.")
        if not isinstance(cast, str):
            raise TypeError(f"The cast of the show needs to be a str or float if NaN), but {type(cast)} is given.")
        if not isinstance(release_year, int):
            raise TypeError(f"The release year of the show needs to be an int, but {type(release_year)} is given.")
        date_today = date.today()
        if release_year <= 0 or release_year > date_today.year:
            raise ValueError(f"The release year is expected to be a positive integer less than 2022, but {release_year} is given.")
        if not isinstance(rating, str):
            raise TypeError(f"The rating of the show needs to be a str (or float if NaN), but {type(rating)} is given.")
        if not isinstance(duration, str):
            raise TypeError(f"The duration of the show needs to be a str, but {type(duration)} is given.")
        if not isinstance(listed_in, str):
            raise TypeError(f"The category/categories under which the show is listed in needs to be a str, but {type(listed_in)} is given.")
        if not isinstance(description, str):
            raise TypeError(f"The description of the show needs to be a str, but {type(description)} is given.")
 
        self._title = title
        self._show_type = show_type
        self._director = director
        self._cast = cast
        self._release_year = release_year
        self._rating = rating
        self._duration = duration
        self._listed_in = listed_in
        self._description = description
        self._id = Show._id_counter
        Show._id_counter += 1


    def get_id(self):
        '''
        return the unique id of the show (int)
        '''
        return self._id


    def get_title(self):
        '''
        return the title of the show (string)
        '''
        return self._title


    def get_show_type(self):
        '''
        return the show type like TV show or Movie (string)
        '''
        return self._show_type
    
    
    def get_director(self):
        '''
        return the director of the show (string)
        '''
        return self._director
    
    
    def get_cast(self):
        '''
        return the cast of the show (string)
        '''
        return self._cast


    def get_release_year(self):
        '''
        return the year the show was released (int)
        '''
        return self._release_year


    def get_rating(self):
        '''
        return the parental guidelines rating (string)
        '''
        return self._rating


    def get_duration(self):
        '''
        return the duration description (string)
        '''
        return self._duration
    
    
    def get_listed_in(self):
        '''
        return the categories that the show is listed under (string)
        '''
        return self._duration


    def get_description(self):
        '''
        return the description of the show (string)
        '''
        return self._description


    def __str__(self):
        return f"{self.get_title()} ({self.get_show_type()})"


    def __repr__(self):
        return str(self)
    

