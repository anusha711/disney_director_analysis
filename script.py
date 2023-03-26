#!/home/jupyter
# -*- coding: utf-8 -*-
"""
Created on Mon Mar 20 09:36:19 2023

@author: Anusha Anantapatnaikuni

"""
import pandas as pd


def clean_gross_data(d_gross):
    """
    This function cleans the gross data by removing special characters
    from the gross columns,
    converting them to float,
    extracting the release year from the release date column, and
    dropping rows with missing genre or MPAA rating values.

    Parameters:
    -----------
    d_gross : pandas.DataFrame
        The DataFrame containing the gross data to be cleaned.

    Returns:
    --------
    pandas.DataFrame
        The cleaned DataFrame.
    """
    # Check that data is a pandas DataFrame
    if not isinstance(d_gross, pd.DataFrame):
        raise TypeError("data arg must be a pandas DataFrame")

    # Removing \n from '$' from gross columns
    d_gross["inflation_adjusted_gross"] = d_gross[
        "inflation_adjusted_gross"
    ].str.lstrip("$")
    d_gross["total_gross"] = d_gross["total_gross"].str.lstrip("$")

    # Converting gross columns to type float and removing special character ,
    d_gross["total_gross"] = d_gross["total_gross"].str.replace(",", "")
    d_gross["inflation_adjusted_gross"] = d_gross[
        "inflation_adjusted_gross"
    ].str.replace(",", "")
    d_gross["total_gross"] = d_gross["total_gross"].astype(float)
    d_gross["inflation_adjusted_gross"] = d_gross["inflation_adjusted_gross"].astype(
        float
    )

    # Extracting release_year from release_date column
    d_gross["release_year"] = d_gross["release_date"].dt.year

    # Handling NaN value in Genre and MPAA_rating (Droping Rows)
    d_gross = d_gross.dropna(subset=["genre", "MPAA_rating"])

    return d_gross


def clean_dir_data(data):
    """
    Renames the 'name' column to 'movie_title', replaces the name of the director for the movie 'Fantasia', and returns the updated data.

    Parameters:
     -----------
        data (pandas.DataFrame): The input DataFrame containing movie data.

    Returns:
    --------
        pandas.DataFrame: The updated DataFrame with 'name' renamed to 'movie_title' and the name of the director for 'Fantasia' updated.
    """
    # Check that data is a pandas DataFrame
    if not isinstance(data, pd.DataFrame):
        raise TypeError("data arg must be a pandas DataFrame")

    data = data.rename(columns={"name": "movie_title"})
    data.loc[data["movie_title"] == "Fantasia", "director"] = "Joe Grant"

    return data


def genre_year_range(start_year, end_year, gross_df):
    """
    Filter and group a DataFrame of movie grosses by genre, movie title, and release year.

    Parameters:
        start_year (int): The earliest year of release to include in the output.
        end_year (int): The latest year of release to include in the output.
        gross_df (pd.DataFrame): A DataFrame of movie grosses, with columns for movie title, genre, release year,
            and gross revenue.

    Returns:
        pd.DataFrame: A DataFrame containing the mean gross revenue for each combination of genre, movie title,
            and release year, for movies released between start_year and end_year, inclusive.

    Raises:
        ValueError: If start_year is greater than end_year.

    Examples:
    >>> genre_year_range(1996, 1998, gross_df).shape
        (72, 5)
    """
    # Check that data is a pandas DataFrame
    if not isinstance(gross_df, pd.DataFrame):
        raise TypeError("data arg must be a pandas DataFrame")

    if start_year < 1937:
        raise ValueError(
            "start_year must be between 1937-2015,as data range is 1937-2016!"
        )
    if end_year > 2016:
        raise ValueError(
            "end_year must be between 1938-2016,as data range is 1937-2016!"
        )
    if start_year > end_year:
        raise ValueError("start_year must be less than or equal to end_year")

    filtered_df = gross_df[
        (gross_df["release_year"] >= start_year)
        & (gross_df["release_year"] <= end_year)
    ]
    genre_year = (
        filtered_df.groupby(["movie_title", "genre", "release_year"])
        .mean()
        .reset_index()
    )
    return genre_year
