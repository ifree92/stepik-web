#!/bin/bash
DB_READY=no

while [ $DB_READY == "no" ]
do
    mysql -u root --host=mysqlhost -e "show databases;" 2>/dev/null
    
    if [ $? -eq 0 ]
    then
        echo RIGHTTTT
        DB_READY=yes
    else
        echo "wait for mysql will ready..."
        sleep 5
    fi
done

echo finished