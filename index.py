from random import *
game_borad = list()


def word():
    with open('word.txt', 'r') as file:
        data = file.readlines()
        line = randint(1, 250)
        return data[line]
    
    
def Set_game_board():
    print(word_data, word_len)
    for i in range(0, word_len):
        game_borad.append('_')

def Start_game(word_len, word_data):
    print('총 글자 수는 %d개!' % word_len)
    print('총 기회는 10번 한 단어 씩 입력ㄱㄱ')
    for i in range(0, 10):
        word_game = input('한 단어만 입력!')
        for j in range(0, word_len):
            if word_data[j] == word_game:
                print('발견!')
                game_borad[j] = word_game
                print(game_borad)
                if '_' not in game_borad:
                    print('ㅊㅊ 다 맞춤')
                    return 0
            
        
        print('%d/10' % int(i+1))
    print('영어 공부 더 하고 와')
    print(game_borad)    
        
        
    
word_data = word()
word_len = len(word_data) - 1   
start = input('s를 눌러 시작')
if start == 's':
    print("game start!")
    Set_game_board()
    Start_game(word_len, word_data)
  

