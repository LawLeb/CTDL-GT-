class TuDien:
    def __init__(self):
        self.tu_dong_nghia = {}
        self.tu_trai_nghia = {}

    def hash_function(self, word):
        return word[0]

    def NhapTu(self, tu, dong_nghia=None, trai_nghia=None):
        hash_value = self.hash_function(tu)
        if dong_nghia:
            if hash_value in self.tu_dong_nghia:
                self.tu_dong_nghia[hash_value][tu] = dong_nghia
            else:
                self.tu_dong_nghia[hash_value] = {tu: dong_nghia}
        if trai_nghia:
            if hash_value in self.tu_trai_nghia:
                self.tu_trai_nghia[hash_value][tu] = trai_nghia
            else:
                self.tu_trai_nghia[hash_value] = {tu: trai_nghia}

    def TraTu(self, tu):
        hash_value = self.hash_function(tu)
        dong_nghia = self.tu_dong_nghia.get(hash_value, {}).get(tu, None)
        trai_nghia = self.tu_trai_nghia.get(hash_value, {}).get(tu, None)
        return dong_nghia, trai_nghia

# Test
tudien = TuDien()
tudien.NhapTu("mèo", "cat", "chó")
tudien.NhapTu("chó", "dog", "mèo")
tudien.NhapTu("bút", "pen", "giấy")

tu_dong_nghia, tu_trai_nghia = tudien.TraTu("mèo")
print("Từ đồng nghĩa của 'mèo':", tu_dong_nghia)  # Kết quả: cat
print("Từ trái nghĩa của 'mèo':", tu_trai_nghia)  # Kết quả: chó
