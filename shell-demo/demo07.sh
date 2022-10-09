#! /bin/bash
while [ -n "$1" ]
do
    echo "${@}"
    shift
done
exit 0
