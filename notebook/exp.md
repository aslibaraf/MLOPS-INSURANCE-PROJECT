```python
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from imblearn.over_sampling import RandomOverSampler
sns.set(style='whitegrid')

import warnings
warnings.filterwarnings("ignore")
```


```python
df = pd.read_csv("data.csv")
df.head()

```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>id</th>
      <th>Gender</th>
      <th>Age</th>
      <th>Driving_License</th>
      <th>Region_Code</th>
      <th>Previously_Insured</th>
      <th>Vehicle_Age</th>
      <th>Vehicle_Damage</th>
      <th>Annual_Premium</th>
      <th>Policy_Sales_Channel</th>
      <th>Vintage</th>
      <th>Response</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>1</td>
      <td>Male</td>
      <td>44</td>
      <td>1</td>
      <td>28.0</td>
      <td>0</td>
      <td>&gt; 2 Years</td>
      <td>Yes</td>
      <td>40454.0</td>
      <td>26.0</td>
      <td>217</td>
      <td>1</td>
    </tr>
    <tr>
      <th>1</th>
      <td>2</td>
      <td>Male</td>
      <td>76</td>
      <td>1</td>
      <td>3.0</td>
      <td>0</td>
      <td>1-2 Year</td>
      <td>No</td>
      <td>33536.0</td>
      <td>26.0</td>
      <td>183</td>
      <td>0</td>
    </tr>
    <tr>
      <th>2</th>
      <td>3</td>
      <td>Male</td>
      <td>47</td>
      <td>1</td>
      <td>28.0</td>
      <td>0</td>
      <td>&gt; 2 Years</td>
      <td>Yes</td>
      <td>38294.0</td>
      <td>26.0</td>
      <td>27</td>
      <td>1</td>
    </tr>
    <tr>
      <th>3</th>
      <td>4</td>
      <td>Male</td>
      <td>21</td>
      <td>1</td>
      <td>11.0</td>
      <td>1</td>
      <td>&lt; 1 Year</td>
      <td>No</td>
      <td>28619.0</td>
      <td>152.0</td>
      <td>203</td>
      <td>0</td>
    </tr>
    <tr>
      <th>4</th>
      <td>5</td>
      <td>Female</td>
      <td>29</td>
      <td>1</td>
      <td>41.0</td>
      <td>1</td>
      <td>&lt; 1 Year</td>
      <td>No</td>
      <td>27496.0</td>
      <td>152.0</td>
      <td>39</td>
      <td>0</td>
    </tr>
  </tbody>
</table>
</div>




```python

```



# Customer Vehicle Insurance Dataset Description

- **`ID`**:  
  Unique identifier for the customer.

- **`Gender`**:  
  Gender of the customer.

- **`Age`**:  
  Age of the customer.

- **`Driving_License`**:  
  - `0`: Customer does not have a driving license.  
  - `1`: Customer already has a driving license.

- **`Region_Code`**:  
  Unique code representing the region of the customer.

- **`Previously_Insured`**:  
  - `1`: Customer already has vehicle insurance.  
  - `0`: Customer does not have vehicle insurance.

- **`Vehicle_Age`**:  
  Age of the customer's vehicle.

- **`Vehicle_Damage`**:  
  - `1`: Customer has had their vehicle damaged in the past.  
  - `0`: Customer has not had their vehicle damaged in the past.

- **`Annual_Premium`**:  
  The yearly premium amount the customer is required to pay.

- **`Policy_Sales_Channel`**:  
  An anonymized code representing the outreach channel used to contact the customer (e.g., agents, mail, phone, in-person).

- **`Vintage`**:  
  Number of days the customer has been associated with the company.

- **`Response`**:  
  - `1`: Customer is interested in vehicle insurance.  
  - `0`: Customer is not interested in vehicle insurance.



