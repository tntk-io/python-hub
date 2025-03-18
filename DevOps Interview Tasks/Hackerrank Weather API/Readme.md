# Retrieve and Parse Data

## Rest API 

You are responsible for collecting weather data from an external REST API service and parsing the results into a simplified format.

## Problem Statement

For a given input, write a script using Python that will:

* Perform a GET request against the API service
    * The API endpoint is: **https://jsonmock.hackerrank.com/api/weather**
    * Queries can be made with the following syntax: `/search?name=keyword` where `keyword` is some text that filters the records based on matching cities.
    * The search is case-insensitive, and it checks whether the given city's name starts with the keyword.
    * The response from the API is paginated meaning that if there is more than 1 page of data the next subsequent pages can be accessed with the help of the `page` query parameter in the URL. Example: `&page=num` where `num` is the page number.
* Parse the results into a list of comma separated strings in the format: **city_name,temperature,wind,humidity**
* If specified, remove any records where the temperature is greater than or equal to the temperature specified in the **max_temp** parameter

## API Schema

* **page**: the current page
* **per_page**: the maximum number of results per page
* **total**: the total number of records in the search result
* **total_pages**: the total number of pages to query to get all the results
* **data**: an array of JSON objects that contain weather records 

The data field in the response contains a list of weather records with the following fields:

* **name**: the name of the city
* **weather**: temperature recorded
* **status**: an array of wind speed and humidity records

## Output Format 
Filter records to include a given string in the keyword parameter. Return an array such that each element is a string of comma-separated values: **city_name,temperature,wind,humidity**.

For example, given the following record retrieved from the API:
```
{ 
  "name": "Adelaide",
  "weather": "15 degree",
  "status": [
    "Wind: 8Kmph",
    "Humidity: 61%"
  ]
} 
```

The simplified string returned by your script will be: **Adelaide,15,8,61**. If there are multiple matching records, return the list sorted by **city_name**.

### Function Description
Create a function called `weatherStation(keyword, max_temp=None)`.

**weatherStation** has the following parameter(s):
* **_string_ keyword**: the string to search
* **_int_ max_temp**: records containing temperatures above this value should not be returned 

### Returns
**string[]**: the formatted weather data for each city