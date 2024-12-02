# FaceSpoofingDetection API

```bash
git clone https://github.com/AI-Application-and-Integration-Lab/DGUA_FAS

git clone https://github.com/apple/ml-cvnets
cd ml-cvnets
git checkout 84d992f413e52c0468f86d23196efd9dad885e6f

# replace ./cvnets/models/classification/base_cls.py with the file from https://drive.google.com/file/d/1shq23SpC4X2OoYFELFjHMWpYyolmMEpj/view
pip install -r requirements.txt
```
Move the content of **ml-cvnets** into **DGUA_FAS** repository and create a file `test_inference.py` inside experiment/m/
