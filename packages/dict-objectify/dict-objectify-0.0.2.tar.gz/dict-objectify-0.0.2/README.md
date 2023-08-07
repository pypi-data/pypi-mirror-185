# Dict Objectify [![PyPI](https://img.shields.io/pypi/pyversions/dict-objectify.svg?style=plastic)](https://github.com/reljicd/dict-objectify)

## Introduction

A lot of python libraries that parse XML, JSON, CSV and other structured and 
semistructured data usually return dictionary representations of these object.
If parsed document is hierarchical in nature, return dictionaries are nested.
Working with a tree of nested dictionaries is certainly possible and easy to do in Python, 
but it is error prone, tedious and not developer friendly.

Additional problem is the type conversion of strings from original documents into
proper python types. Parsing libraries are usually strongly opinionated in this regard,
or tedious and verbose to configure.

Dict Objectify (DO) allows specification of python classes hierarchy that are backed by
dictionaries. 
Specification is done similar to ORM frameworks, by declaratively specifying dictionary keys as fields,
Every field is defined as either nested (DO) class for nested dictionaries 
or one of the provided type classes for values of the type: int, float, text, bool, array, datetime or enum.

Mapping between dictionaries and these objects works both ways.

This allows easy parsing of hierarchical documents into python object hierarchy,
doing pre processing on dict values, doing any kind of processing on that hierarchy
and then transforming root objects back into dictionaries for eventual dumping into same document formats. 

## Installation

To install with pip, run: `pip install dict-objectify`

To install Python Fire from source, first clone the repository and then run:
`python setup.py install`

## Basic Usage

```python
class NestedModel(Base):
    text_field = Text(nullable=False)
    text_field_nullable = Text()


class RootModel(Base):
    base_field = FieldBase()
    text_field = Text(tag='_text', primary=True)
    integer_field = Integer()
    datetime_field = Datetime()
    float_field = Float()
    bool_field = Bool()
    string_array_field = Array(str, nullable=False)
    nested_array_field = Array(NestedTestModel, nullable=False)
    enum_field = EnumTag(['a', 'b', 'c'], nullable=False)
    nested_field = NestedModel(nullable=False)
    
    @property
    def derived_field(self):
        return self.nested_field.text_field[:5]
    
example_dict = {
    '_text': 'lorem ipsum',
    'integer_field': '5',
    'string_array_field': ['lorem', 'ipsum'],
    'nested_array_field': [{'text_field': 'lorem ipsum'}, 
                           {'text_field': 'lorem ipsum'}],
    'nested_field': {'text_field': 'lorem ipsum'}
}

example_obj = RootModel(example_dict)

assert example_obj.text_field == example_dict['_text']
assert example_obj.nested_field.text_field == example_dict['nested_field']['text_field']
assert example_obj.derived_field == example_dict['nested_field']['text_field'][:5]
assert example_obj.integer_field == int(example_dict['integer_field'])
```

## Usage
### Object initialization
It can be done either by passing dict to constructor, or kwargs:
```python
example_obj = RootModel(example_dict)
alt_example_obj = RootModel(integer_field=5, text_field='lorem ipsum')
```

### Field types
* **Integer**
* **Float**
* **Text**
* **Bool**
* **Datetime** (**datetime_format**: Specification of datetime format)
* **EnumField** (**enumeration**: A list of allowed values. 
**strict**: If True, no other values will be allowed. If False, values not in enumeration will only raise a warning.)
* **Array** (**model**: Type of elements. Could be builtin python type or one of the Base types)

### Field parameters
* **tag** (default=None) - Needs to be specified as dict key if dict key and attribute names differ
* **primary** (default=False) - Marks field for hashing
* **nullable** (default=True) - Needs to be specified if field is not nullable

### Hashing
Hashing uses fields marked with **primary**.
If no fields are marked with **primary** all fields are hashed.


## Prerequisites for tests

\[Optional\] Install virtual environment:

```bash
$ python -m virtualenv env
```

\[Optional\] Activate virtual environment:

On macOS and Linux:
```bash
$ source env/bin/activate
```

On Windows:
```bash
$ .\env\Scripts\activate
```

Install dependencies:
```bash
$ pip install -r requirements.txt
```

## How to run tests

### Default
Running tests:
```bash
$ python -m pytest tests
```

### Docker

It is also possible to run tests using Docker:

Build the Docker image:
```bash
$ docker build -t reljicd/dict-objectify -f docker/Dockerfile .
```

Run the Docker container:
```bash
$ docker run --rm reljicd/dict-objectify -m pytest tests
```

### Docker helper script

It is possible to run all of the above with helper script:

```bash
$> chmod +x scripts/run_docker.sh
$> scripts/run_docker.sh -m pytest tests
```

## License

Licensed under the
[Apache 2.0](https://github.com/google/python-fire/blob/master/LICENSE) License.