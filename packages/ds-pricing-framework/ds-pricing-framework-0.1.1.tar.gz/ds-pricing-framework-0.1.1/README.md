# ds-pricing-framework

This package contains the following class(es):
- TriageVariable

To use the TriageVariable module, you will need to start with a pandas dataframe that has the following variables:
- ep
- il
- policy_number
- claim_indicator
- policy_gen
- age
- price_per_mile

You will also need:
- a target variable for the model (claim_indicator is the preferred variable)
- a proposed variable that you are testing, summarized at the policy level
- any variables that you would like to control for

The inputs for TriageVariable are:
- pandas dataframe
- target variable
- proposed variable
- list of control variables

Call the function run_triage which will output tables to help make a decision about the variable.

Example:
```
pip install ds-pricing-framework
import pricing_framework_triage as pf
triage = pf.TriageVariable(df, "claim_indicator", "prior_claim", ["package", "seasoning", "age_bucket"])
triage.run_triage()
```