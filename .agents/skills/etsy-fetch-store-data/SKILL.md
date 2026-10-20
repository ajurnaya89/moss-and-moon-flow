---
name: etsy-fetch-store-data
description: "Fetch fresh live data from any configured Etsy shop via the Etsy Open API v3 and generate a comprehensive Markdown CEO report (Executive Summary, Revenue, Listings, Reviews, Inventory, Pricing). Use when refreshing live store data before analysis."
argument-hint: "Optional: specify resource (shop, listings, orders, reviews, ledger) or leave blank for full CEO report"
---

# Fetch Store Data (`etsy-fetch-store-data`)

Получение актуальных данных магазина через официальный **Etsy Open API v3** и генерация полного отчета `reports/ceo_report_<YYYY-MM-DD>.md`. Полностью универсален и работает с любым магазином Etsy, настроенным в `.env`.

---

## Когда использовать

- Перед началом глубокого анализа магазина (если последний отчет старше 24 часов).
- Пользователь просит обновить данные магазина, выгрузить текущие листинги, заказы, отзывы или финансовый леджер.

---

## Процедура

### 1. Полное обновление и генерация CEO-отчета (по умолчанию)

Запустите из корня рабочего проекта (или используйте скрипт плагина, который автоматически найдет `.env` в текущей директории):

```bash
python3 .agents/plugins/etsy-growth/scripts/generate_report.py
```
*(Если в корне проекта есть собственный `generate_report.py`, можно также запустить `python3 generate_report.py`).*

После выполнения прочитайте сгенерированный отчет:
```text
reports/ceo_report_<YYYY-MM-DD>.md
```

### 2. Выгрузка отдельных ресурсов API

Если нужны детальные JSON-данные по конкретному ресурсу:

| Данные | Команда |
|--------|---------|
| Профиль магазина | `python3 .agents/plugins/etsy-growth/scripts/fetch_shop.py` |
| Все листинги (active/inactive/draft) | `python3 .agents/plugins/etsy-growth/scripts/fetch_listings.py` |
| Заказы и чеки | `python3 .agents/plugins/etsy-growth/scripts/fetch_orders.py` |
| Отзывы покупателей | `python3 .agents/plugins/etsy-growth/scripts/fetch_reviews.py` |
| Финансовый леджер | `python3 .agents/plugins/etsy-growth/scripts/fetch_ledger.py` |

---

## Настройка `.env` и обработка ошибок

Для работы с API в корне проекта должен находиться файл `.env` (шаблон: `.agents/plugins/etsy-growth/scripts/.env.example`).

| Ошибка | Решение |
|--------|---------|
| `401 Unauthorized` | Запустите `python3 .agents/plugins/etsy-growth/scripts/oauth_flow.py` для повторной авторизации |
| `Shop ID not configured` | Запустите `python3 .agents/plugins/etsy-growth/scripts/oauth_flow.py` — скрипт автоматически определит `ETSY_SHOP_ID` |
| `ETSY_API_KEY not configured` | Укажите `ETSY_API_KEY` и `ETSY_SHARED_SECRET` в локальном файле `.env` (никогда не запрашивайте их в чате) |
| Истек токен | Скрипты обновляют токен автоматически; для ручного обновления: `python3 .agents/plugins/etsy-growth/scripts/token_refresh.py` |

---

## Вывод

После успешного запуска подтвердите пользователю (на русском языке):
- Путь к свежему отчету: `reports/ceo_report_<YYYY-MM-DD>.md`
- Ключевые метрики `[REPORTED DATA]` (число активных листингов, общие продажи, средняя оценка, выручка).
