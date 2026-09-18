<p align="center">
  <img src="assets/banner.svg" alt="Skazka Hub" width="960">
</p>

<p align="center">
  <a href="https://github.com/kroxaboom-sudo/skazka-hub-releases/releases/latest"><img src="https://img.shields.io/github/v/release/kroxaboom-sudo/skazka-hub-releases?label=Latest&cacheSeconds=300" alt="Latest release"></a>
  <img src="https://img.shields.io/badge/Android-13%2B-3DDC84" alt="Android 13+">
  <img src="https://img.shields.io/badge/languages-RU%20%2F%20EN-blue" alt="RU / EN">
</p>

# Skazka Hub — releases / релизы

> **RU — основной язык · EN — обязательный второй язык**

## RU

### Текущий Latest

**Skazka Hub 0.7.1-preview** — первая основная публичная версия на canonical Android package:

`com.kroxaboom.skazkahub` · `versionCode 30` · Android 13+.

Главная навигация: **Библиотека → Новое → Каталог → Загрузки → Ещё**.
На планшетах используются navigation rail и master-detail интерфейсы Библиотеки, Загрузок и Каталога; Настройки используют левую навигацию и правую панель.

### Обновление существующей canonical установки

Если уже установлен **0.7.0-preview**, устанавливайте **0.7.1-preview** поверх него. HOSTKEY Android 13 gate подтвердил install-over `0.7.0/29 → 0.7.1/30` с сохранением библиотеки, локальных данных и позиции чтения.

### Переход со старого package

Legacy package `me.zaza.reader` больше не является основной линией разработки, но совместимость для старых установок сохранена.

- `update.json` и `update-android9.json` намеренно остаются pinned на неизменяемый **0.6.23-preview / 29**;
- `update-canonical.json` обслуживает `com.kroxaboom.skazkahub`;
- `package-migration.json` сообщает переходной версии, какой canonical APK устанавливать.

Поэтому пользователь 0.6.22/0.6.23 по-прежнему может безопасно дойти до canonical 0.7.1. Старое приложение не удаляется автоматически: его следует удалять только после проверки перенесённых данных.

### Проверка

SERVER-FIRST release gate на HOSTKEY проверяет собственный код, подпись, package/version/minSdk, RU/EN, four-mode responsive UI, install-over, rollback/retry package migration, Downloads IMAGE/TEXT/MIXED, синхронизацию, reader и clean-install offline recovery.

---

## EN

### Current Latest

**Skazka Hub 0.7.1-preview** is the first primary public release on the canonical Android package:

`com.kroxaboom.skazkahub` · `versionCode 30` · Android 13+.

Primary navigation: **Library → New → Catalog → Downloads → More**.
Tablets use a navigation rail plus master-detail Library, Downloads, and Catalog layouts; Settings uses left-side navigation with a right-side detail panel.

### Updating an existing canonical installation

If **0.7.0-preview** is already installed, install **0.7.1-preview** over it. The HOSTKEY Android 13 gate verified `0.7.0/29 → 0.7.1/30` install-over while preserving library data and reading position.

### Migrating from the legacy package

The legacy `me.zaza.reader` package is no longer the primary development line, but old installations remain supported during migration.

- `update.json` and `update-android9.json` intentionally remain pinned to immutable **0.6.23-preview / 29**;
- `update-canonical.json` serves `com.kroxaboom.skazkahub`;
- `package-migration.json` tells the transition build which canonical APK to install.

This keeps the migration path available to 0.6.22/0.6.23 users even though Latest is now canonical. The legacy app is never removed automatically; users should keep it until migrated data has been verified.

### Verification

The HOSTKEY SERVER-FIRST release gate verifies own-code policy, signing, package/version/minSdk, RU/EN, four-mode responsive UI, install-over, rollback/retry package migration, IMAGE/TEXT/MIXED Downloads, synchronization, reader behavior, and clean-install offline recovery.

---

This public repository contains APK files, update metadata and RU/EN release documentation. Android source is maintained separately in the private `kroxaboom-sudo/skazka-hub` repository. Signing keys are never published.
