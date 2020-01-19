
# docker-webapp-change-bg-color

## Author
Raja Adabala

## About
This is a docker web app designed using python flask to change the background color of the page

## How to build image from github source

cd docker-webapp-change-bg-color

docker build -t webapp-change-bg-color .

## How to run using docker image
* with default color

docker run --rm -d -p8081:80 --name webapp1 webapp-change-bg-color
* change color

docker run --rm -d -p8082:80 --name webapp2 -e BG_COLOR=violet webapp-change-bg-color

## Latest source
https://github.com/rajaadabala15/docker-webapp-change-bg-color