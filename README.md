# Biomass Composition Visualization

This repository contains Python code for visualizing the composition of biomass samples using pie charts. The code reads data from a CSV file, extracts relevant columns representing the elemental composition of the biomass, and generates pie charts for each sample.

## Requirements

- Python 3.x
- Pandas library
- Matplotlib library

Install the required libraries using pip:

```
pip install pandas matplotlib
```

## Usage

1. Ensure that your biomass data is in a CSV file format with columns for sample names, carbon, hydrogen, oxygen, nitrogen, sulfur, and higher heating value (HHV).

2. Update the `biomass.csv` file with your data or replace it with your own CSV file.

3. Run the `biomass_visualization.py` script:

   ```
   python biomass_visualization.py
   ```

   The script will generate pie charts for each sample and save them as individual PNG files in a newly created `figures_<current_datetime>` directory.

4. Explore the generated pie charts to gain insights into the elemental composition of your biomass samples.

## Customization

- If you want to customize the colors of the pie charts, modify the `colors` list in the code.
- Adjust the figure size, font sizes, and other visual properties as desired in the code.

## Acknowledgments

- The code was developed as a part of the Biomass Analysis self project.
- Special thanks to (https://github.com/vincentarelbundock?tab=repositories) for providing the biomass dataset used in this project.
- Credits to the developers and contributors of the Pandas and Matplotlib libraries for their invaluable tools.

## License

This project is licensed under the [MIT License](LICENSE).
