#!/usr/bin/env python3
"""把 tools.json 的 site.updated 改成現在時間（台灣時間）。由 pre-commit 自動呼叫。"""
import json, datetime, pathlib
p = pathlib.Path(__file__).resolve().parent.parent / 'tools.json'
d = json.loads(p.read_text(encoding='utf-8'))
tz = datetime.timezone(datetime.timedelta(hours=8))
d['site']['updated'] = datetime.datetime.now(tz).replace(microsecond=0).isoformat()
p.write_text(json.dumps(d, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')
