import pyautogui
import time
import pyperclip
import os


def initialize():
    # print('Monitor size: ', end='')
    # print(pyautogui.size())  # 바탕화면 크기 측정
    # print(pyautogui.position())  # 마우스 좌표 측정
    filter_keyword = input("우추리 사장 카카오톡 이름 검색:")
    my_msg = input("보낼 메세지:")
    return filter_keyword, my_msg


def filter_friend(filter_keyword):
    # 클릭 전 상태의 아이콘 클릭
    try:
        click_img(img_path + 'beforeClick.png')
        # 클릭 후 상태의 아이콘 클릭
        try:
            click_img(img_path + 'afterClick.png')
        except Exception as e:
            print('Click button not existed', e)
    except Exception as e:
        print("Click button not existed", e)
    # 검색어 입력되어 있으면 X버튼 눌러서 기존 검색 키워드 삭제
    try:
        click_img(img_path + 'x_button.png')
    except:
        pass
    time.sleep(1)
    # 친구 키워드 검색하기 위해 돋보기 그림 클릭
    click_img_plus_x(img_path + 'find_friend.png', 30)
    # 지정한 검색 키워드 복사후 붙여넣기
    pyperclip.copy(filter_keyword)
    pyautogui.hotkey('ctrl', 'v')
    pyautogui.keyDown('down')  # 대화상대칸로 커서 옮기기
    time.sleep(2)

def send_msg(my_msg):
    pyautogui.keyDown('enter')  # 대화방으로 들어가기
    pyperclip.copy(my_msg)  # 메세지 전송
    pyautogui.hotkey('ctrl', 'v')
    pyautogui.keyDown('enter')
    pyautogui.keyDown('esc')  # 대화방 닫기


def click_img(imagePath):
    location = pyautogui.locateCenterOnScreen(imagePath, confidence=conf)
    x, y = location
    pyautogui.click(x, y)


def click_img_plus_x(imagePath, pixel):
    location = pyautogui.locateCenterOnScreen(imagePath, confidence=conf)
    x, y = location
    pyautogui.click(x + pixel, y)


# config
img_path = os.path.dirname(os.path.realpath(__file__)) + '/img/'
conf = 0.90
pyautogui.PAUSE = 0.5

if __name__ == '__main__':
    filter_keyword, my_msg = initialize()
    filter_friend(filter_keyword)
    send_msg(my_msg)



