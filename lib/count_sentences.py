#!/usr/bin/env python3
import ipdb

class MyString:
  def __init__(self, value=""):
    self.value = value


  @property
  def value(self):
    return self._value
  
  @value.setter
  def value(self, value):
    if type(value) == str:
      self._value = value
    else:
      print("The value must be a string.")

  def is_sentence(self):
    return self.value.endswith(".") and len(self.value) > 1
  
  def is_question(self):
    return self.value.endswith("?") and len(self.value) > 1
  
  def is_exclamation(self):
    return self.value.endswith("!") and len(self.value) > 1
  
  def count_sentences(self):
    question_version = self.value.replace("!", "?")
    question_version = question_version.replace(".", "?")

    array_version = question_version.split("?")
    count = 0
    # ipdb.set_trace()
    for string in array_version:
      if len(string) > 1:
        count += 1
    return count
  