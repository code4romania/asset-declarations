# Catalog politic  - Declaratii de avere [![GitHub contributors](https://img.shields.io/github/contributors/code4romania/catpol-declaratii.svg)](https://github.com/code4romania/catpol-declaratii/graphs/contributors) [![GitHub last commit](https://img.shields.io/github/last-commit/code4romania/catpol-declaratii.svg)](https://github.com/code4romania/catpol-declaratii/commits/master) [![License: MPL 2.0](https://img.shields.io/badge/license-MPL%202.0-brightgreen.svg)](https://opensource.org/licenses/MPL-2.0)

* MAKING PUBLIC INFORMATION TRULY PUBLIC 
* aggregate data on the higher echelons of elected officials
* data on activity while serving in each of the elected positions held
* details about criminal legal proceeding or past convictions
* data from asset declarations, including a net worth estimation

[See the project live](http://catalogpolitic.ro/)

Currently, in Romania, public information on elected officials is spread on a multitude of media, in a multitude of formats and requires a
priori knowledge of the sources where data resides, making it hard, if not impossible for a regular citizen to make sense of the data.

Furthermore, no comprehensive analysis of data on elected officials can be attempted, as most of it is not digitised, hence not in an open
format.

Catalog Politic is powered by the desire to centralise all public information on elected representatives and lower the information cost necessary for
citizens, making public information truly public. For this end we are digitising hundreds of thousands of asset declarations, scrapping dozens of official websites and manually collecting data where no
automation is possible.

Citizens, who want to find out more about their representatives, but lack the time, energy and know-how to find all the relevant data will gain
access to in-depth information in a friendly and easy to digest format.

The platform will help journalists, watchdogs and researchers identify and verify information on elected officials. The data provided will offer an
unprecedented starting point for in-depth analysis.

Catalog Politic - Declaratii de avere - aims to automate the process of parsing and extracting information from asset declarations of Romanian politicians and public figures, by providing a user friendly platform for volunteers to extract and map information to a fixed datamodel. The implementation is based on [Moonsheep](http://moonsheep.org/) framework.

[Built with](#built-with) | [Repos and projects](#repos-and-projects) | [Deployment](#deployment) | [Contributing](#contributing) | [Feedback](#feedback) | [License](#license) | [About Code4Ro](#about-code4ro)

## Built With 

[Django](https://www.djangoproject.com)   
[Moonsheep](http://moonsheep.org/)    
[PyBossa](https://pybossa.com/)    
[Bootstrap](https://bootstrap.build)

### Programming languages

Python 3.5+    
Please follow [the Python style guide](python_style_guide.md).

### Platforms

Political Catalogue - Asset Declaration is a web application.

### Frontend framework

[Django](https://www.djangoproject.com)

### Package managers

[Pip](https://pypi.org/project/pip/)

### Database technology & provider

This remains currently undecided.   

## Repos and projects

[Moonsheep on GitHub](https://github.com/themoonsheep)    
[PyBossa on GitHub](https://github.com/Scifabric/pybossa)

## Deployment 

Installation process
* Clone this repo: `git clone git@github.com:code4romania/catpol-declaratii.git`
* Open the directory where you have cloned the repo (`cd catpol-declaratii`)
* Create a virtual environment named "venv": `python3 -m venv venv`
* Activate the virtual environment: `source venv/bin/activate`
* `pip install -r requirements-dev.txt` 
* `export DJANGO_SETTINGS_MODULE=project_template.settings.dev`
* `python manage.py migrate`
* `python manage.py runserver`

## Contributing 

If you would like to contribute to one of our repositories, first identify the scale of what you would like to contribute. If it is small (grammar/spelling or a bug fix) feel free to start working on a fix. If you are submitting a feature or substantial code contribution, please discuss it with the team and ensure it follows the product roadmap. 

Our collaboration model [is described here](.github/WORKFLOW.md).

[Get familiar with some basic coding guidelines](https://github.com/Microsoft/vscode/wiki/Coding-Guidelines).


## Debugging

As you develop this app, you will surely add / remove / change database models (Django Models).   
In order for your local server to acknowledge these changes, you will need to migrate your new structure.   
During the development stage, while you're still testing things out and you don't care about the data in your local `sqlite` database, the following quick hack will update your models and clean the test database data:

```
rm  project_template/migrations/*
rm db.sqlite3
python manage.py makemigrations
python manage.py migrate --run-syncdb
```

## Feedback 

* Request a new feature on GitHub.
* Vote for popular feature requests.
* File a bug in GitHub Issues.
* Email us with other feedback contact@code4.ro

## License 

This project is licensed under the MPL 2.0 License - see the LICENSE.md file for details

## About Code4Ro

Started in 2016, Code for Romania is a civic tech NGO, official member of the Code for All network. We have a community of over 500 volunteers (developers, ux/ui, communications, data scientists, graphic designers, devops, it security and more) who work pro-bono for developing digital solutions to solve social problems. #techforsocialgood. If you want to learn more details about our projects [visit our site](https://www.code4.ro/en/) or if you want to talk to one of our staff members, please e-mail us at contact@code4.ro.

Last, but not least, we rely on donations to ensure the infrastructure, logistics and management of our community that is widely spread accross 11 timezones, coding for social change to make Romania and the world a better place. If you want to support us, [you can do it here](https://code4.ro/en/donate/).
