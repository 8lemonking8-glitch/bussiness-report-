"""
瞳伴商业计划书 - 5张示意图绘制脚本
使用seaborn和matplotlib绘制，分辨率300dpi
"""

import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from matplotlib.patches import FancyBboxPatch, Circle, Rectangle, FancyArrowPatch, Wedge
import seaborn as sns
import numpy as np
from matplotlib.font_manager import FontProperties
import os

# 设置中文字体（跨平台兼容）
def setup_chinese_font():
    """配置中文字体，确保在Windows和Mac上都能正常显示"""
    import platform
    system = platform.system()
    
    if system == 'Windows':
        # Windows系统字体
        font_paths = [
            'C:/Windows/Fonts/simhei.ttf',      # 黑体
            'C:/Windows/Fonts/simsun.ttc',       # 宋体
        ]
    else:  # Mac/Linux
        font_paths = [
            '/System/Library/Fonts/PingFang.ttc',
            '/Library/Fonts/Arial Unicode.ttf',
        ]
    
    for font_path in font_paths:
        if os.path.exists(font_path):
            return FontProperties(fname=font_path)
    
    # 如果都找不到，返回默认字体
    return FontProperties(family='sans-serif')

# 初始化字体
chinese_font = setup_chinese_font()

# 设置全局样式
sns.set_style("whitegrid")
plt.rcParams['axes.unicode_minus'] = False  # 解决负号显示问题

# 输出目录
output_dir = os.path.dirname(os.path.abspath(__file__))


def draw_user_journey():
    """
    图1：用户使用全流程示意图（泳道时间轴）
    放置位置：Page 6（二、产品简介）
    """
    fig, ax = plt.subplots(figsize=(14, 8))
    
    # 定义步骤数据
    steps = [
        {"step": 1, "title": "语音输入", "desc": "用户说：\n'去3号诊室'", "icon": "🎤"},
        {"step": 2, "title": "路径规划", "desc": "激光雷达\n扫描环境", "icon": "📡"},
        {"step": 3, "title": "手柄引导", "desc": "向前轻推+\n语音提示", "icon": "👆"},
        {"step": 4, "title": "实时避障", "desc": "减速并\n绕过障碍", "icon": "⚠️"},
        {"step": 5, "title": "到达播报", "desc": "'已到达\n3号诊室'", "icon": "✅"}
    ]
    
    # 颜色方案
    colors = ['#3498db', '#2ecc71', '#f39c12', '#e74c3c', '#9b59b6']
    
    # 绘制时间轴主线
    y_center = 4
    line_y = y_center + 0.5
    ax.plot([1, 13], [line_y, line_y], 'k-', linewidth=3, alpha=0.3)
    
    # 绘制每个步骤
    x_positions = np.linspace(1.5, 12.5, 5)
    
    for i, (step_data, x_pos, color) in enumerate(zip(steps, x_positions, colors)):
        # 绘制节点圆圈
        circle = Circle((x_pos, line_y), 0.35, color=color, zorder=3, ec='white', linewidth=2)
        ax.add_patch(circle)
        
        # 添加步骤编号
        ax.text(x_pos, line_y, str(step_data['step']), 
                ha='center', va='center', fontsize=14, fontweight='bold', 
                color='white', fontproperties=chinese_font)
        
        # 绘制箭头连接（除了最后一个）
        if i < len(steps) - 1:
            arrow = FancyArrowPatch(
                (x_pos + 0.4, line_y), (x_positions[i+1] - 0.4, line_y),
                arrowstyle='->', mutation_scale=30, linewidth=2.5,
                color=color, alpha=0.6, zorder=2
            )
            ax.add_patch(arrow)
        
        # 绘制信息框（上方）
        box_width = 2.2
        box_height = 1.8
        box_x = x_pos - box_width/2
        box_y = line_y + 0.8
        
        fancy_box = FancyBboxPatch(
            (box_x, box_y), box_width, box_height,
            boxstyle="round,pad=0.1", 
            facecolor=color, alpha=0.15,
            edgecolor=color, linewidth=2, zorder=1
        )
        ax.add_patch(fancy_box)
        
        # 添加图标和标题
        ax.text(x_pos, box_y + box_height - 0.4, step_data['icon'],
                ha='center', va='center', fontsize=24)
        ax.text(x_pos, box_y + box_height - 0.9, step_data['title'],
                ha='center', va='center', fontsize=11, fontweight='bold',
                fontproperties=chinese_font, color=color)
        
        # 添加描述文字
        ax.text(x_pos, box_y + 0.4, step_data['desc'],
                ha='center', va='center', fontsize=9,
                fontproperties=chinese_font, style='italic')
    
    # 添加标题
    ax.text(7, 7.5, '用户使用全流程示意图', 
            ha='center', va='center', fontsize=18, fontweight='bold',
            fontproperties=chinese_font, color='#2c3e50')
    
    # 添加底部说明
    ax.text(7, 0.5, '从语音指令到完成导引的完整交互流程', 
            ha='center', va='center', fontsize=10,
            fontproperties=chinese_font, style='italic', color='#7f8c8d')
    
    # 设置坐标轴
    ax.set_xlim(0, 14)
    ax.set_ylim(0, 8)
    ax.axis('off')
    
    plt.tight_layout()
    plt.savefig(os.path.join(output_dir, 'user_journey.png'), 
                dpi=300, bbox_inches='tight', facecolor='white')
    plt.close()
    print("✓ 图1已生成：user_journey.png")


