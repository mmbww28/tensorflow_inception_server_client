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

```
2048  [0.2339864820241928, 0.37743332982063293, 0.30994588136672974]...
2048  [0.2339864820241928, 0.37743332982063293, 0.30994588136672974]...
2048  [0.2339864820241928, 0.37743332982063293, 0.30994588136672974]...
2048  [0.2339864820241928, 0.37743332982063293, 0.30994588136672974]...
2048  [0.2339864820241928, 0.37743332982063293, 0.30994588136672974]...
```

