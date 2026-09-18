# Skazka Hub 0.6.22-preview

RU: крупное обновление local/offline-first библиотеки, загрузок IMAGE/TEXT/MIXED, читалки, резервного копирования и RU/EN. EN: major local/offline-first update for the library, IMAGE/TEXT/MIXED downloads, reader, backups, and RU/EN support.

## RU

- Downloads объединены для IMAGE и TEXT: персистентная очередь, пауза/продолжение/повтор/отмена, автоматические загрузки и локальная переиндексация.
- SQLite LocalState стал локальным source of truth; Library v2 получила коллекции, unread/new, расширенные фильтры, list/grid, bulk actions, undo и сохранение позиции прокрутки.
- Добавлены native TEXT и MIXED reading flows; IMAGE reader получил fit-screen, RTL и дополнительные режимы отображения.
- Резервные копии расширены: зашифрованные локальные и HOSTKEY/Telegram-копии, полный архив скачанных глав и clean-install offline recovery.
- Полностью проверены русский и английский интерфейсы; LOC-05 сохраняет стабильные ключи для удалённых исправлений переводов.
- Updater подготовлен к миграции GitHub Releases: новый `skazka-hub-releases` является приоритетным feed, legacy `zaza-reader-releases` остаётся безопасным fallback до отдельного перехода.
- Очередь телеметрии защищена от race при flush; повторяющаяся low-priority usage-телеметрия coalesce-ится без объединения error/source событий.
- Vercel исключён из активных маршрутов и сохранён только как выключенный cold reserve.
- Приватный source-repo переименован в `kroxaboom-sudo/skazka-hub`; `applicationId me.zaza.reader` намеренно сохранён для install-over совместимости.

Устанавливайте 0.6.22 поверх 0.6.21 — удалять приложение не нужно. Android 13+.

## EN

- IMAGE and TEXT downloads now share one persistent queue with pause/resume/retry/cancel, automatic downloads, and local reindexing.
- SQLite LocalState is the local source of truth; Library v2 adds collections, unread/new, advanced filters, list/grid, bulk actions, undo, and scroll-position preservation.
- Native TEXT and MIXED reading flows are included; the IMAGE reader adds fit-screen, RTL, and additional display modes.
- Backup coverage now includes encrypted local and HOSTKEY/Telegram copies, full downloaded-content archives, and clean-install offline recovery.
- Russian and English UI coverage is verified; LOC-05 keeps stable keys for remotely moderated translation fixes.
- The updater is ready for the Releases migration: `skazka-hub-releases` is tried first, while legacy `zaza-reader-releases` remains a safe fallback until the separate cutover.
- Telemetry flush races are fixed; repetitive low-priority usage events are coalesced without merging error/source events.
- Vercel is removed from active routes and retained only as a disabled cold reserve.
- The private source repository is now `kroxaboom-sudo/skazka-hub`; legacy `applicationId me.zaza.reader` is intentionally retained for install-over compatibility.

Install 0.6.22 over 0.6.21; do not uninstall first. Android 13+.
