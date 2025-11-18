# Bubble Sort untuk mengurutkan nilai ujian siswa dari yang terendah ke tertinggi

def bubble_sort_students(students):
    """
    students: list berisi tuple (nama, nilai)
    return: list terurut ascending berdasarkan nilai
    """
    A = students[:]      # duplikasi list agar data asli tidak berubah
    n = len(A)

    while n > 1:
        swapped = False
        for i in range(1, n):
            # bandingkan berdasarkan nilai (index 1)
            if A[i-1][1] > A[i][1]:
                A[i-1], A[i] = A[i], A[i-1]
                swapped = True
        
        if not swapped:
            break  # sudah terurut, hentikan loop

        n -= 1

    return A


# --------------------------
# CONTOH PEMAKAIAN PROGRAM
# --------------------------

students = [
    ("Jeki", 72),
    ("Pir", 65),
    ("Ridho", 88),
    ("Adit", 50),
    ("Gilang", 77)
]

print("Data sebelum diurutkan:")
for s in students:
    print(f"{s[0]} - {s[1]}")

sorted_students = bubble_sort_students(students)

print("\nData setelah diurutkan (ascending):")
for s in sorted_students:
    print(f"{s[0]} - {s[1]}")
