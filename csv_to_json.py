import csv
import json

def norm(s):
    return (s or "").strip()

rows = []

with open("faculty_draft.csv", newline="", encoding="utf-8-sig") as f:
    reader = csv.DictReader(f)
    for r in reader:
        # 把表头统一规范成小写+去空格
        row = { (k or "").strip().lower(): v for k, v in r.items() }

        raw_keywords = norm(row.get("keywords"))
        raw_keywords = raw_keywords.replace("；", ";")
        keywords = [k.strip() for k in raw_keywords.split(";") if k.strip()]

        research_area = norm(row.get(" research area") or row.get("research area"))

        hat = norm(row.get("hat"))
        fellowship = norm(row.get("fellowship"))

        data = {
            "name": norm(row.get("name")),          # 注意这里用的是规范后的 row
            "school": norm(row.get("school")),
            "department": norm(row.get("department")),
            "title": norm(row.get("title")),
            "role": norm(row.get("role")),
            "hat": hat,
            "fellowship": fellowship,
            "keywords": keywords,
            "research_area": research_area,
            "join_year": norm(row.get("join year")),
            "link": norm(row.get("link")),
            "ai_flag": norm(row.get("ai&ai+ or not")),
            "phd_graduation": norm(row.get("phd graduation")),
            "postdoc": norm(row.get("postdoc")),
            "industry_experience": norm(row.get("industry experience")),
            "america_background": norm(row.get("america background")),
            "grant_call_2022_2025": norm(row.get("grant call（2022-2025）")),
        }

        awards = []
        if hat:
            awards.append(hat)
        if fellowship:
            awards.append(fellowship)
        data["awards"] = awards

        rows.append(data)

with open("faculties.json", "w", encoding="utf-8") as f:
    json.dump(rows, f, ensure_ascii=False, indent=2)

print(f"已写入 {len(rows)} 条记录到 faculties.json")