def draw_static_to_dynamic():
    """
    图2："从静态设施到动态服务"价值跃迁对比图
    放置位置：Page 11（六、产品优势与先进性）
    """
    fig, ax = plt.subplots(figsize=(14, 9))
    
    # 左侧：传统静态设施
    left_x = 2
    left_items = [
        {"icon": "🛤️", "name": "盲道", "pain": "能到楼下，\n却找不到诊室"},
        {"icon": "♿", "name": "坡道", "pain": "固定路线，\n无法灵活调整"},
        {"icon": "🛗", "name": "电梯", "pain": "只能到达楼层，\n无室内导航"}
    ]
    
    # 右侧：瞳伴动态服务
    right_x = 10
    right_items = [
        {"icon": "🚪", "name": "门口接驳", "value": "全程陪行至\n最终目的地"},
        {"icon": "🧭", "name": "实时避障导航", "value": "精准定位至\n诊室门口"},
        {"icon": "🎯", "name": "语音确认点", "value": "交互式引导，\n安全可控"}
    ]
    
    # 绘制左侧背景
    left_bg = FancyBboxPatch(
        (left_x - 1.5, 1), 5, 7,
        boxstyle="round,pad=0.2",
        facecolor='#ecf0f1', alpha=0.5,
        edgecolor='#95a5a6', linewidth=2, linestyle='--'
    )
    ax.add_patch(left_bg)
    
    # 绘制右侧背景
    right_bg = FancyBboxPatch(
        (right_x - 1.5, 1), 5, 7,
        boxstyle="round,pad=0.2",
        facecolor='#d5f4e6', alpha=0.5,
        edgecolor='#27ae60', linewidth=2
    )
    ax.add_patch(right_bg)
    
    # 绘制左侧项目
    for i, item in enumerate(left_items):
        y_pos = 6.5 - i * 2
        
        # 图标
        ax.text(left_x, y_pos + 0.5, item['icon'],
                ha='center', va='center', fontsize=28)
        
        # 名称
        ax.text(left_x, y_pos - 0.2, item['name'],
                ha='center', va='center', fontsize=12, fontweight='bold',
                fontproperties=chinese_font, color='#7f8c8d')
        
        # 痛点标注
        pain_box = FancyBboxPatch(
            (left_x - 1, y_pos - 1.2), 2, 0.8,
            boxstyle="round,pad=0.05",
            facecolor='#fadbd8', alpha=0.7,
            edgecolor='#e74c3c', linewidth=1.5
        )
        ax.add_patch(pain_box)
        ax.text(left_x, y_pos - 0.8, item['pain'],
                ha='center', va='center', fontsize=9,
                fontproperties=chinese_font, color='#c0392b')
    
    # 绘制右侧项目
    for i, item in enumerate(right_items):
        y_pos = 6.5 - i * 2
        
        # 图标
        ax.text(right_x, y_pos + 0.5, item['icon'],
                ha='center', va='center', fontsize=28)
        
        # 名称
        ax.text(right_x, y_pos - 0.2, item['name'],
                ha='center', va='center', fontsize=12, fontweight='bold',
                fontproperties=chinese_font, color='#27ae60')
        
        # 价值标注
        value_box = FancyBboxPatch(
            (right_x - 1, y_pos - 1.2), 2, 0.8,
            boxstyle="round,pad=0.05",
            facecolor='#d5f4e6', alpha=0.7,
            edgecolor='#27ae60', linewidth=1.5
        )
        ax.add_patch(value_box)
        ax.text(right_x, y_pos - 0.8, item['value'],
                ha='center', va='center', fontsize=9,
                fontproperties=chinese_font, color='#1e8449')
    
    # 中间转换箭头
    arrow = FancyArrowPatch(
        (5.5, 4.5), (7.5, 4.5),
        arrowstyle='->', mutation_scale=50, linewidth=4,
        color='#3498db', alpha=0.8, zorder=5
    )
    ax.add_patch(arrow)
    
    # 转换标签
    ax.text(6.5, 5.2, '价值跃迁', 
            ha='center', va='center', fontsize=14, fontweight='bold',
            fontproperties=chinese_font, color='#3498db',
            bbox=dict(boxstyle='round,pad=0.5', facecolor='white', 
                     edgecolor='#3498db', linewidth=2))
    
    # 添加标题
    ax.text(6.5, 8.5, '"从静态设施到动态服务"的价值跃迁', 
            ha='center', va='center', fontsize=18, fontweight='bold',
            fontproperties=chinese_font, color='#2c3e50')
    
    # 添加副标题
    ax.text(2, 0.5, '传统静态设施：被动式无障碍', 
            ha='center', va='center', fontsize=11,
            fontproperties=chinese_font, style='italic', color='#7f8c8d')
    ax.text(10, 0.5, '瞳伴动态服务：主动式智能陪行', 
            ha='center', va='center', fontsize=11,
            fontproperties=chinese_font, style='italic', color='#27ae60')
    
    # 设置坐标轴
    ax.set_xlim(0, 13)
    ax.set_ylim(0, 9)
    ax.axis('off')
    
    plt.tight_layout()
    plt.savefig(os.path.join(output_dir, 'static_to_dynamic.png'), 
                dpi=300, bbox_inches='tight', facecolor='white')
    plt.close()
    print("✓ 图2已生成：static_to_dynamic.png")


