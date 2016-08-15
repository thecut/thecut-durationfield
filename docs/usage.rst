=====
Usage
=====


Model field
~~~~~~~~~~~

.. code:: python

    from django.db import models
    from datetime import datetime
    from thecut.durationfield.models import RelativeDeltaField


    class MyModel(models.Model):
        duration = RelativeDeltaField(blank=True, null=True)


    my_instance = MyModel(duration='P7D')
    datetime(2014, 1, 1) + my_instance.duration  # datetime(2014, 1, 8, 0, 0)


Form field
~~~~~~~~~~

Two form fields are provided: ``RelativeDeltaChoiceField`` and
``RelativeDeltaTextInput``:

.. code:: python

    from django import forms
    from thecut.durationfield.models import RelativeDeltaChoiceField

    DURATIONS = [
        ('', 'Never'),
	('P7D', 'One week'),
	('P1M', 'One month'),
    ]

    class MyForm(forms.ModelForm):

        duration = RelativeDeltaChoiceField(choices=DURATIONS)


or, if you'd prefer to type in the (`ISO 8601`_ compliant) value manually:

.. code:: python

    from django import forms
    from thecut.durationfield.forms import RelativeDeltaTextInput

    class MyForm(forms.ModelForm):

        duration = RelativeDeltaTextInput()
