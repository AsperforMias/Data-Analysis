import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import io

#中文字体设置
try:
    plt.rcParams['font.sans-serif'] = ['SimHei']
    plt.rcParams['axes.unicode_minus'] = False
except Exception as e:
    print(f"无法设置SimHei字体{e}.中文可能无法正确显示。")
    print("请确保系统中安装了SimHei字体，或者替换为其他可用中文字体，如 'Microsoft YaHei'.")

# 设定常数数据 
# 沸点 / °C
T_boiling = np.array([78.4, 69.5, 66.1, 66.4, 65.3, 65.5, 65.6, 90.9])
# 液相浓度
x_liquid_conc = np.array([0, 0.0535, 0.2526, 0.1897, 0.5409, 0.6247, 0.6719, 1])
# 气相浓度
y_vapor_conc = np.array([0, 0.3994, 0.5094, 0.4990, 0.5356, 0.5199, 0.4361, 1])

# 液相数据
liquid_data = {
    'x_conc': x_liquid_conc,
    'T_boiling': T_boiling
}
# 按液相浓度排序
df_liq = pd.DataFrame(liquid_data).sort_values(by='x_conc').reset_index(drop=True)

# 气相数据
vapor_data = {
    'y_conc': y_vapor_conc,
     'T_boiling': T_boiling # 气相点和液相点在相同温度下平衡
}
# 按气相浓度排序
df_vap = pd.DataFrame(vapor_data).sort_values(by='y_conc').reset_index(drop=True)

#查找最低共沸点 (基于原始实验温度数据的最低点) 
min_temp_index_in_orig = np.argmin(T_boiling) # 找到原始数据中最低温度的索引
azeo_T = T_boiling[min_temp_index_in_orig]
# 获取该最低温度对应的液相和气相浓度
azeo_x_conc = x_liquid_conc[min_temp_index_in_orig]
azeo_y_conc = y_vapor_conc[min_temp_index_in_orig]

print("\n--- 用于绘图的数据 ---")
print("液相数据 (排序后):")
print(df_liq)
print("\n气相数据 (排序后):")
print(df_vap)
print(f"\n最低沸点信息: T={azeo_T}°C, 液相浓度≈{azeo_x_conc:.4f}, 气相浓度≈{azeo_y_conc:.4f}")

plt.figure(figsize=(8, 6)) # 设置图形大小

# 使用插值使曲线更平滑
# 创建更密集的 x/y 值用于绘制平滑曲线
# 处理 df_vap 中 y_conc 可能存在的非单调或重复值 (基于排序后的数据)
df_vap_unique = df_vap.drop_duplicates(subset=['y_conc'], keep='first') # 保留唯一的 y_conc 用于插值

x_smooth_liq = np.linspace(df_liq['x_conc'].min(), df_liq['x_conc'].max(), 300)
y_smooth_vap = np.linspace(df_vap_unique['y_conc'].min(), df_vap_unique['y_conc'].max(), 300) # 用 unique y

# 插值计算对应的 T 值
T_smooth_liq = np.interp(x_smooth_liq, df_liq['x_conc'], df_liq['T_boiling'])
T_smooth_vap = np.interp(y_smooth_vap, df_vap_unique['y_conc'], df_vap_unique['T_boiling']) # 用 unique y/T

# 绘制曲线和数据点
# 绘制插值后的平滑曲线
plt.plot(x_smooth_liq, T_smooth_liq, marker='', linestyle='-', color='blue', label='液相线 (泡点线, T vs 液相浓度)')
plt.plot(y_smooth_vap, T_smooth_vap, marker='', linestyle='-', color='red', label='气相线 (露点线, T vs 气相浓度)')

# 绘制原始数据点
plt.plot(x_liquid_conc, T_boiling, 'bo', label='液相数据点 (T vs 液相浓度)') # 蓝色圆点
plt.plot(y_vapor_conc, T_boiling, 'ro', label='气相数据点 (T vs 气相浓度)') # 红色圆点

# 标记共沸点 (基于最低温度点及其对应的浓度)
plt.plot(azeo_x_conc, azeo_T, 'k*', markersize=10, label=f'最低沸点 (~{azeo_T}°C, x_c≈{azeo_x_conc:.2f}, y_c≈{azeo_y_conc:.2f})')

# 添加标签、标题和图例
plt.xlabel('环己烷浓度 (x_conc, y_conc)') # X轴标签更改为浓度
plt.ylabel('温度 (°C)') # Y轴标签
plt.title('环己烷-乙醇 气液平衡相图 (T vs 浓度)') # 标题更改为浓度
plt.legend() # 显示图例
plt.grid(True, linestyle='--', alpha=0.6) # 添加网格线
plt.xlim(0, 1) # 设置X轴范围
plt.ylim(60, 100) # 设置Y轴范围

# 添加区域文字标注
plt.text(0.1, 90, '气相区 (V)', ha='center') 
plt.text(0.8, 75, '气液共存区 (L+V)', ha='center')
plt.text(0.1, 63, '液相区 (L)', ha='center')
plt.text(0.5, 58, '注意: 基于图片提供的浓度数据绘制', ha='center', fontsize=7, color='gray') # 修改说明

# 显示或保存图形（2选1）
#plt.show()
plt.savefig('T&L&V-DataAnalyze-v3.png') # dpi是否设置看情况
plt.close()