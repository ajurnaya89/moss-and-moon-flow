---
name: analyze-new-art
description: "7-step workflow for analyzing any new design or product from scratch, building eRank research plans, selecting low-competition transactional keywords, and generating turnkey Copy/Paste Etsy listings (US English Title <=140 chars, 13 Tags <=20 chars, 5-ratio Description, 5x Alt Text, Pricing Tier A/B) with Russian owner explanations. Triggered by ANALYZE NEW ART or CREATE LISTINGS."
argument-hint: "Опишите новую работу (или прикрепите изображение) либо укажите количество листингов для генерации"
---

# Analyze New Art (`analyze-new-art`)

Пошаговый 7-этапный протокол оценки любой новой работы или цифрового/физического товара с нуля и подготовки комплекта для публикации на Etsy под ключ без программирования.

> **Правило изоляции:** Никогда не навязывайте существующие категории магазина (например, `botanical`, `eucalyptus`, `lavender`, `neutral`, `minimalist`) новой работе, если они буквально не изображены на самом товаре.
> **Языковой стандарт:** Диалог и пояснения для владельца магазина — **русский язык** (простой, пошаговый). Все поля листинга для Etsy (`Title`, `13 Tags`, `Description`, `Alt Text`) — строго **US English**.

---

## Когда использовать

- Команда **`ANALYZE NEW ART`**
- Команда **`CREATE LISTINGS: [number]`**
- Пользователь показывает новую картину / принт / товар и просит подобрать ключи, проверить спрос в eRank или собрать готовый листинг для Etsy.

---

## 7-шаговый протокол (`ANALYZE_NEW_ART_WORKFLOW`)

### Шаг 1 — Product Intake (Сбор фактических характеристик)
Зафиксируйте только подтвержденные факты о продукте (по фото или описанию пользователя):
1. **Subject / Motif (Сюжет/мотив):** Что буквально изображено?
2. **Art Style / Medium (Стиль и техника):** Акварель, винтажное масло, линогравюра, скетч, ретро-постер, фото и т.д.
3. **Color Palette (Палитра):** Реальные цвета на изображении.
4. **Product Format (Формат):** `Single Print`, `Set of 2`, `Set of 3`, `Gallery Wall Set`.
5. **Product Type (Тип):** `Digital Download (Printable)` или `Physical Item`.
6. **Intended Room / Space (Комната):** Кухня, спальня, гостиная, детская, ванная, столовая, кабинет.

*Запрещено додумывать неподтвержденные свойства. Если данных не хватает — задайте короткий вопрос на русском языке.*

---

### Шаг 2 — Keyword Hypotheses (Генерация гипотез по 6 направлениям)
Сгенерируйте поисковые фразы (с пометкой `[HYPOTHESIS]`) по 6 направлениям:
1. **Subject / Motif**
2. **Art Style / Medium**
3. **Color Palette**
4. **Product Format**
5. **Intended Room / Space**
6. **Buyer Intent / Occasion**

---

### Шаг 3 — eRank Research Plan (План исследования в eRank)
Выберите **2–4 приоритетные seed-фразы** для проверки в **eRank Keyword Tool** и дайте пользователю простую инструкцию по экспорту CSV/XLSX в папку `data/input/`:
1. Введите фразу в eRank Keyword Tool (регион: **USA**).
2. Экспортируйте таблицу `Keyword Ideas` в CSV/XLSX и положите в `data/input/`.
3. Напишите `UPDATE RESEARCH DATA` (или запустите `python3 .agents/plugins/etsy-growth/scripts/erank_audit.py --input-dir data/input`).

---

### Шаг 4 — Evidence Review (Анализ отчетов eRank)
Проанализируйте метрики из `data/input/` (см. [`DATA_DICTIONARY.md`](../../instructions/DATA_DICTIONARY.md)):
- `Avg Searches`, `Avg Clicks`, `Avg CTR`, `Etsy Competition`, `Keyword Difficulty`, популярные теги конкурентов.
- Каждую точную цифру из файла помечайте **`[REPORTED DATA]`** (с указанием файла и даты). Если поля нет — пишите `NOT AVAILABLE IN PROVIDED DATA`.
- Аналитические выводы помечайте **`[INFERENCE]`**, непроверенные идеи — **`[HYPOTHESIS]`**.

---

### Шаг 5 — Keyword Selection (Отбор ключей)
Отберите рабочие фразы по формуле:
- **Релевантность + Транзакционный интент + Здоровая конкуренция**.
- Отдавайте приоритет целевым многословным фразам с **`Etsy Competition < 50,000`** (оптимально `1,000 – 25,000`) и подтвержденным спросом перед миллионными общими фразами (`wall art`, `digital download`).

---

### Шаг 6 — Listing Deliverables (Готовый пакет Copy/Paste под ключ)

Сформируйте готовые блоки для копирования в Etsy Listing Manager:

#### 1. Title (US English, $\le 140$ символов)
- Главный поисковый ключ в первых **30–40 символах** (front-loaded).
- Естественный, читаемый язык без переспама через запятую.
- Укажите точную длину заголовка в символах.

#### 2. 13 Tags (US English, каждый строго $\le 20$ символов с пробелами)
- Ровно 13 уникальных многословных фраз без дублей и грамматического мусора.
- Выведите нумерованный список `1..13` с длиной каждого тега в символах и метриками `[REPORTED DATA]` (если есть отчет), плюс **одну строку через запятую** для быстрой вставки в Etsy.

#### 3. Description (US English)
- Первые 160 символов — концентрированное описание товара для сниппета Google и покупателя.
- Художественное описание работы и рекомендации по интерьеру.
- Стандартизированный блок **5 масштабируемых соотношений сторон в 300 DPI JPEG**:
  - `2:3 Ratio` (4x6, 8x12, 12x18, 16x24, 20x30, 24x36 in)
  - `3:4 Ratio` (6x8, 9x12, 12x16, 15x20, 18x24 in)
  - `4:5 Ratio` (4x5, 8x10, 12x15, 16x20, 24x30 in)
  - `ISO International` (A5, A4, A3, A2, A1, 50x70 cm)
  - `11x14 inches`
- Пошаговая инструкция по скачиванию и печати + условия `Instant Digital Download (no physical item will be shipped)`.
- Блок ссылок на смежные листинги серии.

#### 4. 5x Alt Text (US English)
- 5 фактических, объективных описаний видимого изображения для 5 слайдов галереи (без спама тегами).

#### 5. Pricing Recommendation (Правило суммы цифр цены со скидкой 50% = 8)
- **Tier A:** `$34.00` $\rightarrow$ со скидкой 50% **`$17.00`** ($1+7+0+0 = 8$)
- **Tier B:** `$32.20` $\rightarrow$ со скидкой 50% **`$16.10`** ($1+6+1+0 = 8$)

#### 6. Валидация скриптом (рекомендуется)
Проверьте длину заголовка, 13 тегов и цену скриптом:
```bash
python3 .agents/plugins/etsy-growth/scripts/validate_listing.py --title "<TITLE>" --tags "<TAG1>,<TAG2>,..." --price 34.00
```

---

### Шаг 7 — Low-Data Mode (Fallback без отчетов eRank)
Если отчеты eRank еще не загружены в `data/input/`, выдайте черновой пакет с обязательной плашкой:
> ⚠️ **`[UNVALIDATED HYPOTHESIS]`** — Отчеты eRank не предоставлены. Рекомендации основаны на семантической структуре и требуют проверки фраз в eRank Keyword Tool.
