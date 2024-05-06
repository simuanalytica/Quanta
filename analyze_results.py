import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy import stats
from openpyxl import load_workbook

def analyze_results(self):
    # Read the Excel file
    file_path = self.entry_result_file.get()
    sheet_name_result = 'Result'
    sheet_name_output = 'Output'
    # Load the workbook
    workbook = load_workbook(filename=file_path, read_only=True)

    # Get the output sheet
    output_sheet = workbook[sheet_name_output]

    # Get the target values and confidence levels
    target_value_1 = output_sheet['F4'].value
    target_value_2 = output_sheet['F5'].value
    confidence_level_chart1 = output_sheet['G4'].value
    confidence_level_chart2 = output_sheet['G5'].value
    boundary_limit_chart1 = output_sheet['H4'].value
    boundary_limit_chart2 = output_sheet['H5'].value
    Output_paramter_1 = output_sheet['D4'].value
    Output_paramter_2 = output_sheet['D4'].value
    # Close the workbook
    workbook.close()

    # Read data from the Result sheet
    df_result = pd.read_excel(file_path, sheet_name=sheet_name_result, skiprows=[0])

    # Calculate confidence intervals for each column
    # Calculate confidence intervals for chart 1
    mean_chart1 = df_result.iloc[:, 0].mean()
    std_dev_chart1 = df_result.iloc[:, 0].std()
    n_chart1 = len(df_result.iloc[:, 0])
    z_score_chart1 = stats.norm.ppf((1 + confidence_level_chart1) / 2)
    margin_of_error_chart1 = z_score_chart1 * (std_dev_chart1 / np.sqrt(n_chart1))
    confidence_interval_chart1 = (mean_chart1 - margin_of_error_chart1, mean_chart1 + margin_of_error_chart1)

    # Calculate confidence intervals for chart 2
    mean_chart2 = df_result.iloc[:, 1].mean()
    std_dev_chart2 = df_result.iloc[:, 1].std()
    n_chart2 = len(df_result.iloc[:, 1])
    z_score_chart2 = stats.norm.ppf((1 + confidence_level_chart2) / 2)
    margin_of_error_chart2 = z_score_chart2 * (std_dev_chart2 / np.sqrt(n_chart2))
    confidence_interval_chart2 = (mean_chart2 - margin_of_error_chart2, mean_chart2 + margin_of_error_chart2)

    # Calculate the probability of a value being greater than the target value for each column
    prob_greater_than_target_1 = 1 - stats.norm.cdf(target_value_1, mean_chart1, std_dev_chart1)
    prob_greater_than_target_2 = 1 - stats.norm.cdf(target_value_2, mean_chart2, std_dev_chart2)

    # Create subplots
    fig, axs = plt.subplots(1, 2, figsize=(14, 6))

    # Plot histogram for the first column (chart 1)
    axs[0].hist(df_result.iloc[:, 0], bins=20, color='skyblue', edgecolor='black', alpha=0.7, label='Histogram')
    axs[0].axvspan(confidence_interval_chart1[0], confidence_interval_chart1[1], color='orange', alpha=0.3)
    axs[0].set_xlabel('Values')
    axs[0].set_ylabel('Frequency')
    # axs[0].set_title('Histogram of Column 1 with 90% CI')

    # Plot probability boundary for 90% (chart 1)
    z_score_chart1 = stats.norm.ppf(confidence_level_chart1)
    axs[0].axvline(x=mean_chart1 + z_score_chart1 * std_dev_chart1, color='red', linestyle='--')
    axs[0].axvline(x=mean_chart1 - z_score_chart1 * std_dev_chart1, color='red', linestyle='--')

    # Plot histogram for the second column (chart 2)
    axs[1].hist(df_result.iloc[:, 1], bins=20, color='skyblue', edgecolor='black', alpha=0.7, label='Histogram')
    axs[1].axvspan(confidence_interval_chart2[0], confidence_interval_chart2[1], color='orange', alpha=0.3)
    axs[1].set_xlabel('Values')
    axs[1].set_ylabel('Frequency')
    # axs[1].set_title('Histogram of Column 2 with 80% CI')

    # Plot probability boundary for 80% (chart 2)
    z_score_chart2 = stats.norm.ppf(confidence_level_chart2)
    axs[1].axvline(x=mean_chart2 + z_score_chart2 * std_dev_chart2, color='red', linestyle='--')
    axs[1].axvline(x=mean_chart2 - z_score_chart2 * std_dev_chart2, color='red', linestyle='--')

    # Display text info above the subplots
    text_lines_chart1 = '\n'.join([
        f'Output: {Output_paramter_1}',
        f'Prob({Output_paramter_1} > {target_value_1}) = {prob_greater_than_target_1 * 100:.2f}%',
        f'Confidence Level: {confidence_level_chart1 * 100:.2f}%',
        f'Confidence Boundary: {confidence_interval_chart1[0]:.2f} - {confidence_interval_chart1[1]:.2f}',
        f'Probability: {boundary_limit_chart1:.2f}',
        f'Probability Interval Bounds: {mean_chart1 - z_score_chart1 * std_dev_chart1:.2f} - {mean_chart1 + z_score_chart1 * std_dev_chart1:.2f}'
    ])
    axs[0].text(0.5, 1.05, text_lines_chart1, transform=axs[0].transAxes, horizontalalignment='center')

    text_lines_chart2 = '\n'.join([
        f'Output: {Output_paramter_2}',
        f'Prob( {Output_paramter_2} > {target_value_2}) = {prob_greater_than_target_2 * 100:.2f}%',
        f'Confidence Level: {confidence_level_chart2 * 100:.2f}%',
        f'Confidence Boundary: {confidence_interval_chart2[0]:.2f} - {confidence_interval_chart2[1]:.2f}',
        f'Probability: {boundary_limit_chart2:.2f}',
        f'Probability Interval Bounds: {mean_chart2 - z_score_chart2 * std_dev_chart2:.2f} - {mean_chart2 + z_score_chart2 * std_dev_chart2:.2f}'
    ])
    axs[1].text(0.5, 1.05, text_lines_chart2, transform=axs[1].transAxes, horizontalalignment='center')

    # Show plot
    plt.tight_layout()
    plt.show()
