from abc import ABC, abstractmethod
from sklearn.base import BaseEstimator, TransformerMixin
import re

# Abstract Base Class for Text Preprocessors
class TextPreprocessorBase(ABC, BaseEstimator, TransformerMixin):
    @abstractmethod
    def preprocess_text(self, text: str) -> str:
        pass

    def fit(self, X, y=None):
        return self

    def transform(self, X, y=None):
        return [self.preprocess_text(text) for text in X]

# Concrete Text Preprocessor
class TextPreprocessor(TextPreprocessorBase):
    def to_lowercase(self, text: str) -> str:
        return text.lower()

    def remove_special_chars(self, text: str) -> str:
        special_chars_pattern = re.compile(r'[^\w\s]|_|[àèìòùñ°ª]', flags=re.UNICODE)
        return re.sub(special_chars_pattern, "", text)

    def remove_single_char(self, text: str) -> str:
        single_char_pattern = re.compile(r'\b[A-Za-z]\b')
        return re.sub(single_char_pattern, "", text)

    def remove_spaces(self, text: str) -> str:
        pattern = re.compile(r'(\s)+')
        return pattern.sub(' ', text).strip()

    def preprocess_text(self, text: str) -> str:
        text = self.remove_special_chars(text)
        text = self.remove_single_char(text)
        text = self.to_lowercase(text)
        text = self.remove_spaces(text)
        return text