def draw_safety_mechanism():
    """
    图3："人-机-环境"三元安全机制同心圆图
    放置位置：Page 30（六、安全保障）
    """
    fig, ax = plt.subplots(figsize=(12, 12))
    
    # 定义三层结构
    layers = [
        {
            "radius": 3.5,
            "color": "#e74c3c",
            "name": "外层：人工兜底",
            "items": ["后台异常告警", "工作人员就近介入"]
        },
        {
            "radius": 2.3,
            "color": "#f39c12",
            "name": "中层：用户控制",
            "items": ["物理急停键", "语音指令'停下'"]
        },
        {
            "radius": 1.2,
            "color": "#3498db",
            "name": "核心层：机器判断",
            "items": ["实时避障", "定位丢失即停", "低电量报警"]
        }
    ]
    
    center_x, center_y = 6, 6
    
    # 从外到内绘制同心圆
    for layer in layers:
        circle = Circle((center_x, center_y), layer['radius'],
                       facecolor=layer['color'], alpha=0.2,
                       edgecolor=layer['color'], linewidth=3)
        ax.add_patch(circle)
    
    # 添加每层的标签和内容
    # 外层
    outer_angle = 90
    for i, item in enumerate(layers[0]['items']):
        angle = outer_angle + i * 60
        rad = np.radians(angle)
        r = 2.9
        x = center_x + r * np.cos(rad)
        y = center_y + r * np.sin(rad)
        
        # 绘制小圆点
        dot = Circle((x, y), 0.15, color=layers[0]['color'], zorder=3)
        ax.add_patch(dot)
        
        # 添加文字
        ax.text(x, y + 0.4, item,
                ha='center', va='center', fontsize=10,
                fontproperties=chinese_font, fontweight='bold',
                color=layers[0]['color'])
    
    # 中层
    middle_angle = 45
    for i, item in enumerate(layers[1]['items']):
        angle = middle_angle + i * 90
        rad = np.radians(angle)
        r = 1.8
        x = center_x + r * np.cos(rad)
        y = center_y + r * np.sin(rad)
        
        # 绘制小圆点
        dot = Circle((x, y), 0.12, color=layers[1]['color'], zorder=3)
        ax.add_patch(dot)
        
        # 添加文字
        ax.text(x, y + 0.35, item,
                ha='center', va='center', fontsize=10,
                fontproperties=chinese_font, fontweight='bold',
                color=layers[1]['color'])
    
    # 核心层
    inner_angles = [90, 210, 330]
    for i, (angle, item) in enumerate(zip(inner_angles, layers[2]['items'])):
        rad = np.radians(angle)
        r = 0.7
        x = center_x + r * np.cos(rad)
        y = center_y + r * np.sin(rad)
        
        # 绘制小圆点
        dot = Circle((x, y), 0.1, color=layers[2]['color'], zorder=3)
        ax.add_patch(dot)
        
        # 添加文字
        ax.text(x, y + 0.3, item,
                ha='center', va='center', fontsize=9,
                fontproperties=chinese_font, fontweight='bold',
                color=layers[2]['color'])
    
    # 中心标识
    center_circle = Circle((center_x, center_y), 0.4,
                          facecolor='#2c3e50', alpha=0.9, zorder=4)
    ax.add_patch(center_circle)
    ax.text(center_x, center_y, '安全\n核心',
            ha='center', va='center', fontsize=11, fontweight='bold',
            fontproperties=chinese_font, color='white')
    
    # 添加层级标签（在圆环外侧）
    ax.text(center_x + 3.8, center_y + 0.5, '外层：人工兜底',
            ha='left', va='center', fontsize=12, fontweight='bold',
            fontproperties=chinese_font, color=layers[0]['color'],
            bbox=dict(boxstyle='round,pad=0.4', facecolor='white', 
                     edgecolor=layers[0]['color'], linewidth=2, alpha=0.8))
    
    ax.text(center_x - 2.5, center_y - 1.5, '中层：用户控制',
            ha='left', va='center', fontsize=12, fontweight='bold',
            fontproperties=chinese_font, color=layers[1]['color'],
            bbox=dict(boxstyle='round,pad=0.4', facecolor='white', 
                     edgecolor=layers[1]['color'], linewidth=2, alpha=0.8))
    
    ax.text(center_x + 1.5, center_y - 2.8, '核心层：机器判断',
            ha='left', va='center', fontsize=12, fontweight='bold',
            fontproperties=chinese_font, color=layers[2]['color'],
            bbox=dict(boxstyle='round,pad=0.4', facecolor='white', 
                     edgecolor=layers[2]['color'], linewidth=2, alpha=0.8))
    
    # 添加标题
    ax.text(center_x, 10.5, '"人-机-环境"三元安全机制架构', 
            ha='center', va='center', fontsize=18, fontweight='bold',
            fontproperties=chinese_font, color='#2c3e50')
    
    # 添加底部说明
    ax.text(center_x, 1, '三层保护体系确保用户绝对安全', 
            ha='center', va='center', fontsize=11,
            fontproperties=chinese_font, style='italic', color='#7f8c8d')
    
    # 设置坐标轴
    ax.set_xlim(0, 12)
    ax.set_ylim(0, 12)
    ax.set_aspect('equal')
    ax.axis('off')
    
    plt.tight_layout()
    plt.savefig(os.path.join(output_dir, 'safety_mechanism.png'), 
                dpi=300, bbox_inches='tight', facecolor='white')
    plt.close()
    print("✓ 图3已生成：safety_mechanism.png")


