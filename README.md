# Welsh Waterbody Chlorophyll Monitoring 🌊

Monitoring chlorophyll-a concentrations in Welsh inland waterbodies using Sentinel-2 satellite imagery and the Living Wales datacube.

## 📋 Overview

This project demonstrates remote sensing analysis for water quality monitoring using the Living Wales datacube infrastructure. The analysis focuses on detecting and tracking chlorophyll-a levels in Welsh lakes and reservoirs, which serves as a key indicator of water quality and potential algal blooms.

### Key Features
- **Sentinel-2 satellite data processing** from the Living Wales datacube
- **Normalized Difference Chlorophyll Index (NDCI)** calculation for chlorophyll-a detection
- **Time-series analysis** to track water quality changes over time
- **Interactive visualizations** including maps and temporal plots
- **Cloud filtering** for accurate water body analysis

## 🎯 Use Case

Inland waterbodies are essential for supporting human life through water supply and recreation. However, they are vulnerable to water quality degradation from agricultural runoff, urban pollution, and climate change. This analysis provides:

- Early detection of algal blooms
- Long-term water quality trend monitoring
- Spatial distribution of chlorophyll concentrations
- Support for water resource management decisions

## 📓 Notebooks

### `Chlorophyll_monitoring.ipynb`
Main analysis notebook that performs:
1. **Data Loading**: Access Sentinel-2 Level 2A data from the Living Wales datacube
2. **Preprocessing**: Cloud masking and quality filtering
3. **Index Calculation**: Compute NDCI from satellite bands
4. **Analysis**: Time-series and spatial analysis of chlorophyll concentrations
5. **Visualization**: Interactive maps and summary plots

**Example Study Site**: Llangorse Lake (Llyn Syfaddan), Wales

## 🛠️ Technologies

- **Python 3.x** - Core programming language
- **Open Data Cube** - Geospatial data management
- **Sentinel-2** - ESA satellite imagery (10m resolution)
- **xarray** - Multi-dimensional array processing
- **matplotlib** - Data visualization
- **Living Wales Datacube** - Analysis Ready Data infrastructure

## 📦 Installation

### Prerequisites
- Access to Living Wales datacube environment
- Python 3.7 or higher

### Required Packages
```bash
pip install -r requirements.txt
```

Key dependencies:
- `datacube` - Open Data Cube framework
- `xarray` - Labeled multi-dimensional arrays
- `numpy` - Numerical computing
- `pandas` - Data manipulation
- `matplotlib` - Plotting and visualization

## 🚀 Usage

1. **Set up datacube connection**
   ```python
   import datacube
   dc = datacube.Datacube()
   ```

2. **Define area of interest**
   - Specify latitude/longitude coordinates
   - Set temporal range for analysis

3. **Run the notebook**
   - Execute cells sequentially
   - Adjust parameters as needed for different waterbodies

4. **Interpret results**
   - Higher NDCI values indicate higher chlorophyll-a concentrations
   - Time-series plots show seasonal and long-term trends

## 📊 Methodology

### Normalized Difference Chlorophyll Index (NDCI)

NDCI leverages the reflectance characteristics of chlorophyll-a:

```
NDCI = (Red Edge - Red) / (Red Edge + Red)
```

Using Sentinel-2 bands:
- **Red**: Band 4 (665 nm)
- **Red Edge**: Band 5 (705 nm)

**Interpretation**:
- Higher NDCI values → Higher chlorophyll-a concentration
- Positive values typically indicate algal blooms
- Temporal trends reveal water quality dynamics

## 🌍 Example Applications

- **Water Quality Monitoring**: Track eutrophication in reservoirs
- **Algal Bloom Detection**: Early warning system for harmful blooms
- **Environmental Impact Assessment**: Evaluate effects of land use changes
- **Seasonal Analysis**: Understand natural variation patterns

## 📈 Sample Outputs

The notebook generates:
- **RGB composite images** - Visual inspection of waterbodies
- **NDCI spatial maps** - Chlorophyll distribution patterns
- **Time-series plots** - Historical trends in water quality
- **Summary statistics** - Quantitative water quality metrics

## 🔬 Technical Skills Demonstrated

- Remote sensing data analysis
- Satellite image processing
- Geospatial programming (Python)
- Cloud computing with datacube infrastructure
- Environmental data science
- Scientific visualization
- Time-series analysis

## 📚 Background

This work is based on the Living Wales project, which provides Analysis Ready Data (ARD) from multiple satellite missions covering Wales. The datacube infrastructure enables efficient access to petabytes of Earth observation data for environmental monitoring.

## 🤝 Contributing

Suggestions for improvements are welcome! Areas for enhancement:
- Additional water quality indices (e.g., turbidity, CDOM)
- Machine learning for bloom prediction
- Multi-waterbody comparison tools
- Automated reporting workflows

## 📄 License

This project uses data from:
- **Copernicus Sentinel-2** data (ESA)
- **Living Wales** datacube infrastructure

## 🔗 Related Resources

- [Living Wales Project](https://livingwales.aber.ac.uk/)
- [Sentinel-2 Mission](https://sentinel.esa.int/web/sentinel/missions/sentinel-2)
- [Open Data Cube](https://www.opendatacube.org/)

## 📧 Contact

Feel free to reach out for questions or collaboration opportunities!

---

**Tags**: `remote-sensing` `water-quality` `sentinel-2` `datacube` `environmental-monitoring` `geospatial` `python` `chlorophyll` `wales` `satellite-imagery`
