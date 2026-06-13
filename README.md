# A Diagnostic Framework for Compositional Generalization via NL-to-FOL Translation

This repository contains the resources supporting the evaluation framework for neural semantic parsing from Natural Language to First-Order Logic (NL-to-FOL), to be presented at the **Student Session of the 36th European Summer School in Logic, Language and Information (ESSLLI 2025)**.

[Link for the preproceedings](https://2025.esslli.eu/courses-workshops-accepted/student-session-call.html).

## Contents

- **Datasets:** `WillowNLtoFOL` and `WillowNLtoFOL_extended` datasets designed to test compositional generalization in semantic parsing. The structured datasets are also available on **[Hugging Face](https://huggingface.co/datasets/iedeveci/WillowNLtoFOL)**.  
- **Code:** Training scripts and evaluation tools implementing the metrics proposed in the article, enabling reproducible experiments

## Purpose

This project provides a systematic and automated evaluation framework for assessing compositional generalization capabilities of neural semantic parsing models. It includes datasets with controlled logical complexity and comprehensive metrics to analyze both structural correctness and semantic equivalence of model outputs.

## Citation
If you use this repository or the accompanying dataset in your research, please cite the following work.
Deveci, İ.E. (2026). A Diagnostic Framework for Compositional Generalization via NL-to-FOL Translation. Journal of Logic, Language and Information. https://doi.org/10.1007/s10849-026-09480-0

@article{deveci_2026,
  author       = {Deveci, İbrahim Ethem},
  title        = {A Diagnostic Framework for Compositional Generalization via {NL}-to-{FOL} Translation},
  journal      = {Journal of Logic, Language and Information},
  year         = {2026},
  month        = {june},
  day          = {13},
  doi          = {10.1007/s10849-026-09480-0},
  url          = {https://doi.org/10.1007/s10849-026-09480-0}
}

## License

Licensed under [Creative Commons Attribution 4.0 International (CC BY 4.0)](https://creativecommons.org/licenses/by/4.0/).

