#!/bin/bash
PATH=/sbin:/usr/sbin/:/usr/local/sbin:/bin:/usr/local/bin

#This script requires gnupg and rsync installed.

#Set variables
binDir=$PWD
presentHour=$(date '+%H')
parentDirectory= #The parent directory of the targetDirectory
backupDirectory=#bw-bkp
targetDirectory=#bw-data
fileName=bw-bkp-$(date '+%F_%H%M%S').tar.gpg
daysLocalBackupKeep=1
gpgPublicKeyID=#Such as CF580D011CA40D45 or me@ous50.moe
language=$(locale | grep LANG | cut -d "=" -f 2 | cut -d "." -f 1)

#Set to parent directory, to simplify the tar structure. Then get the latest backup sum.
cd $parentDirectory
lastAvailableBackupSum=$(cat .lABS)

#Compare backups with the previous ones, skip the process if the two are the same.
presentBackupSum=$(find $targetDirectory -type f -exec md5sum {} \; | sort -k 2 | md5sum | cut -d " " -f 1 ) 
#rm bw-bkp-$presentHour.tar.gz

# Translations
source $binDir/translations.sh

# Tell when the script is executed
echo $presentTime

# Skip backup process if the data directory is not changed
if [[ $lastAvailableBackupSum == $presentBackupSum ]];
then
  echo $duplicatedBackup
  exit
else
  echo $diffrentBackup
  echo $presentBackupSum > .lABS

  #pack all vaultwarden data
  /usr/bin/gpgtar -e -r $gpgPublicKeyID $targetDirectory > $backupDirectory/$fileName | echo $packingCompleted

  #upload to tmp.link
  #/usr/bin/curl -k -F "file=@$parentDirectory/$backupDirectory/$fileName" -F "token=" -F "model=" -F "mrid=" -X POST "https://connect.tmp.link/api_v2/cli_uploader"

  #sync to onedrive folder
  #/usr/bin/rsync -av --partial $backupDirectory {}#the folder onedrive is mounted on


  #Remove last day's local backups on 12AM
  if [ $presentHour -eq 0 ];
  then
	  rm $backupDirectory/bw-bkp-$(date -d -${daysLocalBackupKeep}day '+%F')* | echo $dailyDeleteCompleted
  fi
  echo $end
fi