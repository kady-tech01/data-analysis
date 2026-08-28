
# Paste this script inside Power BI Python Visual Editor:
import matplotlib.pyplot as plt
import seaborn as sns

# dataset dataframe is automatically provided by Power BI
plt.figure(figsize=(8,4))
sns.lineplot(data=dataset, x='transaction_date', y='amount', hue='transaction_type', marker='o')
plt.title('AI-Enhanced Cash Flow & Revenue Projection')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()
