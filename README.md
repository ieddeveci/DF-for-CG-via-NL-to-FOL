# A Diagnostic Framework for Compositional Generalization via NL-to-FOL Translation

This repository contains the resources supporting the evaluation framework for neural semantic parsing from Natural Language to First-Order Logic (NL-to-FOL), to be presented at the **Student Session of the 36th European Summer School in Logic, Language and Information (ESSLLI 2025)**.

[Link for the preproceedings](https://2025.esslli.eu/courses-workshops-accepted/student-session-call.html).

## Contents

- **Datasets:** `WillowNLtoFOL` and `WillowNLtoFOL_extended` datasets designed to test compositional generalization in semantic parsing. The structured datasets are also available on **[Hugging Face](https://huggingface.co/datasets/iedeveci/WillowNLtoFOL)**.  
- **Code:** Training scripts and evaluation tools implementing the metrics proposed in the article, enabling reproducible experiments

## Purpose

This project provides a systematic and automated evaluation framework for assessing compositional generalization capabilities of neural semantic parsing models. It includes datasets with controlled logical complexity and comprehensive metrics to analyze both structural correctness and semantic equivalence of model outputs.

## License

- **Article and textual content:** Licensed under [Creative Commons Attribution 4.0 International (CC BY 4.0)](https://creativecommons.org/licenses/by/4.0/).

## Citation

Plain Text: Deveci, İ. E. (2024). Transformer models for translating natural language sentences into formal logical expressions [M.S. - Master of Science]. Middle East Technical University.
Available at: https://open.metu.edu.tr/handle/11511/109445

If you use this repository or datasets in your research, please cite the accompanying master's thesis:

```bibtex
@mastersthesis{deveci_2024,
  author       = {Deveci, İbrahim Ethem},
  title        = {Transformer models for translating natural language sentences into formal logical expressions},
  school       = {Middle East Technical University},
  year         = {2024},
  url          = {https://open.metu.edu.tr/handle/11511/109445}
}

