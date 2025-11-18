#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import markdown
import os

# 定义HTML模板
HTML_TEMPLATE = '''<!DOCTYPE html>
<html lang="zh-CN">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{title}</title>
    <style>
        /* 全局样式 */
        * {{
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }}

        body {{
            font-family: 'Microsoft YaHei', Arial, sans-serif;
            line-height: 1.6;
            color: #333;
            background-color: #f8f9fa;
            padding: 20px;
        }}

        /* 返回按钮样式 */
        .back-button {{
            display: inline-block;
            margin-bottom: 20px;
            padding: 10px 20px;
            background: #fff;
            color: #333;
            text-decoration: none;
            border-radius: 8px;
            border: 1px solid #ddd;
            transition: all 0.3s ease;
            font-weight: 500;
            box-shadow: 0 2px 8px rgba(0, 0, 0, 0.1);
        }}

        .back-button:hover {{
            background: #f8f9fa;
            box-shadow: 0 4px 12px rgba(0, 0, 0, 0.15);
            transform: translateY(-2px);
        }}

        .back-button i {{
            margin-right: 8px;
        }}

        /* 容器样式 */
        .container {{
            max-width: 1200px;
            margin: 0 auto;
            background-color: #fff;
            border-radius: 8px;
            box-shadow: 0 0 20px rgba(0, 0, 0, 0.1);
            padding: 40px;
        }}

        /* 标题样式 */
        h1 {{
            text-align: center;
            color: #2c3e50;
            margin-bottom: 30px;
            font-size: 2.5em;
            font-weight: 700;
        }}

        h2 {{
            color: #34495e;
            margin: 40px 0 20px;
            padding-bottom: 10px;
            border-bottom: 2px solid #3498db;
            font-size: 2em;
        }}

        h3 {{
            color: #2ecc71;
            margin: 30px 0 15px;
            font-size: 1.5em;
        }}

        h4 {{
            color: #e74c3c;
            margin: 20px 0 10px;
            font-size: 1.2em;
        }}

        /* 段落样式 */
        p {{
            margin-bottom: 15px;
            text-align: justify;
            font-size: 1.1em;
        }}

        /* 列表样式 */
        ul, ol {{
            margin-bottom: 15px;
            margin-left: 25px;
        }}

        li {{
            margin-bottom: 8px;
            font-size: 1.1em;
        }}

        /* 表格样式 */
        table {{
            width: 100%;
            border-collapse: collapse;
            margin-bottom: 20px;
            font-size: 1em;
        }}

        th, td {{
            padding: 12px;
            text-align: left;
            border: 1px solid #ddd;
        }}

        th {{
            background-color: #3498db;
            color: white;
            font-weight: bold;
        }}

        tr:nth-child(even) {{
            background-color: #f2f2f2;
        }}

        /* 分隔线 */
        hr {{
            border: none;
            border-top: 1px solid #eee;
            margin: 30px 0;
        }}

        /* 卡片样式 */
        .card {{
            background-color: #f8f9fa;
            border-radius: 8px;
            padding: 25px;
            margin-bottom: 30px;
            box-shadow: 0 2px 10px rgba(0, 0, 0, 0.05);
        }}

        /* 学习进度表 */
        .progress-table {
            width: 100%;
            border-collapse: collapse;
            margin-bottom: 20px;
        }

        .progress-table th {
            background-color: #2ecc71;
        }

        /* 学习任务样式 */
        .task {
            background-color: #fff3cd;
            border-left: 4px solid #ffc107;
            padding: 15px;
            border-radius: 4px;
            margin: 15px 0;
        }

        /* 页脚 */
        footer {
            text-align: center;
            margin-top: 50px;
            padding-top: 20px;
            border-top: 1px solid #eee;
            color: #777;
            font-size: 0.9em;
        }

        /* 响应式设计 */
        @media (max-width: 768px) {{
            .container {{
                padding: 20px;
            }}

            h1 {{
                font-size: 2em;
            }}

            h2 {{
                font-size: 1.7em;
            }}

            h3 {{
                font-size: 1.4em;
            }}

            h4 {{
                font-size: 1.2em;
            }}

            p, li {{
                font-size: 1em;
            }}

            table {{
                font-size: 0.9em;
            }}

            th, td {{
                padding: 8px;
            }}
        }}
    </style>
</head>
<body>
    <div class="container">
        <!-- 返回按钮 -->
        <a href="index.html" class="back-button">
            <i>←</i> 返回首页
        </a>
        {content}
    </div>
</body>
</html>'''

