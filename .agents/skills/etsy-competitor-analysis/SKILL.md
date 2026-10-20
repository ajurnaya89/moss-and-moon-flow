---
name: etsy-competitor-analysis
description: "Benchmark any Etsy shop against competitor Etsy shops using live public Etsy Open API v3 data and/or eRank competitor exports. Segments competitors into Direct, Positioning, and Inspirational, and identifies Keyword, Positioning, Product, and Presentation gaps."
argument-hint: "Имена магазинов конкурентов или URL, например: shopname1 shopname2"
---

# Competitor Analysis (`etsy-competitor-analysis`)

Сравнительный бенчмаркинг магазина против конкурентов на Etsy с использованием публичного **Etsy Open API v3** и/или таблиц eRank (`data/input/`). Полностью независим от конкретного магазина или ниши.

---

## Когда использовать

- Пользователь просит сравнить свой магазин с конкурентами (`ANALYZE MARKET: [keyword / shop]`).
- Пользователь присылает названия или ссылки на магазины конкурентов на Etsy.
- Стратегический разбор ценообразования, ассортимента, частоты тегов и социальной доказательности (отзывы, избранное).

---

## Доступные источники данных

1. **Публичный Etsy Open API v3** (достаточно только `ETSY_API_KEY` в `.env`, OAuth владельца чужого магазина не нужен):
   - Профиль магазина: общее число продаж (`sales_count`), количество отзывов (`review_count`), средний рейтинг (`review_average`), число активных листингов (`listing_active_count`).
   - Все активные листинги конкурента: `title`, `price`, `views`, `num_favorers`, `tags`, `taxonomy_path`, `created_timestamp`.
2. **Таблицы eRank Competitor / Keyword Tool** в `data/input/`:
   - Оценочные продажи (`Est. Sales`), выручка (`Est. Revenue`), `Daily Views`, `Avg Searches`, `Etsy Competition`.

---

## Процедура выполнения

### Шаг 1 — Определение магазинов для сравнения
Извлеките `shop_name` из названий или URL (например, `etsy.com/shop/<shop_name>`).

### Шаг 2 — Выгрузка данных конкурентов
Если настроен API-ключ в `.env`, выполните:
```bash
python3 .agents/plugins/etsy-growth/scripts/fetch_competitor.py <shop1> [<shop2> ...]
```
Если в `data/input/` лежат CSV/XLSX выгрузки конкурентов из eRank, дополнительно запустите:
```bash
python3 .agents/plugins/etsy-growth/scripts/erank_audit.py --input-dir data/input
```

### Шаг 3 — Сегментация конкурентов и сравнительная таблица

Разделите конкурентов на 3 категории:
- **Direct Competitors** (прямые конкуренты по продукту и цене)
- **Positioning Competitors** (близкий продукт, но другое позиционирование/комната/аудитория)
- **Inspirational Competitors** (лидеры ниши для изучения подачи и линейки)

Постройте сводную таблицу (все цифры помечайте **`[REPORTED DATA]`** с датой):

| Метрика | Наш магазин | Конкурент A | Конкурент B |
|---------|-------------|-------------|-------------|
| Сегмент (Direct / Positioning / Inspirational) | — | | |
| Всего продаж (`sales_count`) | | | |
| Активных листингов | | | |
| Средний рейтинг (число отзывов) | | | |
| Цена: min / median / max | | | |
| Всего избранного по листингам | | | |
| Среднее избранное на 1 листинг | | | |
| Средние просмотры на 1 листинг | | | |

### Шаг 4 — Анализ 4 гэпов (4-Way Gap Analysis)

Проанализируйте разрывы (с маркировкой `[INFERENCE]` и `[HYPOTHESIS]`):
1. **Keyword Gap:** Какие теги стабильно встречаются в топ-10 самых популярных листингов конкурентов (с адекватной конкуренцией `<50,000` по eRank), но не используются у нас?
2. **Positioning Gap:** На какие помещения, поводы или стили делают упор конкуренты?
3. **Product & Pricing Gap:** Какие форматы (одиночные работы, сеты из 2/3/6, размеры) и ценовые уровни дают конкурентам максимум `Favorites` и `Views`?
4. **Presentation Gap:** Как оформлены заголовки и превью у карточек-лидеров?

### Шаг 5 — Выводы и план действий (на русском языке)
Завершите отчет ранжированным списком из **3–5 конкретных действий** для захвата найденных рыночных окон (без изменения наших собственных бестселлеров `KEEP`).
