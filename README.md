# django-registration-templates

## Updates for 1.5

This fork fixes the syntax so templates will work under Django 1.5.x

## Background

This packages is purely for convenience. It is based on the following blog post and bitbucket repo:

		https://devdoodles.wordpress.com/2009/02/16/user-authentication-with-django-registration/
		https://bitbucket.org/devdoodles/registration_templates/src

Both are fantastic resources. django-registration-templates adds a missing _activation-complete_ template and _{% csrf_token %}_ to all the forms.

## Usage

First clone the repo:

		git clone https://github.com/macdhuibh/django-registration-templates.git

Then move the registration directory to your templates directory:

		cd django-registration-templates
		mv registration path/to/your/templates/

base.html and index.html are also included but most likely, you'll already have those present in your templates directory.
