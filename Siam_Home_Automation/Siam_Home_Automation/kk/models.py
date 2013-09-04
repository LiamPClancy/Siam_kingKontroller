# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#     * Rearrange models' order
#     * Make sure each model has one field with primary_key=True
# Feel free to rename the models, but don't rename db_table values or field names.
#
# Also note: You'll have to insert the output of 'django-admin.py sqlcustom [appname]'
# into your database.
from __future__ import unicode_literals

from django.db import models

class Areas(models.Model):
    id = models.IntegerField(primary_key=True, db_column='Id') # Field name made lowercase.
    displayname = models.CharField(max_length=255L, db_column='DisplayName') # Field name made lowercase.
    class Meta:
        db_table = 'areas'

class Areasrooms(models.Model):
    id = models.IntegerField(primary_key=True, db_column='Id') # Field name made lowercase.
    areaid = models.ForeignKey(Areas, db_column='AreaId') # Field name made lowercase.
    roomid = models.ForeignKey('Rooms', db_column='RoomId') # Field name made lowercase.
    class Meta:
        db_table = 'areasrooms'

class AuthGroup(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=80L, unique=True)
    class Meta:
        db_table = 'auth_group'

class AuthGroupPermissions(models.Model):
    id = models.IntegerField(primary_key=True)
    group = models.ForeignKey(AuthGroup)
    permission = models.ForeignKey('AuthPermission')
    class Meta:
        db_table = 'auth_group_permissions'

class AuthPermission(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=50L)
    content_type = models.ForeignKey('DjangoContentType')
    codename = models.CharField(max_length=100L)
    class Meta:
        db_table = 'auth_permission'

class AuthUser(models.Model):
    id = models.IntegerField(primary_key=True)
    password = models.CharField(max_length=128L)
    last_login = models.DateTimeField()
    is_superuser = models.IntegerField()
    username = models.CharField(max_length=30L, unique=True)
    first_name = models.CharField(max_length=30L)
    last_name = models.CharField(max_length=30L)
    email = models.CharField(max_length=75L)
    is_staff = models.IntegerField()
    is_active = models.IntegerField()
    date_joined = models.DateTimeField()
    class Meta:
        db_table = 'auth_user'

class AuthUserGroups(models.Model):
    id = models.IntegerField(primary_key=True)
    user = models.ForeignKey(AuthUser)
    group = models.ForeignKey(AuthGroup)
    class Meta:
        db_table = 'auth_user_groups'

class AuthUserUserPermissions(models.Model):
    id = models.IntegerField(primary_key=True)
    user = models.ForeignKey(AuthUser)
    permission = models.ForeignKey(AuthPermission)
    class Meta:
        db_table = 'auth_user_user_permissions'

class Authority(models.Model):
    id = models.IntegerField(primary_key=True, db_column='Id') # Field name made lowercase.
    displayname = models.CharField(max_length=255L, db_column='DisplayName') # Field name made lowercase.
    class Meta:
        db_table = 'authority'

class Authoritygroupareas(models.Model):
    id = models.IntegerField(primary_key=True, db_column='Id') # Field name made lowercase.
    authoritygroupid = models.ForeignKey('Authoritygroups', db_column='AuthorityGroupId') # Field name made lowercase.
    areaid = models.ForeignKey(Areas, db_column='AreaId') # Field name made lowercase.
    class Meta:
        db_table = 'authoritygroupareas'

class Authoritygroupcontrollers(models.Model):
    id = models.IntegerField(primary_key=True, db_column='Id') # Field name made lowercase.
    authoritygroupid = models.ForeignKey('Authoritygroups', db_column='AuthorityGroupId') # Field name made lowercase.
    controllerid = models.ForeignKey('Controllers', db_column='ControllerId') # Field name made lowercase.
    class Meta:
        db_table = 'authoritygroupcontrollers'

class Authoritygroupdeviceproperty(models.Model):
    id = models.IntegerField(primary_key=True, db_column='Id') # Field name made lowercase.
    authoritygroupid = models.ForeignKey('Authoritygroups', db_column='AuthoritygroupId') # Field name made lowercase.
    devicepropertyid = models.ForeignKey('Deviceproperties', db_column='DevicePropertyId') # Field name made lowercase.
    class Meta:
        db_table = 'authoritygroupdeviceproperty'

