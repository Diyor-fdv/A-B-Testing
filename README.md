# A-B-Testing
This project demonstrates a simple A/B test experiment using Python (Pandas, NumPy, Matplotlib, and SciPy). The goal is to compare two different UI versions of a website to determine which one leads to a higher Click-Through Rate (CTR).

Data Generation: Simulated data for two groups:

Group A: Original website version

Group B: New design version (e.g., button color or text change)

Statistical Testing:

Independent samples t-test to determine if the difference in CTR is statistically significant.

Visualization:

A clean bar chart comparing CTR for both groups using matplotlib.

UI Mockups:

Demo image showing the visual difference between version A and B to support the context of the experiment.

📊 Key Metrics
CTR (Click Through Rate): The ratio of users who clicked to total users.

T-statistic & P-value: Used to evaluate if the new design (Group B) performs significantly better than the original (Group A).

🔧 Technologies Used
Python (Pandas, NumPy)

Matplotlib

SciPy (for ttest_ind)

Power BI (optional visualization)

CSV File (for external dashboard tools)

📂 Files
ab_test_data.csv – Simulated A/B testing dataset

ab_test_plot.png – Visualization of CTR comparison

A_comparison_digital_image.png – UI mockup for Group A and B

ab_test_analysis.ipynb – Code notebook with all logic and plots

✅ Result
According to the simulated test:

Group B had a higher CTR (e.g., 14%) than Group A (e.g., 12%)

The difference was statistically significant with a low p-value, supporting that UI/UX change had a positive effect.

📌 Conclusion
This A/B test helps demonstrate how small UI changes can influence user behavior and how statistical testing can validate design decisions with confidence.
