import csv
import json

def norm(s):
    return (s or "").strip()

rows = []

with open("faculty_draft.csv", newline="", encoding="utf-8") as f:
    reader = csv.DictReader(f)
    for r in reader:
        # 处理 keywords，假设用分号分隔
        raw_keywords = norm(r.get("keywords"))
        # 把中文分号也顺手替换掉
        raw_keywords = raw_keywords.replace("；", ";")
        keywords = [k.strip() for k in raw_keywords.split(";") if k.strip()]

        # Research Area 那一列有空格，兼容两种写法
        research_area = norm(r.get(" Research Area") or r.get("Research Area"))

        hat = norm(r.get("hat"))
        fellowship = norm(r.get("fellowship"))

        row = {
            "name": norm(r.get("name")),
            "school": norm(r.get("school")),
            "department": norm(r.get("department")),
            "title": norm(r.get("title")),
            "role": norm(r.get("role")),

            "hat": hat,
            "fellowship": fellowship,

            "keywords": keywords,
            "research_area": research_area,
            "join_year": norm(r.get("join year")),
            "link": norm(r.get("Link")),

            "ai_flag": norm(r.get("AI&AI+ or not")),
            "phd_graduation": norm(r.get("phd graduation")),
            "postdoc": norm(r.get("postdoc")),
            "industry_experience": norm(r.get("Industry Experience")),
            "america_background": norm(r.get("america background")),
            "grant_call_2022_2025": norm(r.get("Grant Call（2022-2025）"))
        }

        # 汇总一个 awards 字段方便前端展示
        awards = []
        if hat:
            awards.append(hat)
        if fellowship:
            awards.append(fellowship)
        row["awards"] = awards

        rows.append(row)

# 输出 faculties.json
with open("faculties.json", "w", encoding="utf-8") as f:
    json.dump(rows, f, ensure_ascii=False, indent=2)

print(f"已写入 {len(rows)} 条记录到 faculties.json")
