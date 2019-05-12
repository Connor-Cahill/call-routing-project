#!/bin/bash

NUMBER=$1

grep "${NUMBER:0:10}" -w $2
if (($?)); then grep "${NUMBER:0:5}" -w $2;fi
if (($?)); then echo "Phone number prefix not found in data set.";fi
