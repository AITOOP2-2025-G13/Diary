from diaries.AbstractDiary import AbstractDiary
class HoshimiDiary(AbstractDiary):
    def get_date(self):
        return "2025-10-16"
    def get_summary(self):
        return """今日は、日記を作成しました。"""
    def get_author(self):
        return "Hoshimi"