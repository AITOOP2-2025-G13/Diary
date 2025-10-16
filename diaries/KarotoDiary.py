from diaries.AbstractDiary import AbstractDiary

class KarotoDiary(AbstractDiary):

    def get_date(self):
        return "2025-10-16"
    
    def get_summary(self):
        return "先週は、５連休だった。そのため、今週は学校に来るのが辛い。" \
        "しかし、切り替えて頑張ろうと思う。"
    
    def get_author(self):
        return "Karoto"