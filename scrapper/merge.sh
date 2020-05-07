#!/bin/sh
for f in /opt/testspy/*.csv
do
  cat $f >> results
done
