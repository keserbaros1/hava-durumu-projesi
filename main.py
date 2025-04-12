def ortalama_hesapla(notlar):
    if not notlar:
        return 0
    return sum(notlar) / len(notlar)


if __name__ == "__main__":
    ders_sayisi = int(input("Kaç tane dersiniz var? "))
    notlar = []

    for i in range(ders_sayisi):
        n = float(input(f"{i+1}. dersin notunu girin: "))
        notlar.append(n)

    ort = ortalama_hesapla(notlar)
    print(f"Not ortalamanız: {ort:.2f}")

