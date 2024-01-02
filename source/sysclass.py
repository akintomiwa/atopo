from abc import ABC, ABCMeta, abstractmethod
from pydantic import BaseModel, Field
from dataclasses import dataclass
from enum import Enum, auto
from random import random
import string
import logging

logger = logging.getLogger(__name__)

class Country(BaseModel):
    capital: str = Field(description="capital of the country")
    name: str = Field(description="name of the country")

class ThematicAnalysis(BaseModel):
    username: str = Field(description="user's username")
    theme1: str = Field(description="Most common theme in the text")
    theme1kw: str = Field(description="Key words relating to the theme in Theme1")
    theme2: str = Field(description="Second most common theme in the text")
    theme2kw: str = Field(description="Key words relating to the theme in Theme2")
    theme3: str = Field(description="Second most common theme in the text")
    theme3kw: str = Field(description="Key words relating to the theme in Theme3")

class Corpus(ABC):
    
    @abstractmethod
    def preprocess_posts(self) -> None:
        pass

    @abstractmethod
    def generate_id(self, length: int = 8) -> None:
        pass


class XCorpus(Corpus):
    """
    Container object for retreived X posts.

    """

    def __init__(self, username) -> None:
        self.id = self.generate_id()
        self.username = username
        self.tweets = {}
        self.processed_tweets = {}
        logging.info(f"\n XCorpus Initialised. Id: {self.username}")
    
    def generate_id(self, length: int = 80):
        return "".join(random.choices(string.ascii_uppercase, k = length))
        
    def preprocess_posts(self) -> None:
        pass



# @dataclass
# class UserPos:
#     archiveid: str
#     mostrecentdate: str = "" 
#     data: Corpus


class UserService:
    """
    Resposible for user authentication and session management.
    Logging """
    pass