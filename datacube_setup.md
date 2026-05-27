# Living Wales Datacube Setup Guide

This guide provides instructions for setting up and accessing the Living Wales datacube environment for satellite data analysis.

## What is the Open Data Cube?

The Open Data Cube (ODC) is an open-source framework for managing and analyzing large volumes of Earth observation data. The Living Wales project uses ODC to provide Analysis Ready Data (ARD) for Wales.

## Prerequisites

### System Requirements
- **Operating System**: Linux (Ubuntu/Debian recommended) or MacOS
- **Python**: 3.7 or higher
- **Memory**: 8GB RAM minimum (16GB+ recommended)
- **Storage**: Varies by analysis scope (10GB+ free space)

### Knowledge Requirements
- Python programming
- Understanding of geospatial concepts
- Familiarity with Jupyter notebooks

## Installation Options

### Option 1: Living Wales JupyterHub (Recommended for Beginners)

The Living Wales project may provide hosted JupyterHub access with pre-configured datacube environment.

**Advantages**:
- No local installation needed
- Pre-loaded with all dependencies
- Direct access to datacube
- Collaborative environment

**Access**:
Contact the Living Wales team for access credentials.

### Option 2: Local Installation

#### Step 1: Install Python and Dependencies

```bash
# Update system packages
sudo apt-get update
sudo apt-get install python3-pip python3-dev

# Install GDAL dependencies
sudo apt-get install libgdal-dev gdal-bin

# Install PostgreSQL (for datacube index)
sudo apt-get install postgresql postgresql-contrib
```

#### Step 2: Create Virtual Environment

```bash
# Create virtual environment
python3 -m venv datacube-env

# Activate environment
source datacube-env/bin/activate

# Upgrade pip
pip install --upgrade pip
```

#### Step 3: Install Open Data Cube

```bash
# Install datacube core
pip install datacube

# Install additional geospatial packages
pip install rasterio fiona shapely geopandas

# Install scientific computing packages
pip install numpy pandas xarray scipy

# Install visualization packages
pip install matplotlib seaborn folium

# Install Jupyter
pip install jupyter ipywidgets
```

#### Step 4: Verify Installation

```bash
# Check datacube installation
datacube --version

# List available products (if connected to datacube)
datacube product list
```

### Option 3: Docker Container

```bash
# Pull Open Data Cube Docker image
docker pull opendatacube/datacube-core

# Run container
docker run -it -p 8888:8888 opendatacube/datacube-core
```

## Configuration

### Database Setup (for local installation)

#### Step 1: Initialize PostgreSQL Database

```bash
# Create datacube user
sudo -u postgres createuser datacube

# Create datacube database
sudo -u postgres createdb -O datacube datacube

# Set password
sudo -u postgres psql -c "ALTER USER datacube WITH PASSWORD 'your_password';"
```

#### Step 2: Initialize Datacube

```bash
# Initialize datacube database
datacube -v system init
```

### Configuration File

Create `~/.datacube.conf`:

```ini
[datacube]
db_database: datacube
db_hostname: localhost
db_username: datacube
db_password: your_password

[user]
default_environment: datacube
```

## Connecting to Living Wales Datacube

### Authentication

Depending on your access method, you may need:
- **API credentials** for programmatic access
- **VPN connection** to institutional network
- **SSH tunnel** to datacube server

Example connection:

```python
import datacube

# Connect to datacube
dc = datacube.Datacube(app='chlorophyll_monitoring')

# List available products
products = dc.list_products()
print(products)
```

## Loading Sentinel-2 Data

### Basic Data Loading

```python
# Define query parameters
query = {
    'product': 'sen2_l2a_gcp',
    'latitude': (-51.95, -51.93),
    'longitude': (3.25, 3.27),
    'time': ('2022-01-01', '2022-12-31'),
    'measurements': ['red', 'green', 'blue', 'nir', 'red_edge_1'],
    'output_crs': 'EPSG:32630',
    'resolution': (-10, 10)
}

# Load data
ds = dc.load(**query)
```

### Understanding Data Products

**Common Products in Living Wales Datacube**:

