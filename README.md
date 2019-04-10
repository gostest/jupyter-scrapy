# jupyter-scrapy
Docker file to build image with Jupyter and Scrapy

```
git clone https://github.com/gostest/jupyter-scrapy.git
cd jupyter-scrapy
docker build -t jupyter-scrapy .
docker run -d --name jupyter -p 8888:8888 -v jupiter-volume:/opt jupyter-scrapy
```
