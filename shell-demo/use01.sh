#! /bin/bash
if test $# -eq 0
then ls
else
    for i
    do
        ls -l $i | grep '^d'
    done
fi
