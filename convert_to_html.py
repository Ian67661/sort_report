import markdown
import os

def convert_md_to_pretty_html(md_file_path, html_file_path):
    # 讀取 Markdown 內容
    if not os.path.exists(md_file_path):
        print(f"錯誤：找不到檔案 {md_file_path}")
        return

    with open(md_file_path, 'r', encoding='utf-8') as f:
        md_text = f.read()

    # 轉換為 HTML (啟動表格與程式碼高亮擴充)
    html_body = markdown.markdown(md_text, extensions=['extra', 'codehilite', 'toc'])

    # 定義漂亮的 HTML 模板 (包含 Water.css 與 MathJax)
    html_template = f"""<!DOCTYPE html>
<html lang="zh-Hant">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>排序演算法分析報告</title>
    <!-- 使用 Water.css 讓網頁自動變得美觀 -->
    <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/water.css@2/out/water.css">
    <!-- 載入 MathJax 用於顯示 O(n^2) 等數學公式 -->
    <script src="https://polyfill.io/v3/polyfill.min.js?features=es6"></script>
    <script id="MathJax-script" async src="https://cdn.jsdelivr.net/npm/mathjax@3/es5/tex-mml-chtml.js"></script>
    <style>
        body {{ max-width: 900px; margin: 20px auto; padding: 20px; line-height: 1.8; }}
        h1 {{ color: #0056b3; border-bottom: 2px solid #0056b3; padding-bottom: 10px; }}
        h2 {{ color: #007bff; margin-top: 2em; }}
        table {{ width: 100%; border-collapse: collapse; }}
        th {{ background-color: #f8f9fa; }}
        .codehilite {{ background: #f4f4f4; padding: 1em; border-radius: 5px; }}
    </style>
</head>
<body>
    {html_body}
</body>
</html>
"""

    # 寫出 HTML 檔案
    with open(html_file_path, 'w', encoding='utf-8') as f:
        f.write(html_template)
    print(f"轉換成功！網頁已生成至: {html_file_path}")

if __name__ == "__main__":
    input_path = r'd:\Ian\bublle\sort_report\README.md'
    output_path = r'd:\Ian\bublle\sort_report\index.html'
    convert_md_to_pretty_html(input_path, output_path)