from diaries.AbstractDiary import AbstractDiary

class KamataDiary(AbstractDiary):

    def get_date(self):
        return "2025-10-16"
    
    def get_summary(self):
        return """
        オブジェクト演習のグループワークをした。
よくわからないことだらけだった。教えてもらいながら、なんとかできた。
"""

    def get_author(self):
        return "Kamata"