# 定义深色主题HTML模板
DARK_HTML_TEMPLATE = '''<!DOCTYPE html>
<html lang="zh-CN">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{title}</title>
    <style>
        /* 全局样式 - 深色主题 */
        * {{
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }}

        body {{
            font-family: 'Microsoft YaHei', Arial, sans-serif;
            line-height: 1.6;
            color: #e0e0e0;
            background-color: #121212;
            padding: 20px;
        }}

        /* 返回按钮样式 - 深色主题 */
        .back-button {{
            display: inline-block;
            margin-bottom: 20px;
            padding: 10px 20px;
            background: #2c2c2c;
            color: #e0e0e0;
            text-decoration: none;
            border-radius: 8px;
            border: 1px solid #444;
            transition: all 0.3s ease;
            font-weight: 500;
            box-shadow: 0 2px 8px rgba(0, 0, 0, 0.3);
        }}

        .back-button:hover {{
            background: #3a3a3a;
            box-shadow: 0 4px 12px rgba(0, 0, 0, 0.5);
            transform: translateY(-2px);
        }}

        .back-button i {{
            margin-right: 8px;
        }}

        /* 容器样式 - 深色主题 */
        .container {{
            max-width: 1200px;
            margin: 0 auto;
            background-color: #1e1e1e;
            border-radius: 8px;
            box-shadow: 0 0 20px rgba(0, 0, 0, 0.5);
            padding: 40px;
        }}

        /* 标题样式 - 深色主题 */
        h1 {{
            text-align: center;
            color: #ffffff;
            margin-bottom: 30px;
            font-size: 2.5em;
            font-weight: 700;
        }}

        h2 {{
            color: #bb86fc;
            margin: 40px 0 20px;
            padding-bottom: 10px;
            border-bottom: 2px solid #3700b3;
            font-size: 2em;
        }}

        h3 {{
            color: #03dac6;
            margin: 30px 0 15px;
            font-size: 1.5em;
        }}

        h4 {{
            color: #ff5252;
            margin: 20px 0 10px;
            font-size: 1.2em;
        }}

        /* 段落样式 - 深色主题 */
        p {{
            margin-bottom: 15px;
            text-align: justify;
            font-size: 1.1em;
            color: #e0e0e0;
        }}

        /* 列表样式 - 深色主题 */
        ul, ol {{
            margin-bottom: 15px;
            margin-left: 25px;
        }}

        li {{
            margin-bottom: 8px;
            font-size: 1.1em;
            color: #e0e0e0;
        }}

        /* 表格样式 - 深色主题 */
        table {{
            width: 100%;
            border-collapse: collapse;
            margin-bottom: 20px;
            font-size: 1em;
        }}

        th, td {{
            padding: 12px;
            text-align: left;
            border: 1px solid #333;
        }}

        th {{
            background-color: #3700b3;
            color: white;
            font-weight: bold;
        }}

        tr:nth-child(even) {{
            background-color: #2a2a2a;
        }}

        /* 分隔线 - 深色主题 */
        hr {{
            border: none;
            border-top: 1px solid #333;
            margin: 30px 0;
        }}

        /* 卡片样式 - 深色主题 */
        .card {{
            background-color: #2a2a2a;
            border-radius: 8px;
            padding: 25px;
            margin-bottom: 30px;
            box-shadow: 0 2px 10px rgba(0, 0, 0, 0.3);
        }}

        /* 学习进度表 - 深色主题 */
        .progress-table {
            width: 100%;
            border-collapse: collapse;
            margin-bottom: 20px;
        }

        .progress-table th {
            background-color: #018786;
        }

        /* 学习任务样式 - 深色主题 */
        .task {
            background-color: #383838;
            border-left: 4px solid #ffb300;
            padding: 15px;
            border-radius: 4px;
            margin: 15px 0;
        }

        /* 页脚 - 深色主题 */
        footer {
            text-align: center;
            margin-top: 50px;
            padding-top: 20px;
            border-top: 1px solid #333;
            color: #888;
            font-size: 0.9em;
        }}

        /* 响应式设计 - 深色主题 */
        @media (max-width: 768px) {{
            .container {{
                padding: 20px;
            }}

            h1 {{
                font-size: 2em;
            }}

            h2 {{
                font-size: 1.7em;
            }}

            h3 {{
                font-size: 1.4em;
            }}

            h4 {{
                font-size: 1.2em;
            }}

            p, li {{
                font-size: 1em;
            }}

            table {{
                font-size: 0.9em;
            }}

            th, td {{
                padding: 8px;
            }}
        }}
    </style>
</head>
<body>
    <div class="container">
        <!-- 返回按钮 -->
        <a href="index.html" class="back-button">
            <i>←</i> 返回首页
        </a>
        {content}
    </div>
</body>
</html>'''

def convert_md_to_html(md_file, html_file, dark_theme=False):
    """
    将Markdown文件转换为HTML文件
    
    Args:
        md_file: Markdown文件路径
        html_file: 输出HTML文件路径
        dark_theme: 是否使用深色主题
    """
    try:
        # 读取Markdown文件
        with open(md_file, 'r', encoding='utf-8') as f:
            md_content = f.read()
        
        # 转换为HTML
        html_content = markdown.markdown(md_content, extensions=['extra', 'tables', 'attr_list'])
        
        # 提取标题（使用第一个h1标签的内容）
        import re
        match = re.search(r'#\s+(.*)', md_content)
        title = match.group(1) if match else os.path.splitext(os.path.basename(md_file))[0]
        
        # 选择HTML模板
        template = DARK_HTML_TEMPLATE if dark_theme else HTML_TEMPLATE
        
        # 生成完整HTML（使用字符串替换而不是format，避免CSS中的{}被当作占位符）
        full_html = template.replace('{title}', title).replace('{content}', html_content)
        
        # 写入HTML文件
        with open(html_file, 'w', encoding='utf-8') as f:
            f.write(full_html)
        
        print(f"✓ 已转换: {md_file} -> {html_file}")
        
    except Exception as e:
        print(f"✗ 转换失败 {md_file}: {e}")
        import traceback
        traceback.print_exc()

def main():
    """
    转换所有Markdown文件为HTML文件
    """
    # 当前目录
    current_dir = os.path.dirname(os.path.abspath(__file__))
    
    # 遍历当前目录下的所有文件
    for file in os.listdir(current_dir):
        if file.endswith('.md') and not file.startswith('.'):
            md_file = os.path.join(current_dir, file)
            html_file = os.path.join(current_dir, file.replace('.md', '.html'))
            
            # 确定是否使用深色主题（学习任务表使用深色主题）
            dark_theme = '学习任务表' in file
            
            # 转换文件
            convert_md_to_html(md_file, html_file, dark_theme)

if __name__ == '__main__':
    main()