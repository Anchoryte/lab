time_second = int(input())
HH = time_second // 3600
MM = (time_second - (HH*3600)) // 60
SS = ((time_second - (HH*3600)) - (MM*60))
print(f"{HH:02d}:{MM :02d}:{SS:02d}")


