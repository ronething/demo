#! /bin/bash
# an script of backup files or directories
backup_date=`date +'%Y-%m-%d-%H:%M:%S'` # date [] [+format]
backup_dir=~/Documents/Backup
backup_log="${backup_dir}/${backup_date}.log"

function backup_file()
{
    if [ -e "$1" ]
    then
        tarfilename="$1.tar.gz"
        tar -czPf ${tarfilename} $1 1> /dev/null 2>& 1
        cp ${tarfilename} ${backup_dir} 1> /dev/null 2>& 1
        if [ $? -eq 0 ]
        then
            rm ${tarfilename}
            return 0
        fi
    fi
    return 1
}

function write_log()
{
    log_time=`date +'%Y-%m-%d-%H:%M:%S'` # date [] [+format]
    backup_file=$2
    error_msg="${log_time} error in backup ${backup_file}"
    success_msg="${log_time} success in backup ${backup_file}"
    if [ $1 -eq 0 ]
    then
        echo ${success_msg}
        echo ${success_msg} >> ${backup_log} # >> is 追加
    else
        echo ${error_msg}
        echo ${error_msg} >> ${backup_log}
    fi
}

if [ $# -eq 0 ]
then
    echo "Usage: ./filename.sh arg..."
    exit 1
fi

if [ ! -e ${backup_dir} ]
then
    mkdir ${backup_dir}
fi

if [ ! -e ${backup_log} ]
then
    touch ${backup_log}
fi

echo "backup begin at ${backup_date}" >> ${backup_log}
echo "backup begin at ${backup_date}"

for file
do
    backup_file $file
    write_log $? $file
done
echo "backup end..." >> ${backup_log}
echo "backup end..."
exit 0
