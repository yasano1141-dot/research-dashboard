#!/usr/bin/env python3
"""
今日の曜日・テーマ・ファイル名情報を取得するヘルパースクリプト
JSON 形式で出力する。Claude Code から呼び出して使う。

使い方:
    python3 get-today-context.py
    python3 get-today-context.py --date 20260428  # 特定の日付を指定
"""

import json
import sys
from datetime import datetime, timezone, timedelta
from pathlib import Path


THEMES = {
    0: ('老年医学・健康寿命', '月曜日_老年医学・健康寿命', 'Geriatric Medicine & Healthspan'),
    1: ('身体活動・運動疫学', '火曜日_身体活動・運動疫学', 'Physical Activity & Exercise Epidemiology'),
    2: ('筋質・体組成', '水曜日_筋質・体組成', 'Muscle Quality & Body Composition'),
    3: ('脳・認知', '木曜日_脳・認知', 'Cognition & Brain Research'),
    4: ('疫学方法論', '金曜日_疫学方法論', 'Epidemiological Methodology'),
    5: ('AI・データ科学', '土曜日_AI・データ科学', 'AI & Data Science'),
    6: ('遺伝子・オミクス', '日曜日_遺伝子・オミクス', 'Genetics & Omics'),
}

WEEKDAY_JP = ['月', '火', '水', '木', '金', '土', '日']


def get_context(date_str: str = None) -> dict:
    """指定日（または今日）のコンテキスト情報を返す"""
    if date_str:
        target = datetime.strptime(date_str, '%Y%m%d')
    else:
        # JST で取得
        jst = timezone(timedelta(hours=9))
        target = datetime.now(jst)

    weekday = target.weekday()
    theme_jp, folder, theme_en = THEMES[weekday]
    weekday_jp = WEEKDAY_JP[weekday]

    date_key = target.strftime('%Y%m%d')
    date_display = f"{target.year}年{target.month}月{target.day}日（{weekday_jp}曜日）"
    date_short = f"{target.year}年{target.month}月{target.day}日（{weekday_jp}）"

    workspace = Path.home() / "Desktop/3勉強/claudeのファイル"

    base_filename = f"{date_key}_{theme_jp}"

    return {
        'date_key': date_key,
        'date_display': date_display,
        'date_short': date_short,
        'weekday_index': weekday,
        'weekday_jp': weekday_jp,
        'theme_jp': theme_jp,
        'theme_en': theme_en,
        'folder_name': folder,
        'folder_path': str(workspace / folder),
        'workspace_path': str(workspace),
        'regular_html_path': str(workspace / folder / f"{base_filename}.html"),
        'regular_docx_path': str(workspace / folder / f"{base_filename}.docx"),
        'detail_html_path': str(workspace / folder / f"{base_filename}_詳細分析.html"),
        'detail_docx_path': str(workspace / folder / f"{base_filename}_詳細分析.docx"),
        'favorites_viewer_path': str(workspace / "お気に入りビューア.html"),
        'email_subject_regular': f"【研究レポート】{theme_jp} — {date_short}",
        'email_subject_detail': f"【詳細分析】{theme_jp} — {date_short}Top 3論文",
        'email_subject_paths': f"【パス情報】{theme_jp} — {date_short}ローカルファイルパス",
    }


def main():
    date_str = None
    if '--date' in sys.argv:
        idx = sys.argv.index('--date')
        if idx + 1 < len(sys.argv):
            date_str = sys.argv[idx + 1]

    ctx = get_context(date_str)
    print(json.dumps(ctx, ensure_ascii=False, indent=2))


if __name__ == '__main__':
    main()
