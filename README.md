# Quanta: Agile Project Goal Certainty Prediction Framework

Quanta is a structured framework designed to assist in predicting the certainty of meeting project goals in areas such as productivity or defect density. It serves as an open-source alternative to tools like Crystal Ball. The framework utilizes Monte Carlo methods to assess the likelihood of achieving project objectives.

## Framework Sections

### 1. Distribution Generation

This section generates probability distributions for various project phases based on historical data. Each phase's distribution parameters are stored in a JSON log.

### 2. Model Creation

Using the JSON log generated in the Distribution Generation section, this step creates a model for Monte Carlo simulation. Users specify the number of iterations for the simulation.

### 3. Run Simulation

The generated model is utilized to run Monte Carlo simulations. The simulation data for each iteration is made available in the Samples tab of an Excel file.

### 4. Analysis

In this section, users analyze the simulation results to assess the certainty of meeting project goals. By specifying target values and certainty levels, confidence charts are generated to visualize the likelihood of meeting the estimated efforts. Additionally, a sensitivity chart demonstrates how different project phases impact overall output certainty.

## Usage Example: Predicting Sprint Efforts in Agile Projects

1. **Historical Data Collection**: Gather historical data on effort per complexity point for each phase in an Agile project.
   
2. **Distribution Generation**: Input the historical data into Quanta to generate probability distributions for each project phase. Save the distribution parameters in a JSON log.
   
3. **Model Creation**: Specify the number of iterations and use the JSON log to create a model file for Monte Carlo simulation.
   
4. **Run Simulation**: Execute the simulation using the generated model file. Simulation data will be available in the Samples tab of the Excel file.
   
5. **Analysis**: Utilize the Analysis section to generate confidence charts based on specified target values and certainty levels. Evaluate sensitivity to understand how different phases impact overall goal certainty.

## Getting Started

To get started with Quanta, follow these steps:

1. Clone the Quanta repository.
2. Install any necessary dependencies.
3. Prepare historical data for input into the Distribution Generation section.
4. Follow the framework sections sequentially for prediction and analysis.
5. Refer to generated output files for results and insights.

## Contributing

Contributions to Quanta are welcome! If you have suggestions for improvements, open an issue or submit a pull request.

## License

Quanta is licensed under the [MIT License](LICENSE).
