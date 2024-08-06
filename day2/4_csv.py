
import pandas as pd

data = [
    {
        "name":"aryan jaswal",
        "G":"M"
    },
    {
        "name":"ram",
        "G":"M"
    },
    {
        "name":"sham",
        "G":"M"
    }
]

df = pd.DataFrame(data)
df.to_csv("data.csv")