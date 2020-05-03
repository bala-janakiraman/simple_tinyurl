# Simple TinyUrl app

A very basic implementation of url shortener using Flask.

## Features
* Allow users to map a shortname/codes of their choice for web urls  
ex `'go' --> http://google.com`
* Redirects(using the shortname/codes)   
ex `http://localhost/go --> google.com`


### Want to play around?
Requirements to run the project - Docker and docker-compose, thats it!

`git clone <clone link>`  
 `cd simple_tinyurl`  
 `docker-compose up`

Now you can access your own tinyurl site on `http://localhost`

### Tech stack used
* Docker
* Python flask 
* Nginx to front the uWSGI server  
* Redis as KV store  

### Future improvements
* ~~Dockerize~~
* ~~Implement redis~~
* Autogenerate Tinyurls
* swagger page
* Scaling
* Monitoring, operations and visualization
* ...
