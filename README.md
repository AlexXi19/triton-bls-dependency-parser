# triton-bls-dependency-parser
Parses Nvidia Triton BLS Dependencies using python AST (Abstract Syntax Tree)

### How to use 

Randomly sample triton models from model registry (s3)

`S3_BUCKET=<bucket-name> python3 find_python_in_s3.py`

Parse model dependencies 

`python3 find_all_models.py`
