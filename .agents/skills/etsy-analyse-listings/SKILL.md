---
name: etsy-analyse-listings
description: "Deep diagnostic analysis of Etsy shop listings using the Master System v2 Funnel & Decision Engine (KEEP, OPTIMIZE, REPOSITION, TEST, RETIRE). Evaluates performance tiers, pricing opportunities, conversion bottlenecks, zero-view listings, tag strategy, and winner protection."
argument-hint: "Область фокуса: all / pricing / tags / zero-views / top-performers"
---

# Analyse Listings & Funnel Diagnostics (`etsy-analyse-listings`)

Глубокая диагностика каталога листингов любого магазина Etsy по воронке `DATA → DATA SUFFICIENCY → RELEVANCE → FUNNEL DIAGNOSIS → PORTFOLIO CONTEXT → DECISION → OPTIMIZATION → TEST → MEASURE`.

> **Защита бестселлеров (Winner Protection):** Листинги с подтвержденными стабильными продажами и хорошей конверсией получают статус **`KEEP`**. Запрещено менять их `Title` и `13 Tags`.
> **Языковой стандарт:** Аналитика и пояснения — **русский язык**. Готовые тексты для Etsy (`Title`, `13 Tags`, `Description`, `Alt Text`) — **US English**.

---

## Когда использовать

- Поиск слабых, просевших или нулевых (`zero-view`) листингов.
- Воронка диагностики: определение узкого места (Discovery vs CTR/Click Appeal vs Conversion/Offer).
- Анализ ценовых уровней и корреляции цены с добавлениями в избранное.
- Принятие решений: какие карточки защитить (`KEEP`), оптимизировать (`OPTIMIZE`), репозиционировать (`REPOSITION`), протестировать (`TEST`) или отправить в архив (`RETIRE`).

---

## Процедура анализа

### Шаг 1 — Загрузка данных

1. Прочитайте свежий отчет `reports/ceo_report_<today>.md` (если отчета нет или он устарел — используйте навык `etsy-fetch-store-data`) и/или выгрузки из `data/input/`.
2. Для получения полных данных по тегам и датам создания карточек через API выполните:
   ```bash
   python3 .agents/plugins/etsy-growth/scripts/fetch_listings.py
   ```
3. Маркируйте все фактические цифры тегом **`[REPORTED DATA]`**, выводы — **`[INFERENCE]`**, гипотезы — **`[HYPOTHESIS]`**.

---

### Шаг 2 — Воронка и матрица диагностики

#### А. Data Sufficiency Gate (Обязательный фильтр)
Для каждого листинга оцените достаточность данных:
- **`SUFFICIENT`** — достаточно истории и показов/визитов для выводов.
- **`LIMITED`** — предварительные данные, осторожные выводы.
- **`INSUFFICIENT`** — новый листинг (<30 дней) или слишком мало показов. **Запрещено ставить `RETIRE`** — используйте `KEEP — INSUFFICIENT DATA` или `TEST — INSUFFICIENT DATA`.

#### Б. Сегментация каталога (Performance Tiers)
- **Stars (Лидеры / Бестселлеры):** высокие просмотры + высокое избранное/продажи $\rightarrow$ статус **`KEEP`** (защищены от переписывания SEO; используются как база для расширения продуктовой линейки).
- **Hidden Gems (Скрытые жемчужины):** мало просмотров, но высокий процент конверсии в избранное/покупки $\rightarrow$ проблема **Discovery / SEO** (статус **`OPTIMIZE`** — расширить средне- и низкочастотные теги с конкуренцией `<50,000`).
- **Click/Conversion Bottlenecks:** много просмотров, но мало избранного или 0 покупок $\rightarrow$ проблема **Offer / Price / Mockup / Clarity** (не ломать работающие теги, а проверять обложку, цену и описание).
- **Deadweight / Zero-View Listings:** 0 просмотров и 0 избранного после 30–60+ дней $\rightarrow$ статус **`OPTIMIZE`** или **`REPOSITION`** (при полной неактуальности и `SUFFICIENT` данных — `RETIRE`).

#### В. Ценовой анализ и риски остатков
- Диапазон цен (min / median / max) и корреляция цены с избранным.
- Проверка соответствия правилу скидки 50% с суммой цифр `= 8` (Tier A `$34.00 -> $17.00`, Tier B `$32.20 -> $16.10`), если магазин использует эту ценовую модель.
- Контроль остатков (`quantity <= 2` или `quantity = 0` на активных карточках).

---

### Шаг 3 — Формат вывода по каждому листингу и магазину

Для каждого разбираемого листинга укажите:
1. **Listing ID & Title**
2. **Status:** `KEEP` / `OPTIMIZE` / `REPOSITION` / `TEST` / `RETIRE`
3. **Confidence:** `HIGH` / `MEDIUM` / `LOW`
4. **Data Sufficiency:** `SUFFICIENT` / `LIMITED` / `INSUFFICIENT`
5. **Primary Bottleneck:** Discovery / Relevance / CTR / Conversion / Positioning / Pricing / Insufficient Data
6. **Evidence (`[REPORTED DATA]`):** точные метрики
7. **Diagnosis (`[INFERENCE]`):** 1–3 предложения на русском языке
8. **Deliverables (только для `OPTIMIZE` / `REPOSITION` / `TEST`):**
   - Готовый блок Copy/Paste на **US English**: `Title` ($\le 140$ символов) + `13 Tags` ($\le 20$ символов каждый, с указанием длины).
   - Для `KEEP` обязательно пишите: `NO TITLE OR TAG CHANGES RECOMMENDED — PROTECTED WINNER`.

В конце отчета приведите **Приоритетный план действий (Priority Action List)** из топ-5 шагов, ранжированных по `HIGH IMPACT + HIGH EVIDENCE + LOW RISK`.
