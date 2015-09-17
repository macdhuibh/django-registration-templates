# django-registration-templates

## Background

This packages is purely for convenience. It is based on the following blog post and bitbucket repo:

		https://devdoodles.wordpress.com/2009/02/16/user-authentication-with-django-registration/
		https://bitbucket.org/devdoodles/registration_templates/src

Both are fantastic resources. django-registration-templates adds a missing `activation-complete` template and `{% csrf_token %}` to all the forms.

The template seem to work fine with both `django-registration` and `django-registration-redux`.  Please file an issue or pull request if you have any problems.

## Usage

First clone the repo:

		git clone https://github.com/macdhuibh/django-registration-templates.git

Then move the registration directory to your templates directory:

		cd django-registration-templates
		mv registration path/to/your/templates/

`base.html` and `index.html` are also included but most likely, you'll already have those present in your templates directory.
