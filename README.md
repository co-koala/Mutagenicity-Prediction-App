# Mutagenicity-Prediction-App

## This is the test code for a web app that predicts the mutagenicity of a compound, which is based on streamlit.
- Go to [streamlit sharing URL](https://share.streamlit.io/yukisoya/mutagenicity-prediction-app/main/app.py) and input SMILES string of the target molecule. Then, you can get the result of prediction soon.
- The prediction model was built by lightgbm. Data in [“Benchmark Data Set for in Silico Prediction of Ames Mutagenicity” J. Chem. Inf. Model. 2009](https://pubs.acs.org/doi/10.1021/ci900161g) was used as the training data.
- [Mordred](https://github.com/mordred-descriptor/mordred) was uesd as the molecular descriptor calculator.