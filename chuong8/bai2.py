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

    def DongNghia(self, tu):
        hash_value = self.hash_function(tu)
        return list(self.tu_dong_nghia.get(hash_value, {}).get(tu, {}).values())

    def TraiNghia(self, tu):
        hash_value = self.hash_function(tu)
        return list(self.tu_trai_nghia.get(hash_value, {}).get(tu, {}).values())

# Test
tudien = TuDien()
tudien.NhapTu("mèo", dong_nghia={"meo": "cat"}, trai_nghia={"chó": "dog", "thỏ": "rabbit"})
tudien.NhapTu("chó", dong_nghia={"chó săn": "hunting dog"}, trai_nghia={"mèo": "cat"})

tu_dong_nghia = tudien.DongNghia("mèo")
tu_trai_nghia = tudien.TraiNghia("mèo")

print("Từ đồng nghĩa của 'mèo':", tu_dong_nghia)  # Kết quả: ['cat']
print("Từ trái nghĩa của 'mèo':", tu_trai_nghia)  # Kết quả: ['dog', 'rabbit']
