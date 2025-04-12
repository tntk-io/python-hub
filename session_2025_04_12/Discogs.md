# Discogs API

Find your favorite artist on https://www.discogs.com/ and copy their id (you can see it in the address bar, once you opened their page).

Use the `artist_id` you found in this endpoint to retrieve the releases from that artist: https://api.discogs.com/artists/{artist_id}/releases

The releases also include other artists' releases given that your artist appears in one of the tracks.

## Downloader

Create a file called `downloader.py` to download all the releases locally into a file called `data.json`. Note, that the API paginates the data. You only need to store the `releases`, `pagination` does not need to be stored.

## Processor

Create a file called `procesor.py` which will analyze the the downloaded `data.json`. Load the data from the file in a variable.

### Most Wanted

Check which release has the highest `in_wantlist` value. Print the title and the artist of the release.

### Most Collected Songs

Check which release has the highest `in_collection` value. Print the title and the artist of the release and the songs of that release (you can query its `resource_url`).

### Number of Releases per Year

Display the number of releases the artist had per year. Only show years when the artist had at least one release.

Note that it is not guaranteed that all releases have a year specified.

### Main Role

Calculate in what percentage of the releases the artist has a `Main` role.

### Video of Oldest Master Release

Select one of the oldest releases (only of type `master`) of the artist (any in the last year when artist had a release).

By querying the `resource_url` print the titles of the tracks and their corresponding URL to the clip using the `videos` field.

Note that some releases do not contain videos, make sure to handle such scenarios.


### Cover of Latest Release

Select one of the latest releases (only of type `release`) of the artist (any in the last year when artist had a release).

Save the cover images of the release locally. Use the format: `<title>-<year>-<number>`.

Note that you must add a User-Agent header to be able to download images.