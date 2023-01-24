case $language in
  fr_FR|fr_BE|fr_CA|fr_CH|fr_LU|fr_MC)
    presentTime="Il est $(date)."
    duplicatedBackup="Les données de sauvegarde sont les mêmes que la dernière sauvegarde, le processus de sauvegarde est terminé."
    diffrentBackup="Les données de sauvegarde（"$presentBackupSum"）sont différentes que la dernière sauvegarde（"$lastAvailableBackupSum"），le processus de sauvegarde est continué."
    packingCompleted="Le paquetage de $targetDirectory est terminé"
    dailyDeleteCompleted="La sauvegarde de $(date -d -${daysLocalBackupKeep}day '+%F') a été supprimée."
    end="Le processus de sauvegarde est terminé."
    ;;
  yue_HK)
    presentTime="而家係 $(date)。"
    duplicatedBackup="備份數據同最新嘅備份一樣，退出備份進程。"
    diffrentBackup="備份數據（"$presentBackupSum"）唔同於最新嘅備份（"$lastAvailableBackupSum"），繼續備份進程。"
    packingCompleted="已經完成咗 $targetDirectory 嘅打包"
    dailyDeleteCompleted="刪除咗 $(date -d -${daysLocalBackupKeep}day '+%F') 嘅備份。"
    end="備份進程結束。"
    ;;
  es_ES|es_AR|es_BO|es_CL|es_CO|es_CR|es_CU|es_DO|es_EC|es_GT|es_HN|es_MX|es_NI|es_PA|es_PE|es_PR|es_PY|es_SV|es_US|es_UY|es_VE)
    presentTime="Ahora es $(date)."
    duplicatedBackup="Los datos de copia de seguridad son iguales que la última copia de seguridad, se termina el proceso de copia de seguridad."
    diffrentBackup="Los datos de copia de seguridad（"$presentBackupSum"）son diferentes que la última copia de seguridad（"$lastAvailableBackupSum"），se continua el proceso de copia de seguridad."
    packingCompleted="Se ha completado el empaquetado de $targetDirectory"
    dailyDeleteCompleted="Se ha eliminado la copia de seguridad de $(date -d -${daysLocalBackupKeep}day '+%F')."
    end="Se ha terminado el proceso de copia de seguridad."
    ;;
  ja_JP)
    presentTime="現在は $(date) です。"
    duplicatedBackup="バックアップデータは最新のバックアップと同じです。バックアッププロセスを終了します。"
    diffrentBackup="バックアップデータ（"$presentBackupSum"）は最新のバックアップ（"$lastAvailableBackupSum"）と異なります。バックアッププロセスを続行します。"
    packingCompleted="$targetDirectory のパッキングが完了しました"
    dailyDeleteCompleted="バックアップ $(date -d -${daysLocalBackupKeep}day '+%F') を削除しました。"
    end="バックアッププロセスが終了しました。"
    ;;
  zh_HK|zh_TW)
    presentTime="現在是 $(date)。"
    duplicatedBackup="備份數據與最新的備份相同，退出備份進程。"
    diffrentBackup="備份數據（"$presentBackupSum"）與最新的備份（"$lastAvailableBackupSum"）不同，繼續備份進程。"
    packingCompleted="打包 $targetDirectory 完成"
    dailyDeleteCompleted="已刪除 $(date -d -${daysLocalBackupKeep}day '+%F') 的備份。"
    end="備份進程結束。"
    ;;
  zh_CN|zh_SG)
    presentTime="现在是 $(date)。"
    duplicatedBackup="备份数据与最新的备份相同，退出备份进程。"
    diffrentBackup="备份数据（"$presentBackupSum"）与最新的备份（"$lastAvailableBackupSum"）不同，继续备份进程。"
    packingCompleted="打包 $targetDirectory 完成"
    dailyDeleteCompleted="已删除 $(date -d -${daysLocalBackupKeep}day '+%F') 的备份。"
    end="备份进程结束。"
    ;;
  *) # English as default
    presentTime="Backup started at $(date)."
    duplicatedBackup="The present data is duplicated with the latest backups, exit the backup process."
    diffrentBackup="The present data ("$presentBackupSum") is diffrent from the latest backups("$lastAvailableBackupSum"), continue the backup process."
    packingCompleted="Pack up $targetDirectory completed"
    dailyDeleteCompleted="Backups in $(date -d -${daysLocalBackupKeep}day '+%F') deleted."
    end="End of backup process."
    ;;
esac