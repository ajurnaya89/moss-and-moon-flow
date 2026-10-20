# Etsy Analytics & eRank SEO Workspace

This workspace is powered by the global **[Etsy Growth & eRank SEO Suite](~/.gemini/config/plugins/etsy-growth/README.md)** plugin ([`~/.gemini/config/plugins/etsy-growth/`](~/.gemini/config/plugins/etsy-growth/)).

## Quick Commands

| Task | Command |
|------|---------|
| eRank CSV/XLSX Audit | `python3 ~/.gemini/config/plugins/etsy-growth/scripts/erank_audit.py --input-dir data/input` |
| Validate Listing (Title, 13 Tags, Price) | `python3 ~/.gemini/config/plugins/etsy-growth/scripts/validate_listing.py --title "..." --tags "..." --price 34.00` |
| Generate Live API CEO Report | `python3 ~/.gemini/config/plugins/etsy-growth/scripts/generate_report.py` |
| Competitor Public API Fetch | `python3 ~/.gemini/config/plugins/etsy-growth/scripts/fetch_competitor.py <shop_name>` |
| OAuth2 Setup / Re-auth | `python3 ~/.gemini/config/plugins/etsy-growth/scripts/oauth_flow.py` |

## Plugin Trigger Commands (Chat)

- `ANALYZE NEW ART` — 7-step workflow for new product/artwork SEO from scratch.
- `ANALYZE MARKET: [keyword / product]` — Market & competitor gap analysis from `data/input/`.
- `AUDIT MY TAGS` — Full shop tag audit (cannibalization, generic tags, sweet-spot gaps).
- `CREATE LISTINGS: [number]` — Generate turnkey Copy/Paste listing packages.
- `UPDATE RESEARCH DATA` — Parse fresh reports in `data/input/` and archive snapshots to `data/archive/`.
