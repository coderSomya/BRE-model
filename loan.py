import pandas as pd

def calculate_les(row):
    score = 0

    # 1. Income Stability (15%)
    if row['Employment_Duration_Years'] >= 5:
        score += 15
    elif row['Employment_Duration_Years'] >= 3:
        score += 10
    elif row['Employment_Duration_Years'] >= 1:
        score += 5

    # 2. Bank Statement Insights (10%)
    if not row['Bank_Deposit_Gaps'] and row['Avg_EndOfMonth_Balance'] > 0.3 * row['Monthly_Income']:
        score += 10
    elif row['Avg_EndOfMonth_Balance'] > 0.1 * row['Monthly_Income']:
        score += 5

    # 3. Household Income (10%)
    if row['Household_Income'] > 2 * row['Monthly_Income']:
        score += 10
    elif row['Household_Income'] > row['Monthly_Income']:
        score += 7
    elif row['Household_Income'] > 0:
        score += 5

    # 4. FOIL (15%)
    foil = row['Monthly_Obligations'] / row['Monthly_Income']
    if foil <= 0.3:
        score += 15
    elif foil <= 0.5:
        score += 10
    elif foil <= 0.7:
        score += 5

    # 5. Residence Stability (5%)
    if row['Residence_Stability_Years'] >= 5:
        score += 5
    elif row['Residence_Stability_Years'] >= 2:
        score += 3

    # 6. Sector Risk (5%)
    score += {'Low': 5, 'Medium': 3, 'High': 0}.get(row['Sector_Risk_Level'], 0)

    # 7. Alternate Data (5%)
    if row['Mobile_Recharge_Consistency']:
        score += 5

    # 8. Location Risk (5%)
    score += {'Low': 5, 'Medium': 3, 'High': 0}.get(row['Location_Risk_Level'], 0)

    # 9. Credit Score (20%)
    if row['Credit_Score'] >= 750:
        score += 20
    elif row['Credit_Score'] >= 650:
        score += 15
    elif row['Credit_Score'] >= 550:
        score += 10

    # 10. Career Progression & Loyalty (10%)
    if row['Company_Tenure_Years'] >= 3:
        score += 5
    if row['Employment_Progression'] == 'Strong':
        score += 5
    elif row['Employment_Progression'] == 'Moderate':
        score += 3

    return score

def get_loan_multiplier(score):
    if score >= 85:
        return 20
    elif score >= 65:
        return 15
    elif score >= 45:
        return 10
    else:
        return 0

def process_csv(file_path):
    df = pd.read_csv(file_path)

    for index, row in df.iterrows():
        les = calculate_les(row)
        multiplier = get_loan_multiplier(les)
        net_income = row['Monthly_Income'] - row['Monthly_Obligations']
        max_loan = max(0, net_income * multiplier)
        print(f"Row {index + 1}: LES = {les}, Max Loan = ₹{max_loan:,.2f}")

if __name__ == "__main__":
    import sys
    if len(sys.argv) < 2:
        print("Usage: python loan.py data.csv")
    else:
        process_csv(sys.argv[1])
