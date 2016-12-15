# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from __future__ import unicode_literals

from django.db import models


class Division(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    districtid = models.ForeignKey('District', models.DO_NOTHING, db_column='DistrictId')  # Field name made lowercase.
    name = models.CharField(db_column='Name', max_length=-1, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Division'


class Effectedarea(models.Model):
    incidentid = models.ForeignKey('IncidentReport', models.DO_NOTHING, db_column='IncidentId')  # Field name made lowercase.
    disasterid = models.ForeignKey('DisasterType', models.DO_NOTHING, db_column='DisasterId')  # Field name made lowercase.
    provinceid = models.ForeignKey('Province', models.DO_NOTHING, db_column='ProvinceId')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'EffectedArea'
        unique_together = (('incidentid', 'disasterid', 'provinceid'),)


class Gramaniladhari(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    divisionid = models.ForeignKey(Division, models.DO_NOTHING, db_column='DivisionId')  # Field name made lowercase.
    name = models.CharField(db_column='Name', max_length=-1, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'GramaNiladhari'


class Permissiontype(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    name = models.CharField(db_column='Name', max_length=-1, blank=True, null=True)  # Field name made lowercase.
    description = models.CharField(db_column='Description', max_length=-1, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'PermissionType'


class Province(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    name = models.CharField(db_column='Name', max_length=255, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Province'


class Sector(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    name = models.CharField(db_column='Name', max_length=-1, blank=True, null=True)  # Field name made lowercase.
    description = models.CharField(db_column='Description', max_length=-1, blank=True, null=True)  # Field name made lowercase.
    createddate = models.TimeField(db_column='CreatedDate', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Sector'


class User(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    roleid = models.ForeignKey('Userrole', models.DO_NOTHING, db_column='RoleId')  # Field name made lowercase.
    sectorid = models.ForeignKey(Sector, models.DO_NOTHING, db_column='SectorId')  # Field name made lowercase.
    firstname = models.CharField(db_column='FirstName', max_length=-1, blank=True, null=True)  # Field name made lowercase.
    lastname = models.CharField(db_column='LastName', max_length=-1, blank=True, null=True)  # Field name made lowercase.
    username = models.CharField(db_column='UserName', max_length=-1, blank=True, null=True)  # Field name made lowercase.
    password = models.CharField(db_column='Password', max_length=-1, blank=True, null=True)  # Field name made lowercase.
    email = models.CharField(db_column='Email', max_length=-1, blank=True, null=True)  # Field name made lowercase.
    contactno = models.CharField(db_column='ContactNo', max_length=-1, blank=True, null=True)  # Field name made lowercase.
    nic = models.CharField(db_column='NIC', max_length=-1, blank=True, null=True)  # Field name made lowercase.
    designationid = models.ForeignKey('Userdesignation', models.DO_NOTHING, db_column='DesignationId', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'User'


class Userdesignation(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    name = models.CharField(db_column='Name', max_length=-1, blank=True, null=True)  # Field name made lowercase.
    description = models.CharField(db_column='Description', max_length=-1, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'UserDesignation'


class Userrole(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    rolename = models.CharField(db_column='RoleName', max_length=-1, blank=True, null=True)  # Field name made lowercase.
    description = models.CharField(db_column='Description', max_length=-1, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'UserRole'


class AssestType(models.Model):
    name = models.CharField(max_length=-1, blank=True, null=True)
    description = models.CharField(max_length=-1, blank=True, null=True)
    geo_spatial_type = models.CharField(max_length=-1, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'assest_type'


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=80)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.BooleanField()
    username = models.CharField(unique=True, max_length=30)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.CharField(max_length=254)
    is_staff = models.BooleanField()
    is_active = models.BooleanField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class BdSessionKeys(models.Model):
    data_type = models.CharField(max_length=120, blank=True, null=True)
    key = models.BigIntegerField(blank=True, null=True)
    date = models.DateTimeField(blank=True, null=True)
    user = models.IntegerField(blank=True, null=True)
    bs_date = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'bd_session_keys'


class BhsComDiseases(models.Model):
    com_disease = models.CharField(max_length=255, blank=True, null=True)
    male = models.IntegerField(blank=True, null=True)
    female = models.IntegerField(blank=True, null=True)
    children = models.IntegerField(blank=True, null=True)
    elderly = models.IntegerField(blank=True, null=True)
    district = models.ForeignKey('District', models.DO_NOTHING, db_column='district', blank=True, null=True)
    created_user = models.IntegerField(blank=True, null=True)
    lmu = models.IntegerField(blank=True, null=True)
    created_date = models.DateTimeField(blank=True, null=True)
    lmd = models.DateTimeField(blank=True, null=True)
    session_id = models.BigIntegerField(blank=True, null=True)
    bs_date = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'bhs_com_diseases'


class BhsOi(models.Model):
    other_indicators = models.CharField(max_length=255, blank=True, null=True)
    male = models.IntegerField(blank=True, null=True)
    female = models.IntegerField(blank=True, null=True)
    children = models.IntegerField(blank=True, null=True)
    elderly = models.IntegerField(blank=True, null=True)
    district = models.ForeignKey('District', models.DO_NOTHING, db_column='district', blank=True, null=True)
    created_user = models.IntegerField(blank=True, null=True)
    lmu = models.IntegerField(blank=True, null=True)
    created_date = models.DateTimeField(blank=True, null=True)
    lmd = models.DateTimeField(blank=True, null=True)
    session_id = models.BigIntegerField(blank=True, null=True)
    unit_measure = models.CharField(max_length=255, blank=True, null=True)
    bs_date = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'bhs_oi'


class BhsPlc(models.Model):
    male = models.IntegerField(blank=True, null=True)
    female = models.IntegerField(blank=True, null=True)
    children = models.IntegerField(blank=True, null=True)
    elderly = models.IntegerField(blank=True, null=True)
    district = models.ForeignKey('District', models.DO_NOTHING, db_column='district', blank=True, null=True)
    created_user = models.IntegerField(blank=True, null=True)
    lmu = models.IntegerField(blank=True, null=True)
    created_date = models.DateTimeField(blank=True, null=True)
    lmd = models.DateTimeField(blank=True, null=True)
    session_id = models.BigIntegerField(blank=True, null=True)
    bs_date = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'bhs_plc'


class BhsVi(models.Model):
    vital_indicators = models.CharField(max_length=255, blank=True, null=True)
    male = models.IntegerField(blank=True, null=True)
    female = models.IntegerField(blank=True, null=True)
    children = models.IntegerField(blank=True, null=True)
    elderly = models.IntegerField(blank=True, null=True)
    district = models.ForeignKey('District', models.DO_NOTHING, db_column='district', blank=True, null=True)
    created_user = models.IntegerField(blank=True, null=True)
    lmu = models.IntegerField(blank=True, null=True)
    created_date = models.DateTimeField(blank=True, null=True)
    lmd = models.DateTimeField(blank=True, null=True)
    session_id = models.BigIntegerField(blank=True, null=True)
    bs_date = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'bhs_vi'


class BmfPubMf(models.Model):
    type_pub_mf = models.CharField(max_length=255, blank=True, null=True)
    number = models.IntegerField(blank=True, null=True)
    male = models.IntegerField(blank=True, null=True)
    female = models.IntegerField(blank=True, null=True)
    created_user = models.IntegerField(blank=True, null=True)
    lmu = models.IntegerField(blank=True, null=True)
    created_date = models.DateTimeField(blank=True, null=True)
    lmd = models.DateTimeField(blank=True, null=True)
    key = models.BigIntegerField(blank=True, null=True)
    district = models.ForeignKey('District', models.DO_NOTHING, db_column='district', blank=True, null=True)
    bs_date = models.CharField(max_length=20, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'bmf_pub_mf'


class BmfPvtMf(models.Model):
    type_pvt_mf = models.CharField(max_length=255, blank=True, null=True)
    number = models.IntegerField(blank=True, null=True)
    male = models.IntegerField(blank=True, null=True)
    female = models.IntegerField(blank=True, null=True)
    created_user = models.IntegerField(blank=True, null=True)
    lmu = models.IntegerField(blank=True, null=True)
    created_date = models.DateTimeField(blank=True, null=True)
    lmd = models.DateTimeField(blank=True, null=True)
    key = models.BigIntegerField(blank=True, null=True)
    district = models.ForeignKey('District', models.DO_NOTHING, db_column='district', blank=True, null=True)
    bs_date = models.CharField(max_length=20, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'bmf_pvt_mf'


class BucMarMequipment(models.Model):
    particulars = models.CharField(max_length=255, blank=True, null=True)
    teaching_hospital = models.FloatField(blank=True, null=True)
    provincial_general_hospital = models.FloatField(blank=True, null=True)
    district_general_hospital = models.FloatField(blank=True, null=True)
    district = models.ForeignKey('District', models.DO_NOTHING, db_column='district', blank=True, null=True)
    created_user = models.IntegerField(blank=True, null=True)
    lmu = models.IntegerField(blank=True, null=True)
    created_date = models.DateTimeField(blank=True, null=True)
    lmd = models.DateTimeField(blank=True, null=True)
    key = models.BigIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'buc_mar_mequipment'


class BucMarOassets(models.Model):
    particulars = models.CharField(max_length=255, blank=True, null=True)
    teaching_hospital = models.FloatField(blank=True, null=True)
    provincial_general_hospital = models.FloatField(blank=True, null=True)
    district_general_hospital = models.FloatField(blank=True, null=True)
    office = models.FloatField(blank=True, null=True)
    other = models.FloatField(blank=True, null=True)
    district = models.ForeignKey('District', models.DO_NOTHING, db_column='district', blank=True, null=True)
    created_user = models.IntegerField(blank=True, null=True)
    lmu = models.IntegerField(blank=True, null=True)
    created_date = models.DateTimeField(blank=True, null=True)
    lmd = models.DateTimeField(blank=True, null=True)
    key = models.BigIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'buc_mar_oassets'


class BucMarStructure(models.Model):
    particulars = models.CharField(max_length=255, blank=True, null=True)
    teaching_hospital = models.FloatField(blank=True, null=True)
    provincial_general_hospital = models.FloatField(blank=True, null=True)
    district_general_hospital = models.FloatField(blank=True, null=True)
    office = models.FloatField(blank=True, null=True)
    other = models.FloatField(blank=True, null=True)
    district = models.ForeignKey('District', models.DO_NOTHING, db_column='district', blank=True, null=True)
    created_user = models.IntegerField(blank=True, null=True)
    lmu = models.IntegerField(blank=True, null=True)
    created_date = models.DateTimeField(blank=True, null=True)
    lmd = models.DateTimeField(blank=True, null=True)
    key = models.BigIntegerField(blank=True, null=True)
    bs_date = models.CharField(max_length=12, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'buc_mar_structure'


class BucMarSupplies(models.Model):
    particulars = models.CharField(max_length=255, blank=True, null=True)
    teaching_hospital = models.FloatField(blank=True, null=True)
    provincial_general_hospital = models.FloatField(blank=True, null=True)
    district_general_hospital = models.FloatField(blank=True, null=True)
    district = models.ForeignKey('District', models.DO_NOTHING, db_column='district', blank=True, null=True)
    created_user = models.IntegerField(blank=True, null=True)
    lmu = models.IntegerField(blank=True, null=True)
    created_date = models.DateTimeField(blank=True, null=True)
    lmd = models.DateTimeField(blank=True, null=True)
    key = models.BigIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'buc_mar_supplies'


class BucMarcCrpm(models.Model):
    particulars = models.CharField(max_length=255, blank=True, null=True)
    teaching_hospital = models.FloatField(blank=True, null=True)
    provincial_general_hospital = models.FloatField(blank=True, null=True)
    district_general_hospital = models.FloatField(blank=True, null=True)
    office = models.FloatField(blank=True, null=True)
    other = models.FloatField(blank=True, null=True)
    district = models.ForeignKey('District', models.DO_NOTHING, db_column='district', blank=True, null=True)
    created_user = models.IntegerField(blank=True, null=True)
    lmu = models.IntegerField(blank=True, null=True)
    created_date = models.DateTimeField(blank=True, null=True)
    lmd = models.DateTimeField(blank=True, null=True)
    key = models.BigIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'buc_marc_crpm'


class BucMarcMequipment(models.Model):
    particulars = models.CharField(max_length=255, blank=True, null=True)
    teaching_hospital = models.FloatField(blank=True, null=True)
    provincial_general_hospital = models.FloatField(blank=True, null=True)
    district_general_hospital = models.FloatField(blank=True, null=True)
    district = models.ForeignKey('District', models.DO_NOTHING, db_column='district', blank=True, null=True)
    created_user = models.IntegerField(blank=True, null=True)
    lmu = models.IntegerField(blank=True, null=True)
    created_date = models.DateTimeField(blank=True, null=True)
    lmd = models.DateTimeField(blank=True, null=True)
    key = models.BigIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'buc_marc_mequipment'


class BucMarcOassets(models.Model):
    particulars = models.CharField(max_length=255, blank=True, null=True)
    teaching_hospital = models.FloatField(blank=True, null=True)
    provincial_general_hospital = models.FloatField(blank=True, null=True)
    district_general_hospital = models.FloatField(blank=True, null=True)
    office = models.FloatField(blank=True, null=True)
    other = models.FloatField(blank=True, null=True)
    district = models.ForeignKey('District', models.DO_NOTHING, db_column='district', blank=True, null=True)
    created_user = models.IntegerField(blank=True, null=True)
    lmu = models.IntegerField(blank=True, null=True)
    created_date = models.DateTimeField(blank=True, null=True)
    lmd = models.DateTimeField(blank=True, null=True)
    key = models.BigIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'buc_marc_oassets'


class BucMarcStructures(models.Model):
    particulars = models.CharField(max_length=255, blank=True, null=True)
    teaching_hospital = models.FloatField(blank=True, null=True)
    provincial_general_hospital = models.FloatField(blank=True, null=True)
    district_general_hospital = models.FloatField(blank=True, null=True)
    office = models.FloatField(blank=True, null=True)
    other = models.FloatField(blank=True, null=True)
    district = models.ForeignKey('District', models.DO_NOTHING, db_column='district', blank=True, null=True)
    created_user = models.IntegerField(blank=True, null=True)
    lmu = models.IntegerField(blank=True, null=True)
    created_date = models.DateTimeField(blank=True, null=True)
    lmd = models.DateTimeField(blank=True, null=True)
    key = models.BigIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'buc_marc_structures'


class BucOmarMequipment(models.Model):
    particulars = models.CharField(max_length=255, blank=True, null=True)
    base_hospital = models.FloatField(blank=True, null=True)
    divisional_hospital = models.FloatField(blank=True, null=True)
    rural_hospital = models.FloatField(blank=True, null=True)
    central_dispensary = models.FloatField(blank=True, null=True)
    pri_med_cunits = models.FloatField(blank=True, null=True)
    pri_health_ccenters = models.FloatField(blank=True, null=True)
    mat_child_health_clinics = models.FloatField(blank=True, null=True)
    district = models.ForeignKey('District', models.DO_NOTHING, db_column='district', blank=True, null=True)
    created_user = models.IntegerField(blank=True, null=True)
    lmu = models.IntegerField(blank=True, null=True)
    created_date = models.DateTimeField(blank=True, null=True)
    lmd = models.DateTimeField(blank=True, null=True)
    key = models.BigIntegerField(blank=True, null=True)
    bs_date = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'buc_omar_mequipment'


class BucOmarOassets(models.Model):
    particulars = models.CharField(max_length=255, blank=True, null=True)
    base_hospital = models.FloatField(blank=True, null=True)
    divisional_hospital = models.FloatField(blank=True, null=True)
    rural_hospital = models.FloatField(blank=True, null=True)
    central_dispensary = models.FloatField(blank=True, null=True)
    pri_med_cunits = models.FloatField(blank=True, null=True)
    pri_health_ccenters = models.FloatField(blank=True, null=True)
    mat_child_health_clinics = models.FloatField(blank=True, null=True)
    district = models.ForeignKey('District', models.DO_NOTHING, db_column='district', blank=True, null=True)
    created_user = models.IntegerField(blank=True, null=True)
    lmu = models.IntegerField(blank=True, null=True)
    created_date = models.DateTimeField(blank=True, null=True)
    lmd = models.DateTimeField(blank=True, null=True)
    key = models.BigIntegerField(blank=True, null=True)
    bs_date = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'buc_omar_oassets'


class BucOmarStructure(models.Model):
    particulars = models.CharField(max_length=255, blank=True, null=True)
    base_hospital = models.FloatField(blank=True, null=True)
    divisional_hospital = models.FloatField(blank=True, null=True)
    rural_hospital = models.FloatField(blank=True, null=True)
    central_dispensary = models.FloatField(blank=True, null=True)
    pri_med_cunits = models.FloatField(blank=True, null=True)
    pri_health_ccenters = models.FloatField(blank=True, null=True)
    mat_child_health_clinics = models.FloatField(blank=True, null=True)
    district = models.ForeignKey('District', models.DO_NOTHING, db_column='district', blank=True, null=True)
    created_user = models.IntegerField(blank=True, null=True)
    lmu = models.IntegerField(blank=True, null=True)
    created_date = models.DateTimeField(blank=True, null=True)
    lmd = models.DateTimeField(blank=True, null=True)
    key = models.BigIntegerField(blank=True, null=True)
    bs_date = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'buc_omar_structure'


class BucOmarSupplies(models.Model):
    particulars = models.CharField(max_length=255, blank=True, null=True)
    base_hospital = models.FloatField(blank=True, null=True)
    divisional_hospital = models.FloatField(blank=True, null=True)
    rural_hospital = models.FloatField(blank=True, null=True)
    central_dispensary = models.FloatField(blank=True, null=True)
    pri_med_cunits = models.FloatField(blank=True, null=True)
    pri_health_ccenters = models.FloatField(blank=True, null=True)
    mat_child_health_clinics = models.FloatField(blank=True, null=True)
    district = models.ForeignKey('District', models.DO_NOTHING, db_column='district', blank=True, null=True)
    created_user = models.IntegerField(blank=True, null=True)
    lmu = models.IntegerField(blank=True, null=True)
    created_date = models.DateTimeField(blank=True, null=True)
    lmd = models.DateTimeField(blank=True, null=True)
    key = models.BigIntegerField(blank=True, null=True)
    bs_date = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'buc_omar_supplies'


class BucOmarcCrpm(models.Model):
    particulars = models.CharField(max_length=255, blank=True, null=True)
    base_hospital = models.FloatField(blank=True, null=True)
    divisional_hospital = models.FloatField(blank=True, null=True)
    rural_hospital = models.FloatField(blank=True, null=True)
    central_dispensary = models.FloatField(blank=True, null=True)
    pri_med_cunits = models.FloatField(blank=True, null=True)
    pri_health_ccenters = models.FloatField(blank=True, null=True)
    mat_child_health_clinics = models.FloatField(blank=True, null=True)
    district = models.ForeignKey('District', models.DO_NOTHING, db_column='district', blank=True, null=True)
    created_user = models.IntegerField(blank=True, null=True)
    lmu = models.IntegerField(blank=True, null=True)
    created_date = models.DateTimeField(blank=True, null=True)
    lmd = models.DateTimeField(blank=True, null=True)
    key = models.BigIntegerField(blank=True, null=True)
    bs_date = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'buc_omarc_crpm'


class BucOmarcMequipment(models.Model):
    particulars = models.CharField(max_length=255, blank=True, null=True)
    base_hospital = models.FloatField(blank=True, null=True)
    divisional_hospital = models.FloatField(blank=True, null=True)
    rural_hospital = models.FloatField(blank=True, null=True)
    central_dispensary = models.FloatField(blank=True, null=True)
    pri_med_cunits = models.FloatField(blank=True, null=True)
    pri_health_ccenters = models.FloatField(blank=True, null=True)
    mat_child_health_clinics = models.FloatField(blank=True, null=True)
    district = models.ForeignKey('District', models.DO_NOTHING, db_column='district', blank=True, null=True)
    created_user = models.IntegerField(blank=True, null=True)
    lmu = models.IntegerField(blank=True, null=True)
    created_date = models.DateTimeField(blank=True, null=True)
    lmd = models.DateTimeField(blank=True, null=True)
    key = models.BigIntegerField(blank=True, null=True)
    bs_date = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'buc_omarc_mequipment'


class BucOmarcOassets(models.Model):
    particulars = models.CharField(max_length=255, blank=True, null=True)
    base_hospital = models.FloatField(blank=True, null=True)
    divisional_hospital = models.FloatField(blank=True, null=True)
    rural_hospital = models.FloatField(blank=True, null=True)
    central_dispensary = models.FloatField(blank=True, null=True)
    pri_med_cunits = models.FloatField(blank=True, null=True)
    pri_health_ccenters = models.FloatField(blank=True, null=True)
    mat_child_health_clinics = models.FloatField(blank=True, null=True)
    district = models.ForeignKey('District', models.DO_NOTHING, db_column='district', blank=True, null=True)
    created_user = models.IntegerField(blank=True, null=True)
    lmu = models.IntegerField(blank=True, null=True)
    created_date = models.DateTimeField(blank=True, null=True)
    lmd = models.DateTimeField(blank=True, null=True)
    key = models.BigIntegerField(blank=True, null=True)
    bs_date = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'buc_omarc_oassets'


class BucOmarcStructure(models.Model):
    particulars = models.CharField(max_length=255, blank=True, null=True)
    base_hospital = models.FloatField(blank=True, null=True)
    divisional_hospital = models.FloatField(blank=True, null=True)
    rural_hospital = models.FloatField(blank=True, null=True)
    central_dispensary = models.FloatField(blank=True, null=True)
    pri_med_cunits = models.FloatField(blank=True, null=True)
    pri_health_ccenters = models.FloatField(blank=True, null=True)
    mat_child_health_clinics = models.FloatField(blank=True, null=True)
    district = models.ForeignKey('District', models.DO_NOTHING, db_column='district', blank=True, null=True)
    created_user = models.IntegerField(blank=True, null=True)
    lmu = models.IntegerField(blank=True, null=True)
    created_date = models.DateTimeField(blank=True, null=True)
    lmd = models.DateTimeField(blank=True, null=True)
    key = models.BigIntegerField(blank=True, null=True)
    bs_date = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'buc_omarc_structure'


class DapBefOther(models.Model):
    pvt_clinics = models.CharField(max_length=255, blank=True, null=True)
    est_replacement_cost = models.FloatField(blank=True, null=True)
    est_repair_cost = models.FloatField(blank=True, null=True)
    total_damages = models.FloatField(blank=True, null=True)
    est_losses_y1 = models.FloatField(blank=True, null=True)
    est_losses_y2 = models.FloatField(blank=True, null=True)
    total_losses = models.FloatField(blank=True, null=True)
    district = models.ForeignKey('District', models.DO_NOTHING, db_column='district', blank=True, null=True)
    created_user = models.IntegerField(blank=True, null=True)
    lmu = models.IntegerField(blank=True, null=True)
    created_date = models.DateTimeField(blank=True, null=True)
    lmd = models.DateTimeField(blank=True, null=True)
    key = models.BigIntegerField(blank=True, null=True)
    incident = models.ForeignKey('IncidentReport', models.DO_NOTHING, db_column='incident', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'dap_bef_other'


class DapBefPc1(models.Model):
    pvt_clinics = models.CharField(max_length=255, blank=True, null=True)
    est_replacement_cost = models.FloatField(blank=True, null=True)
    est_repair_cost = models.FloatField(blank=True, null=True)
    total_damages = models.FloatField(blank=True, null=True)
    est_losses_y1 = models.FloatField(blank=True, null=True)
    est_losses_y2 = models.FloatField(blank=True, null=True)
    total_losses = models.FloatField(blank=True, null=True)
    district = models.ForeignKey('District', models.DO_NOTHING, db_column='district', blank=True, null=True)
    created_user = models.IntegerField(blank=True, null=True)
    lmu = models.IntegerField(blank=True, null=True)
    created_date = models.DateTimeField(blank=True, null=True)
    lmd = models.DateTimeField(blank=True, null=True)
    key = models.BigIntegerField(blank=True, null=True)
    incident = models.ForeignKey('IncidentReport', models.DO_NOTHING, db_column='incident', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'dap_bef_pc1'


class DapBefPcn(models.Model):
    pvt_clinics = models.CharField(max_length=255, blank=True, null=True)
    est_replacement_cost = models.FloatField(blank=True, null=True)
    est_repair_cost = models.FloatField(blank=True, null=True)
    total_damages = models.FloatField(blank=True, null=True)
    est_losses_y1 = models.FloatField(blank=True, null=True)
    est_losses_y2 = models.FloatField(blank=True, null=True)
    total_losses = models.FloatField(blank=True, null=True)
    district = models.ForeignKey('District', models.DO_NOTHING, db_column='district', blank=True, null=True)
    created_user = models.IntegerField(blank=True, null=True)
    lmu = models.IntegerField(blank=True, null=True)
    created_date = models.DateTimeField(blank=True, null=True)
    lmd = models.DateTimeField(blank=True, null=True)
    key = models.BigIntegerField(blank=True, null=True)
    incident = models.ForeignKey('IncidentReport', models.DO_NOTHING, db_column='incident', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'dap_bef_pcn'


class DapNapTmf(models.Model):
    id = models.AutoField()
    type_med_fac = models.CharField(max_length=255, blank=True, null=True)
    num_affected_fac = models.BigIntegerField(blank=True, null=True)
    male = models.BigIntegerField(blank=True, null=True)
    female = models.BigIntegerField(blank=True, null=True)
    district = models.ForeignKey('District', models.DO_NOTHING, db_column='district', blank=True, null=True)
    created_user = models.IntegerField(blank=True, null=True)
    lmu = models.IntegerField(blank=True, null=True)
    created_date = models.DateTimeField(blank=True, null=True)
    lmd = models.DateTimeField(blank=True, null=True)
    incident = models.ForeignKey('IncidentReport', models.DO_NOTHING, db_column='incident', blank=True, null=True)
    key = models.BigIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'dap_nap_tmf'


class DataEntry(models.Model):
    added_date = models.DateField(blank=True, null=True)
    table_id = models.BigIntegerField(blank=True, null=True)
    user_id = models.BigIntegerField(blank=True, null=True)
    district_id = models.BigIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'data_entry'


class DisasterType(models.Model):
    name = models.CharField(max_length=255, blank=True, null=True)
    description = models.CharField(max_length=500, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'disaster_type'


class District(models.Model):
    province = models.ForeignKey(Province, models.DO_NOTHING)
    name = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'district'


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.SmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class DmfDaMequipment(models.Model):
    asset = models.CharField(max_length=255, blank=True, null=True)
    base_hospital = models.FloatField(blank=True, null=True)
    divisional_hospital = models.FloatField(blank=True, null=True)
    rural_hospital = models.FloatField(blank=True, null=True)
    central_dispensary = models.FloatField(blank=True, null=True)
    pmcus = models.FloatField(blank=True, null=True)
    phccs = models.FloatField(blank=True, null=True)
    mchcs = models.FloatField(blank=True, null=True)
    total = models.FloatField(blank=True, null=True)
    district = models.ForeignKey(District, models.DO_NOTHING, db_column='district', blank=True, null=True)
    created_user = models.IntegerField(blank=True, null=True)
    lmu = models.IntegerField(blank=True, null=True)
    created_date = models.DateTimeField(blank=True, null=True)
    lmd = models.DateTimeField(blank=True, null=True)
    key = models.BigIntegerField(blank=True, null=True)
    incident = models.ForeignKey('IncidentReport', models.DO_NOTHING, db_column='incident', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'dmf_da_mequipment'


class DmfDaOassets(models.Model):
    asset = models.CharField(max_length=255, blank=True, null=True)
    base_hospital = models.FloatField(blank=True, null=True)
    divisional_hospital = models.FloatField(blank=True, null=True)
    rural_hospital = models.FloatField(blank=True, null=True)
    central_dispensary = models.FloatField(blank=True, null=True)
    pmcus = models.FloatField(blank=True, null=True)
    phccs = models.FloatField(blank=True, null=True)
    mchcs = models.FloatField(blank=True, null=True)
    total = models.FloatField(blank=True, null=True)
    district = models.ForeignKey(District, models.DO_NOTHING, db_column='district', blank=True, null=True)
    created_user = models.IntegerField(blank=True, null=True)
    lmu = models.IntegerField(blank=True, null=True)
    created_date = models.DateTimeField(blank=True, null=True)
    lmd = models.DateTimeField(blank=True, null=True)
    key = models.BigIntegerField(blank=True, null=True)
    incident = models.ForeignKey('IncidentReport', models.DO_NOTHING, db_column='incident', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'dmf_da_oassets'


class DmfDaStructure(models.Model):
    asset = models.CharField(max_length=255, blank=True, null=True)
    base_hospital = models.FloatField(blank=True, null=True)
    divisional_hospital = models.FloatField(blank=True, null=True)
    rural_hospital = models.FloatField(blank=True, null=True)
    central_dispensary = models.FloatField(blank=True, null=True)
    pmcus = models.FloatField(blank=True, null=True)
    phccs = models.FloatField(blank=True, null=True)
    mchcs = models.FloatField(blank=True, null=True)
    total = models.FloatField(blank=True, null=True)
    district = models.ForeignKey(District, models.DO_NOTHING, db_column='district', blank=True, null=True)
    created_user = models.IntegerField(blank=True, null=True)
    lmu = models.IntegerField(blank=True, null=True)
    created_date = models.DateTimeField(blank=True, null=True)
    lmd = models.DateTimeField(blank=True, null=True)
    key = models.BigIntegerField(blank=True, null=True)
    incident = models.ForeignKey('IncidentReport', models.DO_NOTHING, db_column='incident', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'dmf_da_structure'


class DmfDaSupplies(models.Model):
    asset = models.CharField(max_length=255, blank=True, null=True)
    base_hospital = models.FloatField(blank=True, null=True)
    divisional_hospital = models.FloatField(blank=True, null=True)
    rural_hospital = models.FloatField(blank=True, null=True)
    central_dispensary = models.FloatField(blank=True, null=True)
    pmcus = models.FloatField(blank=True, null=True)
    phccs = models.FloatField(blank=True, null=True)
    mchcs = models.FloatField(blank=True, null=True)
    total = models.FloatField(blank=True, null=True)
    district = models.ForeignKey(District, models.DO_NOTHING, db_column='district', blank=True, null=True)
    created_user = models.IntegerField(blank=True, null=True)
    lmu = models.IntegerField(blank=True, null=True)
    created_date = models.DateTimeField(blank=True, null=True)
    lmd = models.DateTimeField(blank=True, null=True)
    key = models.BigIntegerField(blank=True, null=True)
    incident = models.ForeignKey('IncidentReport', models.DO_NOTHING, db_column='incident', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'dmf_da_supplies'


class DmfDfaNum(models.Model):
    num_des_facilities = models.CharField(max_length=255, blank=True, null=True)
    base_hospital = models.BigIntegerField(blank=True, null=True)
    divisional_hospital = models.IntegerField(blank=True, null=True)
    rural_hospital = models.BigIntegerField(blank=True, null=True)
    central_dispensary = models.BigIntegerField(blank=True, null=True)
    pmcus = models.BigIntegerField(blank=True, null=True)
    phccs = models.BigIntegerField(blank=True, null=True)
    mchcs = models.BigIntegerField(blank=True, null=True)
    total = models.BigIntegerField(blank=True, null=True)
    district = models.ForeignKey(District, models.DO_NOTHING, db_column='district', blank=True, null=True)
    created_user = models.IntegerField(blank=True, null=True)
    lmu = models.IntegerField(blank=True, null=True)
    created_date = models.DateTimeField(blank=True, null=True)
    lmd = models.DateTimeField(blank=True, null=True)
    key = models.BigIntegerField(blank=True, null=True)
    incident = models.ForeignKey('IncidentReport', models.DO_NOTHING, db_column='incident', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'dmf_dfa_num'


class DmfDfaPaf(models.Model):
    num_patients_affected = models.CharField(max_length=255, blank=True, null=True)
    base_hospital = models.BigIntegerField(blank=True, null=True)
    divisional_hospital = models.IntegerField(blank=True, null=True)
    rural_hospital = models.BigIntegerField(blank=True, null=True)
    central_dispensary = models.BigIntegerField(blank=True, null=True)
    pmcus = models.BigIntegerField(blank=True, null=True)
    phccs = models.BigIntegerField(blank=True, null=True)
    mchcs = models.BigIntegerField(blank=True, null=True)
    total = models.BigIntegerField(blank=True, null=True)
    district = models.ForeignKey(District, models.DO_NOTHING, db_column='district', blank=True, null=True)
    created_user = models.IntegerField(blank=True, null=True)
    lmu = models.IntegerField(blank=True, null=True)
    created_date = models.DateTimeField(blank=True, null=True)
    lmd = models.DateTimeField(blank=True, null=True)
    key = models.BigIntegerField(blank=True, null=True)
    incident = models.ForeignKey('IncidentReport', models.DO_NOTHING, db_column='incident', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'dmf_dfa_paf'


class DmfLosCud(models.Model):
    type_of_losses = models.CharField(max_length=255, blank=True, null=True)
    base_hospital = models.FloatField(blank=True, null=True)
    divisional_hospital = models.FloatField(blank=True, null=True)
    rural_hospital = models.FloatField(blank=True, null=True)
    central_dispensary = models.FloatField(blank=True, null=True)
    pmcus = models.FloatField(blank=True, null=True)
    phccs = models.FloatField(blank=True, null=True)
    mchcs = models.FloatField(blank=True, null=True)
    total = models.FloatField(blank=True, null=True)
    district = models.ForeignKey(District, models.DO_NOTHING, db_column='district', blank=True, null=True)
    created_user = models.IntegerField(blank=True, null=True)
    lmu = models.IntegerField(blank=True, null=True)
    created_date = models.DateTimeField(blank=True, null=True)
    lmd = models.DateTimeField(blank=True, null=True)
    key = models.BigIntegerField(blank=True, null=True)
    incident = models.ForeignKey('IncidentReport', models.DO_NOTHING, db_column='incident', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'dmf_los_cud'


class DmfLosFi(models.Model):
    type_of_losses = models.CharField(max_length=255, blank=True, null=True)
    base_hospital = models.FloatField(blank=True, null=True)
    divisional_hospital = models.FloatField(blank=True, null=True)
    rural_hospital = models.FloatField(blank=True, null=True)
    central_dispensary = models.FloatField(blank=True, null=True)
    pmcus = models.FloatField(blank=True, null=True)
    phccs = models.FloatField(blank=True, null=True)
    mchcs = models.FloatField(blank=True, null=True)
    total = models.FloatField(blank=True, null=True)
    district = models.ForeignKey(District, models.DO_NOTHING, db_column='district', blank=True, null=True)
    created_user = models.IntegerField(blank=True, null=True)
    lmu = models.IntegerField(blank=True, null=True)
    created_date = models.DateTimeField(blank=True, null=True)
    lmd = models.DateTimeField(blank=True, null=True)
    key = models.BigIntegerField(blank=True, null=True)
    incident = models.ForeignKey('IncidentReport', models.DO_NOTHING, db_column='incident', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'dmf_los_fi'


class DmfLosHoc(models.Model):
    type_of_losses = models.CharField(max_length=255, blank=True, null=True)
    base_hospital = models.FloatField(blank=True, null=True)
    divisional_hospital = models.FloatField(blank=True, null=True)
    rural_hospital = models.FloatField(blank=True, null=True)
    central_dispensary = models.FloatField(blank=True, null=True)
    pmcus = models.FloatField(blank=True, null=True)
    phccs = models.FloatField(blank=True, null=True)
    mchcs = models.FloatField(blank=True, null=True)
    total = models.FloatField(blank=True, null=True)
    district = models.ForeignKey(District, models.DO_NOTHING, db_column='district', blank=True, null=True)
    created_user = models.IntegerField(blank=True, null=True)
    lmu = models.IntegerField(blank=True, null=True)
    created_date = models.DateTimeField(blank=True, null=True)
    lmd = models.DateTimeField(blank=True, null=True)
    key = models.BigIntegerField(blank=True, null=True)
    incident = models.ForeignKey('IncidentReport', models.DO_NOTHING, db_column='incident', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'dmf_los_hoc'


class DmfLosOue(models.Model):
    type_of_losses = models.CharField(max_length=255, blank=True, null=True)
    base_hospital = models.FloatField(blank=True, null=True)
    divisional_hospital = models.FloatField(blank=True, null=True)
    rural_hospital = models.FloatField(blank=True, null=True)
    central_dispensary = models.FloatField(blank=True, null=True)
    pmcus = models.FloatField(blank=True, null=True)
    phccs = models.FloatField(blank=True, null=True)
    mchcs = models.FloatField(blank=True, null=True)
    total = models.FloatField(blank=True, null=True)
    district = models.ForeignKey(District, models.DO_NOTHING, db_column='district', blank=True, null=True)
    created_user = models.IntegerField(blank=True, null=True)
    lmu = models.IntegerField(blank=True, null=True)
    created_date = models.DateTimeField(blank=True, null=True)
    lmd = models.DateTimeField(blank=True, null=True)
    key = models.BigIntegerField(blank=True, null=True)
    incident = models.ForeignKey('IncidentReport', models.DO_NOTHING, db_column='incident', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'dmf_los_oue'


class DmfPdaMequipment(models.Model):
    asset = models.CharField(max_length=255, blank=True, null=True)
    base_hospital = models.FloatField(blank=True, null=True)
    divisional_hospital = models.FloatField(blank=True, null=True)
    rural_hospital = models.FloatField(blank=True, null=True)
    central_dispensary = models.FloatField(blank=True, null=True)
    pmcus = models.FloatField(blank=True, null=True)
    phccs = models.FloatField(blank=True, null=True)
    mchcs = models.FloatField(blank=True, null=True)
    total = models.FloatField(blank=True, null=True)
    district = models.ForeignKey(District, models.DO_NOTHING, db_column='district', blank=True, null=True)
    created_user = models.IntegerField(blank=True, null=True)
    lmu = models.IntegerField(blank=True, null=True)
    created_date = models.DateTimeField(blank=True, null=True)
    lmd = models.DateTimeField(blank=True, null=True)
    key = models.BigIntegerField(blank=True, null=True)
    incident = models.ForeignKey('IncidentReport', models.DO_NOTHING, db_column='incident', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'dmf_pda_mequipment'


class DmfPdaOassets(models.Model):
    asset = models.CharField(max_length=255, blank=True, null=True)
    base_hospital = models.FloatField(blank=True, null=True)
    divisional_hospital = models.FloatField(blank=True, null=True)
    rural_hospital = models.FloatField(blank=True, null=True)
    central_dispensary = models.FloatField(blank=True, null=True)
    pmcus = models.FloatField(blank=True, null=True)
    phccs = models.FloatField(blank=True, null=True)
    mchcs = models.FloatField(blank=True, null=True)
    total = models.FloatField(blank=True, null=True)
    district = models.ForeignKey(District, models.DO_NOTHING, db_column='district', blank=True, null=True)
    created_user = models.IntegerField(blank=True, null=True)
    lmu = models.IntegerField(blank=True, null=True)
    created_date = models.DateTimeField(blank=True, null=True)
    lmd = models.DateTimeField(blank=True, null=True)
    key = models.BigIntegerField(blank=True, null=True)
    incident = models.ForeignKey('IncidentReport', models.DO_NOTHING, db_column='incident', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'dmf_pda_oassets'


class DmfPdaStructure(models.Model):
    asset = models.CharField(max_length=255, blank=True, null=True)
    base_hospital = models.FloatField(blank=True, null=True)
    divisional_hospital = models.FloatField(blank=True, null=True)
    rural_hospital = models.FloatField(blank=True, null=True)
    central_dispensary = models.FloatField(blank=True, null=True)
    pmcus = models.FloatField(blank=True, null=True)
    phccs = models.FloatField(blank=True, null=True)
    mchcs = models.FloatField(blank=True, null=True)
    total = models.FloatField(blank=True, null=True)
    district = models.ForeignKey(District, models.DO_NOTHING, db_column='district', blank=True, null=True)
    created_user = models.IntegerField(blank=True, null=True)
    lmu = models.IntegerField(blank=True, null=True)
    created_date = models.DateTimeField(blank=True, null=True)
    lmd = models.DateTimeField(blank=True, null=True)
    key = models.BigIntegerField(blank=True, null=True)
    incident = models.ForeignKey('IncidentReport', models.DO_NOTHING, db_column='incident', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'dmf_pda_structure'


class DmfPdfaNum(models.Model):
    num_pdamaged_facilities = models.CharField(max_length=255, blank=True, null=True)
    base_hospital = models.BigIntegerField(blank=True, null=True)
    divisional_hospital = models.BigIntegerField(blank=True, null=True)
    rural_hospital = models.BigIntegerField(blank=True, null=True)
    central_dispensary = models.BigIntegerField(blank=True, null=True)
    pmcus = models.BigIntegerField(blank=True, null=True)
    phccs = models.BigIntegerField(blank=True, null=True)
    mchcs = models.BigIntegerField(blank=True, null=True)
    total = models.BigIntegerField(blank=True, null=True)
    district = models.ForeignKey(District, models.DO_NOTHING, db_column='district', blank=True, null=True)
    created_user = models.IntegerField(blank=True, null=True)
    lmu = models.IntegerField(blank=True, null=True)
    created_date = models.DateTimeField(blank=True, null=True)
    lmd = models.DateTimeField(blank=True, null=True)
    key = models.BigIntegerField(blank=True, null=True)
    incident = models.ForeignKey('IncidentReport', models.DO_NOTHING, db_column='incident', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'dmf_pdfa_num'


class DmfPdfaPaf(models.Model):
    num_patients_affected = models.CharField(max_length=255, blank=True, null=True)
    base_hospital = models.BigIntegerField(blank=True, null=True)
    divisional_hospital = models.BigIntegerField(blank=True, null=True)
    rural_hospital = models.BigIntegerField(blank=True, null=True)
    central_dispensary = models.BigIntegerField(blank=True, null=True)
    pmcus = models.BigIntegerField(blank=True, null=True)
    phccs = models.BigIntegerField(blank=True, null=True)
    mchcs = models.BigIntegerField(blank=True, null=True)
    total = models.BigIntegerField(blank=True, null=True)
    district = models.ForeignKey(District, models.DO_NOTHING, db_column='district', blank=True, null=True)
    created_user = models.IntegerField(blank=True, null=True)
    lmu = models.IntegerField(blank=True, null=True)
    created_date = models.DateTimeField(blank=True, null=True)
    lmd = models.DateTimeField(blank=True, null=True)
    key = models.BigIntegerField(blank=True, null=True)
    incident = models.ForeignKey('IncidentReport', models.DO_NOTHING, db_column='incident', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'dmf_pdfa_paf'


class DmhDfNum(models.Model):
    num_des_facilities = models.CharField(max_length=255, blank=True, null=True)
    teaching_hospital = models.BigIntegerField(blank=True, null=True)
    provincial_general_hospital = models.BigIntegerField(blank=True, null=True)
    district_general_hospital = models.BigIntegerField(blank=True, null=True)
    office = models.BigIntegerField(blank=True, null=True)
    other = models.BigIntegerField(blank=True, null=True)
    total = models.BigIntegerField(blank=True, null=True)
    district = models.ForeignKey(District, models.DO_NOTHING, db_column='district', blank=True, null=True)
    created_user = models.IntegerField(blank=True, null=True)
    lmu = models.IntegerField(blank=True, null=True)
    created_date = models.DateTimeField(blank=True, null=True)
    lmd = models.DateTimeField(blank=True, null=True)
    key = models.BigIntegerField(blank=True, null=True)
    incident = models.ForeignKey('IncidentReport', models.DO_NOTHING, db_column='incident', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'dmh_df_num'


class DmhDfPaf(models.Model):
    num_patients_affected = models.CharField(max_length=255, blank=True, null=True)
    teaching_hospital = models.BigIntegerField(blank=True, null=True)
    provincial_general_hospital = models.BigIntegerField(blank=True, null=True)
    district_general_hospital = models.BigIntegerField(blank=True, null=True)
    office = models.BigIntegerField(blank=True, null=True)
    other = models.BigIntegerField(blank=True, null=True)
    total = models.BigIntegerField(blank=True, null=True)
    district = models.ForeignKey(District, models.DO_NOTHING, db_column='district', blank=True, null=True)
    created_user = models.IntegerField(blank=True, null=True)
    lmu = models.IntegerField(blank=True, null=True)
    created_date = models.DateTimeField(blank=True, null=True)
    lmd = models.DateTimeField(blank=True, null=True)
    key = models.BigIntegerField(blank=True, null=True)
    incident = models.ForeignKey('IncidentReport', models.DO_NOTHING, db_column='incident', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'dmh_df_paf'


class DmhLosCud(models.Model):
    type_of_losses = models.CharField(max_length=255, blank=True, null=True)
    teaching_hospital = models.FloatField(blank=True, null=True)
    provincial_general_hospital = models.FloatField(blank=True, null=True)
    district_general_hospital = models.FloatField(blank=True, null=True)
    office = models.FloatField(blank=True, null=True)
    other = models.FloatField(blank=True, null=True)
    total = models.FloatField(blank=True, null=True)
    district = models.ForeignKey(District, models.DO_NOTHING, db_column='district', blank=True, null=True)
    created_user = models.IntegerField(blank=True, null=True)
    lmu = models.IntegerField(blank=True, null=True)
    created_date = models.DateTimeField(blank=True, null=True)
    lmd = models.DateTimeField(blank=True, null=True)
    key = models.BigIntegerField(blank=True, null=True)
    incident = models.ForeignKey('IncidentReport', models.DO_NOTHING, db_column='incident', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'dmh_los_cud'


class DmhLosFi(models.Model):
    type_of_losses = models.CharField(max_length=255, blank=True, null=True)
    teaching_hospital = models.FloatField(blank=True, null=True)
    provincial_general_hospital = models.FloatField(blank=True, null=True)
    district_general_hospital = models.FloatField(blank=True, null=True)
    office = models.FloatField(blank=True, null=True)
    other = models.FloatField(blank=True, null=True)
    total = models.FloatField(blank=True, null=True)
    district = models.ForeignKey(District, models.DO_NOTHING, db_column='district', blank=True, null=True)
    created_user = models.IntegerField(blank=True, null=True)
    lmu = models.IntegerField(blank=True, null=True)
    created_date = models.DateTimeField(blank=True, null=True)
    lmd = models.DateTimeField(blank=True, null=True)
    key = models.BigIntegerField(blank=True, null=True)
    incident = models.ForeignKey('IncidentReport', models.DO_NOTHING, db_column='incident', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'dmh_los_fi'


class DmhLosHoc(models.Model):
    type_of_losses = models.CharField(max_length=255, blank=True, null=True)
    teaching_hospital = models.FloatField(blank=True, null=True)
    provincial_general_hospital = models.FloatField(blank=True, null=True)
    district_general_hospital = models.FloatField(blank=True, null=True)
    office = models.FloatField(blank=True, null=True)
    other = models.FloatField(blank=True, null=True)
    total = models.FloatField(blank=True, null=True)
    district = models.ForeignKey(District, models.DO_NOTHING, db_column='district', blank=True, null=True)
    created_user = models.IntegerField(blank=True, null=True)
    lmu = models.IntegerField(blank=True, null=True)
    created_date = models.DateTimeField(blank=True, null=True)
    lmd = models.DateTimeField(blank=True, null=True)
    key = models.BigIntegerField(blank=True, null=True)
    incident = models.ForeignKey('IncidentReport', models.DO_NOTHING, db_column='incident', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'dmh_los_hoc'


class DmhLosOue(models.Model):
    type_of_losses = models.CharField(max_length=255, blank=True, null=True)
    teaching_hospital = models.FloatField(blank=True, null=True)
    provincial_general_hospital = models.FloatField(blank=True, null=True)
    district_general_hospital = models.FloatField(blank=True, null=True)
    office = models.FloatField(blank=True, null=True)
    other = models.FloatField(blank=True, null=True)
    total = models.FloatField(blank=True, null=True)
    district = models.ForeignKey(District, models.DO_NOTHING, db_column='district', blank=True, null=True)
    created_user = models.IntegerField(blank=True, null=True)
    lmu = models.IntegerField(blank=True, null=True)
    created_date = models.DateTimeField(blank=True, null=True)
    lmd = models.DateTimeField(blank=True, null=True)
    key = models.BigIntegerField(blank=True, null=True)
    incident = models.ForeignKey('IncidentReport', models.DO_NOTHING, db_column='incident', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'dmh_los_oue'


class DmhNdatFacMequipment(models.Model):
    asset = models.CharField(max_length=255, blank=True, null=True)
    teaching_hospital = models.FloatField(blank=True, null=True)
    provincial_general_hospital = models.FloatField(blank=True, null=True)
    district_general_hospital = models.FloatField(blank=True, null=True)
    total = models.FloatField(blank=True, null=True)
    district = models.ForeignKey(District, models.DO_NOTHING, db_column='district', blank=True, null=True)
    created_user = models.IntegerField(blank=True, null=True)
    lmu = models.IntegerField(blank=True, null=True)
    created_date = models.DateTimeField(blank=True, null=True)
    lmd = models.DateTimeField(blank=True, null=True)
    key = models.BigIntegerField(blank=True, null=True)
    incident = models.ForeignKey('IncidentReport', models.DO_NOTHING, db_column='incident', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'dmh_ndat_fac_mequipment'


class DmhNdatFacOassets(models.Model):
    asset = models.CharField(max_length=255, blank=True, null=True)
    teaching_hospital = models.FloatField(blank=True, null=True)
    provincial_general_hospital = models.FloatField(blank=True, null=True)
    district_general_hospital = models.FloatField(blank=True, null=True)
    office = models.FloatField(blank=True, null=True)
    other = models.FloatField(blank=True, null=True)
    total = models.FloatField(blank=True, null=True)
    district = models.ForeignKey(District, models.DO_NOTHING, db_column='district', blank=True, null=True)
    created_user = models.IntegerField(blank=True, null=True)
    lmu = models.IntegerField(blank=True, null=True)
    created_date = models.DateTimeField(blank=True, null=True)
    lmd = models.DateTimeField(blank=True, null=True)
    key = models.BigIntegerField(blank=True, null=True)
    incident = models.ForeignKey('IncidentReport', models.DO_NOTHING, db_column='incident', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'dmh_ndat_fac_oassets'


class DmhNdatFacStructure(models.Model):
    asset = models.CharField(max_length=255, blank=True, null=True)
    teaching_hospital = models.FloatField(blank=True, null=True)
    provincial_general_hospital = models.FloatField(blank=True, null=True)
    district_general_hospital = models.FloatField(blank=True, null=True)
    office = models.FloatField(blank=True, null=True)
    other = models.FloatField(blank=True, null=True)
    total = models.FloatField(blank=True, null=True)
    district = models.ForeignKey(District, models.DO_NOTHING, db_column='district', blank=True, null=True)
    created_user = models.IntegerField(blank=True, null=True)
    lmu = models.IntegerField(blank=True, null=True)
    created_date = models.DateTimeField(blank=True, null=True)
    lmd = models.DateTimeField(blank=True, null=True)
    key = models.BigIntegerField(blank=True, null=True)
    incident = models.ForeignKey('IncidentReport', models.DO_NOTHING, db_column='incident', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'dmh_ndat_fac_structure'


class DmhNdatFacSupplies(models.Model):
    asset = models.CharField(max_length=255, blank=True, null=True)
    teaching_hospital = models.FloatField(blank=True, null=True)
    provincial_general_hospital = models.FloatField(blank=True, null=True)
    district_general_hospital = models.FloatField(blank=True, null=True)
    total = models.FloatField(blank=True, null=True)
    district = models.ForeignKey(District, models.DO_NOTHING, db_column='district', blank=True, null=True)
    created_user = models.IntegerField(blank=True, null=True)
    lmu = models.IntegerField(blank=True, null=True)
    created_date = models.DateTimeField(blank=True, null=True)
    lmd = models.DateTimeField(blank=True, null=True)
    key = models.BigIntegerField(blank=True, null=True)
    incident = models.ForeignKey('IncidentReport', models.DO_NOTHING, db_column='incident', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'dmh_ndat_fac_supplies'


class DmhPdfaMequipment(models.Model):
    asset = models.CharField(max_length=255, blank=True, null=True)
    teaching_hospital = models.FloatField(blank=True, null=True)
    provincial_general_hospital = models.FloatField(blank=True, null=True)
    district_general_hospital = models.FloatField(blank=True, null=True)
    total = models.FloatField(blank=True, null=True)
    district = models.ForeignKey(District, models.DO_NOTHING, db_column='district', blank=True, null=True)
    created_user = models.IntegerField(blank=True, null=True)
    lmu = models.IntegerField(blank=True, null=True)
    created_date = models.DateTimeField(blank=True, null=True)
    lmd = models.DateTimeField(blank=True, null=True)
    key = models.BigIntegerField(blank=True, null=True)
    incident = models.ForeignKey('IncidentReport', models.DO_NOTHING, db_column='incident', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'dmh_pdfa_mequipment'


class DmhPdfaNum(models.Model):
    num_des_facilities = models.CharField(max_length=255, blank=True, null=True)
    teaching_hospital = models.BigIntegerField(blank=True, null=True)
    provincial_general_hospital = models.BigIntegerField(blank=True, null=True)
    district_general_hospital = models.BigIntegerField(blank=True, null=True)
    office = models.BigIntegerField(blank=True, null=True)
    other = models.BigIntegerField(blank=True, null=True)
    total = models.BigIntegerField(blank=True, null=True)
    district = models.ForeignKey(District, models.DO_NOTHING, db_column='district', blank=True, null=True)
    created_user = models.IntegerField(blank=True, null=True)
    lmu = models.IntegerField(blank=True, null=True)
    created_date = models.DateTimeField(blank=True, null=True)
    lmd = models.DateTimeField(blank=True, null=True)
    key = models.BigIntegerField(blank=True, null=True)
    bs_date = models.CharField(max_length=255, blank=True, null=True)
    incident = models.ForeignKey('IncidentReport', models.DO_NOTHING, db_column='incident', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'dmh_pdfa_num'


class DmhPdfaOassets(models.Model):
    asset = models.CharField(max_length=255, blank=True, null=True)
    teaching_hospital = models.FloatField(blank=True, null=True)
    provincial_general_hospital = models.FloatField(blank=True, null=True)
    district_general_hospital = models.FloatField(blank=True, null=True)
    office = models.FloatField(blank=True, null=True)
    other = models.FloatField(blank=True, null=True)
    total = models.FloatField(blank=True, null=True)
    district = models.ForeignKey(District, models.DO_NOTHING, db_column='district', blank=True, null=True)
    created_user = models.IntegerField(blank=True, null=True)
    lmu = models.IntegerField(blank=True, null=True)
    created_date = models.DateTimeField(blank=True, null=True)
    lmd = models.DateTimeField(blank=True, null=True)
    key = models.BigIntegerField(blank=True, null=True)
    incident = models.ForeignKey('IncidentReport', models.DO_NOTHING, db_column='incident', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'dmh_pdfa_oassets'


class DmhPdfaPaf(models.Model):
    num_patients_affected = models.CharField(max_length=255, blank=True, null=True)
    teaching_hospital = models.BigIntegerField(blank=True, null=True)
    provincial_general_hospital = models.BigIntegerField(blank=True, null=True)
    district_general_hospital = models.BigIntegerField(blank=True, null=True)
    office = models.BigIntegerField(blank=True, null=True)
    other = models.BigIntegerField(blank=True, null=True)
    total = models.BigIntegerField(blank=True, null=True)
    district = models.ForeignKey(District, models.DO_NOTHING, db_column='district', blank=True, null=True)
    created_user = models.IntegerField(blank=True, null=True)
    lmu = models.IntegerField(blank=True, null=True)
    created_date = models.DateTimeField(blank=True, null=True)
    lmd = models.DateTimeField(blank=True, null=True)
    key = models.BigIntegerField(blank=True, null=True)
    bs_date = models.CharField(max_length=255, blank=True, null=True)
    incident = models.ForeignKey('IncidentReport', models.DO_NOTHING, db_column='incident', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'dmh_pdfa_paf'


class DmhPdfaStructure(models.Model):
    asset = models.CharField(max_length=255, blank=True, null=True)
    teaching_hospital = models.FloatField(blank=True, null=True)
    provincial_general_hospital = models.FloatField(blank=True, null=True)
    district_general_hospital = models.FloatField(blank=True, null=True)
    office = models.FloatField(blank=True, null=True)
    other = models.FloatField(blank=True, null=True)
    total = models.FloatField(blank=True, null=True)
    district = models.ForeignKey(District, models.DO_NOTHING, db_column='district', blank=True, null=True)
    created_user = models.IntegerField(blank=True, null=True)
    lmu = models.IntegerField(blank=True, null=True)
    created_date = models.DateTimeField(blank=True, null=True)
    lmd = models.DateTimeField(blank=True, null=True)
    key = models.BigIntegerField(blank=True, null=True)
    incident = models.ForeignKey('IncidentReport', models.DO_NOTHING, db_column='incident', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'dmh_pdfa_structure'


class DshPubLmh(models.Model):
    facilities_assets = models.CharField(max_length=255, blank=True, null=True)
    total_num_affected = models.BigIntegerField(blank=True, null=True)
    male = models.BigIntegerField(blank=True, null=True)
    female = models.BigIntegerField(blank=True, null=True)
    total_damages = models.FloatField(blank=True, null=True)
    losses_y1 = models.FloatField(blank=True, null=True)
    losses_y2 = models.FloatField(blank=True, null=True)
    total_losses = models.FloatField(blank=True, null=True)
    district = models.ForeignKey(District, models.DO_NOTHING, db_column='district', blank=True, null=True)
    created_user = models.IntegerField(blank=True, null=True)
    lmu = models.IntegerField(blank=True, null=True)
    created_date = models.DateTimeField(blank=True, null=True)
    lmd = models.DateTimeField(blank=True, null=True)
    key = models.BigIntegerField(blank=True, null=True)
    incident = models.ForeignKey('IncidentReport', models.DO_NOTHING, db_column='incident', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'dsh_pub_lmh'


class DshPubMoh(models.Model):
    facilities_assets = models.CharField(max_length=255, blank=True, null=True)
    total_num_affected = models.BigIntegerField(blank=True, null=True)
    male = models.BigIntegerField(blank=True, null=True)
    female = models.BigIntegerField(blank=True, null=True)
    total_damages = models.FloatField(blank=True, null=True)
    losses_y1 = models.FloatField(blank=True, null=True)
    losses_y2 = models.FloatField(blank=True, null=True)
    total_losses = models.FloatField(blank=True, null=True)
    district = models.ForeignKey(District, models.DO_NOTHING, db_column='district', blank=True, null=True)
    created_user = models.IntegerField(blank=True, null=True)
    lmu = models.IntegerField(blank=True, null=True)
    created_date = models.DateTimeField(blank=True, null=True)
    lmd = models.DateTimeField(blank=True, null=True)
    key = models.BigIntegerField(blank=True, null=True)
    incident = models.ForeignKey('IncidentReport', models.DO_NOTHING, db_column='incident', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'dsh_pub_moh'


class DshPubOmf(models.Model):
    facilities_assets = models.CharField(max_length=255, blank=True, null=True)
    total_num_affected = models.BigIntegerField(blank=True, null=True)
    male = models.BigIntegerField(blank=True, null=True)
    female = models.BigIntegerField(blank=True, null=True)
    total_damages = models.FloatField(blank=True, null=True)
    losses_y1 = models.FloatField(blank=True, null=True)
    losses_y2 = models.FloatField(blank=True, null=True)
    total_losses = models.FloatField(blank=True, null=True)
    district = models.ForeignKey(District, models.DO_NOTHING, db_column='district', blank=True, null=True)
    created_user = models.IntegerField(blank=True, null=True)
    lmu = models.IntegerField(blank=True, null=True)
    created_date = models.DateTimeField(blank=True, null=True)
    lmd = models.DateTimeField(blank=True, null=True)
    key = models.BigIntegerField(blank=True, null=True)
    incident = models.ForeignKey('IncidentReport', models.DO_NOTHING, db_column='incident', blank=True, null=True)
    id = models.AutoField()

    class Meta:
        managed = False
        db_table = 'dsh_pub_omf'


class DshPvtFa(models.Model):
    facilities_assets = models.CharField(max_length=255, blank=True, null=True)
    total_num_affected = models.BigIntegerField(blank=True, null=True)
    male = models.BigIntegerField(blank=True, null=True)
    female = models.BigIntegerField(blank=True, null=True)
    total_damages = models.FloatField(blank=True, null=True)
    losses_y1 = models.FloatField(blank=True, null=True)
    losses_y2 = models.FloatField(blank=True, null=True)
    total_losses = models.FloatField(blank=True, null=True)
    district = models.ForeignKey(District, models.DO_NOTHING, db_column='district', blank=True, null=True)
    created_user = models.IntegerField(blank=True, null=True)
    lmu = models.IntegerField(blank=True, null=True)
    created_date = models.DateTimeField(blank=True, null=True)
    lmd = models.DateTimeField(blank=True, null=True)
    key = models.BigIntegerField(blank=True, null=True)
    incident = models.ForeignKey('IncidentReport', models.DO_NOTHING, db_column='incident', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'dsh_pvt_fa'


class DshTdlOwship(models.Model):
    ownership = models.CharField(max_length=255, blank=True, null=True)
    damages = models.FloatField(blank=True, null=True)
    losses_y1 = models.FloatField(blank=True, null=True)
    losses_y2 = models.FloatField(blank=True, null=True)
    total = models.FloatField(blank=True, null=True)
    district = models.ForeignKey(District, models.DO_NOTHING, db_column='district', blank=True, null=True)
    created_user = models.IntegerField(blank=True, null=True)
    lmu = models.IntegerField(blank=True, null=True)
    created_date = models.DateTimeField(blank=True, null=True)
    lmd = models.DateTimeField(blank=True, null=True)
    key = models.BigIntegerField(blank=True, null=True)
    incident = models.ForeignKey('IncidentReport', models.DO_NOTHING, db_column='incident', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'dsh_tdl_owship'


class DsnPubP1Lmh(models.Model):
    facilities_assets = models.CharField(max_length=255, blank=True, null=True)
    total_num_affected = models.BigIntegerField(blank=True, null=True)
    male = models.BigIntegerField(blank=True, null=True)
    female = models.BigIntegerField(blank=True, null=True)
    total_damages = models.FloatField(blank=True, null=True)
    losses_y1 = models.FloatField(blank=True, null=True)
    losses_y2 = models.FloatField(blank=True, null=True)
    total_losses = models.FloatField(blank=True, null=True)
    district = models.ForeignKey(District, models.DO_NOTHING, db_column='district', blank=True, null=True)
    created_user = models.IntegerField(blank=True, null=True)
    lmu = models.IntegerField(blank=True, null=True)
    created_date = models.DateTimeField(blank=True, null=True)
    lmd = models.DateTimeField(blank=True, null=True)
    key = models.BigIntegerField(blank=True, null=True)
    incident = models.ForeignKey('IncidentReport', models.DO_NOTHING, db_column='incident', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'dsn_pub_p1_lmh'


class DsnPubP1Moh(models.Model):
    facilities_assets = models.CharField(max_length=255, blank=True, null=True)
    total_num_affected = models.BigIntegerField(blank=True, null=True)
    male = models.BigIntegerField(blank=True, null=True)
    female = models.BigIntegerField(blank=True, null=True)
    total_damages = models.FloatField(blank=True, null=True)
    losses_y1 = models.FloatField(blank=True, null=True)
    losses_y2 = models.FloatField(blank=True, null=True)
    total_losses = models.FloatField(blank=True, null=True)
    district = models.ForeignKey(District, models.DO_NOTHING, db_column='district', blank=True, null=True)
    created_user = models.IntegerField(blank=True, null=True)
    lmu = models.IntegerField(blank=True, null=True)
    created_date = models.DateTimeField(blank=True, null=True)
    lmd = models.DateTimeField(blank=True, null=True)
    key = models.BigIntegerField(blank=True, null=True)
    incident = models.ForeignKey('IncidentReport', models.DO_NOTHING, db_column='incident', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'dsn_pub_p1_moh'


class DsnPubP1Omc(models.Model):
    facilities_assets = models.CharField(max_length=255, blank=True, null=True)
    total_num_affected = models.BigIntegerField(blank=True, null=True)
    male = models.BigIntegerField(blank=True, null=True)
    female = models.BigIntegerField(blank=True, null=True)
    total_damages = models.FloatField(blank=True, null=True)
    losses_y1 = models.FloatField(blank=True, null=True)
    losses_y2 = models.FloatField(blank=True, null=True)
    total_losses = models.FloatField(blank=True, null=True)
    district = models.ForeignKey(District, models.DO_NOTHING, db_column='district', blank=True, null=True)
    created_user = models.IntegerField(blank=True, null=True)
    lmu = models.IntegerField(blank=True, null=True)
    created_date = models.DateTimeField(blank=True, null=True)
    lmd = models.DateTimeField(blank=True, null=True)
    key = models.BigIntegerField(blank=True, null=True)
    incident = models.ForeignKey('IncidentReport', models.DO_NOTHING, db_column='incident', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'dsn_pub_p1_omc'


class DsnPubPnLmh(models.Model):
    facilities_assets = models.CharField(max_length=255, blank=True, null=True)
    total_num_affected = models.BigIntegerField(blank=True, null=True)
    male = models.BigIntegerField(blank=True, null=True)
    female = models.BigIntegerField(blank=True, null=True)
    total_damages = models.FloatField(blank=True, null=True)
    losses_y1 = models.FloatField(blank=True, null=True)
    losses_y2 = models.FloatField(blank=True, null=True)
    total_losses = models.FloatField(blank=True, null=True)
    district = models.ForeignKey(District, models.DO_NOTHING, db_column='district', blank=True, null=True)
    created_user = models.IntegerField(blank=True, null=True)
    lmu = models.IntegerField(blank=True, null=True)
    created_date = models.DateTimeField(blank=True, null=True)
    lmd = models.DateTimeField(blank=True, null=True)
    key = models.BigIntegerField(blank=True, null=True)
    incident = models.ForeignKey('IncidentReport', models.DO_NOTHING, db_column='incident', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'dsn_pub_pn_lmh'


class DsnPubPnMoh(models.Model):
    facilities_assets = models.CharField(max_length=255, blank=True, null=True)
    total_num_affected = models.BigIntegerField(blank=True, null=True)
    male = models.BigIntegerField(blank=True, null=True)
    female = models.BigIntegerField(blank=True, null=True)
    total_damages = models.FloatField(blank=True, null=True)
    losses_y1 = models.FloatField(blank=True, null=True)
    losses_y2 = models.FloatField(blank=True, null=True)
    total_losses = models.FloatField(blank=True, null=True)
    district = models.ForeignKey(District, models.DO_NOTHING, db_column='district', blank=True, null=True)
    created_user = models.IntegerField(blank=True, null=True)
    lmu = models.IntegerField(blank=True, null=True)
    created_date = models.DateTimeField(blank=True, null=True)
    lmd = models.DateTimeField(blank=True, null=True)
    key = models.BigIntegerField(blank=True, null=True)
    incident = models.ForeignKey('IncidentReport', models.DO_NOTHING, db_column='incident', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'dsn_pub_pn_moh'


class DsnPubPnOmc(models.Model):
    facilities_assets = models.CharField(max_length=255, blank=True, null=True)
    total_num_affected = models.BigIntegerField(blank=True, null=True)
    male = models.BigIntegerField(blank=True, null=True)
    female = models.BigIntegerField(blank=True, null=True)
    total_damages = models.FloatField(blank=True, null=True)
    losses_y1 = models.FloatField(blank=True, null=True)
    losses_y2 = models.FloatField(blank=True, null=True)
    total_losses = models.FloatField(blank=True, null=True)
    district = models.ForeignKey(District, models.DO_NOTHING, db_column='district', blank=True, null=True)
    created_user = models.IntegerField(blank=True, null=True)
    lmu = models.IntegerField(blank=True, null=True)
    created_date = models.DateTimeField(blank=True, null=True)
    lmd = models.DateTimeField(blank=True, null=True)
    key = models.BigIntegerField(blank=True, null=True)
    incident = models.ForeignKey('IncidentReport', models.DO_NOTHING, db_column='incident', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'dsn_pub_pn_omc'


class DsnPvtP1(models.Model):
    facilities_assets = models.CharField(max_length=255, blank=True, null=True)
    total_num_affected = models.BigIntegerField(blank=True, null=True)
    male = models.BigIntegerField(blank=True, null=True)
    female = models.BigIntegerField(blank=True, null=True)
    total_damages = models.FloatField(blank=True, null=True)
    losses_y1 = models.FloatField(blank=True, null=True)
    losses_y2 = models.FloatField(blank=True, null=True)
    total_losses = models.FloatField(blank=True, null=True)
    district = models.ForeignKey(District, models.DO_NOTHING, db_column='district', blank=True, null=True)
    created_user = models.IntegerField(blank=True, null=True)
    lmu = models.IntegerField(blank=True, null=True)
    created_date = models.DateTimeField(blank=True, null=True)
    lmd = models.DateTimeField(blank=True, null=True)
    key = models.BigIntegerField(blank=True, null=True)
    incident = models.ForeignKey('IncidentReport', models.DO_NOTHING, db_column='incident', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'dsn_pvt_p1'


class DsnPvtPn(models.Model):
    facilities_assets = models.CharField(max_length=255, blank=True, null=True)
    total_num_affected = models.BigIntegerField(blank=True, null=True)
    male = models.BigIntegerField(blank=True, null=True)
    female = models.BigIntegerField(blank=True, null=True)
    total_damages = models.FloatField(blank=True, null=True)
    losses_y1 = models.FloatField(blank=True, null=True)
    losses_y2 = models.FloatField(blank=True, null=True)
    total_losses = models.FloatField(blank=True, null=True)
    district = models.ForeignKey(District, models.DO_NOTHING, db_column='district', blank=True, null=True)
    created_user = models.IntegerField(blank=True, null=True)
    lmu = models.IntegerField(blank=True, null=True)
    created_date = models.DateTimeField(blank=True, null=True)
    lmd = models.DateTimeField(blank=True, null=True)
    key = models.BigIntegerField(blank=True, null=True)
    incident = models.ForeignKey('IncidentReport', models.DO_NOTHING, db_column='incident', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'dsn_pvt_pn'


class DsnTdlOwship(models.Model):
    ownership = models.CharField(max_length=255, blank=True, null=True)
    damages = models.FloatField(blank=True, null=True)
    losses_y1 = models.FloatField(blank=True, null=True)
    losses_y2 = models.FloatField(blank=True, null=True)
    total = models.FloatField(blank=True, null=True)
    district = models.ForeignKey(District, models.DO_NOTHING, db_column='district', blank=True, null=True)
    created_user = models.IntegerField(blank=True, null=True)
    lmu = models.IntegerField(blank=True, null=True)
    created_date = models.DateTimeField(blank=True, null=True)
    lmd = models.DateTimeField(blank=True, null=True)
    key = models.BigIntegerField(blank=True, null=True)
    incident = models.ForeignKey('IncidentReport', models.DO_NOTHING, db_column='incident', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'dsn_tdl_owship'


class GeoLine(models.Model):
    assest_type = models.ForeignKey(AssestType, models.DO_NOTHING, db_column='assest_type', blank=True, null=True)
    geon = models.TextField(blank=True, null=True)  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'geo_line'


class GeoPoint(models.Model):
    assest_type = models.ForeignKey(AssestType, models.DO_NOTHING, db_column='assest_type', blank=True, null=True)
    geon = models.TextField(blank=True, null=True)  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'geo_point'


class GeoPolygon(models.Model):
    assest_type = models.ForeignKey(AssestType, models.DO_NOTHING, db_column='assest_type', blank=True, null=True)
    geon = models.TextField(blank=True, null=True)  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'geo_polygon'


class IncidentReport(models.Model):
    disaster_type = models.ForeignKey(DisasterType, models.DO_NOTHING)
    description = models.CharField(max_length=500, blank=True, null=True)
    reported_date_time = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'incident_report'


class SectorTabelCol(models.Model):
    sector_tabel = models.ForeignKey(User, models.DO_NOTHING)
    col_name = models.CharField(max_length=-1, blank=True, null=True)
    value = models.CharField(max_length=-1, blank=True, null=True)
    data_type = models.CharField(max_length=-1, blank=True, null=True)
    lmu = models.BigIntegerField(blank=True, null=True)
    lmd = models.TimeField(blank=True, null=True)
    created_date = models.TimeField(blank=True, null=True)
    data_entry_id = models.BigIntegerField(blank=True, null=True)
    district_id = models.BigIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'sector_tabel_col'


class SectorTable(models.Model):
    name = models.CharField(max_length=-1, blank=True, null=True)
    description = models.CharField(max_length=-1, blank=True, null=True)
    table_type = models.NullBooleanField()

    class Meta:
        managed = False
        db_table = 'sector_table'


class UserRolePermission(models.Model):
    user_role = models.ForeignKey(Userrole, models.DO_NOTHING, blank=True, null=True)
    sector_property = models.ForeignKey(SectorTabelCol, models.DO_NOTHING, blank=True, null=True)
    permission_type = models.ForeignKey(Permissiontype, models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'user_role_permission'
