#! /bin/bash
if [ $# -eq 0 ]
then
    echo "usage:sumints integer list"
    exit 1
fi
sum=0
until [ $# -eq 0 ]
do
    sum=`expr $sum + $1`
    shift
done
echo $sum
