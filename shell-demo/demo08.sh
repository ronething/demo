#! /bin/bash

n=1

function yesorno(){
    echo "is your name $*? "
    while true
    do
        read -p "Enter yes or no: " x
        case $x in
            yes|Yes)
                return 0
                ;;
            no|No)
                return 1
                ;;
            *)
                echo "answer yes or no"
        esac
    done
}

echo "original parameters are ${*}"
if yesorno "$1"
then
    echo "Hi $1, nice name. "
else
    echo "Never mind. "
fi
exit 0
