def grades(nilai):
	nama = input("Masukkan nama: ")
	jurusan = input("Masukkan Jurusan: ")
	if nilai >= 85:
		grade = "A"
	elif nilai >= 75:
		grade ="B"
	elif nilai >= 65:
		grade = "C"
	else:
		grade = "Mahasiswa ini mendapat grade D dan belum lulus"
	return grade
	
nilai = grades((int(input("Masukkan nilai: "))))
print(nilai)