def draw_milestone_roadmap():
    """
    图4：五年规划关键里程碑路线图
    放置位置：Page 31（七、商业与技术落地里程碑）
    """
    fig, ax = plt.subplots(figsize=(16, 8))
    
    # 定义三个阶段
    phases = [
        {
            "name": "初创期",
            "period": "2027-2028",
            "x_range": (1, 5.5),
            "color": "#3498db",
            "milestones": [
                {"time": "第6个月", "event": "产品定型", "y": 5},
                {"time": "第12个月", "event": "现金流回正", "y": 3}
            ]
        },
        {
            "name": "成长验证期",
            "period": "2029-2030",
            "x_range": (5.5, 10),
            "color": "#2ecc71",
            "milestones": [
                {"time": "第24个月", "event": "盈亏平衡", "y": 5},
                {"time": "第36个月", "event": "累计盈亏平衡", "y": 3}
            ]
        },
        {
            "name": "规模复制期",
            "period": "2031+",
            "x_range": (10, 14.5),
            "color": "#9b59b6",
            "milestones": [
                {"time": "第48个月", "event": "全国布局", "y": 5},
                {"time": "第60个月", "event": "市场领先", "y": 3}
            ]
        }
    ]
    
    # 绘制阶段背景
    for phase in phases:
        rect = Rectangle(
            (phase['x_range'][0], 0.5), 
            phase['x_range'][1] - phase['x_range'][0], 6,
            facecolor=phase['color'], alpha=0.1,
            edgecolor=phase['color'], linewidth=2, linestyle='--'
        )
        ax.add_patch(rect)
        
        # 阶段标签
        ax.text(np.mean(phase['x_range']), 6.8, phase['name'],
                ha='center', va='center', fontsize=14, fontweight='bold',
                fontproperties=chinese_font, color=phase['color'])
        ax.text(np.mean(phase['x_range']), 6.3, phase['period'],
                ha='center', va='center', fontsize=10,
                fontproperties=chinese_font, style='italic', color=phase['color'])
    
    # 绘制时间轴主线
    ax.plot([1, 14.5], [3.5, 3.5], 'k-', linewidth=4, alpha=0.3)
    
    # 年份标记
    years = [2027, 2028, 2029, 2030, 2031]
    year_positions = np.linspace(1, 14.5, 5)
    for year, x_pos in zip(years, year_positions):
        ax.plot([x_pos, x_pos], [3.3, 3.7], 'k-', linewidth=2)
        ax.text(x_pos, 2.8, str(year),
                ha='center', va='center', fontsize=11, fontweight='bold',
                fontproperties=chinese_font, color='#2c3e50')
    
    # 绘制里程碑
    milestone_icons = ["🎯", "💰", "⚖️", "📈", "🌟", "🏆"]
    icon_idx = 0
    
    for phase in phases:
        for milestone in phase['milestones']:
            # 计算x位置（根据时间在阶段内的相对位置）
            phase_start, phase_end = phase['x_range']
            month = int(milestone['time'].replace('第', '').replace('个月', ''))
            
            if phase['name'] == "初创期":
                x_pos = phase_start + (month / 24) * (phase_end - phase_start)
            elif phase['name'] == "成长验证期":
                x_pos = phase_start + ((month - 12) / 24) * (phase_end - phase_start)
            else:
                x_pos = phase_start + ((month - 24) / 36) * (phase_end - phase_start)
            
            y_pos = milestone['y']
            
            # 绘制里程碑节点
            circle = Circle((x_pos, y_pos), 0.35, 
                          color=phase['color'], zorder=3,
                          ec='white', linewidth=2)
            ax.add_patch(circle)
            
            # 添加图标
            ax.text(x_pos, y_pos, milestone_icons[icon_idx % len(milestone_icons)],
                    ha='center', va='center', fontsize=20)
            icon_idx += 1
            
            # 连接线到时间轴
            ax.plot([x_pos, x_pos], [y_pos - 0.35, 3.5], 
                   '--', color=phase['color'], linewidth=1.5, alpha=0.5)
            
            # 里程碑文字
            ax.text(x_pos, y_pos + 0.7, milestone['time'],
                    ha='center', va='center', fontsize=9, fontweight='bold',
                    fontproperties=chinese_font, color=phase['color'])
            ax.text(x_pos, y_pos + 0.4, milestone['event'],
                    ha='center', va='center', fontsize=9,
                    fontproperties=chinese_font, color='#34495e')
    
    # 添加标题
    ax.text(7.75, 7.8, '五年规划关键里程碑路线图', 
            ha='center', va='center', fontsize=18, fontweight='bold',
            fontproperties=chinese_font, color='#2c3e50')
    
    # 添加图例
    legend_elements = [
        mpatches.Patch(facecolor='#3498db', alpha=0.3, label='初创期 (2027-2028)'),
        mpatches.Patch(facecolor='#2ecc71', alpha=0.3, label='成长验证期 (2029-2030)'),
        mpatches.Patch(facecolor='#9b59b6', alpha=0.3, label='规模复制期 (2031+)')
    ]
    ax.legend(handles=legend_elements, loc='upper right', 
             prop={'family': chinese_font.get_name(), 'size': 10},
             framealpha=0.9)
    
    # 设置坐标轴
    ax.set_xlim(0, 15.5)
    ax.set_ylim(0, 8.5)
    ax.axis('off')
    
    plt.tight_layout()
    plt.savefig(os.path.join(output_dir, 'milestone_roadmap.png'), 
                dpi=300, bbox_inches='tight', facecolor='white')
    plt.close()
    print("✓ 图4已生成：milestone_roadmap.png")


