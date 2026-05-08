# 瞳伴商业计划书 格式核查报告

## 要求规范

| 元素 | 字体 | 字号 | 加粗 | 对齐 | 缩进 | 行距 |
|------|------|------|------|------|------|------|
| 题目 | 宋体 | 小二 (18bp) | 加粗 | 居中 | — | 固定 22 磅 |
| 一级标题 | 宋体 | 四号 (14bp) | 加粗 | 左对齐 | — | 固定 22 磅 |
| 二级标题 | 宋体 | 小四 (12bp) | 加粗 | — | 首行缩进 2 字符 | 固定 22 磅 |
| 正文 | 宋体 | 小四 (12bp) | 不加粗 | 两端对齐 | 首行缩进 2 字符 | 固定 22 磅 |

> [!NOTE]
> 中文字号与 bp 的标准换算：小二 = 18bp，四号 = 14bp，小四 = 12bp。

---

## 逐项核查

### 1. 题目（`\ReportTitle` 命令，第 122–126 行）

```latex
\newcommand{\ReportTitle}[1]{%
  \begin{center}
    \SongBold\fontsize{18bp}{22bp}\selectfont #1
  \end{center}
}
```

| 项目 | 要求 | 实际 | 是否符合 |
|------|------|------|----------|
| 字体 | 宋体 | `\SongBold` → SimSun / Songti SC | ✅ 符合 |
| 字号 | 小二 (18bp) | `\fontsize{18bp}{...}` | ✅ 符合 |
| 加粗 | 加粗 | `\SongBold` (FakeBold=2.5) | ✅ 符合 |
| 居中 | 居中 | `\begin{center}...\end{center}` | ✅ 符合 |
| 行距 | 固定 22 磅 | `\fontsize{18bp}{22bp}` → baselineskip=22bp | ✅ 符合 |

> [!WARNING]
> **潜在问题**：`\ReportTitle` 在文档中**从未被调用**！搜索全文发现，文档中没有 `\ReportTitle{...}` 的使用。这意味着文档标题可能没有按此格式排版，或是使用了其他方式（如封面 PDF 中包含了标题）。请确认标题是通过 `\includepdf` 导入的封面实现的，还是需要在正文中使用 `\ReportTitle` 命令。

---

### 2. 一级标题（`\section`，第 68–73 行）

```latex
\titleformat{\section}
  {\raggedright\SongBold\fontsize{14bp}{22bp}\selectfont}
  {\chinese{section}、}
  {0pt}
  {}
\titlespacing*{\section}{0pt}{18bp}{12bp}
```

| 项目 | 要求 | 实际 | 是否符合 |
|------|------|------|----------|
| 字体 | 宋体 | `\SongBold` → SimSun / Songti SC | ✅ 符合 |
| 字号 | 四号 (14bp) | `\fontsize{14bp}{...}` | ✅ 符合 |
| 加粗 | 加粗 | `\SongBold` (FakeBold=2.5) | ✅ 符合 |
| 左对齐 | 左对齐 | `\raggedright` | ✅ 符合 |
| 行距 | 固定 22 磅 | `\fontsize{14bp}{22bp}` → baselineskip=22bp | ✅ 符合 |

> [!TIP]
> 一级标题完全符合要求。

---

### 3. 二级标题（`\subsection`，第 75–80 行）

```latex
\titleformat{\subsection}
  {\raggedright\SongBold\fontsize{12bp}{22bp}\selectfont}
  {\hspace{2em}（\chinese{subsection}）}
  {0pt}
  {}
\titlespacing*{\subsection}{0pt}{14bp}{6bp}
```

| 项目 | 要求 | 实际 | 是否符合 |
|------|------|------|----------|
| 字体 | 宋体 | `\SongBold` → SimSun / Songti SC | ✅ 符合 |
| 字号 | 小四 (12bp) | `\fontsize{12bp}{...}` | ✅ 符合 |
| 加粗 | 加粗 | `\SongBold` (FakeBold=2.5) | ✅ 符合 |
| 首行缩进 2 字符 | 首行缩进 2 字符 | ⚠️ 见下方分析 | ⚠️ 需确认 |
| 行距 | 固定 22 磅 | `\fontsize{12bp}{22bp}` → baselineskip=22bp | ✅ 符合 |

