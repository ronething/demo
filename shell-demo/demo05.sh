#! /bin/bash
echo -n "Which OS do you like, Linux or Windows? Please answer Linux or Windows? "
read answer
case "$answer" in 
Linux|linux)
    echo "Linux is good. "
    ;;
Windows|windows)
    echo "Windows is not bad. "
    ;;
*)
    echo "sorry, $answer not recognized. Please enter Linux or Windows. "
    exit 1
esac
exit 0
