import pandas as pd

risks = [
    {
        "Risk": "Public S3 Bucket",
        "Likelihood": "High",
        "Impact": "High",
        "Risk Score": "Critical"
    },
    {
        "Risk": "MFA Disabled",
        "Likelihood": "Medium",
        "Impact": "High",
        "Risk Score": "High"
    }
]

df = pd.DataFrame(risks)

print("\n[+] ISO27001 Risk Register\n")
print(df)

df.to_csv("risk_register.csv", index=False)

print("\n[+] Risk register exported to risk_register.csv")
