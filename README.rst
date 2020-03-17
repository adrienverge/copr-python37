Python 3.7 for CentOS
=====================

This repository provides unofficial packages of Python 3.7 for CentOS 7 and 8,
while waiting for official packaging upstream.

Built packages are available at:

https://copr.fedorainfracloud.org/coprs/adrienverge/python37/

Install
-------

CentOS 7:

.. code:: shell

 sudo yum copr enable adrienverge/python37
 sudo yum install python37 python37-devel python37-pip

CentOS 8:

.. code:: shell

 sudo dnf copr enable adrienverge/python37
 sudo dnf install python37 python37-devel python37-pip
