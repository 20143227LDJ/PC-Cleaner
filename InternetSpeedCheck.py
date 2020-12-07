from speedtest import Speedtest  # 인터넷 속도 측정 모듈

class InternetSpeedCheck:
    def __init__(self):
        super().__init__()
        self.speed = Speedtest()  # 인터넷 속도 측정 객체

    def DownloadSpeedCheck(self):
        download = self.speed.download()
        download_speed = round(download / (10 ** 6), 2)
        return str(download_speed)

    def UploadSpeedCheck(self):
        upload = self.speed.upload()
        upload_speed = round(upload / (10 ** 6), 2)
        return str(upload_speed)

