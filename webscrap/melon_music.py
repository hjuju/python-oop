from bs4 import BeautifulSoup

class MelonMusic(object):

    url = ''

    def __str__(self):
        return self.url

    @staticmethod
    def main():
        melon = MelonMusic()
        while 1:
            menu = input('0. 프로그램 종료\n1. URL 입력\n2. 음악 순위\n숫자입력: ')
            if menu == '0':
                print('프로그램을 종료 합니다.')
                break
            elif menu == '1':
                melon.url = input('URL 입력: ')
            elif menu == '2':
                pass



MelonMusic.main()
