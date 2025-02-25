{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 3,
   "id": "ac74517a-c74b-4505-a145-40c790ff9303",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\n",
      "When:  (2015, 2, 9, 2, 11, 39, -8)\n",
      "Where:  (-63.59214, 146.18322)\n",
      "Azimuth:  240.86\n",
      "Elevation:  2.66\n"
     ]
    }
   ],
   "source": [
    "# positionofsun.py\n",
    "import math\n",
    "def sunpos(when, location, refraction):\n",
    "# Extract the passed data\n",
    "    year, month, day, hour, minute, second, timezone = when\n",
    "    latitude, longitude = location\n",
    "# Math typing shortcuts\n",
    "    rad, deg = math.radians, math.degrees\n",
    "    sin, cos, tan = math.sin, math.cos, math.tan\n",
    "    asin, atan2 = math.asin, math.atan2\n",
    "# Convert latitude and longitude to radians\n",
    "    rlat = rad(latitude)\n",
    "    rlon = rad(longitude)\n",
    "# Decimal hour of the day at Greenwich\n",
    "    greenwichtime = hour - timezone + minute / 60 + second / 3600\n",
    "# Days from J2000, accurate from 1901 to 2099\n",
    "    daynum = (\n",
    "        367 * year\n",
    "        - 7 * (year + (month + 9) // 12) // 4\n",
    "        + 275 * month // 9\n",
    "        + day\n",
    "        - 730531.5\n",
    "        + greenwichtime / 24\n",
    "    )\n",
    "# Mean longitude of the sun\n",
    "    mean_long = daynum * 0.01720279239 + 4.894967873\n",
    "# Mean anomaly of the Sun\n",
    "    mean_anom = daynum * 0.01720197034 + 6.240040768\n",
    "# Ecliptic longitude of the sun\n",
    "    eclip_long = (\n",
    "        mean_long\n",
    "        + 0.03342305518 * sin(mean_anom)\n",
    "        + 0.0003490658504 * sin(2 * mean_anom)\n",
    "    )\n",
    "# Obliquity of the ecliptic\n",
    "    obliquity = 0.4090877234 - 0.000000006981317008 * daynum\n",
    "# Right ascension of the sun\n",
    "    rasc = atan2(cos(obliquity) * sin(eclip_long), cos(eclip_long))\n",
    "# Declination of the sun\n",
    "    decl = asin(sin(obliquity) * sin(eclip_long))\n",
    "# Local sidereal time\n",
    "    sidereal = 4.894961213 + 6.300388099 * daynum + rlon\n",
    "# Hour angle of the sun\n",
    "    hour_ang = sidereal - rasc\n",
    "# Local elevation of the sun\n",
    "    elevation = asin(sin(decl) * sin(rlat) + cos(decl) * cos(rlat) * cos(hour_ang))\n",
    "# Local azimuth of the sun\n",
    "    azimuth = atan2(\n",
    "        -cos(decl) * cos(rlat) * sin(hour_ang),\n",
    "        sin(decl) - sin(rlat) * sin(elevation),\n",
    "    )\n",
    "# Convert azimuth and elevation to degrees\n",
    "    azimuth = into_range(deg(azimuth), 0, 360)\n",
    "    elevation = into_range(deg(elevation), -180, 180)\n",
    "# Refraction correction (optional)\n",
    "    if refraction:\n",
    "        targ = rad((elevation + (10.3 / (elevation + 5.11))))\n",
    "        elevation += (1.02 / tan(targ)) / 60\n",
    "# Return azimuth and elevation in degrees\n",
    "    return (round(azimuth, 2), round(elevation, 2))\n",
    "def into_range(x, range_min, range_max):\n",
    "    shiftedx = x - range_min\n",
    "    delta = range_max - range_min\n",
    "    return (((shiftedx % delta) + delta) % delta) + range_min\n",
    "if __name__ == \"__main__\":\n",
    "# Close Encounters latitude, longitude\n",
    "    location = (-63.59214, 146.18322)\n",
    "# Fourth of July, 2022 at 11:20 am MDT (-6 hours)\n",
    "    when = (2015, 2, 9, 2, 11, 39, -8)\n",
    "# Get the Sun's apparent location in the sky\n",
    "    azimuth, elevation = sunpos(when, location, True)\n",
    "# Output the results\n",
    "    print(\"\\nWhen: \", when)\n",
    "    print(\"Where: \", location)\n",
    "    print(\"Azimuth: \", azimuth)\n",
    "    print(\"Elevation: \", elevation)\n",
    "# When:  (2022, 7, 4, 11, 20, 0, -6)\n",
    "# Where:  (40.602778, -104.741667)\n",
    "# Azimuth:  121.38\n",
    "# Elevation:  61.91"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "id": "7c5b1c69-92c0-422d-bb6b-08d45389e20d",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Collecting package metadata (current_repodata.json): done\n",
      "Solving environment: done\n",
      "\n",
      "# All requested packages already installed.\n",
      "\n",
      "\n",
      "Note: you may need to restart the kernel to use updated packages.\n"
     ]
    }
   ],
   "source": [
    "conda install -c conda-forge timezonefinder\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "e60c78b0-3490-4cd7-aa60-819f820d75ef",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python [conda env:bioacoustics]",
   "language": "python",
   "name": "conda-env-bioacoustics-py"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.9.6"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
