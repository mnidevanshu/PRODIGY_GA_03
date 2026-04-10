```markdown
# Task 03: Text Generation with Markov Chains

This project implements a statistical text generation algorithm using Markov Chains as part of my internship curriculum.

## 🚀 Project Overview
The objective of this task is to create a statistical model that predicts the probability of a word based on the previous one. By processing "training" text, the algorithm builds a transition map to generate original sentences that mimic the style of the input data.

### Key Features
* **Statistical Modeling**: Implements a first-order Markov Chain to map word transitions.
* **Interactive GUI**: A Tkinter-based interface for entering training text and generation parameters.
* **Customization**: Users can define the "Start Word" and the desired length of the generated output.
* **Dynamic Generation**: Uses weighted randomness to ensure varied results each time.

## 🛠️ Technical Stack
* **Language**: Python 3.x
* **Algorithm**: Markov Chain (Stochastic Model)
* **GUI Framework**: Tkinter

## ⚙️ Installation & Usage

1. **Clone the repository**:
   ```bash
   https://github.com/mnidevanshu/PRODIGY_GA_03.git

```
 2. **Run the application**:
   ```bash
   python main.py
   
   ```
## 📝 Future Scope
Enhancing the model to use higher-order Markov Chains (predicting based on the previous 2 or 3 words) to improve grammatical coherence.
```
