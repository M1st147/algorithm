import tkinter as tk
from tkinter import filedialog, messagebox
from tkinter import scrolledtext
import joblib
import os
import sys
import sklearn

# 加载模型和矢量化器
tfidf_vectorizer = joblib.load('tfidf_vectorizer.pkl')
pac = joblib.load('passive_aggressive_classifier.pkl')

# 定义预测函数
def predict_news(text):
    # 进行TF-IDF转换
    text_tfidf = tfidf_vectorizer.transform([text])
    # 进行预测
    prediction = pac.predict(text_tfidf)
    return prediction[0]

# 定义处理单条新闻的函数
def handle_single_news():
    news_text = single_entry.get("1.0", tk.END).strip()
    if news_text:
        result = predict_news(news_text)
        messagebox.showinfo("预测结果", f'该新闻预测为: {result}')
    else:
        messagebox.showwarning("输入错误", "请输入新闻文本。")

# 定义处理文件中的新闻的函数
def handle_file_news():
    file_path = filedialog.askopenfilename(title="选择新闻文件", filetypes=[("Text files", "*.txt")])
    if file_path:
        with open(file_path, 'r', encoding='utf-8') as f:
            news_list = f.readlines()
        
        results = []
        for news in news_list:
            result = predict_news(news.strip())
            results.append((news.strip(), result))
        
        save_results(results)
    else:
        messagebox.showwarning("文件错误", "未选择文件。")

# 定义保存结果的函数
def save_results(results):
    save_path = filedialog.asksaveasfilename(title="保存结果", defaultextension=".txt", filetypes=[("Text files", "*.txt")])
    if save_path:
        with open(save_path, 'w', encoding='utf-8') as f:
            for news, result in results:
                f.write(f'{news}\t{result}\n')
        messagebox.showinfo("保存成功", f'结果已保存到 {save_path}')
    else:
        messagebox.showwarning("保存错误", "未指定保存路径。")

# 创建主窗口
root = tk.Tk()
root.title("新闻真实性分类器")
root.geometry("600x400")

# 设置字体样式
font_style = ("Arial", 12)

# 创建单条新闻输入框
tk.Label(root, text="输入新闻文本:", font=("Arial", 14)).pack(pady=10)
single_entry = scrolledtext.ScrolledText(root, height=10, width=70, font=font_style, wrap=tk.WORD)
single_entry.pack(pady=10)

# 创建按钮
single_button = tk.Button(root, text="分类单条新闻", font=font_style, command=handle_single_news, bg="#4CAF50", fg="white")
single_button.pack(pady=5)

file_button = tk.Button(root, text="从文件分类新闻", font=font_style, command=handle_file_news, bg="#2196F3", fg="white")
file_button.pack(pady=5)

# 运行主循环
root.mainloop()
