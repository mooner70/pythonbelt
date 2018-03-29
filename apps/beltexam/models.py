# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
import re
from  datetime import *
import bcrypt
email_regex = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
password_regex = re.compile('^(?=\S{6,20}$)(?=.*?\d)(?=.*?[a-z])(?=.*?[A-Z])(?=.*?[^A-Za-z\s0-9])')
class RegManager(models.Manager):
    def basic_validator(self, postData):
        errors = {}
        if len(postData["name"]) < 3:
            errors["name"] = "Name should be more than 3 characters"
        if len(postData["username"]) < 3:
            errors["username"] = "Username should be more than 3 characters"
        if len(postData["password"]) < 8:     
            errors["password"] = "Password should be more thatn 8 characters"
        if postData["password"] != postData["confirm"]:
            errors["confirm"] = "Password confirmation does not match"
        if len(postData["hiredate"]) < 1:
            errors["hiredate"] = "Hire date field cannot be empty"
        if postData["hiredate"] > datetime.now().strftime("%Y-%m-%d"):
            errors["hiredate"] = "Hire date can not be in the future"   
        return errors

        # if len(postData["email"]) < 1:
        #     errors["email"] = "Email field cannot be empty"
        # elif not email_regex.match(postData["email"]):  
        #     errors["email"] = "Invalid email address"
        # count = User.objects.filter(email=postData["email"]).count()
        # if count > 0:
        #     errors["email"] = "Email already exists"


    def login_validator(self, postData):
        errors = {}
        if len(postData["username"]) < 3:
            errors["username"] = "Username should be more than 3 characters"
        if len(postData["password"]) < 8:
            errors["password"] = "Password must be longer than 8 characters"
        check = User.objects.filter(username=postData["username"])
        if len(check) == 0:
            errors["password"] = "You must enter a password"
            return errors
        if not bcrypt.checkpw(postData["password"].encode(), check[0].password.encode()):
            errors["password"] = "Password doesn't match"
        return errors


        # if len(postData["email"]) < 1:
        #     errors["email"] = "Email field cannot be empty"
        # elif not email_regex.match(postData["email"]):  
        #     errors["email"] = "Invalid email address"


    def add_validator(self, postData):
        errors = {}
        if len(postData["items"]) < 3:
            errors["items"] = "Item/Product field must contain more than 3 characters"
        if len(postData["items"]) < 0:
            errors["items"] = "You must provide an Item/Product"
        return errors

class User(models.Model):
    name = models.CharField(max_length=255)
    username = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    hiredate = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = RegManager()

class Item(models.Model):
    items = models.CharField(max_length=255)
    date_added = models.DateField(null=True)
    addedby = models.CharField(max_length=255)
    users = models.ForeignKey(User, related_name = "products")
    wish_list_itmes = models.ManyToManyField(User, related_name = "users")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = RegManager()