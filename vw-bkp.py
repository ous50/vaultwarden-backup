import os;
import requests;
import time;
import subprocess;
# import re;

# Define Variables
# Your backup directory
backupDir = "bw-bkp";
# Your data directory
targetDir = "bw-data";
# Rsync folder
rsyncFolder = "";
# Your parent directory
parentDirectory = "/home/ous50/";
presentHour = int(time.strftime("%H", time.localtime())) ;
# Your backup file name
fileName = "bw-bkp-" + time.strftime("%Y-%m-%d_%H%M%S", time.localtime()) + ".tar.gpg";
#How many days to keep local backup
daysLocalBackupKeep=1;
gpgPublicKeyID='CF580D011CA40D45'; #For gpg encryption Such as CF580D011CA40D45 or me@ous50.moe
date = time.strftime("%a %b %d %H:%M:%S %Y", time.localtime()) ;



# Tell when the script is executed
taskTime="Backup started at " + date + ".";
print(taskTime);

# Switch working directory
os.chdir(parentDirectory);

# Get last backup sum
if os.path.exists('.lABS'):
    print("Found last available backup data.")
    lastAvailableBackupSum = subprocess.run(args=['cat', '.lABS'], stdout=subprocess.PIPE).stdout.decode('utf-8').split(' ')[0];
    # os.system('cat .lABS | cut -d " " -f 1');
else:
    print("Last available backup data not found.")
    lastAvailableBackupSum = "";
    
print("Last avaliable backup checksum: " + lastAvailableBackupSum + "." )

# Get present backup sum
presentBackupSum = str(subprocess.run(args=['find', targetDir, ' -type f ', '-exec', 'md5sum', '{}', '\;'], stdout=subprocess.PIPE).stdout.decode('utf-8').split(' ')[0]);
print("Present data checksum: " + presentBackupSum + ".")


# Create the backup/target directory if either of them doesn't exist
if not os.path.exists(backupDir):
    os.makedirs(backupDir);

if not os.path.exists(targetDir):
    os.makedirs(targetDir);

# Get the current locale
locale = os.environ['LANG'];
if locale == None:
    lang = 'en_US';
lang = locale.split('.')[0];



duplicatedBackup="The present data is duplicated with the latest backups, exit the backup process.";
diffrentBackup="The present data (" + presentBackupSum + ") is diffrent from the latest backups(" + lastAvailableBackupSum + "), continue the backup process.";
packingCompleted="Pack up " + targetDir + "completed";
dailyDeleteCompleted="Backups in the day " + str(int(time.strftime("%d", time.localtime())) - 1) + " deleted.";
end="End of backup process.";
gpgNotInstalledError="GPG is not installed, please install it first.";


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
        subprocess.run(args=['gpgtar', '-e', '-r', gpgPublicKeyID, targetDir, '>', backupDir + '/' + fileName], stdout=subprocess.PIPE).stdout.decode('utf-8');
        #os.system("gpgtar -e -r" + gpgPublicKeyID + "" + targetDir > backupDir + "/" + fileName);
    except subprocess.CalledProcessError:
        print(subprocess.CalledProcessError.with_traceback(self, tb));
        exit();

    print(packingCompleted);

    # Upload the backups to tmp.link
    files = {'file': open(parentDirectory + backupDir + '/' + fileName, 'rb')}
        ## Extract from the tmp.link website
    form_data = {
        'token': '',
        'model': '99',
        'mrid': ''}; 
    tmp_link_upload = requests.post('https://connect.tmp.link/api_v2/cli_uploader', files=files, data=form_data);
    print(tmp_link_upload.text);


    # Rsync to remote server
    rsync_run = subprocess.run(args=['rsync', '-av', '--partial', backupDir, rsyncFolder], stdout=subprocess.PIPE).stdout.decode('utf-8');
    print(rsync_run);
    

    # Delete backups in the day set in daysLocalBackupKeep
    if presentHour == 0:
        os.system('find ' + backupDir + ' -mtime +' + daysLocalBackupKeep + ' -delete');
        print(dailyDeleteCompleted);
    
    print(end);
    exit();








    
