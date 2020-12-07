import psutil
import os


class ProcessClean:
    def __init__(self):
        super().__init__()

    def processList(self):
        processList = []
        for proc in psutil.process_iter():
            try:
                # 프로세스 이름 가져오기
                processName = proc.name()
                processList += [processName]
                # print(processList) # 리스트에 프로세스 값 들어가는지 확인

            except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):  # 예외처리
                pass
        return str(processList)

    def processKill(self):
        killProgramTargetList = ['notepad.exe', 'SnippingTool.exe']
        killProgramList = []
        for programName in killProgramTargetList:
            for proc in psutil.process_iter():
                try:
                    if programName == proc.name():
                        os.system('taskkill /f /im ' + programName)  # 해당 프로세스 종료
                        killProgramList.append(programName)  # 종료한 프로세스 리스트에 저장
                except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):  # 예외처리
                    pass
        return killProgramList


'''
if __name__ == '__main__':
    PC = ProcessClean()
    PC.processKill()
'''

