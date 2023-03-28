def solution(wallpaper):
    lux, luy, rdx, rdy = 50, 50, 0, 0 

    for i, v in enumerate(wallpaper):
        if "#" in v:
            lux = min(lux, i)
            rdx = max(rdx, i)
            luy = min(luy, v.find("#"))
            rdy = max(rdy, v.rfind("#"))

    return [lux, luy, rdx+1, rdy+1]
