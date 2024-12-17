
.. image:: images/bash-logo.png
   :width: 100

Bash
####

..  code-block:: bash

    #!/bin/bash

    FILE=output.txt

    readarray -t my_list < list

    execute()
    {
        element=$1

        echo $1 >> $FILE

        OUTPUT=$(aws sts assume-role --role-arn arn:aws:iam:::$1:role/ca-iam-cie-engineer --role-session-name 5000000 | egrep 'AccessKeyId|SecretAccessKey|SessionToken')

        ACCESS_KEY=$(echo $OUTPUT | cut -d '"' -f4)
        SECRET_KEY=$(echo $OUTPUT | cut -d '"' -f8)
        SESSION_TOK=$(echo $OUTPUT | cut -d '"' -f12)

        aws describe-instances | grep InstanceId | wc -l >> $FILE
        aws describe-volumes | grep -B1 Sieze | grep VolumeId | wc -l >> $FILE
        aws autoscaling describe-auto-scaling-groups | grep AutoScalingGroupName | wc -l >> $FILE
        aws rds describe-db-instances | grep DBInstanceIdentifier | wc -l >> $FILE

        echo >> $FILE
     }

     for item in "${my_list[@]}"; do

         #spawns a fresh bash process so don't need to switch roles back
         execute "$item" &

         #wait for process to end so OUTPUT file won't be written out of sync from other processes
         wait
     done

