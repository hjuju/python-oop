from bs4 import BeautifulSoup
from urllib.request import urlopen
class BugsMusic(object):

    url = ''

    def __str__(self):
        return self.url

# 벅스: https://music.bugs.co.kr/chart/track/realtime/total?wl_ref=M_contents_03_01

    @staticmethod
    def get_ranking(soup, musicinfo):
        count = 0
        print(f'----------------------{musicinfo} ranking-------------------------')
        for i in soup.find_all(name='p', attrs=({"class": musicinfo})):
            count += 1
            print(f'{str(count)}위) {musicinfo}: {i.find("a").text}')

    @staticmethod
    def main():
        bugs = BugsMusic()
        while 1:
            menu = (input('0. 프로그램 종료\n1. URL 입력\n2. 음악 순위\n숫자입력: '))
            if menu == '0':
                print('프로그램을 종료 합니다.')
                break
            elif menu == '1':
                bugs.url = input('URL 입력: ')
            elif menu == '2':
                print(f'URL: {bugs}')
                soup = BeautifulSoup(urlopen(bugs.url), 'lxml')
                BugsMusic.get_ranking(soup, input('artist or title: '))
            else:
                print('잘못된 선택 입니다.')
                continue


BugsMusic.main()
