#!/bin/bash
date
for ip in 176.52.10.{1..254}
do
    ping -c2 $ip &>/dev/null && echo "$ip is up"  || echo "$ip is down"
done

