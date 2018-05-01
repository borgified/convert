#!/usr/bin/env bash

set -e

if [[ $# == 0 ]]; then
  echo "usage: $0 file.srt"
  exit 0
fi

enconding=$(file -i $1 | awk 'BEGIN {FS="=";}{print $2}')

output=$(basename $1 .srt)

iconv -f $enconding -t utf-8 $1 -o ${output}_out.srt
