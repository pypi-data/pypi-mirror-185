|travis_pic| |codecov_pic|

==============
Word to Number (Es)
==============
This is a Python module to convert number words (eg. veintiuno) to numeric digits (21). It works for positive numbers upto the range of 999,999,999,999 (i.e. billions).

++++++++++++
Installation
++++++++++++
Please ensure that you have **updated pip** to the latest version before installing word2number_es.

You can install the module using Python Package Index using the below command.

.. code-block:: python

  pip install word2number_es

Make sure you install all requirements given in requirements.txt

.. code-block:: python

  pip install -r requirements.txt

+++++
Usage
+++++
First you have to import the module using the below code.
.. code-block:: python

    from word2number_es import w2n

Then you can use the **word_to_num** method to convert a number-word to numeric digits, as shown below.

.. code-block:: python

    >>> print(w2n.word_to_num('dos punto tres'))
    2.3

    >>> print(w2n.word_to_num('112'))
    112

    >>> print(w2n.word_to_num('punto cinco')) 
    0.5

    >>> print(w2n.word_to_num('dosmil veintitres')) 
    2023

    >>> print(w2n.word_to_num('millon millon'))
    Error: Redundant number! Please enter a valid number word (eg. two million twenty three thousand and forty nine)
    None

    >>> print(w2n.word_to_num('blah'))
    Error: No valid number words found! Please enter a valid number word (eg. two million twenty three thousand and forty nine)
    None

You can also use the **numwords_in_sentence** to convert all number words in a sentence to numeric digits, as shown below.

.. code-block:: python

    >>> print(w2n.numwords_in_sentence("el reloj me costo diez mil pesos"))
    el reloj me costo 10000 pesos

++++++++++++
Contributors
++++++++++++
- Ben Batorsky (`bpben <https://github.com/bpben>`__)
- Alex (`ledovsky <https://github.com/ledovsky>`__)
- Tal Yarkoni (`tyarkoni <https://github.com/tyarkoni>`__)
- ButteredGroove (`ButteredGroove <https://github.com/ButteredGroove>`__)
- TurqW (`TurqW <https://github.com/TurqW>`__)
