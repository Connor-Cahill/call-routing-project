#!/bin/bash

NUMBER=$1

grep "${NUMBER:0:7}" $2
if (($?)); then grep -w "${NUMBER:0:5}" $2;fi
if (($?)); then echo "Phone number prefix not found in data set.";fi
