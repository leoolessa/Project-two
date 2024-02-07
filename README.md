ReadMe:

# Marvel Comics Data Analysis

This project performs data analysis on Marvel Comics with over 121 characters, focusing on Avengers and X-Men heroes and villains. It uses the Marvel API to retrieve information about various characters and their comic book appearances. The analysis includes visualizations and insights into the distribution of comics among different character groups.

## Overview

Marvel Comics has a vast universe of characters, including both heroes and villains. This project aims to analyze the distribution of comics among Avengers and X-Men characters, as well as their respective villains. It utilizes the Marvel API to collect data about these characters and their comic book appearances.

## Dependencies

To run this project, you need to have the following dependencies installed:

- pandas (To create the DataFrame and manage the data after extraction)
- matplotlib (To create the graphics to better visualizing and meet the hipnesses of the project)
- seaborn (Works together with Matplotlib)
- os (Module is a standard library module that provides a way to interact with the operating system)
- time (Module is a standard library module that provides various time-related functions)
- marvel (A custom module for interacting with the Marvel API )
- keys (A file containing your Marvel API public and private keys)

## Installation

To install the required dependencies, you can use pip:

```bash
pip install pandas, matplotlib, seaborn and marvel
```

You also need to set up the `marvel` and `keys` modules. Ensure that you have obtained your Marvel API public and private keys and stored them in the `keys.py` module.

## Usage

1. Ensure that you have set up your Marvel API keys in the `keys.py` module.
2. Run the provided Python script containing the code.
3. The script fetches data about Marvel Comics characters using the Marvel API.
4. It then performs analysis and generates visualizations to understand the distribution of comics among different character groups.
5. The script outputs insights about the top characters with the most comic book appearances and their affiliations.

## Features

- Retrieves data about Marvel Comics characters from the Marvel API.
- Analyzes the distribution of comics among Avengers and X-Men heroes and villains.
- Generates visualizations to represent the data, including bar charts showing the top characters with the most comic book appearances.
- Calculates the percentage of comics featuring Avengers and X-Men characters.

## Conclusion

This project provides valuable insights into the comic book appearances of Marvel Comics characters, particularly focusing on the Avengers and X-Men teams. By analyzing comic distribution, fans and enthusiasts can gain a better understanding of the prominence of different characters within the Marvel Comics universe.