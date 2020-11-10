from django.shortcuts import render


import random
# Create your views here.
def generate_token(length=10):
    return ''.join(random.SystemRandom().choice([chr(i) for i in range(97,123)]+[str(j) for j in range(10)]) for _ in range(length))
