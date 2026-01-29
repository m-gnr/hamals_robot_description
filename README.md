# Robot Teknik Bilgileri (Özet)

## Genel Yapı

- **Sürüş tipi:** Diferansiyel sürüş
- **Teker düzeni:**
    - 2 adet tahrik tekeri (sağ–sol)
    - 2 adet pasif bilye teker (denge amaçlı)
- **Referans koordinat sistemi:**
    - `base_link` → şasenin geometrik merkezi
    - X: ileri, Y: sol, Z: yukarı

---

## Tahrik Tekerlekleri

- **Teker yarıçapı:** `3.5 cm`
- **Teker kalınlığı (yerle temas eden):** `3.9 cm`
- **Sağ–sol teker merkezleri arası mesafe:** `18.0 cm`
    - Sol teker: `Y = +9.0 cm`
    - Sağ teker: `Y = -9.0 cm`
- **Teker merkezinin yerden yüksekliği:** `3.5 cm`

---

## Şase (Base)

- **Şekil:** Dikdörtgen prizma

### Üstten Görünüm

- **Uzunluk (X):** `22.0 cm`
- **Genişlik (Y):** `15.6 cm`

### Yandan Görünüm

- **Toplam yükseklik:** `9.0 cm`
- **Yerden şase altı boşluk:** `~1.8 cm`
- **Şase merkezinin yerden yüksekliği (yaklaşık):** `6.3 cm`

---

## LiDAR Sistemi

### LiDAR Yuvası (3D Print)

- **Yükseklik:** `1.5 cm`
- **Genişlik:** `6.0 cm`
- **Konum:** Şasenin tam merkezi

### LiDAR

- **Yükseklik:** `3.0 cm`
- **Genişlik:** `6.2 cm`
- **Konum:**
    - X = `0`, Y = `0`
    - Z ≈ `9.3 cm`
- **Tarama düzlemi:** Şase orijini (X–Y) ile hizalı

---

## Bilye Tekerler (Caster Wheels)

- **Adet:** 2
- **Yarıçap:** `1.5 cm`
- **Konum:**
    - Kısa kenarlardan merkeze doğru `3 cm` geride
    - X ≈ `±8.0 cm`
    - Sağ–sol simetrik
- **Görev:** Denge, hareket iletmez