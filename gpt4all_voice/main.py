from os import system
import speech_recognition as sr
from playsound import playsound
from gpt4all import GPT4All
import sys
import whisper
import warnings
import time
import os

wake_word='jarvis'
model = GPT4All("ggml-model-gpt4all-falcon-q4_0.bin")