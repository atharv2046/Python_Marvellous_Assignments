import os
import time
import shutil
import schedule 
import datetime


def backup_file():
    source_file = "important_data.txt"
    backup_folder = "Backup"


    os.makedirs(backup_folder, exist_ok=True)

    timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
    backup_filename = f"{os.path.splitext(source_file)[0]}_{timestamp}.bak"
    backup_path = os.path.join(backup_folder, backup_filename)


    try:
        shutil.copy2(source_file, backup_path)
        log_entry = f"[{timestamp}] Backup successful: {backup_filename}\n"
    except Exception as e:
        log_entry = f"[{timestamp}] Backup failed: {e}\n"

    with open("backuplog.txt", "a") as log_file:
        log_file.write(log_entry)

    print(log_entry.strip())

schedule.every().hour.do(backup_file)

if __name__ == "__main__":
    print("Backup scheduler started...")
    while True:
        schedule.run_pending()
        time.sleep(1)
