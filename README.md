# HAMAL’S Robot Description

> URDF/Xacro tabanlı robot model paketi.
> 

> Bu paket yalnızca robotun geometrik ve kinematik tanımını içerir
> 

## Paket Amacı

hamals_robot_description, robotun:

- 3D modelini
- Frame hiyerarşisini
- Sensör ve teker konumlarını

tanımlar.

Bu paket yalnızca URDF içerir.

Bu paket:

- Odometry hesaplamaz
- TF publish etmez
- Sensör verisi üretmez
- Hareket kontrolü yapmaz

## Bağımlılık

Bu paket tek başına çalışmaz.

Robot, aşağıdaki pakete ihtiyaç duyar:

[hamals_localization](https://github.com/m-gnr/hamals_localization)

Bu paket robotun dünyada hareket etmesini sağlar

## Mimari

```
          hamals_localization
                    │
                TF üretir
                    │
                    ▼
          hamals_robot_description
                (URDF)
```

Bu paket

- TF zincirinin alt katmanıdır
- Görsel ve fiziksel model sağlar
- Localization katmanına bağımlıdır

## Dosya Yapısı

```
urdf/
  robot.urdf.xacro   ← Ana giriş dosyası
  base.xacro
  wheels.xacro
  casters.xacro
  lidar.xacro
  materials.xacro

config/
  robot_dimensions.yaml
```

## Frame Yapısı

```
base_footprint
   ↓
base_link
   ↓
wheels / lidar / casters
```

## Tasarım Prensibi

- Modüler
- Config-driven
- Localization’dan ayrılmış
- Navigation-ready
