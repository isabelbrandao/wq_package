# Methodology: Chlorophyll-a Monitoring Using Sentinel-2

## Overview

This document describes the scientific methodology used for monitoring chlorophyll-a concentrations in Welsh inland waterbodies using satellite remote sensing.

## 1. Data Source

### Sentinel-2 Mission
- **Satellite**: Copernicus Sentinel-2A and Sentinel-2B
- **Operator**: European Space Agency (ESA)
- **Temporal Resolution**: 5 days (with both satellites)
- **Spatial Resolution**: 10m, 20m, and 60m depending on spectral band
- **Data Level**: Level 2A (atmospherically corrected surface reflectance)

### Living Wales Datacube
- Analysis Ready Data (ARD) infrastructure
- Pre-processed Sentinel-2 imagery for Wales
- Cloud-optimized data storage
- Temporal coverage: 2015-present

## 2. Study Area

### Llangorse Lake (Llyn Syfaddan)
- **Location**: Brecon Beacons National Park, Wales
- **Type**: Natural freshwater lake
- **Area**: ~1.4 km²
- **Ecological Importance**: Largest natural lake in South Wales, SSSI designation

*Note: Methodology is transferable to other Welsh waterbodies*

## 3. Spectral Indices for Chlorophyll Detection

### Normalized Difference Chlorophyll Index (NDCI)

**Formula**:
```
NDCI = (ρ_RE - ρ_RED) / (ρ_RE + ρ_RED)
```

Where:
- **ρ_RE**: Surface reflectance in red-edge band (Sentinel-2 Band 5, 705 nm)
- **ρ_RED**: Surface reflectance in red band (Sentinel-2 Band 4, 665 nm)

**Physical Basis**:
- Chlorophyll-a absorbs strongly in the red region (~665 nm)
- Reflectance increases at red-edge wavelengths (~705 nm) with chlorophyll presence
- The ratio amplifies this spectral difference

**Interpretation**:
- **NDCI > 0**: Indicates presence of chlorophyll-a
- **Higher values**: Greater chlorophyll-a concentration
- **Typical range**: -1 to +1 (waterbodies typically 0 to 0.5)

### Why NDCI for Inland Waters?

1. **Sensitivity**: Red-edge is particularly sensitive to chlorophyll absorption
2. **Robustness**: Less affected by atmospheric scattering than blue/green bands
3. **Resolution**: Both bands available at 10m resolution (after resampling)
4. **Validation**: Well-established in scientific literature for inland waters

## 4. Data Processing Workflow

### 4.1 Data Acquisition
```python
# Load Sentinel-2 data from datacube
ds = dc.load(
    product='sen2_l2a_gcp',
    latitude=(-51.95, -51.93),
    longitude=(3.25, 3.27),
    time=('2020-01-01', '2023-12-31'),
    measurements=['red', 'red_edge_1']
)
```

### 4.2 Quality Filtering

**Cloud Masking**:
- Utilize Scene Classification Layer (SCL) from Sentinel-2 L2A
- Mask clouds, cloud shadows, and snow/ice
- Retain only clear water pixels

**Criteria**:
- Cloud cover threshold: < 20% per scene
- Valid pixel requirement: > 50% of waterbody area

### 4.3 Index Calculation

```python
# Calculate NDCI
ndci = (ds.red_edge_1 - ds.red) / (ds.red_edge_1 + ds.red)
```

### 4.4 Spatial Aggregation

**Waterbody Mask**:
- Define region of interest (ROI) polygon
- Extract pixels within waterbody boundary
- Exclude land/shore pixels

**Aggregation**:
- Mean NDCI across all valid waterbody pixels
- Standard deviation for variability assessment
- Pixel count for data quality metrics

### 4.5 Temporal Analysis

**Time Series Construction**:
- Aggregate NDCI values by date
- Handle irregular temporal sampling
- Identify seasonal patterns

**Quality Checks**:
- Remove outliers (e.g., residual cloud contamination)
- Flag low-confidence observations

## 5. Analysis Methods

### 5.1 Temporal Trend Analysis

**Objective**: Identify seasonal patterns and long-term trends

**Methods**:
- Time series plotting with confidence intervals
- Seasonal decomposition
- Trend detection (Mann-Kendall test)

