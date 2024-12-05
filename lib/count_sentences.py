#!/usr/bin/env python3
import re

class MyString:
  def __init__(self, value=''):
    self._value = value

  @property
  def value(self):
    return self._value

  @value.setter
  def value(self, val):
    if type(val) != str:
      print("The value must be a string.")
    self._value = val

  def is_sentence(self):
    return self._value.endswith('.')

  def is_question(self):
    return self._value.endswith('?')

  def is_exclamation(self):
    return self._value.endswith('!')

  def count_sentences(self):
    result = re.split(r'[?.!]', self._value)
    cleaned_list = [item for item in result if item]
    return len(cleaned_list)
  pass

