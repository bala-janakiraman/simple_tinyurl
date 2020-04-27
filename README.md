# Simple TinyUrl app

A very basic implementation of url shortener using Flask.

## Features
* Create shortname/codes for web urls  
ex `'go' --> http://google.com`
* Redirects using the shortname/codes  
ex `http://localhost/go --> google.com`


### Playing around
Requirements - Docker and docker-compose

`git clone <clone link>`  
 `cd simple_tinyurl`  
 `docker-compose up`

Now you can access your own tinyurl site on `localhost`

### Future improvements
* ~~Dockerize~~
* ~~Implement redis~~
* Autogenerate Tinyurls
* swagger page
* Scaling
* Monitoring, operations and visualization
* etc
