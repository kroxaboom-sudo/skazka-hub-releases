# Skazka Hub 0.7.1-preview

## RU

### Навигация и структура
- Главная навигация приведена к постоянной схеме: **Библиотека → Новое → Каталог → Загрузки → Ещё**.
- `Ещё` всегда открывает глобальный раздел; действия текущей главы и сайта вынесены в отдельное контекстное меню `⋮`.
- Выбранная вкладка теперь определяется стабильным внутренним ID, а не видимым русским текстом, поэтому RU/EN больше не влияет на навигацию.
- Фоновая синхронизация больше не блокирует переходы между разделами.

### Библиотека, загрузки и планшеты
- Верх Библиотеки на телефоне упрощён: поиск, фильтры и быстрые фильтры остаются на виду, категория/сортировка/вид собраны в компактное меню.
- На планшете Библиотека получила master-detail: список/сетка слева, выбранное произведение и быстрые действия справа.
- Загрузки получили контекстную Пауза/Продолжить, Retry показывается только при ошибках, редкие действия находятся в `⋮`.
- На планшете Загрузки работают как очередь слева и главы выбранного произведения справа.
- Каталог на планшете показывает результаты слева и preview выбранного произведения справа.
- Settings на планшете используют отдельную левую навигацию и правую панель параметров.

### Настройки
- Настройки сгруппированы в четыре понятных блока: **Чтение**, **Офлайн и файлы**, **Аккаунт и данные**, **Приложение**.
- `Аккаунт Skazka` и `Синхронизация` объединены в один раздел **Аккаунт и синхронизация**.
- `Источники` переименованы в **Источники и зеркала**, `Сервис` — в **Поддержка и диагностика**.
- Экран package migration больше не занимает постоянное место в настройках после успешного переноса.

### Окончательный package transition
- Основной Android package: **`com.kroxaboom.skazkahub`**.
- Версия: **0.7.1-preview**, `versionCode 30`, Android 13+.
- Новый canonical release становится Latest.
- Для старых установок `releases/latest/download/update.json` остаётся совместимым bridge-feed и продолжает указывать на уже опубликованный `me.zaza.reader` 0.6.23-preview.
- `update-canonical.json` и `package-migration.json` указывают на canonical 0.7.1-preview. Поэтому пользователь 0.6.22/0.6.23 всё ещё может безопасно пройти миграцию даже после переключения Latest на canonical release.

## EN

### Navigation and structure
- Primary navigation is now stable: **Library → New → Catalog → Downloads → More**.
- `More` always opens global navigation; current chapter/site actions live in a separate contextual `⋮` menu.
- Selected navigation uses stable internal IDs rather than visible Russian labels, so RU/EN can no longer break tab state.
- Background synchronization no longer blocks navigation.

### Library, downloads, and tablets
- The phone Library header is simplified: search, filters, and quick filters stay visible while category/sort/view move into one compact menu.
- Tablet Library now uses master-detail: collection on the left, selected title and quick actions on the right.
- Downloads use one contextual Pause/Resume action; Retry appears only when errors exist; rare actions move to `⋮`.
- Tablet Downloads use queue-on-the-left and selected-title chapters/actions on the right.
- Tablet Catalog keeps results on the left and a selected-title preview on the right.
- Tablet Settings use a dedicated left navigation column and right-side settings panel.

### Settings
- Settings are grouped into **Reading**, **Offline and files**, **Account and data**, and **App**.
- Skazka account and synchronization are combined into **Account and sync**.
- Sources are now **Sources and mirrors**; Service is now **Support and diagnostics**.
- Package migration no longer occupies a permanent settings row after migration completes.

### Final package transition
- Canonical Android package: **`com.kroxaboom.skazkahub`**.
- Version: **0.7.1-preview**, `versionCode 30`, Android 13+.
- The canonical release becomes Latest.
- `releases/latest/download/update.json` remains a compatibility bridge for old installs and still points to the immutable `me.zaza.reader` 0.6.23-preview APK.
- `update-canonical.json` and `package-migration.json` point to canonical 0.7.1-preview, so 0.6.22/0.6.23 users can still migrate safely after Latest moves to the canonical line.
