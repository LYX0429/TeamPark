from django.db import models

# Create your models here.


class Project(models.Model):
    project_name = models.CharField(max_length=50)
    project_desc = models.CharField(max_length=200)
    create_date = models.DateTimeField(blank=True)
    update_date = models.DateTimeField(blank=True)

    def __str__(self):
        return self.project_name


class Product(models.Model):
    product_name = models.CharField(max_length=50)
    product_desc = models.CharField(max_length=200)
    create_date = models.DateTimeField(blank=True)
    update_date = models.DateTimeField(blank=True)

    def __str__(self):
        return self.product_name


class Server(models.Model):
    project = models.ManyToManyField(Project)
    product = models.ManyToManyField(Product)
    server_name = models.CharField(max_length=50)
    ilo_ip = models.GenericIPAddressField(blank=True, null=True)
    server_desc = models.CharField(max_length=200)
    server_type = models.CharField(max_length=50)
    server_vendor = models.CharField(max_length=50)
    create_date = models.DateTimeField(blank=True)
    update_date = models.DateTimeField(blank=True)

    def __str__(self):
        return self.server_name


class Network(models.Model):
    server = models.ForeignKey(Server, on_delete=models.CASCADE)
    network_name = models.CharField(max_length=50)
    network_desc = models.CharField(max_length=200)
    vlan = models.CharField(max_length=50)
    bond = models.CharField(max_length=50)
    ethnet = models.CharField(max_length=50)
    bridge_name = models.CharField(max_length=50)
    ipv4 = models.GenericIPAddressField()
    ipv4_prefix = models.IntegerField()
    ipv4_gw = models.GenericIPAddressField()
    ipv6 = models.GenericIPAddressField()
    ipv6_prefix = models.IntegerField()
    ipv6_gw = models.GenericIPAddressField()
    create_date = models.DateTimeField(blank=True)
    update_date = models.DateTimeField(blank=True)

    def __str__(self):
        return self.network_name


class UserInfo(models.Model):
    server = models.ForeignKey(Server, on_delete=models.CASCADE)
    user_name = models.CharField(max_length=50)
    password = models.CharField(max_length=50)
    user_desc = models.CharField(max_length=200)
    create_date = models.DateTimeField(blank=True)
    update_date = models.DateTimeField(blank=True)

    def __str__(self):
        return self.user_name
