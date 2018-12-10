# Real-time Image Feature Extraction with InceptionV3

Server-client software for extracting image features using pretrained Inception V3

## Installation

run

```
pip install -r requirements.txt
```

## Start

Start server

```
python iv3_server.py
```

Start client

```
python get_feature.py
```

Client will display a summary of features (number of features, the first three elements from the feature list).
