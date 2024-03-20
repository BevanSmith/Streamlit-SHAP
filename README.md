# Shap Values Calculator

This Python application is a Streamlit app designed to calculate SHAP (SHapley Additive exPlanations) values for educational and occupational data entered by the user. SHAP values provide insights into the contribution of different features to a model's output.

## How to Use

1. **Installation**: Ensure you have Python installed on your system. Clone this repository to your local machine.

2. **Setup**: Install the required dependencies by running the following command:

pip install -r requirements.txt


3. **Running the App**: Start the Streamlit app by executing the following command in your terminal:

streamlit run app3.py


4. **Usage**: Once the app is running, navigate to the provided URL in your web browser. You will see dropdown menus where you can select your education level and occupation. After making your selections, the SHAP values will be calculated and displayed as plots on the web app.

## Features

- **Interactive Interface**: Users can easily input their education and occupation through dropdown menus.
- **SHAP Value Calculation**: The app utilizes the SHAP library to calculate SHAP values for the selected input.
- **Visualization**: SHAP values are visualized as plots, providing insights into feature contributions.

## Example


![Shap_screenshot](https://github.com/BevanSmith/Streamlit-SHAP/assets/40493099/d0e81958-b4f4-48a5-be7b-a5caf24eaf3b)


## Dependencies

- Python 3.x
- Streamlit
- SHAP

## Contributing

Contributions are welcome! If you have any suggestions, bug reports, or feature requests, please open an issue or submit a pull request following the guidelines in the [CONTRIBUTING.md](CONTRIBUTING.md) file.

## License

This project is licensed under the [MIT License](LICENSE.txt).