class Authoritygroupdevices(models.Model):
    id = models.IntegerField(primary_key=True, db_column='Id') # Field name made lowercase.
    authoritygroupid = models.ForeignKey('Authoritygroups', db_column='AuthorityGroupId') # Field name made lowercase.
    deviceid = models.ForeignKey('Devices', db_column='DeviceId') # Field name made lowercase.
    class Meta:
        db_table = 'authoritygroupdevices'

class Authoritygrouprooms(models.Model):
    id = models.IntegerField(primary_key=True, db_column='Id') # Field name made lowercase.
    authoritygroupid = models.ForeignKey('Authoritygroups', db_column='AuthorityGroupId') # Field name made lowercase.
    roomid = models.ForeignKey('Rooms', db_column='RoomId') # Field name made lowercase.
    class Meta:
        db_table = 'authoritygrouprooms'

class Authoritygroups(models.Model):
    id = models.IntegerField(primary_key=True, db_column='Id') # Field name made lowercase.
    authorityid = models.ForeignKey(Authority, db_column='AuthorityId') # Field name made lowercase.
    groupid = models.ForeignKey('Groups', db_column='GroupId') # Field name made lowercase.
    class Meta:
        db_table = 'authoritygroups'

class Commandscripts(models.Model):
    id = models.IntegerField(primary_key=True, db_column='Id') # Field name made lowercase.
    displayname = models.CharField(max_length=255L, db_column='DisplayName') # Field name made lowercase.
    scriptname = models.CharField(max_length=500L, db_column='ScriptName') # Field name made lowercase.
    class Meta:
        db_table = 'commandscripts'

class Commandscriptscriptparameters(models.Model):
    id = models.IntegerField(primary_key=True, db_column='Id') # Field name made lowercase.
    commandscriptid = models.ForeignKey(Commandscripts, db_column='CommandScriptId') # Field name made lowercase.
    scriptparameterid = models.ForeignKey('Scriptparameters', db_column='ScriptParameterId') # Field name made lowercase.
    class Meta:
        db_table = 'commandscriptscriptparameters'

class Commandscriptscriptparametersvaluetypes(models.Model):
    id = models.IntegerField(primary_key=True, db_column='Id') # Field name made lowercase.
    commandscriptscriptparameterid = models.ForeignKey(Commandscriptscriptparameters, db_column='CommandScriptScriptParameterId') # Field name made lowercase.
    valuetypeid = models.ForeignKey('Valuetypes', db_column='ValueTypeId') # Field name made lowercase.
    class Meta:
        db_table = 'commandscriptscriptparametersvaluetypes'

class Configuration(models.Model):
    id = models.IntegerField(primary_key=True, db_column='Id') # Field name made lowercase.
    displayname = models.CharField(max_length=255L, db_column='DisplayName') # Field name made lowercase.
    value = models.CharField(max_length=255L, db_column='Value') # Field name made lowercase.
    attributename = models.CharField(max_length=255L, db_column='AttributeName') # Field name made lowercase.
    class Meta:
        db_table = 'configuration'

class Connectiontypes(models.Model):
    id = models.IntegerField(primary_key=True, db_column='Id') # Field name made lowercase.
    displayname = models.CharField(max_length=255L, db_column='DisplayName') # Field name made lowercase.
    class Meta:
        db_table = 'connectiontypes'

class Controllerdevices(models.Model):
    id = models.IntegerField(primary_key=True, db_column='Id') # Field name made lowercase.
    controllerid = models.ForeignKey('Controllers', db_column='ControllerId') # Field name made lowercase.
    deviceid = models.ForeignKey('Devices', db_column='DeviceId') # Field name made lowercase.
    class Meta:
        db_table = 'controllerdevices'

class Controllermessagingprotocols(models.Model):
    id = models.IntegerField(primary_key=True, db_column='Id') # Field name made lowercase.
    messagingprotocolid = models.ForeignKey('Messagingprotocols', db_column='MessagingProtocolId') # Field name made lowercase.
    controllerid = models.ForeignKey('Controllers', db_column='ControllerId') # Field name made lowercase.
    class Meta:
        db_table = 'controllermessagingprotocols'

