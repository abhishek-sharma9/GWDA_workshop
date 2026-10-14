#!/usr/bin/env python3

"""
Download GW150914 and GW190814 strain data from GWOSC.
"""

from pathlib import Path

import numpy as np
from gwpy.timeseries import TimeSeries
from pycbc.types import TimeSeries as PyCBCTimeSeries
from pycbc.frame import write_frame


# Event information: GPS trigger time, duration, detectors
events = {
    "GW150914": (1126259462.4, 64, ["H1", "L1"]),
    "GW190814": (1249852257.0, 256, ["H1", "L1", "V1"])
}

sample_rate = 4096

data_dir = Path(__file__).resolve().parent / "data"
data_dir.mkdir(exist_ok=True)

for event, (gps, duration, detectors) in events.items():

    start = int(gps) - duration // 2
    end = start + duration

    for ifo in detectors:

        filename = f"{event}_{ifo}_{sample_rate}Hz_{duration}s.gwf"
        filepath = data_dir / filename

        if filepath.exists():
            print(f"Already exists: {filename}")
            continue

        print(f"Downloading {event} - {ifo} ...")

        # Fetch public strain data from GWOSC
        strain = TimeSeries.fetch_open_data(ifo, start, end, sample_rate=sample_rate, format="hdf5", cache=False)

        data = PyCBCTimeSeries(np.asarray(strain.value), delta_t=1.0 / sample_rate, epoch=float(strain.t0.value))

        # Save as GWF frame file
        channel = f"{ifo}:GWOSC-4KHZ_R1_STRAIN"
        write_frame(str(filepath), channel, data)

        print(f"Saved: {filepath}")

print("\nAll data downloaded successfully!")