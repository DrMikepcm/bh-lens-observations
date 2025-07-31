# Observational BH-Type Object Counts Near Strong Lenses

Observational dataset of BH-type object counts near selected strong gravitational lenses. SIMBAD-based queries were performed at multiple radii (10′, 15′, 20′), with results including fields showing zero detections. Useful for validating clustering signals and comparison with random fields.

## Example Query Code

```python
from astroquery.simbad import Simbad
from astropy.coordinates import SkyCoord
import astropy.units as u

# Define a lens position (RA, Dec in degrees)
lens_coord = SkyCoord(ra=104.6458, dec=-55.6748, unit="deg", frame="icrs")

# Set SIMBAD query radius
radius = 15 * u.arcmin

# Filter for BH-type objects
custom_simbad = Simbad()
custom_simbad.TIMEOUT = 120
custom_simbad.add_votable_fields("otype")

# Define object types of interest
bh_types = ['BH', 'BH?', 'XRB', 'BHXRB', 'QSO', 'BLLac', 'Blazar', 'AGN']

# Run the query
results = custom_simbad.query_region(lens_coord, radius=radius)

# Filter by object type
if results:
    bh_objects = results[[otype.decode("utf-8") in bh_types for otype in results["OTYPE"]]]
    print(f"Found {len(bh_objects)} BH-type objects within {radius}")
else:
    print("No objects found in this field.")
