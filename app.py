import streamlit as st
import lightgbm as lgb
import numpy as np
import pandas as pd
from rdkit import Chem
from rdkit.Chem import PandasTools, Draw
from mordred import Calculator, descriptors
from io import BytesIO

clf = lgb.Booster(model_file='model.txt')

st.title("Mutagenicity Prediction App")
st.title("-----------------------")

st.sidebar.header('Input SMILES of target molecule')

def user_input_smiles():
        smiles = st.sidebar.text_input('SMILES')
        return smiles

smiles = user_input_smiles()

submit = st.sidebar.button("Predict")

if submit:
    mol = Chem.MolFromSmiles(smiles)
    df = pd.Series(smiles)
    df = pd.DataFrame(df)
    PandasTools.AddMoleculeColumnToFrame(df, smilesCol=0)

    img  = Draw.MolToImage(mol)
    bio = BytesIO()
    img.save(bio, format='png')
    st.header("Input molecule:")
    st.image(img)

    calc = Calculator(descriptors, ignore_3D=True)
    df_descriptors_mordred = calc.pandas(df['ROMol'])
    df_descriptors = df_descriptors_mordred.astype(str)
    masks = df_descriptors.apply(lambda d: d.str.contains('[a-zA-Z]' ,na=False))
    df_descriptors = df_descriptors[~masks]
    df_descriptors = df_descriptors.astype(float)

    pred_prob = float(clf.predict(df_descriptors, num_iteration=clf.best_iteration))
    pred_label = np.where(pred_prob < 0.5, 0, 1)

    if pred_label == 1:
        st.header("Mutagenicity risk : high")
    else:
        st.header("Mutagenicity risk : low")

    st.subheader('Prediction Probability : '+"{:.3f}".format(pred_prob))