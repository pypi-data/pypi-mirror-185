# lotr_movie_sdk package

## Submodules

## lotr_movie_sdk.movie module

Lord Of The Rings Movie SDK, based on the api exposed by: [https://the-one-api.dev/](https://the-one-api.dev/).


### _class_ lotr_movie_sdk.movie.Movie(key, url='https://the-one-api.dev/v2')
Bases: `object`


#### \__init__(key, url='https://the-one-api.dev/v2')
Initialization of the movie SDK that sets the api key & URL of the endpoint.

Args:

    key (str): String representing the api key.
    url (str): Optional parameter - a string representing the base URL for the API endpoint

    > (defaults to [https://the-one-api.dev/v2](https://the-one-api.dev/v2)).

Examples:

    ```python
    >>> hello("Roman")
    'Hello Roman!'
    ```


#### get(id)
Get the metadata of a movie with the specified id.

Args:

    id (str): String representing the movie id.

Returns:

    Dict: movie details

Examples:

    ```python
    >>> m.get("345t453t3")
    '{"_id":"345t453t3","name":"movie1",....}'
    ```


* **Return type**

    `dict`



#### list()
Get list of all the movies with their metadata.

Returns:

    List: list of movies with their metadata

Examples:

    ```python
    >>> m.list()
    '[{"_id":"45t5t45t454",'name':'movie1',....},...]'
    ```


* **Return type**

    `list`



#### quotes(id)
List all the quotes of a movie with the specified id.

Args:

    id (str): String representing the movie id.

Returns:

    List: list of movie quotes

Examples:

    ```python
    >>> m.quotes("345t453t3")
    '[{"_id":"34r43r43r","quote":"Hello world"},....]'
    ```


* **Return type**

    `list`


## Module contents

Lord Of TheRings Movie SDK - Test for LibLab


### lotr_movie_sdk.get_version()

* **Return type**

    `str`
