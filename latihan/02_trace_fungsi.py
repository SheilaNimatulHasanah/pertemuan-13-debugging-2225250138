def hitung_diskon(total, persen):
    diskon = total * persen / 100
    return total - diskon

print(hitung_diskon(200000, 10))