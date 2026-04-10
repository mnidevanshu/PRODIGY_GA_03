# Task 3 : Text Generation with Markov Chains

This repository contains the implementation of a statistical text generation tool using Markov Chains.

## 🚀 Project Overview
The application leverages Markov Chains to predict the probability of a word based on the previous one. By processing training text, it builds a transition map to generate original sentences that mimic the input style. It features a custom Graphical User Interface (GUI) for seamless interaction.

## Key Features
* **Statistical Modeling:** Implements a first-order Markov Chain to map word transitions.
* **Interactive GUI:** A user-friendly interface built with Tkinter for entering training text and viewing results.
* **Customization:** Users can define a specific start word and the desired length of generated text.
* **Dynamic Generation:** Uses weighted randomness to ensure varied results each time.

## 🛠️ Technical Stack
* **Language:** Python 3.x.
* **Algorithm:** Markov Chain (Stochastic Model).
* **GUI Framework:** Tkinter.

## ⚙️ Installation & Usage
1. **Clone the repository:**
   ```bash
   https://github.com/mnidevanshu/PRODIGY_GA_03.git

2. **Run the application:**
   ```bash
   main.py

 ```
## 📝 Future Scope
Enhancing the model to use higher-order Markov Chains (predicting based on the previous 2 or 3 words) to improve grammatical coherence.
