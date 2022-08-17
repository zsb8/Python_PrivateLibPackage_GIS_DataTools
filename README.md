# data-tools-gis
Only for GIS private package
Enter the geographic coordinates, and then get which area this coordinate corresponds to from the Statistics Canada data package. Result is the area code.   

# How to install this private Python package through install original code from Github?
This test in Ubuntu, you need to get personal token from Github first because it forbit you use really password when you down load.
~~~
python3 -m pip install git+https://github.com/waybase-data-analytics/data-tools-gis.git@master
~~~
Then you can use it in Python environment because you install it already. 
![image](https://user-images.githubusercontent.com/75282285/158874454-473e362f-0ad8-43ff-9df4-f9b5719eb962.png)
![image](https://user-images.githubusercontent.com/75282285/158874491-a8969ee0-963b-4ee6-a4fa-dd8f45381626.png)
![image](https://user-images.githubusercontent.com/75282285/158874537-d0fc469d-fb42-447b-afc1-7d1c5e5c5982.png)



You also can instll it as a individual package. The number such as 1.3 will be changed because these code might be changed.
## Ubuntu 
~~~
pipenv install wb_data_tools_gis-1.3.tar.gz
~~~
![image](https://user-images.githubusercontent.com/75282285/158869675-f03d9a7a-bec1-4e05-b095-a2305403fb18.png)
![image](https://user-images.githubusercontent.com/75282285/158869695-940c5eb6-24db-40fa-9678-29e908637720.png)

# How to uninstall this lib?
~~~
pip uninstall wb_data_tools_gis
~~~
![image](https://user-images.githubusercontent.com/75282285/158869574-3b51b33c-8300-4825-915e-51967d415fd8.png)


# How to use the gis of this private package? -- Two ways.

## 1. Use default path in gis of this private package
You can not need to input the boundary_path because it will use the .shp which be place in the private package.
The folder is '/wbdt/shapfiles/Tour_Boundaries.shp'
In my case, the folder will be '/usr/local/lib/python3.8/dist-packages/wbdt_gis/shapefiles/Tour_Boundaries.shp'
Test code: 
~~~
from wbdt_gis import gis
import pandas as pd
mydf = pd.DataFrame({'my_point': [[-104.497882, 52.328702], [-79.246943, 42.985294]]})
print(mydf)
result_test = gis.point_areadata(mydf, "my_point")
print(result_test)
~~~
![image](https://user-images.githubusercontent.com/75282285/158871272-9cca3aaf-c315-4608-b9ec-94626af886fe.png)

## 2. You can input the boundary path.
You can run these commends to get the geocode with Statistics Canada 2016 Census Boundary files. 
You can input the boundary path, such as '/home/zsb/waybase_package/lcma000a16a_e.shp'.
~~~
from wbdt_gis import gis
import pandas as pd
mydf = pd.read_csv('/home/zsb/waybase_package/gis.csv')
my_df_point_column = 'pointStr'
my_boundary_path = '/home/zsb/waybase_package/lcma000a16a_e.shp'
result_test = gis.point_areadata(mydf, my_df_point_column, my_boundary_path)
~~~
![image](https://user-images.githubusercontent.com/75282285/155016567-0651dc91-cac9-4e13-85aa-4e07ed806aad.png)


# Why it can't be installed in some Windows?  
Fiona was only readon you can't instll this wb_data_tools_gis private package.  
But it is OK to install in Mac and Linux env.
But you can install Fiona by this way, then you can install our private package.
## How to install Fiona in your Windows?
Use a new python env. 
~~~
 conda create -n my_env2
~~~
![image](https://user-images.githubusercontent.com/75282285/158899516-00614b67-fe5f-4220-9e00-686735676528.png)

Then active this env.
~~~
conda activate my_env2
~~~
![image](https://user-images.githubusercontent.com/75282285/158899606-1c5778fc-941e-464a-a758-6fbaf43a0a20.png)

Install pip tool.
~~~
conda install pip
~~~
Then install Fiona
~~~
 conda install fiona 
~~~
![image](https://user-images.githubusercontent.com/75282285/158899718-b827ee55-41b6-466d-aff3-b7eb3347ae6b.png)
![image](https://user-images.githubusercontent.com/75282285/158899730-b8e3b9e6-c8d6-4395-b6e9-ab0367eddb9f.png)
At last, you can install our private package.
~~~
pip install wb_data_tools_gis-1.3.tar.gz 
~~~
![image](https://user-images.githubusercontent.com/75282285/158899775-97d32a4d-37d5-4847-89d9-a233f32dd212.png)


#  the data from the Statistics Canada
![image](https://user-images.githubusercontent.com/75282285/185015538-432e5fa5-baba-4f93-b468-eca20c8b8700.png)





