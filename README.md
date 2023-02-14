# triton-bls-dependency-parser
Parses Nvidia Triton BLS Dependencies using python AST (Abstract Syntax Tree)

### How to use 

#### Parse a single model 
`python3 model_parser.py <dir-to-model>`

#### A more comprehensive test

Randomly sample triton models from model registry (s3)

`S3_BUCKET=<bucket-name> python3 find_python_in_s3.py`

Parse model dependencies 

`python3 find_all_models.py`

### Known limitations 

Currenlty only handles when `model_name` is a string, a variable of a string, or a class attribute. 
