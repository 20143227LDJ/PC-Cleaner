import sqlite3
import sys
import os


class DeleteInternetSearch:
    def __init__(self):
        super().__init__()
        self.path = None
        self.conn = None
        self.cur = None

    def getChromePath(self):
        return "~\\AppData\\Local\\Google\\Chrome\\User Data\\Default\\History"

    def getWhalePath(self):
        return "~\\AppData\\Local\\Naver\\Naver Whale\\User Data\\Profile 1\\History"

    def getInternetHistory(self, ChoiceBrowser):
        self.path = os.path.expanduser(ChoiceBrowser)  # 해당 브라우저 킨 상태로는 안열어짐
        self.conn = sqlite3.connect(self.path)
        self.cur = self.conn.cursor()
        historyList = []

        sql = f"select title FROM urls"
        text = open('history.txt', 'w', -1, 'utf-8')
        for row in self.cur.execute(sql):
            historyList += row
            strtest = str(row).replace('(', '').replace(')', '').rstrip(',')
            text.write(strtest + '\n')

        text.close()
        return str(historyList)

    def deleteHistory(self):
        self.cur.execute('DELETE FROM urls')
        self.conn.commit()


if __name__ == '__main__':
    DIS = DeleteInternetSearch()
    browser = DIS.getChromePath()
    historyList = DIS.getInternetHistory(browser)
    #DIS.deleteHistory()
    #print(historyList)
    file = open('history.txt', "r", -1, 'utf-8')
    while True:
        str = file.readline()
        print(str)
        if file.readline() == '':
            break

