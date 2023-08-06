Welcome to Datomize Python SDK
==============================

Datomize is a Data-Driven Solution to machine learning. Datomize augments source data with synthetic data of exceptional quality, and can be used to generate synthetic replicas, optimize training data with balanced and richer data, and address the data bias challenge.

# Getting Started

## Getting your application user & password

In order to use the Datomize Python SDK client, you first need to register the Datomize solution. Once registering Datomize, you will be provided with ``username`` and ``password``, which get passed to ``datomize.Datomizer()`` when starting your application.

Please register the Datomize solution on Datomize [Registration](https://app.datomize.com/#/dcs-on-boarding-page).

## Installation

```shell
pip install datomize
```

## Important links

- [Documentation](https://datomize.github.io/datomizeSDK)

### Usage Example

```python
# Import relevant packages
from datomizer import Datomizer, DatoMapper, DatoTrainer, DatoGenerator, DatoEnhancer
from sklearn.datasets import load_iris
import pandas as pd

# load input data:
data = load_iris(return_X_y=False, as_frame=True)
df = pd.concat([data.data, data.target], axis=1)

# Create a Datomizer with your credentials:
datomizer = Datomizer(username=username, password=password)

# Create a DatoMapper and analyze the data structure:
mapper = DatoMapper(datomizer)
mapper.discover(df_map={"df1": df})

# Create a DatoTrainer and train the generative model:
trainer = DatoTrainer(mapper)
trainer.train()

# Create a DatoGenerator and generate a syntheyic replica:
generator = DatoGenerator(trainer)
generator.generate(output_ratio=5)  # 5 times the original number of records will be created
synth_data = pd.read_csv(generator.get_generated_data_csv())

# Create a DatoEnhancer for a spedific prediction task and generate a balanced and augmented data to enhance your training data:
enhancer = DatoEnhancer(mapper)
enhancer.generate(target_column="target")
train_enhanced = pd.read_csv(enhancer.get_generated_data_csv())
```

### Async Usage Example

```python
from datomizer import Datomizer, DatoMapper, DatoTrainer, DatoGenerator

datomizer = Datomizer(username=username, password=password)

mapper = DatoMapper(datomizer)
mapper.discover(df_map={"df1": df}, title="Some Title", wait=False)
...
do something...
mapper.wait()

trainer = DatoTrainer(mapper)
trainer.train(wait=False)
...
do something...
trainer.wait()

generator = DatoGenerator(trainer)
generator.generate(wait=False)
...
do something...
generator.wait()

dato_df = pd.read_csv(generator.get_generated_data_csv())
```
