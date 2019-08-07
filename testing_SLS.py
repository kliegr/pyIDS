import pandas as pd
from pyids.ids_classifier import IDS, mine_CARs

from pyarc.qcba.data_structures import QuantitativeDataFrame


df = pd.read_csv("./data/titanic.csv")

cars = mine_CARs(df, rule_cutoff=80)

quant_dataframe = QuantitativeDataFrame(df)


ids = IDS()
ids.fit(class_association_rules=cars, quant_dataframe=quant_dataframe, debug=True)

auc = ids.score_auc(quant_dataframe)
print(auc)
