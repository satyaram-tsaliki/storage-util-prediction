# 📊 APPLYING STATISTICAL MODELING TO ANALYZE AND PREDICT STORAGE CAPACITY UTILIZATION

## 📝 Abstract
This project presents a predictive modeling approach to manage storage capacity utilization in artifact repository managers like Sonatype Nexus Repository (NXRM). Leveraging Python and machine learning techniques, we developed a regression-based model to forecast storage requirements, enabling proactive capacity management and reducing risks of unexpected server downtime.

The research addresses the challenges of managing digital artifacts (Maven, npm, Docker, etc.) in agile and DevOps workflows. It demonstrates the effectiveness of data-driven strategies for optimizing storage utilization by analyzing historical log data, performing feature engineering, and applying univariate linear regression. The solution empowers administrators with insights for proactive storage planning and aligns with modern software development lifecycle (SDLC) requirements.

---

## 📚 Publication Details

- **Journal**: International Journal of Research and Analytical Reviews (IJRAR)
- **Paper Id**: 303596
- **Link**: [http://www.ijrar.org/IJRAR19S1828.pdf](http://www.ijrar.org/IJRAR19S1828.pdf)
- **ISSN**: 2348-1269
- **Impact Factor**: 7.17
- **Publication Info**: Volume 7, Issue 1, January 2020

---

## 🚀 Key Contributions

✅ **Log Data Engineering**  
Collected, cleaned, and structured historical repository logs using Python (Pandas and NumPy), extracting key attributes like artifact size, operation type, timestamps, and repository names.  
✅ **System Architecture & Visualization**  
Designed detailed system diagrams illustrating interactions between GitHub, Jenkins CI/CD, and Sonatype Nexus repositories. Developed comprehensive visualizations to highlight data trends in artifact uploads, deletions, and storage consumption.  
✅ **Predictive Regression Model**  
Developed and evaluated a univariate linear regression model to forecast daily, weekly, and monthly storage consumption. The model provides administrators with actionable insights for proactive disk space planning and management.  
✅ **Operational Strategy**  
Proposed practical guidelines for incremental model deployment, phased implementation, and ongoing monitoring to maintain predictive accuracy and operational relevance.

---

## 🌐 Relevance and Impact

💡 **High-Quality Data Pipeline**  
The robust data preprocessing workflow ensured accurate and reliable datasets for machine learning, minimizing the risk of misleading predictions.  
📈 **Improved Storage Planning**  
The regression model delivered valuable predictions that enable proactive storage capacity planning, reducing unexpected downtime incidents.  
🧠 **Data-Driven Decision Support**  
System visualizations and analysis enhanced understanding of storage utilization trends, facilitating informed decisions by administrators and DevOps teams.  
🔧 **Scalable and Adaptable Solution**  
The proposed approach can be tailored to different repository formats and environments, supporting scaling strategies in dynamic development workflows.

---

## 📊 Experimental Results (Summary)

| Day      | Actual Total Size (GB) | Predicted Total Size (GB) |
|----------|------------------------|---------------------------|
| Day 1    | 81                     | 63.80                    |
| Day 2    | 58                     | 63.67                    |
| Day 3    | 60                     | 63.53                    |
| Day 4    | 62                     | 63.40                    |
| Day 5    | 54                     | 63.27                    |
| Day 6    | 45                     | 63.13                    |
| Day 7    | 79                     | 63.00                    |
| Day 8    | 61                     | 62.87                    |
| Day 9    | 61                     | 62.73                    |
| Day 10   | 71                     | 62.60                    |

📈 **Regression Equation**:  
`Predicted Total Size = 63.93 - 0.1333 * Day`

### Key Metrics:
- **Intercept (β₀)**: 63.93  
- **Slope (β₁)**: -0.1333  
- **Prediction Accuracy**: Consistent for trend analysis, suitable for proactive capacity planning.

---

## 🏗️ System Architecture Overview

- **Development Teams** push code to **GitHub**.
- **Jenkins CI/CD** pipelines build and publish artifacts.
- Artifacts are uploaded to **Sonatype Nexus Repository**:
  - Snapshot Repositories (development/testing artifacts)
  - Release Repositories (production-ready artifacts)
  - NuGet, npm repositories for package management.
- Repository logs are extracted, analyzed, and used for predictive modeling.

---

## 🔬 Methodology

1. **Data Collection**  
   - Extracted log files from NXRM repositories.
2. **Data Cleaning & Feature Engineering**  
   - Parsed URLs, extracted repository types, operation types, and timestamps.
   - Cleaned inconsistent entries and filtered PUT operations.
3. **Regression Analysis**  
   - Applied univariate linear regression to predict storage requirements based on time series data.
4. **Validation & Comparison**  
   - Compared actual vs. predicted storage consumption to validate model performance.
5. **Implementation Strategy**  
   - Phased model deployment and ongoing monitoring to adapt to evolving storage trends.

---

## 🛠️ Technologies Used

- **Python**: Data analysis & machine learning (Pandas, NumPy, Matplotlib)
- **Jenkins**: CI/CD integration for artifact automation
- **Sonatype Nexus Repository**: Artifact management and storage utilization
- **GitHub**: Source control and integration with Jenkins pipelines
- **Machine Learning**: Univariate Linear Regression (scikit-learn, manual calculation)

---

## 📜 Citation

If you use this work, please cite it as follows:

**Satya Ram Tsaliki, Dr. B. Purnachandra Rao** (2020).  
**"APPLYING STATISTICAL MODELING TO ANALYZE AND PREDICT STORAGE CAPACITY UTILIZATION"**,  
IJRAR - International Journal of Research and Analytical Reviews (IJRAR),  
Volume 7, Issue 1, Pages 518-533, January 2020.  
Available at: [http://www.ijrar.org/IJRAR19S1828.pdf](http://www.ijrar.org/IJRAR19S1828.pdf)

```bibtex
@article{tsaliki2020storage,
  title={APPLYING STATISTICAL MODELING TO ANALYZE AND PREDICT STORAGE CAPACITY UTILIZATION},
  author={Satya Ram Tsaliki and B. Purnachandra Rao},
  journal={International Journal of Research and Analytical Reviews (IJRAR)},
  volume={7},
  number={1},
  pages={518-533},
  year={2020},
  issn={2348-1269},
  url={http://www.ijrar.org/IJRAR19S1828.pdf}
}
