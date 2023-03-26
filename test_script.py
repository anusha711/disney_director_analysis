#!/home/jupyter
# -*- coding: utf-8 -*-
"""
Created on Mon Mar 20 09:39:19 2023

@author: Anusha Anantapatnaikuni

"""


#This function creates a helper data to test the sample script created for 
#the sample solution to the Python Programming for Data Science project.

import pandas as pd
import numpy as np
from script import *

def test_genre_year_range():
    # Create some test data
    gross_df = pd.DataFrame({
        'movie_title': ['The Avengers', 'The Avengers', 'Iron Man', 'Iron Man', 'Iron Man 2', 'Iron Man 2'],
        'genre': ['Action', 'Adventure', 'Action', 'Sci-Fi', 'Action', 'Sci-Fi'],
        'release_year': [2012, 2012, 2008, 2008, 2010, 2010],
        'inflation_adjusted_gross': [623357910, 623357910, 585058914, 679127022, 424084233, 493282778]
    })

    # Test that the function returns a DataFrame
    assert isinstance(genre_year_range(2008, 2012, gross_df), pd.DataFrame)

    # Test that the function returns a DataFrame with the expected shape
    assert genre_year_range(2008, 2012, gross_df).shape == (5, 4)
    
    
def test_clean_gross_data():    
# Create helper data for testing clean_gross_data
raw_data = {
    "movie_title": [
        "Avatar",
        "Titanic",
        "Star Wars: Episode VII - The Force Awakens",
        "The Avengers",
        "The Dark Knight",
    ],
    "inflation_adjusted_gross": ["$3,290,000,000", "$3,050,000,000", "$2,065,000,000", "$1,565,000,000", "$1,345,000,000"],
    "total_gross": ["$2,789,000,000", "$2,194,000,000", "$2,068,000,000", "$1,519,000,000", "$1,005,000,000"],
    "release_date": ["2009-12-18", "1997-12-19", "2015-12-18", "2012-05-04", "2008-07-18"],
    "genre": ["Action", "Drama", "Sci-Fi", "Action", "Action"],
    "MPAA_rating": ["PG-13", "PG-13", "PG-13", "PG-13", "PG-13"]
}

d_gross = pd.DataFrame(raw_data)


    # Test removing \n from '$' from gross columns
    clean_data = clean_gross_data(d_gross)
    assert clean_data["inflation_adjusted_gross"].iloc[0] == "3290000000.0"
    assert clean_data["total_gross"].iloc[0] == "2789000000.0"

    # Test converting gross columns to type float and removing special character ,
    assert isinstance(clean_data["total_gross"].iloc[0], float)
    assert isinstance(clean_data["inflation_adjusted_gross"].iloc[0], float)

test_clean_gross_data()