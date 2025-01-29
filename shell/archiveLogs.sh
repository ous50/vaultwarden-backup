#!/bin/bash
PATH=/sbin:/usr/sbin/:/usr/local/sbin:/bin:/usr/local/bin

binDir="$(dirname "$(readlink -f "$0")")"
daysLogKeep=1
logLocation=<bkplocation>/log/
log=${logLocation}vw-bkp.log
archive=${logLocation}vw-bkp-$(date '+%F').log

# Translations
source $binDir/translations.sh

# Main function
mv $log $archive | echo $dailyLogArchiveCompleted >> $log

