=======
Yee CLI
=======
.. image:: https://brands.home-assistant.io/_/yeelight/logo.png

.. image:: https://img.shields.io/pypi/v/yee-cli.svg
        :target: https://pypi.python.org/pypi/yee-cli

.. image:: https://github.com/adamwojt/yee-cli/workflows/ci/badge.svg?branch=master&event=push
        :target: https://github.com/adamwojt/yee-cli/actions

.. image:: https://img.shields.io/badge/%20imports-isort-%231674b1?style=flat&labelColor=ef8336
        :target: https://timothycrosley.github.io/isort/

.. image:: https://img.shields.io/badge/code%20style-black-000000.svg
        :target: https://github.com/psf/black


Simple Yeelight Room control CLI written in Python.

Installation
------------

.. code-block:: text

    pip install yee-cli
    

Config
------

* Location: ``~/.yee_rooms``
* Format: ``JSON``
* Example:

.. code-block:: json

    {
       "office":[
          "192.168.1.1",
          "192.168.1.2"
       ],
       "bedroom":[
          "192.168.1.3",
          "192.168.1.4"
       ]
    }

* Config path can be also passed with ``-c`` flag or ``YEE_ROOM_CONFIG`` env variable
* To find bulb IPs use tools like ``nmap``, ``putty`` or check on your `YeeLight app <https://play.google.com/store/apps/details?id=com.yeelight.cherry&hl=en&gl=US>`_

Usage
-----
``yee [-c --config] [ROOM_NAME*] COMMAND [ARGS]...```

*\*Use room names from config*

**Example Usage:**

.. code-block:: text

    yee bedroom on
    yee office dim 10
    yee color_list
    yee office color indianred
    ... romance on !

**Commands:**

.. code-block:: text

    color         Set lights to given color.
    color_list    Available color list
    dim           Dim lights to level (1-100).
    off           Turn lights off.
    on            Turn lights on.
    random_color  Switch to random color.
    toggle        Toggle lights.


Troubleshooting
---------------

Connection Issues (make sure):
    * IP addresses of bulbs in config are correct.
    * LAN Control is ON (https://www.yeelight.com/faqs/lan_control).
    * You are connected to same WIFI network as your bulbs.
Other:
    * For more debug ideas visit https://github.com/skorokithakis/python-yeelight

Credits
-------

* Wouldn't be possible without `skorokithakis/python-yeelight <https://github.com/skorokithakis/python-yeelight>`_.
* Uses `webcolors <https://pypi.org/project/webcolors/>`_
* Uses `click <https://click.palletsprojects.com/en/7.x/>`_
* Created with Cookiecutter_ and the `johanvergeer/cookiecutter-poetry`_ project template.

After writing almost all I realised that author of `python-yeelight <https://github.com/skorokithakis/python-yeelight>`_ also wrote CLI. Check it out - it has different API / config and more features >>> `yeecli <https://github.com/skorokithakis/yeecli>`_

.. _Cookiecutter: https://github.com/audreyr/cookiecutter
.. _`johanvergeer/cookiecutter-poetry`: https://github.com/johanvergeer/cookiecutter-poetry
