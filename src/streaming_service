from show import Show
from inverted_index import create_inverted_index, add_to_inverted_index
from text_analysis import clean_phrase

class StreamingService:
    '''
    StreamingService represents a streaming service that stores and provides different TV and movie shows
    '''
    def __init__(self, name, df):
        '''
        Parameters
        ----------
        name : str
            name of the streaming service
        df : pandas DataFrame
            each row contains the information about title, type, director, cast, year added, rating, duration, genre, description

        Returns
        -------
        None.
        '''
        if not isinstance(name, str):
            raise TypeError(f"The name of the streaming service needs to be a str, but {type(name)} is given.")

        self._inverted_index = create_inverted_index(df)
        self._indexing = {} #This is dictionary which contains the indexes of all the shows
        self._name = name
        self._shows = {}
        for _, row in df.iterrows():
            self.add_show(*row)


    def get_name(self):
        '''
        return the name (string)
        '''
        return self._name
    

    def get_all_shows(self):
        '''
        Returns all the the shows in the streaming service

        Returns
        ------
        show : Show
            Show available from the streaming service
        '''
        for show in self._shows.values():
            return show


    def add_show(self, title, show_type, director, cast, release_year, rating, duration, listed_in, description):
        '''
        Adds a show to the streaming service. Show title is unique

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
            the year that the movie or TV show was released
        rating : str
            parental guidelines rating
        duration : str
            length of the movie or the TV show
        listed_in : str
            genre of the show
        description : str
            description of the show
            
        Returns
        -------
        None.

        '''
        self._shows[title] = Show(title, show_type, director, cast, release_year, rating, duration, listed_in, description)
        self._indexing[len(self._indexing)] = self._shows[title]
        parameters = [title, show_type, director, cast, release_year, rating, duration, listed_in, description]
        for item in parameters:             
            item = str(item)
            cleaned_item = clean_phrase(item)            
            add_to_inverted_index(self._inverted_index, cleaned_item, len(self._indexing)-1)
                
            
    def remove_show(self, show_title):
        '''
        remove a show from the streaming service given the title of the show
    
        Parameters
        ----------
        show_title : string
            title of the show to remove. It has to match the title perfectly (including case, spacing, etc)
    
        Raises
        ------
        KeyError
            if the corresponding show is not available from the streaming service
    
        Returns
        -------
        None.
        '''
        try:
            del self._shows[show_title]
        except KeyError:
            raise KeyError(f"The show {show_title} is not available from {self.get_name()}.")


    def get_show(self, phrase_related_to_show):
        '''
        Get a show given a phrase related to the show. If no show matches all the given criteria, all the shows with a partial match are provided

        Parameters
        ----------
        phrase_related_to_show : str
            A phrase related to the show

        Raises
        ------
        KeyError
            if the corresponding show is not available from the streaming service

        Prints
        -------
        show
            all the shows that are related to the given phrase

        '''
        string = str(phrase_related_to_show)
        word_list = clean_phrase(string) #this is a list of cleaned words
        list_of_indexes = [] #this is a list of sets        
        for word in word_list:
            if word in self._inverted_index.keys():
                list_of_indexes.append(self._inverted_index[word]) #self._inverted_index[word] is a set of integers  
            else:  
                continue # move onto the next word
        if len(list_of_indexes) == 0:
            print(f"No show is related to {word_list}.")            
        else:
            indexes_intersection = list_of_indexes[0].intersection(*list_of_indexes) #this is a set containing the row numbers (indexes) corresponding to the shows that are related to all the aspects provided
            if len(indexes_intersection) > 0: 
              for index in indexes_intersection:
                    if index in self._indexing.keys():
                        print(self._indexing[index])
            else:
                indexes_union = list_of_indexes[0].union(*list_of_indexes) #this is a set containing the row numbers (indexes) corresponding to the shows that are partially related to the phrase provided
                if len(indexes_union) > 0:
                    for index in indexes_union:
                        if index in self._indexing.keys():
                            print(self._indexing[index])
                else:
                    print(f"No show is related to {word}.")
                                            
                
        
