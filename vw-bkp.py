import os;
import requests;
import time;
# import re;

# Define Variables
# Your backup directory
backupDir = 'bw-bkp';
# Your data directory
targetDir = 'bw-data';
# Your parent directory
parentDirectory = '/home/username/';
presentHour = int(time.strftime("%H", time.localtime())) ;
# Your backup file name
fileName = "bw-bkp-" + time.strftime("%Y%m%d-%H%M%S", time.localtime()) + ".tar.gpg";
#How many days to keep local backup
daysLocalBackupKeep=1;
gpgPublicKeyID='CF580D011CA40D45'; #For gpg encryption Such as CF580D011CA40D45 or me@ous50.moe
date = int(time.strftime("%a %b %d %H:%M:%S %Y", time.localtime())) ;

# Define print outs
presentTime="Backup started at" + date + ".";
duplicatedBackup="The present data is duplicated with the latest backups, exit the backup process.";
diffrentBackup="The present data (" + presentBackupSum + ") is diffrent from the latest backups(" + lastAvailableBackupSum + "), continue the backup process.";
packingCompleted="Pack up " + targetDirectory + "completed";
dailyDeleteCompleted="Backups in the day " + int(time.strftime("%d", time.localtime())) - 1 + " deleted.";
end="End of backup process.";
gpgNotInstalledError="GPG is not installed, please install it first.";

# Get last backup sum
if os.path.exists('.lABS'):
    lastAvailableBackupSum = os.system('cat .lABS | cut -d " " -f 1');
else:
    lastBackupSum = '';

# Get present backup sum
presentBackupSum = os.system('find $targetDirectory -type f -exec md5sum {} \; | sort -k 2 | md5sum | cut -d " " -f 1');

# Tell when the script is executed
print(presentTime);

# Switch working directory
os.chdir(parentDirectory);

# Create the backup/target directory if either of them doesn't exist
if not os.path.exists(backupDir):
    os.makedirs(backupDir);

if not os.path.exists(targetDir):
    os.makedirs(targetDir);

# Get the current locale
locale = os.environ['LANG'];
if locale == None:
    locale = 'en_US.UTF-8';
lang = locale.split('.')[0];

# Check if the present backup is duplicated with the latest backup
if presentBackupSum == lastAvailableBackupSum:
    print(duplicatedBackup)
    exit()
else:
    print(diffrentBackup)

    # Write the present backup sum to the file
    if (os.path.exists(".lABS")):
        os.remove(".lABS")
    f = open(".lABS", "w")
    f.write(presentBackupSum)
    f.close()  

    #For cases gnupg is not installed
    try:
        os.system("gpgtar -e -r $gpgPublicKeyID $targetDirectory > $backupDirectory/$fileName");
    except OSError:
        print(gpgNotInstalledError);
        exit();

    print(packingCompleted);


    # Rsync to remote server
    os.system('rsync -av --partial ' + backupDirectory)

    # Delete backups in the day set in daysLocalBackupKeep
    if presentHour == 0:
        os.system('find ' + backupDirectory + ' -mtime +' + daysLocalBackupKeep + ' -delete');
        print(dailyDeleteCompleted);
    
    print(end);
    exit();








    