class Controllers(models.Model):
    id = models.IntegerField(primary_key=True, db_column='Id') # Field name made lowercase.
    displayname = models.CharField(max_length=255L, db_column='DisplayName') # Field name made lowercase.
    class Meta:
        db_table = 'controllers'

class Controllerscontrollertypes(models.Model):
    id = models.IntegerField(primary_key=True, db_column='Id') # Field name made lowercase.
    controllerid = models.ForeignKey(Controllers, db_column='ControllerId') # Field name made lowercase.
    controllertypeid = models.ForeignKey('Controllertypes', db_column='ControllerTypeId') # Field name made lowercase.
    class Meta:
        db_table = 'controllerscontrollertypes'

class Controllertypes(models.Model):
    id = models.IntegerField(primary_key=True, db_column='Id') # Field name made lowercase.
    displayname = models.CharField(max_length=255L, db_column='DisplayName') # Field name made lowercase.
    class Meta:
        db_table = 'controllertypes'

class Deviceconnection(models.Model):
    id = models.IntegerField(primary_key=True, db_column='Id') # Field name made lowercase.
    connectiontypeid = models.ForeignKey(Connectiontypes, db_column='ConnectionTypeId') # Field name made lowercase.
    deviceid = models.ForeignKey('Devices', db_column='DeviceId') # Field name made lowercase.
    connectionidentifier = models.TextField(db_column='ConnectionIdentifier') # Field name made lowercase.
    class Meta:
        db_table = 'deviceconnection'

class Deviceproperties(models.Model):
    id = models.IntegerField(primary_key=True, db_column='Id') # Field name made lowercase.
    deviceid = models.ForeignKey('Devices', db_column='DeviceId') # Field name made lowercase.
    propertyid = models.ForeignKey('Properties', db_column='PropertyId') # Field name made lowercase.
    class Meta:
        db_table = 'deviceproperties'

class Devicepropertiesstates(models.Model):
    id = models.IntegerField(primary_key=True, db_column='Id') # Field name made lowercase.
    propertystateid = models.ForeignKey('Propertiesstates', db_column='PropertyStateId') # Field name made lowercase.
    devicepropertyid = models.ForeignKey(Deviceproperties, db_column='DevicePropertyId') # Field name made lowercase.
    class Meta:
        db_table = 'devicepropertiesstates'

class Devicepropertycommandscripts(models.Model):
    id = models.IntegerField(primary_key=True, db_column='Id') # Field name made lowercase.
    devicepropertyid = models.ForeignKey(Deviceproperties, db_column='DevicePropertyId') # Field name made lowercase.
    commandscriptid = models.ForeignKey(Commandscripts, db_column='CommandScriptId') # Field name made lowercase.
    class Meta:
        db_table = 'devicepropertycommandscripts'

class Devicepropertymessagingprotocoll(models.Model):
    id = models.IntegerField(primary_key=True, db_column='Id') # Field name made lowercase.
    messagingprotocollid = models.ForeignKey('Messagingprotocols', db_column='MessagingProtocollId') # Field name made lowercase.
    devicepropertyid = models.ForeignKey(Deviceproperties, db_column='DevicePropertyId') # Field name made lowercase.
    class Meta:
        db_table = 'devicepropertymessagingprotocoll'

class Devicepropertystatesscriptparameters(models.Model):
    id = models.IntegerField(primary_key=True, db_column='Id') # Field name made lowercase.
    devicepropertystateid = models.ForeignKey(Devicepropertiesstates, db_column='DevicePropertyStateId') # Field name made lowercase.
    scriptparameterid = models.ForeignKey('Scriptparameters', db_column='ScriptParameterId') # Field name made lowercase.
    class Meta:
        db_table = 'devicepropertystatesscriptparameters'