| Product | Description | Spatial Resolution |
|---------|-------------|-------------------|
| `sen2_l2a_gcp` | Sentinel-2 L2A Surface Reflectance | 10/20/60m |
| `sen1_rtc` | Sentinel-1 SAR Backscatter | 10m |
| `ls8_sr` | Landsat 8 Surface Reflectance | 30m |

### Available Measurements (Sentinel-2)

| Band Name | Wavelength | Resolution | Use |
|-----------|------------|------------|-----|
| `coastal_aerosol` | 443 nm | 60m | Atmospheric correction |
| `blue` | 490 nm | 10m | Water, vegetation |
| `green` | 560 nm | 10m | Vegetation, water |
| `red` | 665 nm | 10m | Chlorophyll absorption |
| `red_edge_1` | 705 nm | 20m | Vegetation, chlorophyll |
| `red_edge_2` | 740 nm | 20m | Vegetation |
| `red_edge_3` | 783 nm | 20m | Vegetation |
| `nir` | 842 nm | 10m | Vegetation, water |
| `nir_narrow` | 865 nm | 20m | Atmospheric correction |
| `swir_1` | 1610 nm | 20m | Moisture, geology |
| `swir_2` | 2190 nm | 20m | Geology, moisture |

## Working with Xarray Datasets

Data from datacube is returned as xarray Datasets:

```python
# Examine dataset structure
print(ds)

# Access specific band
red_band = ds['red']

# Get dimensions
print(ds.dims)  # Output: {'time': 50, 'latitude': 200, 'longitude': 200}

# Get coordinates
print(ds.coords)
```

## Troubleshooting

### Common Issues

#### 1. Connection Errors
```
Error: Could not connect to datacube database
```
**Solution**: Check database credentials in `~/.datacube.conf`

#### 2. Product Not Found
```
Error: Product 'sen2_l2a_gcp' not found
```
**Solution**: Verify product name with `datacube product list`

#### 3. Out of Memory
```
MemoryError: Unable to allocate array
```
**Solution**: 
- Reduce spatial/temporal extent
- Use `dask` for lazy loading
- Increase available memory

#### 4. Slow Performance
**Solutions**:
- Use smaller time ranges
- Enable dask chunking
- Request only needed measurements
- Use appropriate spatial resolution

### Performance Optimization

```python
# Enable dask for lazy loading
ds = dc.load(
    product='sen2_l2a_gcp',
    latitude=(-51.95, -51.93),
    longitude=(3.25, 3.27),
    time=('2022-01-01', '2022-12-31'),
    measurements=['red', 'nir'],
    dask_chunks={'time': 1, 'latitude': 1000, 'longitude': 1000}
)

# Compute only when needed
result = ds.mean(dim=['latitude', 'longitude']).compute()
```

## Best Practices

### 1. Query Optimization
- Request only necessary bands
- Use appropriate time ranges
- Limit spatial extent to area of interest

### 2. Memory Management
- Use dask for large datasets
- Process in chunks/batches
- Clear unused variables

### 3. Data Quality
- Always check for cloud cover
- Use quality flags/masks
- Validate results visually

### 4. Reproducibility
- Document all query parameters
- Save analysis code in notebooks
- Version control your analysis

## Additional Resources

### Documentation
- [Open Data Cube Manual](https://datacube-core.readthedocs.io/)
- [Living Wales Documentation](https://livingwales.aber.ac.uk/)
- [Xarray Documentation](http://xarray.pydata.org/)

### Training Materials
- Open Data Cube Jupyter notebooks
- Living Wales workshops and tutorials
- Sentinel-2 user guides from ESA

### Community Support
- Open Data Cube Slack
- GitHub issues
- Research group forums

## Contact and Support

For Living Wales datacube specific support:
- Visit: https://livingwales.aber.ac.uk/
- Contact: Living Wales team at Aberystwyth University

For Open Data Cube general questions:
- GitHub: https://github.com/opendatacube/datacube-core
- Slack: http://slack.opendatacube.org/

---

*This guide is current as of 2024. Check official documentation for latest updates.*
