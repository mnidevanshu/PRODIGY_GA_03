```markdown
# Task 03: Text Generation with Markov Chains

This project implements a statistical text generation algorithm using Markov Chains as part of my internship curriculum.

## 🚀 Project Overview
The goal of this task is to create a statistical model that predicts the probability of a word based on the previous one. By processing a body of "training" text, the algorithm builds a state-transition map to generate new, original sentences that mimic the style of the input data.

### Key Features
* **Statistical Modeling**: Implements a first-order Markov Chain to map word transitions.
* **Interactive GUI**: A Tkinter-based interface allowing users to input training text and define generation parameters.
* **Customization**: Users can specify the "Start Word" and the desired length of the generated output.
* **Dynamic Generation**: Uses weighted randomness to select subsequent words, ensuring varied results each time.

## 🛠️ Technical Stack
* **Language**: Python 3.x
* **Libraries**: Random (Standard Library), Tkinter (Standard Library)
* **Algorithm**: Markov Chain (Stochastic Model)

## ⚙️ Installation & Usage

1. **Clone the repository**:
   ```bash
   https://github.com/mnidevanshu/PRODIGY_GA_03.git

```
 2. **Run the application**:
   ```bash
   python main.py
   
   ```
## 📂 How It Works
 1. **Building the Model**: The script splits the training text into individual tokens and creates a dictionary where each word points to a list of words that follow it in the text.
 2. **Generating Text**: Starting with a user-defined word, the algorithm randomly picks the next word from the observed transitions and repeats this process until the requested word count is reached.
## 📝 Future Scope
Enhancing the model to use higher-order Markov Chains (predicting based on the previous 2 or 3 words) to improve the grammatical coherence of the generated text.
```