> [!IMPORTANT]
> **缩进问题分析**：当前实现方式是通过 `\hspace{2em}` 在**编号前面**手动加空格来模拟缩进（如 `\hspace{2em}（一）`）。但 `\titlespacing*` 的左缩进设置为 `0pt`，且格式中使用 `\raggedright`（左对齐而非两端对齐）。
>
> 严格来说，这**不是真正的"首行缩进 2 字符"**，而是编号前手动加了 2em 空白。视觉效果上接近，但实现方式不同于正文的 `\parindent`。如果二级标题文字过长折行，**第二行将从左边距开始**，而非从缩进位置开始——这是与要求中"首行缩进"含义一致的（首行缩进只影响第一行）。
>
> **结论**：视觉效果基本符合要求，但建议将 `\titlespacing*` 的左缩进改为 `2em` 并去掉 `\hspace{2em}`，这样更规范。

---

### 4. 正文（全局设置，第 51–66 行）

```latex
\renewcommand\normalsize{%
  \@setfontsize\normalsize{12bp}{22bp}%
  ...
}
\normalsize
\setlength{\parindent}{2em}
\setlength{\parskip}{0pt}
\setstretch{1}
```

| 项目 | 要求 | 实际 | 是否符合 |
|------|------|------|----------|
| 字体 | 宋体 | `\setCJKmainfont{SimSun}` (第 32 行) | ✅ 符合 |
| 字号 | 小四 (12bp) | `\@setfontsize\normalsize{12bp}{22bp}` | ✅ 符合 |
| 加粗 | 不加粗 | 正文默认不加粗 | ✅ 符合 |
| 两端对齐 | 两端对齐 | LaTeX 默认就是两端对齐（justified） | ✅ 符合 |
| 首行缩进 2 字符 | 首行缩进 2 字符 | `\setlength{\parindent}{2em}` + `\usepackage{indentfirst}` | ✅ 符合 |
| 行距 | 固定 22 磅 | `\@setfontsize\normalsize{12bp}{22bp}` → baselineskip=22bp | ✅ 符合 |

> [!TIP]
> 正文格式完全符合要求。`indentfirst` 宏包确保了第一段也有首行缩进。

---

## 总结

| 元素 | 字体 | 字号 | 加粗 | 对齐/缩进 | 行距 | 总评 |
|------|:----:|:----:|:----:|:---------:|:----:|:----:|
| 题目 | ✅ | ✅ | ✅ | ✅ | ✅ | ⚠️ 命令定义正确，但未在正文中被调用 |
| 一级标题 | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ 完全符合 |
| 二级标题 | ✅ | ✅ | ✅ | ⚠️ | ✅ | ⚠️ 缩进实现方式可优化 |
| 正文 | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ 完全符合 |

---

## 发现的问题与建议

### 问题 1：`\ReportTitle` 未被调用

> [!CAUTION]
> `\ReportTitle` 命令在第 122–126 行定义，但**全文未使用**。如果你的"题目"是需要出现在正文中的（而非仅在封面 PDF 中），你需要在 `\begin{document}` 后的适当位置调用它，例如：
> ```latex
> \ReportTitle{瞳伴——智能导盲陪行机器人商业计划书}
> ```

### 问题 2：二级标题缩进方式不够规范

当前：用 `\hspace{2em}` 在编号前手动添加空格
建议：改用 `\titlespacing*` 的 `indent` 参数

```diff
 \titleformat{\subsection}
-  {\raggedright\SongBold\fontsize{12bp}{22bp}\selectfont}
-  {\hspace{2em}（\chinese{subsection}）}
+  {\SongBold\fontsize{12bp}{22bp}\selectfont}
+  {（\chinese{subsection}）}
   {0pt}
   {}
-\titlespacing*{\subsection}{0pt}{14bp}{6bp}
+\titlespacing*{\subsection}{2em}{14bp}{6bp}
```

> [!NOTE]
> 这个修改会让二级标题的整体左边距为 2em（包括编号和标题文字），视觉效果与当前基本一致，但更符合"首行缩进"的语义。同时去掉了 `\raggedright`，使二级标题在文字较长时也能两端对齐（如果不需要两端对齐，可以保留 `\raggedright`）。

### 其他注意事项

- **行距说明**：文档使用 `\@setfontsize{...}{12bp}{22bp}` 设置 baselineskip 为 22bp。同时 `\setstretch{1}` 确保没有额外的行距倍数。这等效于固定行距 22 磅。✅ 正确。
- **字体一致性**：所有宋体通过 `\setCJKmainfont[AutoFakeBold=2.5]{SimSun}` 统一设置，加粗通过 `\SongBold`（`FakeBold=2.5`）实现。✅ 正确。
- **页边距**：`top=2.54cm, bottom=2.54cm, left=3.175cm, right=3.175cm` — 标准 Word 页边距。✅ 正确。
