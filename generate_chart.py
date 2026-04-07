import matplotlib.pyplot as plt
import os

# 數據規模 (n)
n_values = [100, 500, 1000, 2000, 5000]

# 實驗數據 (秒) - 根據 README.md 中的真實數據
data = {
    'Bubble Sort': [0.0005, 0.0132, 0.0541, 0.2150, 1.3520],
    'Selection Sort': [0.0003, 0.0085, 0.0342, 0.1380, 0.8750],
    'Insertion Sort': [0.0002, 0.0048, 0.0195, 0.0780, 0.4950],
    'Merge Sort': [0.0001, 0.0007, 0.0016, 0.0035, 0.0092],
    'Quick Sort': [0.0001, 0.0005, 0.0011, 0.0023, 0.0061]
}

plt.figure(figsize=(10, 6))

markers = ['o', 's', '^', 'x', 'd']
for (label, times), marker in zip(data.items(), markers):
    plt.plot(n_values, times, label=label, marker=marker, linewidth=2)

plt.title('Sorting Algorithms Performance: Time vs. Data Size', fontsize=14, fontweight='bold')
plt.xlabel('Data Size (n)', fontsize=12)
plt.ylabel('Execution Time (seconds)', fontsize=12)
plt.yscale('log')  # 使用對數尺度，因為 O(n^2) 和 O(n log n) 差距極大
plt.grid(True, which="both", ls="--", alpha=0.7)
plt.legend()

plt.tight_layout()
output_file = os.path.join(os.path.dirname(__file__), 'sort_comparison.png')
plt.savefig(output_file, dpi=300)
print(f"圖表已成功生成並儲存為: {output_file}")