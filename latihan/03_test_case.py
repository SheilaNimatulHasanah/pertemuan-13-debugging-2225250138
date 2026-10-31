def status_lulus(nilai):
    if nilai >= 60:  # Perbaikan operator pembanding (> menjadi >=)
        return "Lulus"
    return "Tidak lulus"

# Pengujian test case
print("59 ->", status_lulus(59))
print("60 ->", status_lulus(60))
print("61 ->", status_lulus(61))