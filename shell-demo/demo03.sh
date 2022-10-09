#! /bin/bash
echo -n "Which OS do you like, Linux or Windows? Please answer Linux or Windows? "
read answer
if [ "$answer" = "Linux" ]
then
	echo "Liunx is good. "
elif [ "$answer" = "Windows" ]
then
	echo "Windows is not bad. "
else
	echo "sorry,$answer not recognized. Please enter Linux or Windows. "
	exit 1
fi
exit 0
