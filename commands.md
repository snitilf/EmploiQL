# JSearch Commands Reference

## fetching Jobs (src/jsearch.py)

### using Presets

```bash
python3 src/jsearch.py --preset software --live
python3 src/jsearch.py --preset devops --live
python3 src/jsearch.py --preset data --live
python3 src/jsearch.py --preset frontend --live
python3 src/jsearch.py --preset backend --live
python3 src/jsearch.py --preset fullstack --live
python3 src/jsearch.py --preset ml --live
python3 src/jsearch.py --preset cyber --live
python3 src/jsearch.py --preset qa --live
```
```python
for bank in rbc td bmo scotiabank cibc national desjardins manulife sunlife; do
    python3 scripts/load_jsearch.py --preset $bank --mock
done
```
### custom Queries

```bash
python3 src/jsearch.py --query "python intern" --live
python3 src/jsearch.py --query "react developer intern" --live
python3 src/jsearch.py --query "junior software engineer" --live
python3 src/jsearch.py --query "data analyst intern" --live
```

### multiple Pages (10 jobs per page)

```bash
python3 src/jsearch.py --query "python intern" --pages 3 --live
```

### different Location

```bash
python3 src/jsearch.py --query "software intern" --location "Toronto, Canada" --live
python3 src/jsearch.py --query "software intern" --location "Vancouver, Canada" --live
```

### utility Commands

```bash
python3 src/jsearch.py --list-cache      # show cached searches
python3 src/jsearch.py --list-presets    # show available presets
```

## Loading Jobs to Database (scripts/load_jsearch.py)

### load from preset

```bash
python3 scripts/load_jsearch.py --preset software --mock
python3 scripts/load_jsearch.py --preset devops --mock
```

```python
for bank in rbc td bmo scotiabank cibc national desjardins manulife sunlife; do
    python3 scripts/load_jsearch.py --preset $bank --mock
done
```
### load from Custom Query

```bash
python3 scripts/load_jsearch.py --query "python intern" --mock
```

### load All Presets

```bash
python3 scripts/load_jsearch.py --all --mock
```

### with OpenAI Extraction (costs API credits)

```bash
python3 scripts/load_jsearch.py --preset software
```

### limit for Testing

```bash
python3 scripts/load_jsearch.py --preset software --mock --limit 5
```

---

## date posted filter

currently hardcoded in `src/jsearch.py` line 184. edit `_fetch_page()` to change:

```python
"date_posted": "month",  # change this value
```

| Value | Meaning |
|-------|---------|
| `today` | Last 24 hours |
| `3days` | Last 3 days |
| `week` | Last 7 days |
| `month` | Last 30 days (default) |
| `all` | No date filter |

### examples After Editing

```python
# for jobs posted today
"date_posted": "today",

# for jobs posted in last 3 days
"date_posted": "3days",

# for jobs posted this week
"date_posted": "week",
```

---

## full workflow example

```bash
# 1. fetch fresh jobs from today
#    (after editing date_posted to "today")
python3 src/jsearch.py --preset software --live
# get 30 jobs (3 pages)
python3 src/jsearch.py --preset software --pages 3 --live
# get 50 jobs (5 pages)
python3 src/jsearch.py --preset devops --pages 5 --live
# custom query with more pages
python3 src/jsearch.py --query "python intern" --pages 4 --live

# 2. load into database
python3 scripts/load_jsearch.py --preset software --mock

# 3. query
python3 src/cli.py "show me software internships"
```