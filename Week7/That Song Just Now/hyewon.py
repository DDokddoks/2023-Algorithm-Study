def calcPlayTime(start, end):
    s = list(map(int, start.split(':')))
    e = list(map(int, end.split(':')))
    return (e[0] - s[0]) * 60 + (e[1] - s[1])


def getMelody(m):
    return m.replace('C#', 'c').replace('D#', 'd').replace('F#', 'f').replace('G#', 'g').replace('A#', 'a')


def solution(m, musicinfos):
    answers = []
    for info in musicinfos:
        start, end, title, music = info.split(',')
        music = getMelody(music)
        playTime = calcPlayTime(start, end)
        length = len(music)
        music = music * (playTime // length) + music[:playTime % length]
        if getMelody(m) in music:
            answers.append((title, playTime))
    answers.sort(key=lambda x:-x[1])
    return answers[0][0] if answers else '(None)'