class Devicepropertystatesvaluestypes(models.Model):
    id = models.IntegerField(primary_key=True, db_column='Id') # Field name made lowercase.
    devicepropertyid = models.ForeignKey(Deviceproperties, db_column='DevicePropertyId') # Field name made lowercase.
    valuetypeid = models.ForeignKey('Valuetypes', db_column='ValueTypeId') # Field name made lowercase.
    class Meta:
        db_table = 'devicepropertystatesvaluestypes'

class Devices(models.Model):
    id = models.IntegerField(primary_key=True, db_column='Id') # Field name made lowercase.
    displayname = models.CharField(max_length=255L, db_column='DisplayName') # Field name made lowercase.
    macaddress = models.CharField(max_length=500L, db_column='MacAddress') # Field name made lowercase.
    ipaddress = models.CharField(max_length=255L, db_column='IpAddress') # Field name made lowercase.
    class Meta:
        db_table = 'devices'

class DjangoContentType(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=100L)
    app_label = models.CharField(max_length=100L)
    model = models.CharField(max_length=100L)
    class Meta:
        db_table = 'django_content_type'

class DjangoSession(models.Model):
    session_key = models.CharField(max_length=40L, primary_key=True)
    session_data = models.TextField()
    expire_date = models.DateTimeField()
    class Meta:
        db_table = 'django_session'

class DjangoSite(models.Model):
    id = models.IntegerField(primary_key=True)
    domain = models.CharField(max_length=100L)
    name = models.CharField(max_length=50L)
    class Meta:
        db_table = 'django_site'

class Groups(models.Model):
    id = models.IntegerField(primary_key=True, db_column='Id') # Field name made lowercase.
    displayname = models.CharField(max_length=255L, db_column='DisplayName') # Field name made lowercase.
    class Meta:
        db_table = 'groups'

class Messagingprotocols(models.Model):
    id = models.IntegerField(primary_key=True, db_column='Id') # Field name made lowercase.
    displayname = models.CharField(max_length=255L, db_column='DisplayName') # Field name made lowercase.
    class Meta:
        db_table = 'messagingprotocols'

class Properties(models.Model):
    id = models.IntegerField(primary_key=True, db_column='Id') # Field name made lowercase.
    dispalyname = models.CharField(max_length=255L, db_column='DispalyName') # Field name made lowercase.
    description = models.CharField(max_length=500L, db_column='Description', blank=True) # Field name made lowercase.
    class Meta:
        db_table = 'properties'

class Propertiesstates(models.Model):
    id = models.IntegerField(primary_key=True, db_column='Id') # Field name made lowercase.
    propertyid = models.ForeignKey(Properties, db_column='PropertyId') # Field name made lowercase.
    stateid = models.ForeignKey('States', db_column='StateId') # Field name made lowercase.
    class Meta:
        db_table = 'propertiesstates'

class Rooms(models.Model):
    id = models.IntegerField(primary_key=True, db_column='Id') # Field name made lowercase.
    displayname = models.CharField(max_length=255L, db_column='DisplayName') # Field name made lowercase.
    class Meta:
        db_table = 'rooms'

class Roomsdevices(models.Model):
    id = models.IntegerField(primary_key=True, db_column='Id') # Field name made lowercase.
    deviceid = models.ForeignKey(Devices, db_column='DeviceId') # Field name made lowercase.
    roomid = models.ForeignKey(Rooms, db_column='RoomId') # Field name made lowercase.
    class Meta:
        db_table = 'roomsdevices'

class Sceneactivationrules(models.Model):
    id = models.IntegerField(primary_key=True, db_column='Id') # Field name made lowercase.
    scenesid = models.ForeignKey('Scenes', db_column='ScenesId') # Field name made lowercase.
    activetimestart = models.DateTimeField(db_column='ActiveTimeStart') # Field name made lowercase.
    activetimeend = models.DateTimeField(db_column='ActiveTimeEnd') # Field name made lowercase.
    activedays = models.IntegerField(db_column='ActiveDays') # Field name made lowercase.
    activationtime = models.DateTimeField(db_column='ActivationTime') # Field name made lowercase.
    class Meta:
        db_table = 'sceneactivationrules'

