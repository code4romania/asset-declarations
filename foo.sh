#!/bin/bash

SOME_VAR="foo-$1"
echo $SOME_VAR

echo $SOME_VAR > foo.txt

foo="$1"
for (( i=0; i<${#foo}; i++ )); do
  echo "${foo:$i:1}"
done
