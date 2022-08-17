from setuptools import setup, find_packages
setup(
    name="wb_data_tools_gis",
    version='1.3',
    description="WayBase data tools created by data team",
    packages=['wbdt_gis','wbdt_gis/shapefiles'],
    author="Songbin Zhang",
    author_email="songbin.zhang@waybase.com",
    py_modules=['wbdt_gis'],
    include_package_data=True,
    package_data={'': ['shapefiles/*']},
    install_requires=[
       'pandas>=1.3.4',
       'fiona>=1.8.21',
       'geopandas>=0.10.2'
   ]
)
