#! /bin/bash
max_n=0
if [ $# -eq 0 ]
then
for n in 1 2 3 4 5 6 7 8 9 10
do
    if test $max_n -lt $n
    then
        max_n=$n
    fi
done
else
for n
do
    if test $max_n -lt $n
    then
        max_n=$n
    fi
done
fi
echo "The maximum value is $max_n"
exit 0
