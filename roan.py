import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from scipy.stats import ttest_ind
from itertools import combinations

def load_and_validate_data(filepath, required_columns):
    """
    Loads data from a CSV file and validates if required columns are present.
    """
    data = pd.read_csv(filepath)
    if not all(col in data.columns for col in required_columns):
        raise ValueError("Missing required columns")
    return data

def preprocess_data(data):
    """
    Splits 'Hpf' into 'Hpf_start' and 'Hpf_end' and handles NaN values.
    """
    data[['Hpf_start', 'Hpf_end']] = data['Hpf'].str.split('-', expand=True).apply(pd.to_numeric, errors='coerce')
    return data.dropna(subset=['Hpf_start', 'Hpf_end', 'Value'])

def calculate_statistics(grouped_data):
    """
    Calculates mean and standard deviation for each group.
    """
    stats = grouped_data['Value'].agg(['mean', 'std'])
    print(stats)

def create_boxplot(data):
    """
    Creates a boxplot of the data.
    """
    plt.figure(figsize=(12, 8))
    sns.boxplot(x='Type', y='Value', hue='Hpf', data=data, linewidth=2.5)
    plt.title('Nerve Density in Zebrafish Pancreatic Islets', fontsize=16)
    plt.xlabel('Treatment Type', fontsize=14)
    plt.ylabel('Nerve Density', fontsize=14)
    plt.legend(title='Hour Post-Fertilization (Hpf)', fontsize=12)
    plt.savefig('boxplot.png', dpi=300, bbox_inches='tight')
    plt.show()

def perform_t_tests(grouped_data):
    """
    Performs t-tests between all combinations of groups within the same type.
    """
    group_pairs = [(g1, g2) for g1, g2 in combinations(grouped_data.groups.keys(), 2) if g1[0] == g2[0]]
    t_test_results = [{
        'Group1': group1, 
        'Group2': group2, 
        'T-Statistic': ttest_ind(grouped_data.get_group(group1)['Value'], 
                                 grouped_data.get_group(group2)['Value'], 
                                 equal_var=False).statistic,
        'P-Value': ttest_ind(grouped_data.get_group(group1)['Value'], 
                             grouped_data.get_group(group2)['Value'], 
                             equal_var=False).pvalue
    } for group1, group2 in group_pairs]
    return pd.DataFrame(t_test_results)

def plot_t_test_results(t_test_results_df):
    """
    Plots T-Statistics and P-Values from the t-test results.
    """
    plt.figure(figsize=(14, 8))
    group_comparison = t_test_results_df['Group1'].astype(str) + ' vs ' + t_test_results_df['Group2'].astype(str)
    plt.scatter(group_comparison, t_test_results_df['T-Statistic'], color='skyblue', label='T-Statistic')
    for i, txt in enumerate(t_test_results_df['P-Value']):
        plt.annotate(f"{txt:.2e}", (group_comparison[i], t_test_results_df['T-Statistic'][i]), textcoords="offset points", xytext=(0,10), ha='center')
    plt.xlabel('Group Comparisons', fontsize=14)
    plt.ylabel('T-Statistic / P-Value', fontsize=14)
    plt.title('T-Statistics and P-Values for Zebrafish Transgenic Model Comparisons', fontsize=16)
    plt.xticks(rotation=45)
    plt.legend()
    plt.tight_layout()
    plt.savefig('t_test_results.png', dpi=300, bbox_inches='tight')
    plt.show()

# Main execution
REQUIRED_COLUMNS = ['Type', 'Hpf', 'Value']
data = load_and_validate_data('data.csv', REQUIRED_COLUMNS)
preprocessed_data = preprocess_data(data)
grouped_data = preprocessed_data.groupby(['Type', 'Hpf'])

calculate_statistics(grouped_data)
create_boxplot(preprocessed_data)
t_test_results_df = perform_t_tests(grouped_data)
plot_t_test_results(t_test_results_df)