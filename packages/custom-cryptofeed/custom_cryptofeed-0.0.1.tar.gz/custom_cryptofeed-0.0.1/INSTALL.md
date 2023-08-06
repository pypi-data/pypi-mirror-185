# custom_cryptofeed installation
 
The custom_cryptofeed library is intended for use by Python developers.

Several ways to get/use custom_cryptofeed:

* Pip - `pip install custom_cryptofeed`
* Git - `git clone https://github.com/bmoscon/custom_cryptofeed`
* Zipped source code - Download [github.com/bmoscon/custom_cryptofeed/archive/master.zip](https://github.com/bmoscon/custom_cryptofeed/archive/master.zip)

## Installation with Pip

The safe way to install and upgrade the custom_cryptofeed library:

    pip install --user --upgrade custom_cryptofeed

custom_cryptofeed supports many backends as Redis, ZeroMQ, RabbitMQ, MongoDB, PostgreSQL, Google Cloud and many others.
custom_cryptofeed is usually used with a subset of the available backends, and installing the dependencies of all backends is not required. 
Thus, to minimize the number of dependencies, the backend dependencies are optional, but easy to install.

See the file [`setup.py`](https://github.com/bmoscon/custom_cryptofeed/blob/master/setup.py#L60)
for the exhaustive list of these *extra* dependencies.

* Install all optional dependencies  
  To install custom_cryptofeed along with all optional dependencies in one bundle:

        pip install --user --upgrade custom_cryptofeed[all]

* Arctic backend  
  To install custom_cryptofeed along with [Arctic](https://github.com/man-group/arctic/) in one bundle:

         pip install --user --upgrade custom_cryptofeed[arctic]

* Google Cloud Pub / Sub backend

         pip install --user --upgrade custom_cryptofeed[gcp_pubsub]

* Kafka backend

         pip install --user --upgrade custom_cryptofeed[kafka]

* MongoDB backend

         pip install --user --upgrade custom_cryptofeed[mongo]

* PostgreSQL backend

         pip install --user --upgrade custom_cryptofeed[postgres]

* RabbitMQ backend

         pip install --user --upgrade custom_cryptofeed[rabbit]

* Redis backend

          pip install --user --upgrade custom_cryptofeed[redis]

* ZeroMQ backend

         pip install --user --upgrade custom_cryptofeed[zmq]

If you have a problem with the installation/hacking of custom_cryptofeed, you are welcome to:
* open a new issue: https://github.com/bmoscon/custom_cryptofeed/issues/
* join us on Slack: [custom_cryptofeed-dev.slack.com](https://join.slack.com/t/custom_cryptofeed-dev/shared_invite/enQtNjY4ODIwODA1MzQ3LTIzMzY3Y2YxMGVhNmQ4YzFhYTc3ODU1MjQ5MDdmY2QyZjdhMGU5ZDFhZDlmMmYzOTUzOTdkYTZiOGUwNGIzYTk)
* or on GitHub Discussion: https://github.com/bmoscon/custom_cryptofeed/discussions

Your Pull Requests are also welcome, even for minor changes.
