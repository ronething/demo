#! /bin/bash
echo -n "please input a directory: "
read dir
if cd $dir 1> ./output.txt 2>& 1
then
    echo "enter directory $dir succeed. "
else
    echo "enter directory $dir failed. "
fi

