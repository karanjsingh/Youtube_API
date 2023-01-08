## ABOUT

To make an API to fetch latest videos sorted in reverse chronological order of their publishing date-time from YouTube for a given tag/search query in a paginated response.

## BASIC REQUIREMENTS:	

* Server should call the YouTube API continuously in background (async) with some interval (say 10 seconds) for fetching the latest videos for a predefined search query and should store the data of videos (specifically these fields - Video title, description, publishing datetime, thumbnails URLs and any other fields you require) in a database with proper indexes.
* A GET API which returns the stored video data in a paginated response sorted in descending order of published datetime.
* A basic search API to search the stored videos using their title and description.
* Dockerize the project.
* It should be scalable and optimised.
* Add support for supplying multiple API keys so that if quota is exhausted on one, it automatically uses the next available key.
* Make a dashboard to view the stored videos with filters and sorting options (optional)
* Optimise search api, so that it's able to search videos containing partial match for the search query in either video title or description.

## Tech Stack:
 * Django
 * Django Rest Framework
 * YouTube data v3 API


## Setting Up 🔨

 <details>
  <summary><strong>Setup Steps</strong></summary>

- Clone the Repository
 ```
$ git clone {repo_url}
 ```
- Go the the folder
 ```
$ cd API_Youtube
 ```
- Setup Virtual environment
 ```
$ python3 -m venv env
```
- Activate the virtual environment
```
$ source env/bin/activate
```
- Install dependencies using
```
$ pip install -r requirements.txt
```
- Create an .env file and add 
        NUM_KEYS=3
        API_KEY_1=KEY_1
        API_KEY_2=KEY_2
        API_KEY_3=Key_3
        QUERRY=mountain
        INTERVAL_SECONDS=10
```
- Make migrations using
```
$ python manage.py makemigrations
```
- Migrate Database
```
$ python manage.py migrate
```
- Create a superuser
```
$ python manage.py createsuperuser
```
- Run server using
```
 python manage.py runserver
``` 
  
</details>


## Usage :label:

Run the command to build from docker:

$ docker-compose build

$ docker-comopse up

## API CALLS

        For Paginated View of Latest content: http://127.0.0.1:8000/
        To search using a keyword: http://127.0.0.1:8000/?search=news


## Reference:

    YouTube data v3 API: https://developers.google.com/youtube/v3/getting-started
    Search API reference: https://developers.google.com/youtube/v3/docs/search/list


