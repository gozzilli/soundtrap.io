# soundtrap.io 

## Public-facing Website

### Requirements

* Python (with pip to install dependencies)
* PostgreSQL server.

To develop this website locally, install python and pip. 

You may want to use a virtual environment, which keeps a separate copy of all 
the python packages required by the project:

    virtualenv venv
    
or if you use Canopy python (backported from Python 3):

    venv venv
    
where the latter ``venv`` is the destination folder.  

Then install all requirements with:
    
    pip install -r requirements.txt

The file ``requirements.txt`` can be found in the root of this repository.

On the server, you might need to some extra special things to get Pillow (image 
library) working:

    # apt-get install libtiff5-dev libjpeg8-dev zlib1g-dev libfreetype6-dev \
    	liblcms2-dev libwebp-dev tcl8.6-dev tk8.6-dev python-tk \
    	python-dev python-setuptools
    
    # pip install -I Pillow ## re-installs if already installed
    
Assuming an ubuntu server.  

### Development

Once all dependencies are satisfied, sync the database with:

    ./manage.py migrate

and then run the development server with:

    ./manage.py runserver

The project can also be imported into Eclipse as a PyDev project.

### Live demo

The pre-production live demo can be found at http://soundtrap.io/_staging/