class Scenedevicepropertystate(models.Model):
    id = models.IntegerField(primary_key=True, db_column='Id') # Field name made lowercase.
    scenesid = models.ForeignKey('Scenes', db_column='ScenesId') # Field name made lowercase.
    devicepropertystateid = models.ForeignKey(Devicepropertiesstates, db_column='DevicePropertyStateId') # Field name made lowercase.
    class Meta:
        db_table = 'scenedevicepropertystate'

class Sceneprofiles(models.Model):
    id = models.IntegerField(primary_key=True, db_column='Id') # Field name made lowercase.
    scenesid = models.ForeignKey('Scenes', db_column='ScenesId') # Field name made lowercase.
    activetimestart = models.DateTimeField(db_column='ActiveTimeStart') # Field name made lowercase.
    activetimeend = models.DateTimeField(db_column='ActiveTimeEnd') # Field name made lowercase.
    activedays = models.IntegerField(db_column='ActiveDays') # Field name made lowercase.
    starttime = models.DateTimeField(db_column='StartTime') # Field name made lowercase.
    endtime = models.DateTimeField(null=True, db_column='EndTime', blank=True) # Field name made lowercase.
    class Meta:
        db_table = 'sceneprofiles'

class Scenes(models.Model):
    id = models.IntegerField(primary_key=True, db_column='Id') # Field name made lowercase.
    displayname = models.IntegerField(db_column='DisplayName') # Field name made lowercase.
    class Meta:
        db_table = 'scenes'

class Scriptparameters(models.Model):
    id = models.IntegerField(primary_key=True, db_column='Id') # Field name made lowercase.
    displayname = models.CharField(max_length=255L, db_column='DisplayName') # Field name made lowercase.
    value = models.CharField(max_length=500L, db_column='Value') # Field name made lowercase.
    description = models.CharField(max_length=500L, db_column='Description') # Field name made lowercase.
    class Meta:
        db_table = 'scriptparameters'

class States(models.Model):
    id = models.IntegerField(primary_key=True, db_column='Id') # Field name made lowercase.
    displayname = models.CharField(max_length=255L, db_column='DisplayName') # Field name made lowercase.
    description = models.CharField(max_length=500L, db_column='Description', blank=True) # Field name made lowercase.
    value = models.CharField(max_length=500L, db_column='Value') # Field name made lowercase.
    class Meta:
        db_table = 'states'

class Users(models.Model):
    id = models.IntegerField(primary_key=True, db_column='Id') # Field name made lowercase.
    username = models.CharField(max_length=255L, db_column='UserName') # Field name made lowercase.
    firstname = models.CharField(max_length=255L, db_column='FirstName') # Field name made lowercase.
    lastname = models.CharField(max_length=255L, db_column='LastName') # Field name made lowercase.
    email = models.CharField(max_length=500L, db_column='Email') # Field name made lowercase.
    pass_field = models.CharField(max_length=255L, db_column='Pass') # Field name made lowercase. Field renamed because it was a Python reserved word.
    secretquestion = models.CharField(max_length=500L, db_column='SecretQuestion', blank=True) # Field name made lowercase.
    answer = models.CharField(max_length=500L, db_column='Answer', blank=True) # Field name made lowercase.
    class Meta:
        db_table = 'users'

class Usersgroups(models.Model):
    id = models.IntegerField(primary_key=True, db_column='Id') # Field name made lowercase.
    userid = models.ForeignKey(Users, db_column='UserId') # Field name made lowercase.
    groupid = models.ForeignKey(Groups, db_column='GroupId') # Field name made lowercase.
    class Meta:
        db_table = 'usersgroups'

class Valuetypes(models.Model):
    id = models.IntegerField(primary_key=True, db_column='Id') # Field name made lowercase.
    displayname = models.CharField(max_length=255L, db_column='DisplayName') # Field name made lowercase.
    class Meta:
        db_table = 'valuetypes'

class Versions(models.Model):
    id = models.IntegerField(primary_key=True, db_column='Id') # Field name made lowercase.
    displayname = models.CharField(max_length=255L, db_column='DisplayName') # Field name made lowercase.
    module = models.CharField(max_length=255L, db_column='Module') # Field name made lowercase.
    version = models.CharField(max_length=255L, db_column='Version') # Field name made lowercase.
    class Meta:
        db_table = 'versions'

