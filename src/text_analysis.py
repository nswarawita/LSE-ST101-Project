from nltk.corpus import stopwords
from nltk.stem.porter import *
stemmer = PorterStemmer()

def is_stopping_words(word):
    '''
    Checks if the word provided is a stopping word

    Parameters
    ----------
    word : str
        word to check

    Returns
    -------
    bool
        True if the given word is a stopping word

    '''
    STOPPING_WORDS = stopwords.words('english')
    return word in STOPPING_WORDS


def clean_phrase(phrase):
    '''
    Returns a list of the cleaned words in the phrase provided
    
    Parameters
    ----------
    phrase : list of string

    Returns
    -------
    clean_words : list
        list of all the cleaned words
    '''
    words = phrase.split(' ')
    clean_words = []
    for word in words:
        word = word.lower()                 # Convert all the letters into lowercase
        word = word.strip(",.();'\"-!?&:")  # Remove punctuation
        word = stemmer.stem(word)           # Obtain the stem of the word
        if not is_stopping_words(word) and len(word):
            clean_words.append(word)            
    return clean_words

    
def get_topics(phrase):
    '''
    Returns a dictionary of the words that occur in the given phrase and the number of times each word occurs (in the given phrase) 
    Stopping words are excluded for this function

    Parameters
    ----------
    phrase : list of string

    Returns
    -------
    bag_of_words : dict
        dict with keys are words (str) and values are occurance (int)
    '''
    clean_words = clean_phrase(phrase)
    topics = {}
    for i in range(len(clean_words)):
        topics[clean_words[i]] = topics.get(clean_words[i], 0) + 1            
    return topics


def get_freq_words(topics, rating, threshold):
    '''
    Returns all the words whose number of appearances exceeds the threshold
    Stopping words are excluded from this function

    Parameters
    ----------
    topics : dictionary 
    rating : string
    threshold : int

    Returns
    -------
    freq_words : list of string
    '''
    freq_words = {}
    for word, count in topics[rating].items():
        if count >= threshold:
            freq_words[word] = count
    return freq_words




