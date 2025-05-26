import pickle
import os
def input_scores():
    scores = []
    i = 0
    while True:
        score = int(input(f'#{i+1}? '))
        if score < 0:
            break
        scores.append(score)
        i += 1
    return scores

def get_average(scores):
    return sum(scores) / len(scores)

def show_scores(scores):
    print('[점수 출력]')
    print('개인점수:', sum(scores))

def save_scores(filename, scores):
    with open(filename, 'wb') as file:
        pickle.dump(scores, file)

def load_scores(filename):
    with open(filename, 'rb') as file:
        existing_file = pickle.load(file)
        return existing_file

filename = 'score.bin'

if not os.path.exists(filename):
    scores= input_scores()
    show_scores(scores)
    print(f'평균: {get_average(scores):.1f}')
    save_scores(filename, scores)
else:
    existing_file = load_scores(filename)
    print('[파일 읽기]\n')
    show_scores(existing_file)
    print(f'평균: {get_average(existing_file):.1f}')