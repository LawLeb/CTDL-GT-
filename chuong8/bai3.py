class BaiHat:
    def __init__(self, ten_bai_hat, ten_nhac_si, ten_ca_si):
        self.ten_bai_hat = ten_bai_hat
        self.ten_nhac_si = ten_nhac_si
        self.ten_ca_si = ten_ca_si

class Album:
    def __init__(self, ten_album):
        self.ten_album = ten_album
        self.danh_sach_bai_hat = []

    def them_bai_hat(self, bai_hat):
        self.danh_sach_bai_hat.append(bai_hat)

class TuDien:
    def __init__(self):
        self.albums = {}

    def hash_function(self, ten_album):
        return hash(ten_album)

    def NhapAlbum(self, ten_album, danh_sach_bai_hat):
        hash_value = self.hash_function(ten_album)
        if hash_value not in self.albums:
            self.albums[hash_value] = Album(ten_album)
        for bai_hat in danh_sach_bai_hat:
            self.albums[hash_value].them_bai_hat(bai_hat)

    def XemAlbum(self, ten_album):
        hash_value = self.hash_function(ten_album)
        if hash_value in self.albums:
            album = self.albums[hash_value]
            print("Tên album:", album.ten_album)
            print("Danh sách bài hát:")
            for bai_hat in album.danh_sach_bai_hat:
                print("- Tên bài hát:", bai_hat.ten_bai_hat)
                print("  Nhạc sĩ sáng tác:", bai_hat.ten_nhac_si)
                print("  Ca sĩ:", bai_hat.ten_ca_si)
        else:
            print("Không tìm thấy album có tên", ten_album)

# Test
tudien = TuDien()
danh_sach_bai_hat_album1 = [BaiHat("Hãy trao cho anh", "Sơn Tùng M-TP", "Sơn Tùng M-TP"),
                             BaiHat("Em của ngày hôm qua", "Sơn Tùng M-TP", "Sơn Tùng M-TP")]
tudien.NhapAlbum("M-TP", danh_sach_bai_hat_album1)

danh_sach_bai_hat_album2 = [BaiHat("Chạy ngay đi", "Sơn Tùng M-TP", "Sơn Tùng M-TP"),
                             BaiHat("Nắng ấm xa dần", "Sơn Tùng M-TP", "Sơn Tùng M-TP")]
tudien.NhapAlbum("Chạy ngay đi", danh_sach_bai_hat_album2)

tudien.XemAlbum("M-TP")
tudien.XemAlbum("Chạy ngay đi")
tudien.XemAlbum("Không phải dạng vừa đâu")