**Outputs**:
- Monthly/seasonal average NDCI
- Inter-annual variability
- Bloom event identification

### 5.2 Spatial Analysis

**Objective**: Map chlorophyll distribution within waterbody

**Methods**:
- Pixel-level NDCI mapping
- Hotspot identification
- Spatial autocorrelation analysis

**Outputs**:
- False-color composite (NDCI values)
- Spatial heterogeneity metrics
- Zone classification (high/medium/low chlorophyll)

### 5.3 Comparative Analysis

**Temporal Comparison**:
- Before/after event comparison
- Seasonal contrasts (spring vs. summer)
- Year-over-year changes

## 6. Limitations and Uncertainties

### 6.1 Atmospheric Effects
- **Issue**: Residual atmospheric contamination despite L2A correction
- **Impact**: Can bias reflectance values
- **Mitigation**: Multi-temporal averaging, outlier removal

### 6.2 Mixed Pixels
- **Issue**: Shore pixels contain land and water signals
- **Impact**: Biased NDCI near edges
- **Mitigation**: Buffer zones, strict waterbody masking

### 6.3 Optical Depth
- **Issue**: NDCI reflects surface chlorophyll only
- **Impact**: May not represent full water column
- **Limitation**: Valid for optically shallow interpretation

### 6.4 Cloud Cover
- **Issue**: Frequent cloud cover in Wales reduces temporal resolution
- **Impact**: Data gaps, missed bloom events
- **Mitigation**: 5-day revisit, multi-year analysis

### 6.5 Sensor Resolution
- **Issue**: 10m pixels may not resolve small features
- **Impact**: Limited for very small waterbodies (<0.1 km²)
- **Suitability**: Adequate for Llangorse Lake and similar-sized bodies

## 7. Validation and Accuracy

### 7.1 Ground Truth Comparison
**Ideal Approach**:
- In-situ chlorophyll-a measurements (lab analysis)
- Matchup within ±3 hours of satellite overpass
- Spatial averaging to match pixel scale

### 7.2 Expected Accuracy
**Literature-based estimates**:
- NDCI correlation with chlorophyll-a: R² = 0.7-0.85
- Detection limit: ~5-10 μg/L chlorophyll-a
- Best performance: 10-100 μg/L range

### 7.3 Quality Indicators
- Clear sky conditions
- High percentage of valid pixels (>80%)
- Consistent multi-temporal pattern
- Agreement with known seasonal cycles

## 8. Applications

### 8.1 Operational Monitoring
- Regular (weekly/monthly) water quality assessment
- Algal bloom early warning system
- Compliance monitoring for Water Framework Directive

### 8.2 Research Applications
- Climate change impact studies
- Nutrient loading assessment
- Ecosystem health evaluation
- Land use change impacts

### 8.3 Decision Support
- Water treatment facility alerts
- Recreational water safety advisories
- Fishery management
- Conservation planning

## 9. Future Enhancements

### 9.1 Additional Indices
- **Turbidity indices**: For suspended sediment
- **CDOM indices**: Colored dissolved organic matter
- **Multi-index approach**: Improve classification

### 9.2 Machine Learning
- Random forest for chlorophyll concentration estimation
- Time series forecasting
- Anomaly detection algorithms

### 9.3 Integration
- Combine with in-situ sensor networks
- Weather data integration
- Hydrological model coupling

## 10. References

### Key Publications
- Mishra, S., & Mishra, D. R. (2012). Normalized difference chlorophyll index: A novel model for remote estimation of chlorophyll-a concentration in turbid productive waters. *Remote Sensing of Environment*.

- Gitelson, A. A., et al. (2008). Remote estimation of chlorophyll-a concentration in inland waters. *Advances in Space Research*.

- Moses, W. J., et al. (2012). Estimation of chlorophyll-a concentration in turbid productive waters using airborne hyperspectral data. *Water Research*.

### Sentinel-2 Resources
- ESA Sentinel-2 User Handbook
- Sen2Cor Atmospheric Correction Documentation
- Copernicus Open Access Hub

### Living Wales
- Living Wales Project Documentation
- Open Data Cube User Guide

---

*This methodology document provides the scientific foundation for the chlorophyll monitoring analysis. For implementation details, see the Jupyter notebook.*
