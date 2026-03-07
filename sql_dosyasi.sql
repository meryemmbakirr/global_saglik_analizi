create table saglik_analizleri (
country_code VARCHAR(5),
    country_name VARCHAR(100),
    region VARCHAR(100),
    sub_region VARCHAR(100),
    year INTEGER,
    month INTEGER,
    period VARCHAR(10),
    monthly_analyses INTEGER,
    cumulative_analyses INTEGER,
    unique_users INTEGER,
    repeat_user_rate DOUBLE PRECISION,
    avg_biomarkers_per_test DOUBLE PRECISION,
    condition_healthy_pct DOUBLE PRECISION,
    condition_cardiovascular_pct DOUBLE PRECISION,
    condition_diabetes_pct DOUBLE PRECISION,
    condition_metabolic_syndrome_pct DOUBLE PRECISION,
    condition_anemia_pct DOUBLE PRECISION,
    condition_thyroid_pct DOUBLE PRECISION,
    condition_vitamin_d_deficiency_pct DOUBLE PRECISION,
    condition_vitamin_b12_deficiency_pct DOUBLE PRECISION,
    condition_liver_pct DOUBLE PRECISION,
    condition_kidney_pct DOUBLE PRECISION,
    condition_inflammation_pct DOUBLE PRECISION,
    risk_optimal_pct DOUBLE PRECISION,
    risk_normal_pct DOUBLE PRECISION,
    risk_attention_pct DOUBLE PRECISION,
    risk_elevated_pct DOUBLE PRECISION,
    risk_critical_pct DOUBLE PRECISION,
    age_18_29_pct DOUBLE PRECISION,
    age_30_44_pct DOUBLE PRECISION,
    age_45_59_pct DOUBLE PRECISION,
    age_60_plus_pct DOUBLE PRECISION,
    gender_male_pct DOUBLE PRECISION,
    gender_female_pct DOUBLE PRECISION,
    mobile_usage_pct DOUBLE PRECISION,
    web_usage_pct DOUBLE PRECISION,
    avg_report_pages DOUBLE PRECISION,
    nutrition_plan_requested_pct DOUBLE PRECISION,
    supplement_rec_requested_pct DOUBLE PRECISION,
    primary_language VARCHAR(50),
    avg_health_score DOUBLE PRECISION,
    avg_cardiovascular_risk_score DOUBLE PRECISION,
    avg_metabolic_risk_score DOUBLE PRECISION,
    avg_nutrient_score DOUBLE PRECISION,
    top_abnormal_biomarker_1 VARCHAR(100),
    top_abnormal_biomarker_2 VARCHAR(100),
    top_abnormal_biomarker_3 VARCHAR(100),
    avg_biomarkers_out_of_range DOUBLE PRECISION,
    biomarker_abnormal_rate DOUBLE PRECISION
);

-- aylık büyüme analizi
-- her ülkenin aylık analiz sayısındaki değişimö oranı 
select 
region,
country_name,
period,
monthly_analyses,
LAG(monthly_analyses) over (PARTITION BY country_name order by period) as prev_month_analyses,
ROUND(
((monthly_analyses - LAG (monthly_analyses) over (PARTITION BY country_name order by period))* 100.0)/
NULLIF(LAG(monthly_analyses) over (PARTITION BY country_name order by period),0),
2) as growth_pct
FROM saglik_analizleri

SELECT * FROM saglik_analizleri