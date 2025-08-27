#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Word文档内容预览工具
"""

from docx import Document
import os

def preview_docx(filename):
    """预览Word文档内容"""
    try:
        doc = Document(filename)
        content = []
        
        for paragraph in doc.paragraphs:
            if paragraph.text.strip():
                content.append(paragraph.text)
        
        full_text = '\n'.join(content)
        
        print(f"=== 文档预览：{filename} ===")
        print(f"总段落数：{len([p for p in content if p.strip()])}")
        print(f"总字符数：{len(full_text)}")
        print("\n" + "="*50)
        print("前1000字预览：")
        print("="*50)
        print(full_text[:1000] + "..." if len(full_text) > 1000 else full_text)
        print("="*50)
        
        return True
        
    except Exception as e:
        print(f"读取文档失败：{e}")
        return False

if __name__ == "__main__":
    # 查找最新的docx文件
    docx_files = [f for f in os.listdir('.') if f.endswith('.docx')]
    
    if docx_files:
        latest_file = max(docx_files, key=os.path.getctime)
        print(f"找到文档：{latest_file}")
        preview_docx(latest_file)
    else:
        print("未找到Word文档")
