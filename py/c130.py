import pandas as pd
import csv

df = pd.read_csv("preprocessed.csv")

del df["hyperlink"]
del df["temp_planet_date"]
del df["temp_mass"]
# del df["pl_letter"]
del df["pl_name"]
del df["pl_controv_flag"]
del df["sy_pnum"]
del df["sy_snum"]
del df["disc_year"]
del df["pl_orbper"]
del df["pl_orbpererr1"]
del df["pl_orbpererr2"]
del df["pl_orbperlim"]
del df["pl_orbsmax"]
del df["pl_orbsmaxerr1"]
del df["pl_orbsmaxerr2"]
del df["pl_orbsmaxlim"]
del df["pl_orbeccen"]
del df["pl_orbeccenerr1"]
del df["pl_orbeccenerr2"]
del df["pl_orbeccenlim"]
del df["pl_bmassj"]
del df["pl_bmassjerr1"]
del df["pl_bmassjerr2"]
del df["pl_bmassjlim"]
del df["pl_bmassprov"]
del df["pl_radj"]
del df["pl_radjerr1"]
del df["pl_radjerr2"]
del df["pl_radjlim"]
del df["pl_rade"]
del df["pl_radeerr1"]
del df["pl_radeerr2"]
del df["pl_radelim"]
del df["ttv_flag"]
# del df["pl_kepflag"]
# del df["pl_k2flag"]
# del df["pl_nnotes"]
del df["ra"]
del df["dec"]
del df["sy_dist"]
del df["sy_disterr1"]
del df["sy_disterr2"]
# del df["st_distlim"]
# del df["gaia_dist"]
# del df["gaia_disterr1"]
# del df["gaia_disterr2"]
# del df["gaia_distlim"]
del df["sy_gaiamag"]
del df["sy_gaiamagerr1"]
del df["sy_gaiamagerr2"]

# del df["st_optmag"]
# del df["st_optmagerr"]
# del df["st_optmaglim"]
# del df["st_optband"]
# del df["gaia_gmag"]
# del df["gaia_gmagerr"]
# del df["gaia_gmaglim"]
del df["st_tefferr1"]
del df["st_tefferr2"]
del df["st_tefflim"]
del df["st_masserr1"]
del df["st_masserr2"]
del df["st_masslim"]
del df["st_raderr1"]
del df["st_raderr2"]
del df["st_radlim"]
del df["st_logg"]
del df["st_loggerr1"]
del df["st_loggerr2"]
del df["st_logglim"]

del df["st_met"]
del df["st_meterr1"]
del df["st_meterr2"]
del df["st_metlim"]
del df["st_metratio"]

del df["pl_bmasse"]
del df["pl_bmasseerr1"]
del df["pl_bmasseerr2"]
del df["pl_bmasselim"]
del df["pl_insol"]
del df["pl_insolerr1"]
del df["pl_insolerr2"]
del df["pl_insollim"]
del df["pl_eqt"]
del df["pl_eqterr1"]
del df["pl_eqterr2"]
del df["pl_eqtlim"]
del df["st_spectype"]
				


del df["sy_kmag"]
del df["sy_kmagerr1"]
del df["sy_kmagerr2"]
del df["sy_vmag"]
del df["sy_vmagerr1"]
del df["sy_vmagerr2"]
# del df["rowupdate"]
del df["disc_facility"]

df = df.rename({
                'hostname': "solar_system_name", 
                'discoverymethod': "planet_discovery_method", 
                # 'pl_orbincl': "planet_orbital_inclination", 
                # 'pl_dens': "planet_density", 
                'rastr': "right_ascension", 
                'decstr': "declination", 
                "st_teff": "host_temperature", 
                'st_mass': "host_mass", 
                'st_rad': "host_radius"
            }, axis='columns')

df.to_csv('main.csv') 