import pandas as pd

# Load the dataset - Ensure to replace 'financial_data.csv' with the actual path to your CSV file in the Flask environment
financial_data = pd.read_csv('financial_data.csv')

def financial_chatbot(company, year, query):
    # Convert year to int for comparison
    year = int(year)
    company_data_current_year = financial_data[(financial_data['Company'] == company) & (financial_data['Year'] == year)]
    
    if company_data_current_year.empty:
        return f"Data for {company} in {year} is not available."
    
    if "total revenue" in query.lower():
        total_revenue = company_data_current_year.iloc[0]['Total Revenue']
        return f"The total revenue of {company} in {year} was {total_revenue} million USD."
    elif "net income changed" in query.lower():
        company_data_previous_year = financial_data[(financial_data['Company'] == company) & (financial_data['Year'] == year - 1)]
        if company_data_previous_year.empty:
            return f"Net income change data from {year - 1} to {year} for {company} is not available."
        
        net_income_change = company_data_current_year.iloc[0]['Net Income'] - company_data_previous_year.iloc[0]['Net Income']
        direction = "increased" if net_income_change > 0 else "decreased"
        return f"The net income of {company} {direction} by {abs(net_income_change)} million USD from {year - 1} to {year}."
    elif "total assets and liabilities" in query.lower():
        total_assets = company_data_current_year.iloc[0]['Total Assets']
        total_liabilities = company_data_current_year.iloc[0]['Total Liabilities']
        return f"The total assets of {company} in {year} were {total_assets} million USD, and the total liabilities were {total_liabilities} million USD."
    else:
        return "Sorry, I don't understand that question."

