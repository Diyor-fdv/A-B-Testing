import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


np.random.seed(42)


n_users = 5000

# A guruhi (
group_a = pd.DataFrame({
    'user_id': range(1, n_users + 1),
    'group': 'A',
    'clicked': np.random.binomial(1, 0.12, n_users)
})

# B guruhi new
group_b = pd.DataFrame({
    'user_id': range(n_users + 1, 2 * n_users + 1),
    'group': 'B',
    'clicked': np.random.binomial(1, 0.14, n_users)
})


df = pd.concat([group_a, group_b], ignore_index=True)


ctr = df.groupby('group')['clicked'].mean() * 100

print("CTR (Click Through Rate):")
print(ctr)

from scipy.stats import ttest_ind


a_clicks = df[df['group'] == 'A']['clicked']
b_clicks = df[df['group'] == 'B']['clicked']


t_stat, p_value = ttest_ind(a_clicks, b_clicks)

print(f"T-statistic: {t_stat}")
print(f"P-value: {p_value}")


# Vizualizatsiya
ctr.plot(kind='bar', color=['skyblue', 'lightgreen'])
plt.title('CTR Comparison: Group A vs Group B')
plt.ylabel('Click Through Rate (%)')
plt.xlabel('Group')
plt.xticks(rotation=0)
plt.ylim(0, max(ctr) + 5)
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.show()
