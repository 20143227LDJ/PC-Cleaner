def btn3Event(self):  # 신은철 임시파일 제거
    tb = QTextBrowser(self)
    self.dialog_btn3Event.setWindowTitle('임시파일제거')
    self.dialog_btn3Event.setWindowModality(Qt.ApplicationModal)
    self.dialog_btn3Event.resize(350, 200)
    self.dialog_btn3Event.show()
    bat_script = r"""
        REG ADD "HKLM\SOFTWARE\Microsoft\Windows\CurrentVersion\Explorer\VolumeCaches\Active Setup Temp Folders" /v StateFlags0108 /d 2 /t REG_DWORD /f
        REG ADD "HKLM\SOFTWARE\Microsoft\Windows\CurrentVersion\Explorer\VolumeCaches\BranchCache" /v StateFlags0108 /d 2 /t REG_DWORD /f
        REG ADD "HKLM\SOFTWARE\Microsoft\Windows\CurrentVersion\Explorer\VolumeCaches\Downloaded Program Files" /v StateFlags0108 /d 2 /t REG_DWORD /f
        REG ADD "HKLM\SOFTWARE\Microsoft\Windows\CurrentVersion\Explorer\VolumeCaches\GameNewsFiles" /v StateFlags0108 /d 2 /t REG_DWORD /f
        REG ADD "HKLM\SOFTWARE\Microsoft\Windows\CurrentVersion\Explorer\VolumeCaches\GameStatisticsFiles" /v StateFlags0108 /d 2 /t REG_DWORD /f
        REG ADD "HKLM\SOFTWARE\Microsoft\Windows\CurrentVersion\Explorer\VolumeCaches\GameUpdateFiles" /v StateFlags0108 /d 2 /t REG_DWORD /f
        REG ADD "HKLM\SOFTWARE\Microsoft\Windows\CurrentVersion\Explorer\VolumeCaches\Internet Cache Files" /v StateFlags0108 /d 2 /t REG_DWORD /f
        REG ADD "HKLM\SOFTWARE\Microsoft\Windows\CurrentVersion\Explorer\VolumeCaches\Memory Dump Files" /v StateFlags0108 /d 2 /t REG_DWORD /f
        REG ADD "HKLM\SOFTWARE\Microsoft\Windows\CurrentVersion\Explorer\VolumeCaches\Offline Pages Files" /v StateFlags0108 /d 2 /t REG_DWORD /f
        REG ADD "HKLM\SOFTWARE\Microsoft\Windows\CurrentVersion\Explorer\VolumeCaches\Old ChkDsk Files" /v StateFlags0108 /d 2 /t REG_DWORD /f
        REG ADD "HKLM\SOFTWARE\Microsoft\Windows\CurrentVersion\Explorer\VolumeCaches\Previous Installations" /v StateFlags0108 /d 2 /t REG_DWORD /f
        REG ADD "HKLM\SOFTWARE\Microsoft\Windows\CurrentVersion\Explorer\VolumeCaches\Recycle Bin" /v StateFlags0108 /d 2 /t REG_DWORD /f
        REG ADD "HKLM\SOFTWARE\Microsoft\Windows\CurrentVersion\Explorer\VolumeCaches\Service Pack Cleanup" /v StateFlags0108 /d 2 /t REG_DWORD /f
        REG ADD "HKLM\SOFTWARE\Microsoft\Windows\CurrentVersion\Explorer\VolumeCaches\Setup Log Files" /v StateFlags0108 /d 2 /t REG_DWORD /f
        REG ADD "HKLM\SOFTWARE\Microsoft\Windows\CurrentVersion\Explorer\VolumeCaches\System error memory dump files" /v StateFlags0108 /d 2 /t REG_DWORD /f
        REG ADD "HKLM\SOFTWARE\Microsoft\Windows\CurrentVersion\Explorer\VolumeCaches\System error minidump files" /v StateFlags0108 /d 2 /t REG_DWORD /f
        REG ADD "HKLM\SOFTWARE\Microsoft\Windows\CurrentVersion\Explorer\VolumeCaches\Temporary Files" /v StateFlags0108 /d 2 /t REG_DWORD /f
        REG ADD "HKLM\SOFTWARE\Microsoft\Windows\CurrentVersion\Explorer\VolumeCaches\Temporary Setup Files" /v StateFlags0108 /d 2 /t REG_DWORD /f
        REG ADD "HKLM\SOFTWARE\Microsoft\Windows\CurrentVersion\Explorer\VolumeCaches\Temporary Sync Files" /V StateFlags0108 /d 2 /t REG_DWORD /f
        REG ADD "HKLM\SOFTWARE\Microsoft\Windows\CurrentVersion\Explorer\VolumeCaches\Thumbnail Cache" /v StateFlags0108 /d 2 /t REG_DWORD /f
        REG ADD "HKLM\SOFTWARE\Microsoft\Windows\CurrentVersion\Explorer\VolumeCaches\Update Cleanup" /v StateFlags0108 /d 2 /t REG_DWORD /f
        REG ADD "HKLM\SOFTWARE\Microsoft\Windows\CurrentVersion\Explorer\VolumeCaches\Upgrade Discarded Files" /v StateFlags0108 /d 2 /t REG_DWORD /f
        REG ADD "HKLM\SOFTWARE\Microsoft\Windows\CurrentVersion\Explorer\VolumeCaches\User file versions" /v StateFlags0108 /d 2 /t REG_DWORD /f
        REG ADD "HKLM\SOFTWARE\Microsoft\Windows\CurrentVersion\Explorer\VolumeCaches\Windows Defender" /v StateFlags0108 /d 2 /t REG_DWORD /f
        REG ADD "HKLM\SOFTWARE\Microsoft\Windows\CurrentVersion\Explorer\VolumeCaches\Windows Error Reporting Archive Files" /v StateFlags0108 /d 2 /t REG_DWORD /f
        REG ADD "HKLM\SOFTWARE\Microsoft\Windows\CurrentVersion\Explorer\VolumeCaches\Windows Error Reporting Queue Files" /v StateFlags0108 /d 2 /t REG_DWORD /f
        REG ADD "HKLM\SOFTWARE\Microsoft\Windows\CurrentVersion\Explorer\VolumeCaches\Windows Error Reporting System Archive Files" /v StateFlags0108 /d 2 /t REG_DWORD /f
        REG ADD "HKLM\SOFTWARE\Microsoft\Windows\CurrentVersion\Explorer\VolumeCaches\Windows Error Reporting System Queue Files" /v StateFlags0108 /d 2 /t REG_DWORD /f
        REG ADD "HKLM\SOFTWARE\Microsoft\Windows\CurrentVersion\Explorer\VolumeCaches\Windows ESD installation files" /v StateFlags0108 /d 2 /t REG_DWORD /f
        REG ADD "HKLM\SOFTWARE\Microsoft\Windows\CurrentVersion\Explorer\VolumeCaches\Windows Upgrade Log Files" /v StateFlags0108 /d 2 /t REG_DWORD /f"""

    current_user = os.environ['USERPROFILE']

    def diskUsage():
        try:
            _, _, free = shutil.disk_usage(current_user[0:3])
            free = free
            return free
        except Exception as ex:
            tb.append("Error in diskUsage=" + str(ex))

    def cleaned(bfs, afs):
        tfs = afs - bfs
        return tfs

    def deleteBatScript():
        try:
            os.remove("bat.bat")
        except Exception as ex:
            tb.append("Error in deleteBatScript=" + str(ex))

    def createBatScript():
        try:
            with open('bat.bat', 'w') as file:
                file.write(self.bat_script)
            subprocess.call("powershell.exe Start-Process bat.bat -Verb runAs")
            time.sleep(2)
            subprocess.call("cleanmgr.exe /sagerun:108")
            self.deleteBatScript()
        except Exception as ex:
            tb.append("Error in createBatScript=" + str(ex))

    def cleanup():
        try:
            temp_folder = os.path.join(current_user, 'AppData', 'Local', 'temp', '')
            temp2_folder = os.path.join(current_user[0:3], 'Windows', 'Temp', '')
            temp3_folder = os.path.join(current_user, 'Temp', '')

            folders = [temp_folder, temp2_folder, temp3_folder]

            for folder in folders:
                if os.path.exists(folder):
                    shutil.rmtree(folder, ignore_errors=True)
            subprocess.call('powershell.exe Clear-RecycleBin -Force -ErrorAction SilentlyContinue')
        except Exception as ex:
            tb.append("Error in cleanup=" + str(ex))

    try:

        before_free_space = diskUsage()
        tb.append("\n임시파일들을 삭제하는 중입니다.")

        t1 = threading.Thread(target=cleanup)
        t2 = threading.Thread(target=createBatScript)

        t2.start()
        t1.start()

        t1.join()
        t2.join()

        cleanup()

        after_free_space = diskUsage()

        total_cleaned_space = cleaned(before_free_space, after_free_space)
        if total_cleaned_space < 0:
            total_cleaned_space = 0

        tb.append("정리된 파일의 용량 {} MB ".format(total_cleaned_space))
    except Exception as ex:
        tb.append("Error in main=" + str(ex))