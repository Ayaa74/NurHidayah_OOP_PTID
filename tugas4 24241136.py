# class Parent
class MhsAlumni:
    def lulus(self):
        print("Anda sudah lulus")

    def ijazah(self):
        print("Anda memiliki ijazah kelulusan.")


class MhsAktif:
    def aktif(self):
        print("Anda mahasiswa aktif")

    def ktm(self):
        print("Anda memiliki Kartu Tanda Mahasiswa (KTM).")

    def beasiswa(self):
        print("Anda terdaftar sebagai penerima beasiswa.")


# class Child
class aya(MhsAlumni):
    pass


class bunga(MhsAktif):
    pass


class ipha(MhsAlumni, MhsAktif):
    pass



aya = aya()
bunga = bunga()
ipha = ipha()


ipha.ktm()
ipha.ijazah()