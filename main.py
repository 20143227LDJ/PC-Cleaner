import os
import shutil
import subprocess
import sys
from os import listdir

# UI
from PyQt5.QtCore import *
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import *

# 사용자 정의 모듈
from ProcessClean import ProcessClean  # 프로세스 정리 모듈
from InternetSpeedCheck import InternetSpeedCheck  # 인터넷 속도 측정 모듈
from DeleteInternetSearch import DeleteInternetSearch  # 인터넷 검색 기록 삭제 모듈
from MalwareVaccine import MalwareVaccine  # 멀웨어 탐색/제거 모듈


class MyApp(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()
        self.dialog_btn1Event = QDialog()  # 추가(신은철) - 서비스관리
        self.dialog_btn2Event = QDialog()  # 추가(신은철) - 파일삭제
        self.dialog_btn3Event = QDialog()  # 추가(신은철) - 임시파일제거
        self.dialog_btn4Event = QDialog()  # 추가(신은철) - 임시파일제거
        self.runServiceDialog = QDialog()  # 추가(신은철) - 서비스관리-모달
        self.removefileDialog = QDialog()  # 추가(신은철) - 파일삭제
        self.dialog_btn5Event = QDialog()  # 추가(이동준) - 프로세스 정리 다이얼로그
        self.dialog_btn6Event = QDialog()  # 추가(이동준) - 인터넷 속도 측정 다이얼로그
        self.dialog_btn7Event = QDialog()  # 추가(이동준) - 인터넷 검색 기록 삭제 다이얼로그
        self.dialog_btn8Event = QDialog()  # 추가(이동준) - 멀웨어 탐색/제거 다이얼로그
        self.chromeClicked_dialog = QDialog()  # 추가(이동준) - 크롬 선택시 다이얼로그
        self.whaleClicked_dialog = QDialog()  # 추가(이동준) - 웨일 선택시 다이얼로그

        # 프로세스 정리
        self.PC = ProcessClean()  # 추가(이동준) - ProcessClean 모듈 객체 생성
        self.tb2 = QTextBrowser(self.dialog_btn5Event)  # 추가(이동준) - 프로세스 정리 다이얼로그

        # 인터넷 속도 측정
        self.ISC = InternetSpeedCheck()  # 추가(이동준) - InternetSpeedCheck 모듈 객체 생성
        self.download_speed = 0.0  # 추가(이동준) - 인터넷 속도 측정 변수(다운로드 속도)
        self.upload_speed = 0.0  # 추가(이동준) - 인터넷 속도 측정 변수(업로드 속도)
        self.download_label = QLabel('                  ', self.dialog_btn6Event)  # 추가(이동준) - 다운로드, 업로드 속도 라벨
        self.upload_label = QLabel('                  ', self.dialog_btn6Event)  # 추가(이동준) - 문자열 크기를 정적으로 받음
        self.pbar = QProgressBar(self.dialog_btn6Event)  # 인터넷 속도 측정 ProgressBar

        # 인터넷 검색 기록 삭제
        self.DIS = DeleteInternetSearch()  # 추가(이동준) - 인터넷 검색 기록 모듈 객체 생성
        self.chromeClicked_tb = QTextBrowser(self.chromeClicked_dialog)
        self.whaleClicked_tb = QTextBrowser(self.whaleClicked_dialog)
        # 멀웨어 탐색/제거
        self.vaccine_label = QLabel('탐색 대기중...          ', self.dialog_btn8Event)  # 추가(이동준) - 백신 라벨
        self.treatmentButton = QPushButton("치료", self.dialog_btn8Event)  # 추가(이동준) - 백신 다이얼로그 치료 버튼
        self.targetFile = ''  # 추가(이동준) - 타겟 파일 경로 저장할 변수

    # 서비스 실행 명령어
    def inputRunServiceText(self, lineedit):
        subprocess.call('/user:Administrator powershell Start-Service -Name "' + lineedit.text() + '"')

    # 서비스 중지 명령어
    def inputStopServiceText(self, lineedit):
        subprocess.call('powershell Start-Service -Name "' + lineedit.text() + '"')

    # 서비스실행함수
    def runService(self):
        label1 = QLabel('실행시킬 서비스 입력', self.runServiceDialog)
        label1.setAlignment(Qt.AlignCenter)
        label1.setGeometry(5, 10, 150, 20)
        inputservice = QLineEdit(self.runServiceDialog)
        inputservice.move(10, 40)
        inputservice.show()
        label1.show()
        inputservice.setWindowModality(Qt.ApplicationModal)
        btnInput = QPushButton("Run", self.runServiceDialog)
        btnInput.move(100, 70)
        btnInput.clicked.connect(lambda: self.inputRunServiceText(inputservice))

        self.runServiceDialog.show()

    # 서비스 중지 함수
    def stopService(self):
        label1 = QLabel('정지시킬 서비스 입력', self.stopServiceDialog)
        label1.setAlignment(Qt.AlignCenter)
        label1.setGeometry(5, 10, 150, 20)
        input = QLineEdit(self.stopServiceDialog)
        input.move(10, 40)

        input.show()
        label1.show()
        input.setWindowModality(Qt.ApplicationModal)
        btnInput = QPushButton("Stop", self.stopServiceDialog)
        btnInput.move(100, 70)

        btnInput.clicked.connect(lambda: self.inputStopServiceText(input))

        self.stopServiceDialog.show()

    # 파일삭제 함수
    def removeFile(self, folder_path, extension):

        msg = QMessageBox()
        msg.setWindowTitle("Remove File")

        path = folder_path
        ext = extension.text()

        if not path.endswith("\\"):
            path = path + "\\"

        for file_name in listdir(path):
            if file_name.endswith(ext):
                os.remove(path + file_name)
                msg.setText("remove complete")

        result = msg.exec_()

    # 서비스 관리 이벤트
    def btn1Event(self):

        tb = QTextBrowser(self.dialog_btn1Event)
        self.dialog_btn1Event.setWindowTitle('서비스 관리')
        self.dialog_btn1Event.resize(710, 300)
        self.dialog_btn1Event.show()
        tb.resize(600, 300)
        btnRun = QPushButton("Run service", self.dialog_btn1Event)
        btnRun.setCheckable(True)
        btnRun.move(610, 20)
        btnRun.clicked.connect(lambda: self.runService())
        btnRun.show()
        btnStop = QPushButton("Stop service", self.dialog_btn1Event)
        btnStop.setCheckable(True)
        btnStop.move(610, 60)
        btnStop.clicked.connect(lambda: self.stopService())
        btnStop.show()

        try:
            file_path = 'C:/Users/' + os.getlogin() + '/Desktop/makers/service.txt'
            subprocess.call('powershell Get-Service | Out-File -FilePath ' + file_path)

            file = open(file_path, "r", encoding="utf-16")
            while (True):
                str = file.readline()
                tb.append(str)
                if file.readline() == '':
                    break

        except Exception as e:
            print(e)
            tb.append('Access Denied: %s')

    # 파일 정리 이벤트
    def btn2Event(self):
        self.dialog_btn2Event.setWindowTitle('파일삭제')
        self.dialog_btn2Event.resize(200, 150)
        label1 = QLabel('삭제할 확장자 입력', self.dialog_btn2Event)
        label1.setAlignment(Qt.AlignCenter)
        label1.setGeometry(5, 30, 150, 20)
        folder_path = QFileDialog.getExistingDirectory(self.dialog_btn2Event)
        extension = QLineEdit(self.dialog_btn2Event)
        extension.move(10, 60)
        btnRun = QPushButton("삭제", self.dialog_btn2Event)
        btnRun.setCheckable(True)
        btnRun.move(100, 90)
        btnRun.clicked.connect(lambda: self.removeFile(folder_path, extension))
        extension.show()
        btnRun.show()
        self.dialog_btn2Event.show()

    # 임시파일 제거 이벤트
    def btn3Event(self):  # 신은철 임시파일 제거

        tb = QTextBrowser(self.dialog_btn3Event)
        self.dialog_btn3Event.setWindowTitle('임시파일 정리')
        self.dialog_btn3Event.setWindowModality(Qt.ApplicationModal)
        self.dialog_btn3Event.resize(350, 200)
        self.dialog_btn3Event.show()

        folder = 'C:/Users/' + os.getlogin() + '/AppData/Local/Temp'

        deleteFileCount = 0
        deleteFolderCount = 0

        for the_file in os.listdir(folder):
            file_path = os.path.join(folder, the_file)

            indexNo = file_path.find('\\')
            itemName = file_path[indexNo + 1:]
            try:
                if os.path.isfile(file_path):
                    os.unlink(file_path)
                    tb.append('%s file deleted' % itemName)
                    deleteFileCount = deleteFileCount + 1

                elif os.path.isdir(file_path):
                    if file_path.__contains__('chocolatey'):  continue
                    shutil.rmtree(file_path)
                    tb.append('%s file deleted' % itemName)
                    deleteFolderCount = deleteFolderCount + 1

            except Exception as e:
                tb.append('Access Denied: %s' % itemName)
            tb.append('%s file deleted' % deleteFileCount)

    # 시작 프로그램 관리 이벤트
    def btn4Event(self):
        tb = QTextBrowser(self.dialog_btn4Event)
        self.dialog_btn4Event.setWindowTitle('서비스 관리')
        self.dialog_btn4Event.resize(600, 300)
        self.dialog_btn4Event.show()
        tb.resize(600, 300)

        try:
            file_path = 'C:/Users/' + os.getlogin() + '/Desktop/makers/startup.txt'
            subprocess.call('powershell Get-CimInstance Win32_StartupCommand | Out-File -FilePath ' + file_path)

            file = open(file_path, "r", encoding="utf-16")
            while (True):
                str = file.readline()
                tb.append(str)
                if file.readline() == '':
                    break

        except Exception as e:
            print(e)
            tb.append('Access Denied: %s')

    ###########################################################################
    # 프로세스 정리 이벤트
    def btn5Event(self):
        processList = self.PC.processList()

        processList = processList.replace('[', '').replace(']', '').replace(',', '\n')

        download_label_text = QLabel('현재 프로세스 목록', self.dialog_btn5Event)
        upload_label_text = QLabel('종료된 프로세스 목록', self.dialog_btn5Event)
        download_label_text.move(90, 18)
        upload_label_text.move(345, 18)

        tb = QTextBrowser(self.dialog_btn5Event)
        tb.append(str(processList))
        tb.move(5, 40)
        self.tb2.move(270, 40)

        btnDialog = QPushButton("정리", self.dialog_btn5Event)
        btnDialog.move(230, 255)
        btnDialog.clicked.connect(self.dialog_clean)  # 정리 버튼 이벤트 처리

        self.dialog_btn5Event.setWindowTitle('프로세스 정리')
        self.dialog_btn5Event.setWindowModality(Qt.ApplicationModal)
        self.dialog_btn5Event.resize(550, 300)
        self.dialog_btn5Event.show()

    # 프로세스 정리 다이얼로그 - 정리 버튼 이벤트
    def dialog_clean(self):
        killProgramList = self.PC.processKill()
        for ProcessName in killProgramList:
            self.tb2.append(ProcessName)

    # 인터넷 속도 측정 이벤트
    def btn6Event(self):
        download_label_text = QLabel('다운로드 속도 : ', self.dialog_btn6Event)
        upload_label_text = QLabel('업로드 속도 : ', self.dialog_btn6Event)
        download_label_text.move(11, 15)
        upload_label_text.move(22, 50)

        self.download_label.move(102, 15)
        self.upload_label.move(102, 50)

        self.pbar.setGeometry(0, 110, 235, 10)

        btnDialog = QPushButton("측정", self.dialog_btn6Event)
        btnDialog.move(70, 75)
        btnDialog.clicked.connect(self.dialog_check)  # 측정 버튼 이벤트 처리

        self.dialog_btn6Event.setWindowTitle('인터넷 속도')
        self.dialog_btn6Event.setWindowModality(Qt.ApplicationModal)
        self.dialog_btn6Event.resize(200, 120)
        self.dialog_btn6Event.show()

    # 인터넷 속도 측정 다이얼로그 - 측정 버튼 이벤트
    def dialog_check(self):
        self.download_speed = self.ISC.DownloadSpeedCheck()
        self.upload_speed = self.ISC.UploadSpeedCheck()
        self.download_label.setText(str(self.download_speed) + 'Mbps')
        self.upload_label.setText(str(self.upload_speed) + 'Mbps')
        self.pbar.setValue(100)
        self.download_label.repaint()
        self.upload_label.repaint()

    # 인터넷 검색 기록 삭제 이벤트
    def btn7Event(self):
        btnDialog = QPushButton("크롬", self.dialog_btn7Event)
        btnDialog.move(15, 20)
        btnDialog.clicked.connect(self.chromeClicked)  # 크롬 버튼 이벤트 처리

        btnDialog = QPushButton("웨일", self.dialog_btn7Event)
        btnDialog.move(100, 20)
        btnDialog.clicked.connect(self.whaleClicked)  # 웨일 버튼 이벤트 처리

        self.dialog_btn7Event.setWindowTitle('인터넷 선택')
        self.dialog_btn7Event.setWindowModality(Qt.ApplicationModal)
        self.dialog_btn7Event.resize(190, 60)
        self.dialog_btn7Event.show()

    def chromeClicked(self):
        browser = self.DIS.getChromePath()
        self.DIS.getInternetHistory(browser)

        download_label_text = QLabel('크롬 검색 기록', self.chromeClicked_dialog)
        download_label_text.move(90, 18)
        self.chromeClicked_tb.clear()

        file = open('history.txt', "r", -1, 'utf-8')
        while True:
            str = file.readline()
            self.chromeClicked_tb.append(str)
            if file.readline() == '':
                break

        self.chromeClicked_tb.move(5, 40)

        btnDialog = QPushButton("기록 삭제", self.chromeClicked_dialog)
        btnDialog.move(95, 250)
        btnDialog.clicked.connect(self.chromeHistoryDeleteClicked)  # 삭제 버튼 이벤트 처리

        self.chromeClicked_dialog.setWindowTitle('크롬 검색 기록')
        self.chromeClicked_dialog.setWindowModality(Qt.ApplicationModal)
        self.chromeClicked_dialog.resize(270, 300)
        self.chromeClicked_dialog.show()

    def whaleClicked(self):
        browser = self.DIS.getWhalePath()
        self.DIS.getInternetHistory(browser)

        download_label_text = QLabel('웨일 검색 기록', self.whaleClicked_dialog)
        download_label_text.move(90, 18)
        self.whaleClicked_tb.clear()

        file = open('history.txt', "r", -1, 'utf-8')
        while True:
            str = file.readline()
            self.whaleClicked_tb.append(str)
            if file.readline() == '':
                break

        self.whaleClicked_tb.move(5, 40)

        btnDialog = QPushButton("기록 삭제", self.whaleClicked_dialog)
        btnDialog.move(95, 250)
        btnDialog.clicked.connect(self.whaleHistoryDeleteClicked)  # 삭제 버튼 이벤트 처리

        self.whaleClicked_dialog.setWindowTitle('웨일 검색 기록')
        self.whaleClicked_dialog.setWindowModality(Qt.ApplicationModal)
        self.whaleClicked_dialog.resize(270, 300)
        self.whaleClicked_dialog.show()

    def chromeHistoryDeleteClicked(self):
        self.DIS.deleteHistory()
        self.chromeClicked_tb.append('')
        self.chromeClicked_tb.clear()

    def whaleHistoryDeleteClicked(self):
        self.DIS.deleteHistory()
        self.whaleClicked_tb.append('')
        self.whaleClicked_tb.clear()

    # 멀웨어 탐색/제거 이벤트
    def btn8Event(self):
        openFileButton = QPushButton("파일 열기", self.dialog_btn8Event)
        openFileButton.clicked.connect(self.openFileClicked)

        self.treatmentButton = QPushButton("제거", self.dialog_btn8Event)
        self.treatmentButton.move(65, 90)
        self.treatmentButton.hide()  # 버튼 안보이게 설정
        self.treatmentButton.clicked.connect(self.treatmentClicked)

        self.vaccine_label.move(65, 50)

        self.dialog_btn8Event.setWindowTitle('멀웨어 탐색')
        self.dialog_btn8Event.setWindowModality(Qt.ApplicationModal)
        self.dialog_btn8Event.resize(200, 120)
        self.dialog_btn8Event.show()

    def openFileClicked(self):
        self.targetFile = QFileDialog.getOpenFileName(self.dialog_btn8Event)  # targetFile 변수에 파일 경로 저장


        MV = MalwareVaccine()
        if MV.matchingVirus(self.targetFile[0]):  # 반환값이 True면 바이러스, False면 일반 파일
            self.vaccine_label.setText('바이러스 파일입니다.')
            self.vaccine_label.setStyleSheet("color: red;")
            self.vaccine_label.move(50, 50)
            self.treatmentButton.show()  # 바이러스 파일 발견시 버튼 보이게 설정
            self.vaccine_label.repaint()
        else:
            self.vaccine_label.setText('일반 파일입니다.')
            self.vaccine_label.setStyleSheet("color: green;")
            self.vaccine_label.move(55, 50)
            self.vaccine_label.repaint()

    def treatmentClicked(self):
        os.chmod(self.targetFile[0], 0o0777)  # 파일이 읽기전용인 경우 chmod를 해주고 ######### 임시 주석 처리
        os.remove(self.targetFile[0])  # 파일을 강제 삭제

    def initUI(self):
        grid = QGridLayout()
        self.setLayout(grid)

        btn1 = QPushButton('서비스 관리', self)
        btn2 = QPushButton('파일 정리', self)
        btn3 = QPushButton('임시파일 제거', self)
        btn4 = QPushButton('시작 프로그램 관리', self)
        btn5 = QPushButton('프로세스 정리', self)
        btn6 = QPushButton('인터넷 속도 측정', self)
        btn7 = QPushButton('인터넷 검색 기록 삭제', self)
        btn8 = QPushButton('멀웨어 탐색/제거', self)

        grid.addWidget(btn1, 0, 0)
        grid.addWidget(btn2, 1, 0)
        grid.addWidget(btn3, 2, 0)
        grid.addWidget(btn4, 3, 0)
        grid.addWidget(btn5, 0, 1)
        grid.addWidget(btn6, 1, 1)
        grid.addWidget(btn7, 2, 1)
        grid.addWidget(btn8, 3, 1)

        btn1.clicked.connect(self.btn1Event)
        btn2.clicked.connect(self.btn2Event)
        btn3.clicked.connect(self.btn3Event)
        btn4.clicked.connect(self.btn4Event)
        btn5.clicked.connect(self.btn5Event)
        btn6.clicked.connect(self.btn6Event)
        btn7.clicked.connect(self.btn7Event)
        btn8.clicked.connect(self.btn8Event)

        self.setWindowTitle('PC Cleaner')
        self.setWindowIcon(QIcon('Cleaner.png'))
        self.setGeometry(300, 300, 300, 200)
        self.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())
