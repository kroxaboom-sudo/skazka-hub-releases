# Skazka Hub — переход 0.6.23-preview → 0.7.0-preview / transition 0.6.23-preview → 0.7.0-preview

## RU

Этот релиз выполняет безопасный переход Android package ID с `me.zaza.reader` на `com.kroxaboom.skazkahub` без удаления старого приложения и без потери локальных данных.

### Для существующих установок

1. Установите **Skazka Hub 0.6.23-preview** поверх 0.6.22-preview. Не удаляйте старое приложение.
2. В переходной версии запустите переход на новый package ID. Она скачает и проверит **Skazka Hub 0.7.0-preview** с package `com.kroxaboom.skazkahub`.
3. Новый Skazka Hub перенесёт библиотеку, историю, прогресс, настройки, IMAGE/TEXT/MIXED-контент, сохранённые обложки и защищённые сессии.
4. Старая установка `me.zaza.reader` останется на устройстве. Не удаляйте её до быстрой проверки библиотеки, прогресса и скачанного контента в 0.7.0-preview.
5. Разрешения Android на ранее выбранные внешние папки могут потребовать повторного предоставления. Сам перенесённый внутренний контент при этом не удаляется.

### Для новых установок

Новые пользователи могут установить **Skazka Hub 0.7.0-preview** и выбрать новую установку без legacy-данных.

### Совместимость релиза

Переходный GitHub Release публикуется под tag **v0.6.23-preview** и временно остаётся **Latest**, чтобы существующие 0.6.22-клиенты получили совместимый `update.json`.

В одном release должны находиться оба APK и три раздельных manifest-файла:

- `update.json` → legacy `me.zaza.reader` / 0.6.23-preview;
- `update-canonical.json` → canonical `com.kroxaboom.skazkahub` / 0.7.0-preview;
- `package-migration.json` → проверенный canonical APK, который устанавливает переходная версия.

Не заменяйте этот переходный Latest на canonical-only release, пока legacy migration window не будет закрыт отдельным решением.

Экраны перехода, диалоги и пользовательские ошибки входят в общий словарь локализации и проверены для RU/EN.

Минимальная версия Android: **13 / API 33**. Оба APK подписаны тем же доверенным сертификатом проекта.

---

## EN

This release performs the safe Android package-ID transition from `me.zaza.reader` to `com.kroxaboom.skazkahub` without uninstalling the old app and without discarding local data.

### Existing installations

1. Install **Skazka Hub 0.6.23-preview** over 0.6.22-preview. Do not uninstall the old app.
2. Start the package transition from the transition build. It downloads and verifies **Skazka Hub 0.7.0-preview** with package `com.kroxaboom.skazkahub`.
3. The new Skazka Hub imports the library, history, reading progress, settings, IMAGE/TEXT/MIXED content, saved artwork, and protected sessions.
4. The old `me.zaza.reader` installation remains on the device. Keep it until the library, progress, and downloaded content have been checked in 0.7.0-preview.
5. Android permissions for previously selected external folders may need to be granted again. Migrated internal content is not removed by this requirement.

### New installations

New users may install **Skazka Hub 0.7.0-preview** and choose a fresh installation without legacy data.

### Release compatibility

The transition GitHub Release uses tag **v0.6.23-preview** and temporarily remains **Latest** so existing 0.6.22 clients receive a compatible `update.json`.

The same release must contain both APKs and three separate manifests:

- `update.json` → legacy `me.zaza.reader` / 0.6.23-preview;
- `update-canonical.json` → canonical `com.kroxaboom.skazkahub` / 0.7.0-preview;
- `package-migration.json` → the verified canonical APK installed by the transition build.

Do not replace this transition Latest with a canonical-only release until the legacy migration window is explicitly closed.

Migration screens, dialogs, and user-facing errors use the shared localization catalog and are verified for RU/EN.

Minimum Android version: **13 / API 33**. Both APKs are signed with the same trusted project certificate.