def draw_investment_return():
    """
    图5：投资回报逻辑阶梯图
    放置位置：Page 37-38（八、投资回报分析）
    """
    fig, ax = plt.subplots(figsize=(14, 10))
    
    # 定义阶梯数据
    steps = [
        {
            "level": 1,
            "title": "起点：投资投入",
            "content": "投资人投入300万元\n获12%股权\n投后估值2500万",
            "x": 2,
            "y": 1.5,
            "width": 3,
            "height": 1.5,
            "color": "#e74c3c"
        },
        {
            "level": 2,
            "title": "过程：业务增长",
            "content": "资金驱动：样机→试点→复制\n业务数据持续增长\n市场份额扩大",
            "x": 5.5,
            "y": 3.5,
            "width": 3.5,
            "height": 1.8,
            "color": "#f39c12"
        },
        {
            "level": 3,
            "title": "终点：估值提升",
            "content": "2031年净利润1376万\n× 15-20倍PE\n= 估值2.1-2.8亿",
            "x": 9.5,
            "y": 5.5,
            "width": 3.5,
            "height": 1.8,
            "color": "#2ecc71"
        },
        {
            "level": 4,
            "title": "结果：投资退出",
            "content": "投资人12%股权价值\n2500-3300万\n8-11倍增值退出",
            "x": 10,
            "y": 7.8,
            "width": 3,
            "height": 1.5,
            "color": "#9b59b6"
        }
    ]
    
    # 绘制阶梯
    for step in steps:
        # 绘制矩形块
        rect = FancyBboxPatch(
            (step['x'], step['y']), step['width'], step['height'],
            boxstyle="round,pad=0.15",
            facecolor=step['color'], alpha=0.2,
            edgecolor=step['color'], linewidth=3
        )
        ax.add_patch(rect)
        
        # 添加标题
        ax.text(step['x'] + step['width']/2, step['y'] + step['height'] - 0.3,
                step['title'],
                ha='center', va='center', fontsize=12, fontweight='bold',
                fontproperties=chinese_font, color=step['color'])
        
        # 添加内容
        ax.text(step['x'] + step['width']/2, step['y'] + step['height']/2,
                step['content'],
                ha='center', va='center', fontsize=9.5,
                fontproperties=chinese_font, color='#2c3e50',
                linespacing=1.6)
        
        # 添加级别标识
        level_circle = Circle((step['x'] + 0.3, step['y'] + step['height'] - 0.3), 
                             0.2, color=step['color'], zorder=3)
        ax.add_patch(level_circle)
        ax.text(step['x'] + 0.3, step['y'] + step['height'] - 0.3,
                str(step['level']),
                ha='center', va='center', fontsize=10, fontweight='bold',
                color='white')
    
    # 绘制连接箭头
    arrows = [
        ((5, 2.5), (5.5, 3.5)),   # 步骤1 → 步骤2
        ((9, 4.8), (9.5, 5.5)),   # 步骤2 → 步骤3
        ((11.5, 7), (10, 7.8))    # 步骤3 → 步骤4
    ]
    
    for start, end in arrows:
        arrow = FancyArrowPatch(
            start, end,
            arrowstyle='->', mutation_scale=40, linewidth=3,
            color='#34495e', alpha=0.6, zorder=2
        )
        ax.add_patch(arrow)
    
    # 添加关键数据高亮框
    highlight_box = FancyBboxPatch(
        (0.5, 0.2), 13, 0.8,
        boxstyle="round,pad=0.1",
        facecolor='#fff3cd', alpha=0.8,
        edgecolor='#ffc107', linewidth=2
    )
    ax.add_patch(highlight_box)
    
    ax.text(7, 0.6, '核心投资逻辑：300万投入 → 2500-3300万退出 → 8-11倍回报',
            ha='center', va='center', fontsize=13, fontweight='bold',
            fontproperties=chinese_font, color='#856404')
    
    # 添加标题
    ax.text(7, 9.5, '投资回报逻辑示意图', 
            ha='center', va='center', fontsize=18, fontweight='bold',
            fontproperties=chinese_font, color='#2c3e50')
    
    # 添加装饰性元素 - ROI倍数
    roi_text = "ROI\n8-11×"
    ax.text(13.5, 8.5, roi_text,
            ha='center', va='center', fontsize=16, fontweight='bold',
            fontproperties=chinese_font, color='#e74c3c',
            bbox=dict(boxstyle='circle,pad=0.5', facecolor='#fadbd8', 
                     edgecolor='#e74c3c', linewidth=3))
    
    # 设置坐标轴
    ax.set_xlim(0, 14.5)
    ax.set_ylim(0, 10.5)
    ax.axis('off')
    
    plt.tight_layout()
    plt.savefig(os.path.join(output_dir, 'investment_return.png'), 
                dpi=300, bbox_inches='tight', facecolor='white')
    plt.close()
    print("✓ 图5已生成：investment_return.png")


if __name__ == "__main__":
    print("=" * 60)
    print("开始绘制瞳伴商业计划书示意图...")
    print("=" * 60)
    
    try:
        draw_user_journey()
        draw_static_to_dynamic()
        draw_safety_mechanism()
        draw_milestone_roadmap()
        draw_investment_return()
        
        print("\n" + "=" * 60)
        print("所有图片绘制完成！")
        print(f"输出目录：{output_dir}")
        print("=" * 60)
        
    except Exception as e:
        print(f"\n❌ 绘制过程中出现错误：{str(e)}")
        import traceback
        traceback.print_exc()
