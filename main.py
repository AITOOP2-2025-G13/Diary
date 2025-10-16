from diaries.DiarySample import DiarySample
from diaries.HoshimiDiary import HoshimiDiary
from diaries.KarotoDiary import KarotoDiary

# ↓のリストには、メンバーの各日記が格納されます。
diaries = [DiarySample(),
           HoshimiDiary(), 
           KarotoDiary()]

for d in diaries:
    print("---------------------------------")
    print(d.get_date())
    print(d.get_summary())
    print(d.get_author())
    print()