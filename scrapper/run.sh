#!/bin/sh
scrapy crawl aviadata -o $1.csv -t csv -a url=https://www.airfleets.net/recherche/list-airline-$1.htm
