#!/bin/bash

NUMBER=$1

grep "${NUMBER:0:7}" $2 

if (($?)) ; then grep "${NUMBER:0:4}"; fi

