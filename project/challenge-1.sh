#!/bin/bash

NUMBER=$1

grep "${NUMBER:0:7}" $2
if (($?)); then grep -w "${NUMBER:0:4}" $2;fi
