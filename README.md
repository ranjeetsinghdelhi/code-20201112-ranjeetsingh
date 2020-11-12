# BMI Analytics Challange

BMI analytics tool help you to analyse BMI Data.
You can download a release version for windows by clicking on [release](https://github.com/ranjeetsinghdelhi/code-20201112-ranjeetsingh/releases) link.

### Tech

BMI Analytics tool uses few open source projects to work properly:

* [python3](https://www.python.org/) - Interpreter
* [Pandas](https://pandas.pydata.org/) - pandas is a fast, powerful, flexible and easy to use open source data analysis and   manipulation tool, built on top of the Python programming language.
* [unittest](https://docs.python.org/3/library/unittest.html) - Python builtin package supports test automation.


### Installation

BMI Analytics tool requires [python](https://www.python.org/) v3+ to run.

Install the dependencies and start the server.

```sh
$ git clone https://github.com/ranjeetsinghdelhi/code-20201112-ranjeetsingh.git
$ cd code-20201112-ranjeetsingh
$ python setup.py install
```

build dependencies

```sh
$ python setup.py build
```

install dependencies

```sh
$ python setup.py install
```

test script

```sh
$ python setup.py test
```

To run this script

```sh
$ python bmi_calculator.py
```

### Docker
bmi_calculator is very easy to install and deploy in a Docker container.

```sh
$ docker pull ranjeetsinghara/code-20201112-ranjeetsingh
$ docker run --rm ranjeetsinghara/code-20201112-ranjeetsingh:latest
```
This will create the code-20201112-ranjeetsingh image and pull in the necessary dependencies. 
and will produce test result in console

License
----

MIT
