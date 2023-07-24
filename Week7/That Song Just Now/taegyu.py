def solution(m, musicinfos):
    m = m.replace("C#", "c").replace("D#", "d").replace("F#", "f").replace("G#", "g").replace("A#", "a")

    result = []
    for info in musicinfos:
        start, end, title, melody = info.split(",")
        melody = melody.replace("C#", "c").replace("D#", "d").replace("F#", "f").replace("G#", "g").replace("A#", "a")

        duration = (int(end[:2]) - int(start[:2]))*60 + int(end[3:]) - int(start[3:])
        played = melody*(duration//len(melody)) + melody[:duration%len(melody)]
        
        if m in played:
            result.append((duration, title, played))

    if result:
        result.sort(key = lambda x: -x[0])
        print(result)
        return result[0][1]
    
    return "(None)"

solution("ABC", ["12:00,12:14,HELLO,C#DEFGAB", "13:00,13:05,WORLD,ABCDEF"])