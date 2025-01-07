# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class AnalysisArticle(models.Model):
    id = models.BigAutoField(primary_key=True)
    title = models.CharField(max_length=200)
    summary = models.TextField()
    created_at = models.DateTimeField()
    pdf = models.CharField(max_length=100)
    picture = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'analysis_article'


class AnalysisProfile(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=100)
    picture = models.CharField(max_length=100)
    summary = models.TextField()
    resume = models.CharField(max_length=100)
    created_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'analysis_profile'


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

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
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
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


class C2019B(models.Model):
    unitid = models.IntegerField(db_column='UNITID', blank=True, null=True)  # Field name made lowercase.
    xcstotlt = models.CharField(db_column='XCSTOTLT', max_length=50, blank=True, null=True)  # Field name made lowercase.
    cstotlt = models.IntegerField(db_column='CSTOTLT', blank=True, null=True)  # Field name made lowercase.
    xcstotlm = models.CharField(db_column='XCSTOTLM', max_length=50, blank=True, null=True)  # Field name made lowercase.
    cstotlm = models.IntegerField(db_column='CSTOTLM', blank=True, null=True)  # Field name made lowercase.
    xcstotlw = models.CharField(db_column='XCSTOTLW', max_length=50, blank=True, null=True)  # Field name made lowercase.
    cstotlw = models.IntegerField(db_column='CSTOTLW', blank=True, null=True)  # Field name made lowercase.
    xcsaiant = models.CharField(db_column='XCSAIANT', max_length=50, blank=True, null=True)  # Field name made lowercase.
    csaiant = models.IntegerField(db_column='CSAIANT', blank=True, null=True)  # Field name made lowercase.
    xcsaianm = models.CharField(db_column='XCSAIANM', max_length=50, blank=True, null=True)  # Field name made lowercase.
    csaianm = models.IntegerField(db_column='CSAIANM', blank=True, null=True)  # Field name made lowercase.
    xcsaianw = models.CharField(db_column='XCSAIANW', max_length=50, blank=True, null=True)  # Field name made lowercase.
    csaianw = models.IntegerField(db_column='CSAIANW', blank=True, null=True)  # Field name made lowercase.
    xcsasiat = models.CharField(db_column='XCSASIAT', max_length=50, blank=True, null=True)  # Field name made lowercase.
    csasiat = models.IntegerField(db_column='CSASIAT', blank=True, null=True)  # Field name made lowercase.
    xcsasiam = models.CharField(db_column='XCSASIAM', max_length=50, blank=True, null=True)  # Field name made lowercase.
    csasiam = models.IntegerField(db_column='CSASIAM', blank=True, null=True)  # Field name made lowercase.
    xcsasiaw = models.CharField(db_column='XCSASIAW', max_length=50, blank=True, null=True)  # Field name made lowercase.
    csasiaw = models.IntegerField(db_column='CSASIAW', blank=True, null=True)  # Field name made lowercase.
    xcsbkaat = models.CharField(db_column='XCSBKAAT', max_length=50, blank=True, null=True)  # Field name made lowercase.
    csbkaat = models.IntegerField(db_column='CSBKAAT', blank=True, null=True)  # Field name made lowercase.
    xcsbkaam = models.CharField(db_column='XCSBKAAM', max_length=50, blank=True, null=True)  # Field name made lowercase.
    csbkaam = models.IntegerField(db_column='CSBKAAM', blank=True, null=True)  # Field name made lowercase.
    xcsbkaaw = models.CharField(db_column='XCSBKAAW', max_length=50, blank=True, null=True)  # Field name made lowercase.
    csbkaaw = models.IntegerField(db_column='CSBKAAW', blank=True, null=True)  # Field name made lowercase.
    xcshispt = models.CharField(db_column='XCSHISPT', max_length=50, blank=True, null=True)  # Field name made lowercase.
    cshispt = models.IntegerField(db_column='CSHISPT', blank=True, null=True)  # Field name made lowercase.
    xcshispm = models.CharField(db_column='XCSHISPM', max_length=50, blank=True, null=True)  # Field name made lowercase.
    cshispm = models.IntegerField(db_column='CSHISPM', blank=True, null=True)  # Field name made lowercase.
    xcshispw = models.CharField(db_column='XCSHISPW', max_length=50, blank=True, null=True)  # Field name made lowercase.
    cshispw = models.IntegerField(db_column='CSHISPW', blank=True, null=True)  # Field name made lowercase.
    xcsnhpit = models.CharField(db_column='XCSNHPIT', max_length=50, blank=True, null=True)  # Field name made lowercase.
    csnhpit = models.IntegerField(db_column='CSNHPIT', blank=True, null=True)  # Field name made lowercase.
    xcsnhpim = models.CharField(db_column='XCSNHPIM', max_length=50, blank=True, null=True)  # Field name made lowercase.
    csnhpim = models.IntegerField(db_column='CSNHPIM', blank=True, null=True)  # Field name made lowercase.
    xcsnhpiw = models.CharField(db_column='XCSNHPIW', max_length=50, blank=True, null=True)  # Field name made lowercase.
    csnhpiw = models.IntegerField(db_column='CSNHPIW', blank=True, null=True)  # Field name made lowercase.
    xcswhitt = models.CharField(db_column='XCSWHITT', max_length=50, blank=True, null=True)  # Field name made lowercase.
    cswhitt = models.IntegerField(db_column='CSWHITT', blank=True, null=True)  # Field name made lowercase.
    xcswhitm = models.CharField(db_column='XCSWHITM', max_length=50, blank=True, null=True)  # Field name made lowercase.
    cswhitm = models.IntegerField(db_column='CSWHITM', blank=True, null=True)  # Field name made lowercase.
    xcswhitw = models.CharField(db_column='XCSWHITW', max_length=50, blank=True, null=True)  # Field name made lowercase.
    cswhitw = models.IntegerField(db_column='CSWHITW', blank=True, null=True)  # Field name made lowercase.
    xcs2mort = models.CharField(db_column='XCS2MORT', max_length=50, blank=True, null=True)  # Field name made lowercase.
    cs2mort = models.IntegerField(db_column='CS2MORT', blank=True, null=True)  # Field name made lowercase.
    xcs2morm = models.CharField(db_column='XCS2MORM', max_length=50, blank=True, null=True)  # Field name made lowercase.
    cs2morm = models.IntegerField(db_column='CS2MORM', blank=True, null=True)  # Field name made lowercase.
    xcs2morw = models.CharField(db_column='XCS2MORW', max_length=50, blank=True, null=True)  # Field name made lowercase.
    cs2morw = models.IntegerField(db_column='CS2MORW', blank=True, null=True)  # Field name made lowercase.
    xcsunknt = models.CharField(db_column='XCSUNKNT', max_length=50, blank=True, null=True)  # Field name made lowercase.
    csunknt = models.IntegerField(db_column='CSUNKNT', blank=True, null=True)  # Field name made lowercase.
    xcsunknm = models.CharField(db_column='XCSUNKNM', max_length=50, blank=True, null=True)  # Field name made lowercase.
    csunknm = models.IntegerField(db_column='CSUNKNM', blank=True, null=True)  # Field name made lowercase.
    xcsunknw = models.CharField(db_column='XCSUNKNW', max_length=50, blank=True, null=True)  # Field name made lowercase.
    csunknw = models.IntegerField(db_column='CSUNKNW', blank=True, null=True)  # Field name made lowercase.
    xcsnralt = models.CharField(db_column='XCSNRALT', max_length=50, blank=True, null=True)  # Field name made lowercase.
    csnralt = models.IntegerField(db_column='CSNRALT', blank=True, null=True)  # Field name made lowercase.
    xcsnralm = models.CharField(db_column='XCSNRALM', max_length=50, blank=True, null=True)  # Field name made lowercase.
    csnralm = models.IntegerField(db_column='CSNRALM', blank=True, null=True)  # Field name made lowercase.
    xcsnralw = models.CharField(db_column='XCSNRALW', max_length=50, blank=True, null=True)  # Field name made lowercase.
    csnralw_field = models.IntegerField(db_column='CSNRALW ', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.

    class Meta:
        managed = False
        db_table = 'c2019_b'


class C2022A(models.Model):
    unitid = models.IntegerField(db_column='UNITID', blank=True, null=True)  # Field name made lowercase.
    cipcode = models.IntegerField(db_column='CIPCODE', blank=True, null=True)  # Field name made lowercase.
    majornum = models.IntegerField(db_column='MAJORNUM', blank=True, null=True)  # Field name made lowercase.
    awlevel = models.IntegerField(db_column='AWLEVEL', blank=True, null=True)  # Field name made lowercase.
    ctotalt = models.IntegerField(db_column='CTOTALT', blank=True, null=True)  # Field name made lowercase.
    ctotalm = models.IntegerField(db_column='CTOTALM', blank=True, null=True)  # Field name made lowercase.
    ctotalw = models.IntegerField(db_column='CTOTALW', blank=True, null=True)  # Field name made lowercase.
    caiant = models.IntegerField(db_column='CAIANT', blank=True, null=True)  # Field name made lowercase.
    caianm = models.IntegerField(db_column='CAIANM', blank=True, null=True)  # Field name made lowercase.
    caianw = models.IntegerField(db_column='CAIANW', blank=True, null=True)  # Field name made lowercase.
    casiat = models.IntegerField(db_column='CASIAT', blank=True, null=True)  # Field name made lowercase.
    casiam = models.IntegerField(db_column='CASIAM', blank=True, null=True)  # Field name made lowercase.
    casiaw = models.IntegerField(db_column='CASIAW', blank=True, null=True)  # Field name made lowercase.
    cbkaat = models.IntegerField(db_column='CBKAAT', blank=True, null=True)  # Field name made lowercase.
    cbkaam = models.IntegerField(db_column='CBKAAM', blank=True, null=True)  # Field name made lowercase.
    cbkaaw = models.IntegerField(db_column='CBKAAW', blank=True, null=True)  # Field name made lowercase.
    chispt = models.IntegerField(db_column='CHISPT', blank=True, null=True)  # Field name made lowercase.
    chispm = models.IntegerField(db_column='CHISPM', blank=True, null=True)  # Field name made lowercase.
    chispw = models.IntegerField(db_column='CHISPW', blank=True, null=True)  # Field name made lowercase.
    cnhpit = models.IntegerField(db_column='CNHPIT', blank=True, null=True)  # Field name made lowercase.
    cnhpim = models.IntegerField(db_column='CNHPIM', blank=True, null=True)  # Field name made lowercase.
    cnhpiw = models.IntegerField(db_column='CNHPIW', blank=True, null=True)  # Field name made lowercase.
    cwhitt = models.IntegerField(db_column='CWHITT', blank=True, null=True)  # Field name made lowercase.
    cwhitm = models.IntegerField(db_column='CWHITM', blank=True, null=True)  # Field name made lowercase.
    cwhitw = models.IntegerField(db_column='CWHITW', blank=True, null=True)  # Field name made lowercase.
    c2mort = models.IntegerField(db_column='C2MORT', blank=True, null=True)  # Field name made lowercase.
    c2morm = models.IntegerField(db_column='C2MORM', blank=True, null=True)  # Field name made lowercase.
    c2morw = models.IntegerField(db_column='C2MORW', blank=True, null=True)  # Field name made lowercase.
    cunknt = models.IntegerField(db_column='CUNKNT', blank=True, null=True)  # Field name made lowercase.
    cunknm = models.IntegerField(db_column='CUNKNM', blank=True, null=True)  # Field name made lowercase.
    cunknw = models.IntegerField(db_column='CUNKNW', blank=True, null=True)  # Field name made lowercase.
    cnralt = models.IntegerField(db_column='CNRALT', blank=True, null=True)  # Field name made lowercase.
    cnralm = models.IntegerField(db_column='CNRALM', blank=True, null=True)  # Field name made lowercase.
    cnralw = models.IntegerField(db_column='CNRALW', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'c2022_a'


class C2023B(models.Model):
    unitid = models.IntegerField(db_column='UNITID', primary_key=True)  # Specify primary key
    xcstotlt = models.CharField(db_column='XCSTOTLT', max_length=50, blank=True, null=True)  # Field name made lowercase.
    cstotlt = models.IntegerField(db_column='CSTOTLT', blank=True, null=True)  # Field name made lowercase.
    xcstotlm = models.CharField(db_column='XCSTOTLM', max_length=50, blank=True, null=True)  # Field name made lowercase.
    cstotlm = models.IntegerField(db_column='CSTOTLM', blank=True, null=True)  # Field name made lowercase.
    xcstotlw = models.CharField(db_column='XCSTOTLW', max_length=50, blank=True, null=True)  # Field name made lowercase.
    cstotlw = models.IntegerField(db_column='CSTOTLW', blank=True, null=True)  # Field name made lowercase.
    xcsaiant = models.CharField(db_column='XCSAIANT', max_length=50, blank=True, null=True)  # Field name made lowercase.
    csaiant = models.IntegerField(db_column='CSAIANT', blank=True, null=True)  # Field name made lowercase.
    xcsaianm = models.CharField(db_column='XCSAIANM', max_length=50, blank=True, null=True)  # Field name made lowercase.
    csaianm = models.IntegerField(db_column='CSAIANM', blank=True, null=True)  # Field name made lowercase.
    xcsaianw = models.CharField(db_column='XCSAIANW', max_length=50, blank=True, null=True)  # Field name made lowercase.
    csaianw = models.IntegerField(db_column='CSAIANW', blank=True, null=True)  # Field name made lowercase.
    xcsasiat = models.CharField(db_column='XCSASIAT', max_length=50, blank=True, null=True)  # Field name made lowercase.
    csasiat = models.IntegerField(db_column='CSASIAT', blank=True, null=True)  # Field name made lowercase.
    xcsasiam = models.CharField(db_column='XCSASIAM', max_length=50, blank=True, null=True)  # Field name made lowercase.
    csasiam = models.IntegerField(db_column='CSASIAM', blank=True, null=True)  # Field name made lowercase.
    xcsasiaw = models.CharField(db_column='XCSASIAW', max_length=50, blank=True, null=True)  # Field name made lowercase.
    csasiaw = models.IntegerField(db_column='CSASIAW', blank=True, null=True)  # Field name made lowercase.
    xcsbkaat = models.CharField(db_column='XCSBKAAT', max_length=50, blank=True, null=True)  # Field name made lowercase.
    csbkaat = models.IntegerField(db_column='CSBKAAT', blank=True, null=True)  # Field name made lowercase.
    xcsbkaam = models.CharField(db_column='XCSBKAAM', max_length=50, blank=True, null=True)  # Field name made lowercase.
    csbkaam = models.IntegerField(db_column='CSBKAAM', blank=True, null=True)  # Field name made lowercase.
    xcsbkaaw = models.CharField(db_column='XCSBKAAW', max_length=50, blank=True, null=True)  # Field name made lowercase.
    csbkaaw = models.IntegerField(db_column='CSBKAAW', blank=True, null=True)  # Field name made lowercase.
    xcshispt = models.CharField(db_column='XCSHISPT', max_length=50, blank=True, null=True)  # Field name made lowercase.
    cshispt = models.IntegerField(db_column='CSHISPT', blank=True, null=True)  # Field name made lowercase.
    xcshispm = models.CharField(db_column='XCSHISPM', max_length=50, blank=True, null=True)  # Field name made lowercase.
    cshispm = models.IntegerField(db_column='CSHISPM', blank=True, null=True)  # Field name made lowercase.
    xcshispw = models.CharField(db_column='XCSHISPW', max_length=50, blank=True, null=True)  # Field name made lowercase.
    cshispw = models.IntegerField(db_column='CSHISPW', blank=True, null=True)  # Field name made lowercase.
    xcsnhpit = models.CharField(db_column='XCSNHPIT', max_length=50, blank=True, null=True)  # Field name made lowercase.
    csnhpit = models.IntegerField(db_column='CSNHPIT', blank=True, null=True)  # Field name made lowercase.
    xcsnhpim = models.CharField(db_column='XCSNHPIM', max_length=50, blank=True, null=True)  # Field name made lowercase.
    csnhpim = models.IntegerField(db_column='CSNHPIM', blank=True, null=True)  # Field name made lowercase.
    xcsnhpiw = models.CharField(db_column='XCSNHPIW', max_length=50, blank=True, null=True)  # Field name made lowercase.
    csnhpiw = models.IntegerField(db_column='CSNHPIW', blank=True, null=True)  # Field name made lowercase.
    xcswhitt = models.CharField(db_column='XCSWHITT', max_length=50, blank=True, null=True)  # Field name made lowercase.
    cswhitt = models.IntegerField(db_column='CSWHITT', blank=True, null=True)  # Field name made lowercase.
    xcswhitm = models.CharField(db_column='XCSWHITM', max_length=50, blank=True, null=True)  # Field name made lowercase.
    cswhitm = models.IntegerField(db_column='CSWHITM', blank=True, null=True)  # Field name made lowercase.
    xcswhitw = models.CharField(db_column='XCSWHITW', max_length=50, blank=True, null=True)  # Field name made lowercase.
    cswhitw = models.IntegerField(db_column='CSWHITW', blank=True, null=True)  # Field name made lowercase.
    xcs2mort = models.CharField(db_column='XCS2MORT', max_length=50, blank=True, null=True)  # Field name made lowercase.
    cs2mort = models.IntegerField(db_column='CS2MORT', blank=True, null=True)  # Field name made lowercase.
    xcs2morm = models.CharField(db_column='XCS2MORM', max_length=50, blank=True, null=True)  # Field name made lowercase.
    cs2morm = models.IntegerField(db_column='CS2MORM', blank=True, null=True)  # Field name made lowercase.
    xcs2morw = models.CharField(db_column='XCS2MORW', max_length=50, blank=True, null=True)  # Field name made lowercase.
    cs2morw = models.IntegerField(db_column='CS2MORW', blank=True, null=True)  # Field name made lowercase.
    xcsunknt = models.CharField(db_column='XCSUNKNT', max_length=50, blank=True, null=True)  # Field name made lowercase.
    csunknt = models.IntegerField(db_column='CSUNKNT', blank=True, null=True)  # Field name made lowercase.
    xcsunknm = models.CharField(db_column='XCSUNKNM', max_length=50, blank=True, null=True)  # Field name made lowercase.
    csunknm = models.IntegerField(db_column='CSUNKNM', blank=True, null=True)  # Field name made lowercase.
    xcsunknw = models.CharField(db_column='XCSUNKNW', max_length=50, blank=True, null=True)  # Field name made lowercase.
    csunknw = models.IntegerField(db_column='CSUNKNW', blank=True, null=True)  # Field name made lowercase.
    xcsnralt = models.CharField(db_column='XCSNRALT', max_length=50, blank=True, null=True)  # Field name made lowercase.
    csnralt = models.IntegerField(db_column='CSNRALT', blank=True, null=True)  # Field name made lowercase.
    xcsnralm = models.CharField(db_column='XCSNRALM', max_length=50, blank=True, null=True)  # Field name made lowercase.
    csnralm = models.IntegerField(db_column='CSNRALM', blank=True, null=True)  # Field name made lowercase.
    xcsnralw = models.CharField(db_column='XCSNRALW', max_length=50, blank=True, null=True)  # Field name made lowercase.
    csnralw = models.IntegerField(db_column='CSNRALW', blank=True, null=True)  # Field name made lowercase.
    xcsguugu = models.CharField(db_column='XCSGUUGU', max_length=50, blank=True, null=True)  # Field name made lowercase.
    csguugun = models.IntegerField(db_column='CSGUUGUN', blank=True, null=True)  # Field name made lowercase.
    xcsguuga = models.CharField(db_column='XCSGUUGA', max_length=50, blank=True, null=True)  # Field name made lowercase.
    csguugag = models.IntegerField(db_column='CSGUUGAG', blank=True, null=True)  # Field name made lowercase.
    xcsguugt = models.CharField(db_column='XCSGUUGT', max_length=50, blank=True, null=True)  # Field name made lowercase.
    csguugtt = models.IntegerField(db_column='CSGUUGTT', blank=True, null=True)  # Field name made lowercase.
    xcsgugun = models.CharField(db_column='XCSGUGUN', max_length=50, blank=True, null=True)  # Field name made lowercase.
    csgugun = models.IntegerField(db_column='CSGUGUN', blank=True, null=True)  # Field name made lowercase.
    xcsgugag = models.CharField(db_column='XCSGUGAG', max_length=50, blank=True, null=True)  # Field name made lowercase.
    csgugag = models.IntegerField(db_column='CSGUGAG', blank=True, null=True)  # Field name made lowercase.
    xcsgugtt = models.CharField(db_column='XCSGUGTT', max_length=50, blank=True, null=True)  # Field name made lowercase.
    csgugtot = models.IntegerField(db_column='CSGUGTOT', blank=True, null=True)  # Field name made lowercase.
    xcsguttun = models.CharField(db_column='XCSGUTTUN', max_length=50, blank=True, null=True)  # Field name made lowercase.
    csgutotun = models.IntegerField(db_column='CSGUTOTUN', blank=True, null=True)  # Field name made lowercase.
    xcsguttag = models.CharField(db_column='XCSGUTTAG', max_length=50, blank=True, null=True)  # Field name made lowercase.
    csgutotag = models.IntegerField(db_column='CSGUTOTAG', blank=True, null=True)  # Field name made lowercase.
    xcsgutot = models.CharField(db_column='XCSGUTOT', max_length=50, blank=True, null=True)  # Field name made lowercase.
    csgutot = models.IntegerField(db_column='CSGUTOT', blank=True, null=True)  # Field name made lowercase.
    xcsgukn = models.CharField(db_column='XCSGUKN', max_length=50, blank=True, null=True)  # Field name made lowercase.
    csgukn_field = models.CharField(db_column='CSGUKN    ', max_length=50, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.

    class Meta:
        managed = False
        db_table = 'c2023_b'


class DashboardRankingdata(models.Model):
    id = models.BigAutoField(primary_key=True)
    indicator = models.CharField(db_column='Indicator', max_length=255)  # Field name made lowercase.
    rank_2010 = models.IntegerField(db_column='Rank_2010')  # Field name made lowercase.
    rank_growth_2010_2019 = models.IntegerField(db_column='Rank_Growth_2010_2019')  # Field name made lowercase.
    rank_2019 = models.IntegerField(db_column='Rank_2019')  # Field name made lowercase.
    rank_growth_2019_2023 = models.IntegerField(db_column='Rank_Growth_2019_2023')  # Field name made lowercase.
    rank_2023 = models.IntegerField(db_column='Rank_2023')  # Field name made lowercase.
    state = models.CharField(db_column='State', max_length=255, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'dashboard_rankingdata'


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


class Drvic2023(models.Model):
    cindon = models.IntegerField(blank=True, null=True)
    cinson = models.IntegerField(blank=True, null=True)
    cotson = models.IntegerField(blank=True, null=True)
    cindoff = models.IntegerField(blank=True, null=True)
    cinsoff = models.IntegerField(blank=True, null=True)
    cotsoff = models.IntegerField(blank=True, null=True)
    cindfam = models.IntegerField(blank=True, null=True)
    cinsfam = models.IntegerField(blank=True, null=True)
    cotsfam = models.IntegerField(blank=True, null=True)
    tufeyr0 = models.IntegerField(blank=True, null=True)
    tufeyr1 = models.IntegerField(blank=True, null=True)
    tufeyr2 = models.IntegerField(blank=True, null=True)
    tufeyr3 = models.IntegerField(blank=True, null=True)
    unitid = models.IntegerField(blank=True, null=True)
    cotsfam_field = models.CharField(db_column='COTSFAM ', max_length=50, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.

    class Meta:
        managed = False
        db_table = 'drvic2023'

class Effy2023(models.Model):
    unitid = models.IntegerField(db_column='UNITID', blank=True, null=True)  # Field name made lowercase.
    effyalev = models.CharField(db_column='EFFYALEV', max_length=50, blank=True, null=True)  # Field name made lowercase.
    effylev = models.CharField(db_column='EFFYLEV', max_length=50, blank=True, null=True)  # Field name made lowercase.
    lstudy = models.CharField(db_column='LSTUDY', max_length=50, blank=True, null=True)  # Field name made lowercase.
    xeytotlt = models.CharField(db_column='XEYTOTLT', max_length=50, blank=True, null=True)  # Field name made lowercase.
    efytotlt = models.IntegerField(db_column='EFYTOTLT', blank=True, null=True)  # Field name made lowercase.
    xeytotlm = models.CharField(db_column='XEYTOTLM', max_length=50, blank=True, null=True)  # Field name made lowercase.
    efytotlm = models.IntegerField(db_column='EFYTOTLM', blank=True, null=True)  # Field name made lowercase.
    xeytotlw = models.CharField(db_column='XEYTOTLW', max_length=50, blank=True, null=True)  # Field name made lowercase.
    efytotlw = models.IntegerField(db_column='EFYTOTLW', blank=True, null=True)  # Field name made lowercase.
    xefyaiat = models.CharField(db_column='XEFYAIAT', max_length=50, blank=True, null=True)  # Field name made lowercase.
    efyaiant = models.IntegerField(db_column='EFYAIANT', blank=True, null=True)  # Field name made lowercase.
    xefyaiam = models.CharField(db_column='XEFYAIAM', max_length=50, blank=True, null=True)  # Field name made lowercase.
    efyaianm = models.IntegerField(db_column='EFYAIANM', blank=True, null=True)  # Field name made lowercase.
    xefyaiaw = models.CharField(db_column='XEFYAIAW', max_length=50, blank=True, null=True)  # Field name made lowercase.
    efyaianw = models.IntegerField(db_column='EFYAIANW', blank=True, null=True)  # Field name made lowercase.
    xefyasit = models.CharField(db_column='XEFYASIT', max_length=50, blank=True, null=True)  # Field name made lowercase.
    efyasiat = models.IntegerField(db_column='EFYASIAT', blank=True, null=True)  # Field name made lowercase.
    xefyasim = models.CharField(db_column='XEFYASIM', max_length=50, blank=True, null=True)  # Field name made lowercase.
    efyasiam = models.IntegerField(db_column='EFYASIAM', blank=True, null=True)  # Field name made lowercase.
    xefyasiw = models.CharField(db_column='XEFYASIW', max_length=50, blank=True, null=True)  # Field name made lowercase.
    efyasiaw = models.IntegerField(db_column='EFYASIAW', blank=True, null=True)  # Field name made lowercase.
    xefybkat = models.CharField(db_column='XEFYBKAT', max_length=50, blank=True, null=True)  # Field name made lowercase.
    efybkaat = models.IntegerField(db_column='EFYBKAAT', blank=True, null=True)  # Field name made lowercase.
    xefybkam = models.CharField(db_column='XEFYBKAM', max_length=50, blank=True, null=True)  # Field name made lowercase.
    efybkaam = models.IntegerField(db_column='EFYBKAAM', blank=True, null=True)  # Field name made lowercase.
    xefybkaw = models.CharField(db_column='XEFYBKAW', max_length=50, blank=True, null=True)  # Field name made lowercase.
    efybkaaw = models.IntegerField(db_column='EFYBKAAW', blank=True, null=True)  # Field name made lowercase.
    xefyhist = models.CharField(db_column='XEFYHIST', max_length=50, blank=True, null=True)  # Field name made lowercase.
    efyhispt = models.IntegerField(db_column='EFYHISPT', blank=True, null=True)  # Field name made lowercase.
    xefyhism = models.CharField(db_column='XEFYHISM', max_length=50, blank=True, null=True)  # Field name made lowercase.
    efyhispm = models.IntegerField(db_column='EFYHISPM', blank=True, null=True)  # Field name made lowercase.
    xefyhisw = models.CharField(db_column='XEFYHISW', max_length=50, blank=True, null=True)  # Field name made lowercase.
    efyhispw = models.IntegerField(db_column='EFYHISPW', blank=True, null=True)  # Field name made lowercase.
    xefynhpt = models.CharField(db_column='XEFYNHPT', max_length=50, blank=True, null=True)  # Field name made lowercase.
    efynhpit = models.IntegerField(db_column='EFYNHPIT', blank=True, null=True)  # Field name made lowercase.
    xefynhpm = models.CharField(db_column='XEFYNHPM', max_length=50, blank=True, null=True)  # Field name made lowercase.
    efynhpim = models.IntegerField(db_column='EFYNHPIM', blank=True, null=True)  # Field name made lowercase.
    xefynhpw = models.CharField(db_column='XEFYNHPW', max_length=50, blank=True, null=True)  # Field name made lowercase.
    efynhpiw = models.IntegerField(db_column='EFYNHPIW', blank=True, null=True)  # Field name made lowercase.
    xefywhit = models.CharField(db_column='XEFYWHIT', max_length=50, blank=True, null=True)  # Field name made lowercase.
    efywhitt = models.IntegerField(db_column='EFYWHITT', blank=True, null=True)  # Field name made lowercase.
    xefywhim = models.CharField(db_column='XEFYWHIM', max_length=50, blank=True, null=True)  # Field name made lowercase.
    efywhitm = models.IntegerField(db_column='EFYWHITM', blank=True, null=True)  # Field name made lowercase.
    xefywhiw = models.CharField(db_column='XEFYWHIW', max_length=50, blank=True, null=True)  # Field name made lowercase.
    efywhitw = models.IntegerField(db_column='EFYWHITW', blank=True, null=True)  # Field name made lowercase.
    xefy2mot = models.CharField(db_column='XEFY2MOT', max_length=50, blank=True, null=True)  # Field name made lowercase.
    efy2mort = models.IntegerField(db_column='EFY2MORT', blank=True, null=True)  # Field name made lowercase.
    xefy2mom = models.CharField(db_column='XEFY2MOM', max_length=50, blank=True, null=True)  # Field name made lowercase.
    efy2morm = models.IntegerField(db_column='EFY2MORM', blank=True, null=True)  # Field name made lowercase.
    xefy2mow = models.CharField(db_column='XEFY2MOW', max_length=50, blank=True, null=True)  # Field name made lowercase.
    efy2morw = models.IntegerField(db_column='EFY2MORW', blank=True, null=True)  # Field name made lowercase.
    xeyunknt = models.CharField(db_column='XEYUNKNT', max_length=50, blank=True, null=True)  # Field name made lowercase.
    efyunknt = models.IntegerField(db_column='EFYUNKNT', blank=True, null=True)  # Field name made lowercase.
    xeyunknm = models.CharField(db_column='XEYUNKNM', max_length=50, blank=True, null=True)  # Field name made lowercase.
    efyunknm = models.IntegerField(db_column='EFYUNKNM', blank=True, null=True)  # Field name made lowercase.
    xeyunknw = models.CharField(db_column='XEYUNKNW', max_length=50, blank=True, null=True)  # Field name made lowercase.
    efyunknw = models.IntegerField(db_column='EFYUNKNW', blank=True, null=True)  # Field name made lowercase.
    xeynralt = models.CharField(db_column='XEYNRALT', max_length=50, blank=True, null=True)  # Field name made lowercase.
    efynralt = models.IntegerField(db_column='EFYNRALT', blank=True, null=True)  # Field name made lowercase.
    xeynralm = models.CharField(db_column='XEYNRALM', max_length=50, blank=True, null=True)  # Field name made lowercase.
    efynralm = models.IntegerField(db_column='EFYNRALM', blank=True, null=True)  # Field name made lowercase.
    xeynralw = models.CharField(db_column='XEYNRALW', max_length=50, blank=True, null=True)  # Field name made lowercase.
    efynralw = models.IntegerField(db_column='EFYNRALW', blank=True, null=True)  # Field name made lowercase.
    xefyguun = models.CharField(db_column='XEFYGUUN', max_length=50, blank=True, null=True)  # Field name made lowercase.
    efyguun = models.IntegerField(db_column='EFYGUUN', blank=True, null=True)  # Field name made lowercase.
    xefyguan = models.CharField(db_column='XEFYGUAN', max_length=50, blank=True, null=True)  # Field name made lowercase.
    efyguan = models.CharField(db_column='EFYGUAN', max_length=50, blank=True, null=True)  # Field name made lowercase.
    xefyguto = models.CharField(db_column='XEFYGUTO', max_length=50, blank=True, null=True)  # Field name made lowercase.
    efygutot = models.IntegerField(db_column='EFYGUTOT', blank=True, null=True)  # Field name made lowercase.
    xefygukn = models.CharField(db_column='XEFYGUKN', max_length=50, blank=True, null=True)  # Field name made lowercase.
    efygukn_field = models.IntegerField(db_column='EFYGUKN ', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.

    class Meta:
        managed = False
        db_table = 'effy2023'

class FrameworkFramework(models.Model):
    id = models.BigAutoField(primary_key=True)
    title = models.CharField(max_length=255)
    pub_date = models.DateTimeField()
    body = models.TextField()
    image = models.CharField(max_length=100)
    index = models.CharField(max_length=20)

    class Meta:
        managed = False
        db_table = 'framework_framework'


class FrameworkImage(models.Model):
    id = models.BigAutoField(primary_key=True)
    title = models.CharField(max_length=100)
    image = models.CharField(max_length=100)
    uploaded_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'framework_image'


class Hd2023(models.Model):
    instnm = models.TextField(blank=True, null=True)
    unitid = models.IntegerField(blank=True, null=False, unique=True, primary_key=True)
    addr = models.TextField(blank=True, null=True)
    city = models.TextField(blank=True, null=True)
    stabbr = models.TextField(blank=True, null=True)
    zip = models.TextField(blank=True, null=True)
    fips = models.IntegerField(blank=True, null=True)
    obereg = models.IntegerField(blank=True, null=True)
    chfnm = models.TextField(blank=True, null=True)
    chftitle = models.TextField(blank=True, null=True)
    gentele = models.TextField(blank=True, null=True)
    faidurl = models.TextField(blank=True, null=True)
    adminurl = models.TextField(blank=True, null=True)
    applurl = models.TextField(blank=True, null=True)
    disaurl = models.TextField(blank=True, null=True)
    ein = models.TextField(blank=True, null=True)
    ueis = models.TextField(blank=True, null=True)
    opeid = models.TextField(blank=True, null=True)
    opeflag = models.IntegerField(blank=True, null=True)
    webaddr = models.TextField(blank=True, null=True)
    npricurl = models.TextField(blank=True, null=True)
    sector = models.IntegerField(blank=True, null=True)
    iclevel = models.IntegerField(blank=True, null=True)
    control = models.IntegerField(blank=True, null=True)
    hloffer = models.IntegerField(blank=True, null=True)
    ugoffer = models.IntegerField(blank=True, null=True)
    groffer = models.IntegerField(blank=True, null=True)
    hdegofr1 = models.IntegerField(blank=True, null=True)
    deggrant = models.IntegerField(blank=True, null=True)
    hbcu = models.IntegerField(blank=True, null=True)
    hospital = models.IntegerField(blank=True, null=True)
    medical = models.IntegerField(blank=True, null=True)
    tribal = models.IntegerField(blank=True, null=True)
    carnegie = models.IntegerField(blank=True, null=True)
    locale = models.IntegerField(blank=True, null=True)
    openpubl = models.IntegerField(blank=True, null=True)
    act = models.TextField(blank=True, null=True)
    newid = models.IntegerField(blank=True, null=True)
    deathyr = models.IntegerField(blank=True, null=True)
    closedat = models.TextField(blank=True, null=True)
    cyactive = models.IntegerField(blank=True, null=True)
    postsec = models.IntegerField(blank=True, null=True)
    pseflag = models.IntegerField(blank=True, null=True)
    pset4flg = models.IntegerField(blank=True, null=True)
    rptmth = models.IntegerField(blank=True, null=True)
    instcat = models.IntegerField(blank=True, null=True)
    ccbasic = models.IntegerField(blank=True, null=True)
    landgrnt = models.IntegerField(blank=True, null=True)
    dfrcgid = models.IntegerField(blank=True, null=True)
    c15basic = models.IntegerField(blank=True, null=True)
    c21ipug = models.IntegerField(blank=True, null=True)
    c21ipgrd = models.IntegerField(blank=True, null=True)
    c21ugprf = models.IntegerField(blank=True, null=True)
    c21enprf = models.IntegerField(blank=True, null=True)
    c21szset = models.IntegerField(blank=True, null=True)
    c18basic = models.IntegerField(blank=True, null=True)
    c21basic = models.IntegerField(blank=True, null=True)
    dfrcuscg = models.IntegerField(blank=True, null=True)
    f1systyp = models.IntegerField(blank=True, null=True)
    f1syscod = models.TextField(blank=True, null=True)
    f1sysnam = models.TextField(blank=True, null=True)
    ialias = models.TextField(blank=True, null=True)
    cbsa = models.IntegerField(blank=True, null=True)
    cbsatype = models.IntegerField(blank=True, null=True)
    csa = models.IntegerField(blank=True, null=True)
    longitud = models.FloatField(blank=True, null=True)
    latitude = models.FloatField(blank=True, null=True)
    countycd = models.IntegerField(blank=True, null=True)
    countynm = models.TextField(blank=True, null=True)
    cngdstcd = models.IntegerField(blank=True, null=True)
    veturl = models.TextField(blank=True, null=True)
    instsize = models.IntegerField(blank=True, null=True)
    athurl = models.TextField(blank=True, null=True)
    

    class Meta:
        managed = False
        db_table = 'hd2023'


class Ic2019Ay(models.Model):
    unitid = models.IntegerField(db_column='UNITID', blank=True, null=True)  # Field name made lowercase.
    xtuit1 = models.CharField(db_column='XTUIT1', max_length=50, blank=True, null=True)  # Field name made lowercase.
    tuition1 = models.CharField(db_column='TUITION1', max_length=50, blank=True, null=True)  # Field name made lowercase.
    xfee1 = models.CharField(db_column='XFEE1', max_length=50, blank=True, null=True)  # Field name made lowercase.
    fee1 = models.CharField(db_column='FEE1', max_length=50, blank=True, null=True)  # Field name made lowercase.
    xhrchg1 = models.CharField(db_column='XHRCHG1', max_length=50, blank=True, null=True)  # Field name made lowercase.
    hrchg1 = models.CharField(db_column='HRCHG1', max_length=50, blank=True, null=True)  # Field name made lowercase.
    xtuit2 = models.CharField(db_column='XTUIT2', max_length=50, blank=True, null=True)  # Field name made lowercase.
    tuition2 = models.CharField(db_column='TUITION2', max_length=50, blank=True, null=True)  # Field name made lowercase.
    xfee2 = models.CharField(db_column='XFEE2', max_length=50, blank=True, null=True)  # Field name made lowercase.
    fee2 = models.CharField(db_column='FEE2', max_length=50, blank=True, null=True)  # Field name made lowercase.
    xhrchg2 = models.CharField(db_column='XHRCHG2', max_length=50, blank=True, null=True)  # Field name made lowercase.
    hrchg2 = models.CharField(db_column='HRCHG2', max_length=50, blank=True, null=True)  # Field name made lowercase.
    xtuit3 = models.CharField(db_column='XTUIT3', max_length=50, blank=True, null=True)  # Field name made lowercase.
    tuition3 = models.CharField(db_column='TUITION3', max_length=50, blank=True, null=True)  # Field name made lowercase.
    xfee3 = models.CharField(db_column='XFEE3', max_length=50, blank=True, null=True)  # Field name made lowercase.
    fee3 = models.CharField(db_column='FEE3', max_length=50, blank=True, null=True)  # Field name made lowercase.
    xhrchg3 = models.CharField(db_column='XHRCHG3', max_length=50, blank=True, null=True)  # Field name made lowercase.
    hrchg3 = models.CharField(db_column='HRCHG3', max_length=50, blank=True, null=True)  # Field name made lowercase.
    xtuit5 = models.CharField(db_column='XTUIT5', max_length=50, blank=True, null=True)  # Field name made lowercase.
    tuition5 = models.CharField(db_column='TUITION5', max_length=50, blank=True, null=True)  # Field name made lowercase.
    xfee5 = models.CharField(db_column='XFEE5', max_length=50, blank=True, null=True)  # Field name made lowercase.
    fee5 = models.CharField(db_column='FEE5', max_length=50, blank=True, null=True)  # Field name made lowercase.
    xhrchg5 = models.CharField(db_column='XHRCHG5', max_length=50, blank=True, null=True)  # Field name made lowercase.
    hrchg5 = models.CharField(db_column='HRCHG5', max_length=50, blank=True, null=True)  # Field name made lowercase.
    xtuit6 = models.CharField(db_column='XTUIT6', max_length=50, blank=True, null=True)  # Field name made lowercase.
    tuition6 = models.CharField(db_column='TUITION6', max_length=50, blank=True, null=True)  # Field name made lowercase.
    xfee6 = models.CharField(db_column='XFEE6', max_length=50, blank=True, null=True)  # Field name made lowercase.
    fee6 = models.CharField(db_column='FEE6', max_length=50, blank=True, null=True)  # Field name made lowercase.
    xhrchg6 = models.CharField(db_column='XHRCHG6', max_length=50, blank=True, null=True)  # Field name made lowercase.
    hrchg6 = models.CharField(db_column='HRCHG6', max_length=50, blank=True, null=True)  # Field name made lowercase.
    xtuit7 = models.CharField(db_column='XTUIT7', max_length=50, blank=True, null=True)  # Field name made lowercase.
    tuition7 = models.CharField(db_column='TUITION7', max_length=50, blank=True, null=True)  # Field name made lowercase.
    xfee7 = models.CharField(db_column='XFEE7', max_length=50, blank=True, null=True)  # Field name made lowercase.
    fee7 = models.CharField(db_column='FEE7', max_length=50, blank=True, null=True)  # Field name made lowercase.
    xhrchg7 = models.CharField(db_column='XHRCHG7', max_length=50, blank=True, null=True)  # Field name made lowercase.
    hrchg7 = models.CharField(db_column='HRCHG7', max_length=50, blank=True, null=True)  # Field name made lowercase.
    xispro1 = models.CharField(db_column='XISPRO1', max_length=50, blank=True, null=True)  # Field name made lowercase.
    isprof1 = models.CharField(db_column='ISPROF1', max_length=50, blank=True, null=True)  # Field name made lowercase.
    xispfe1 = models.CharField(db_column='XISPFE1', max_length=50, blank=True, null=True)  # Field name made lowercase.
    ispfee1 = models.CharField(db_column='ISPFEE1', max_length=50, blank=True, null=True)  # Field name made lowercase.
    xospro1 = models.CharField(db_column='XOSPRO1', max_length=50, blank=True, null=True)  # Field name made lowercase.
    osprof1 = models.CharField(db_column='OSPROF1', max_length=50, blank=True, null=True)  # Field name made lowercase.
    xospfe1 = models.CharField(db_column='XOSPFE1', max_length=50, blank=True, null=True)  # Field name made lowercase.
    ospfee1 = models.CharField(db_column='OSPFEE1', max_length=50, blank=True, null=True)  # Field name made lowercase.
    xispro2 = models.CharField(db_column='XISPRO2', max_length=50, blank=True, null=True)  # Field name made lowercase.
    isprof2 = models.CharField(db_column='ISPROF2', max_length=50, blank=True, null=True)  # Field name made lowercase.
    xispfe2 = models.CharField(db_column='XISPFE2', max_length=50, blank=True, null=True)  # Field name made lowercase.
    ispfee2 = models.CharField(db_column='ISPFEE2', max_length=50, blank=True, null=True)  # Field name made lowercase.
    xospro2 = models.CharField(db_column='XOSPRO2', max_length=50, blank=True, null=True)  # Field name made lowercase.
    osprof2 = models.CharField(db_column='OSPROF2', max_length=50, blank=True, null=True)  # Field name made lowercase.
    xospfe2 = models.CharField(db_column='XOSPFE2', max_length=50, blank=True, null=True)  # Field name made lowercase.
    ospfee2 = models.CharField(db_column='OSPFEE2', max_length=50, blank=True, null=True)  # Field name made lowercase.
    xispro3 = models.CharField(db_column='XISPRO3', max_length=50, blank=True, null=True)  # Field name made lowercase.
    isprof3 = models.CharField(db_column='ISPROF3', max_length=50, blank=True, null=True)  # Field name made lowercase.
    xispfe3 = models.CharField(db_column='XISPFE3', max_length=50, blank=True, null=True)  # Field name made lowercase.
    ispfee3 = models.CharField(db_column='ISPFEE3', max_length=50, blank=True, null=True)  # Field name made lowercase.
    xospro3 = models.CharField(db_column='XOSPRO3', max_length=50, blank=True, null=True)  # Field name made lowercase.
    osprof3 = models.CharField(db_column='OSPROF3', max_length=50, blank=True, null=True)  # Field name made lowercase.
    xospfe3 = models.CharField(db_column='XOSPFE3', max_length=50, blank=True, null=True)  # Field name made lowercase.
    ospfee3 = models.CharField(db_column='OSPFEE3', max_length=50, blank=True, null=True)  # Field name made lowercase.
    xispro4 = models.CharField(db_column='XISPRO4', max_length=50, blank=True, null=True)  # Field name made lowercase.
    isprof4 = models.CharField(db_column='ISPROF4', max_length=50, blank=True, null=True)  # Field name made lowercase.
    xispfe4 = models.CharField(db_column='XISPFE4', max_length=50, blank=True, null=True)  # Field name made lowercase.
    ispfee4 = models.CharField(db_column='ISPFEE4', max_length=50, blank=True, null=True)  # Field name made lowercase.
    xospro4 = models.CharField(db_column='XOSPRO4', max_length=50, blank=True, null=True)  # Field name made lowercase.
    osprof4 = models.CharField(db_column='OSPROF4', max_length=50, blank=True, null=True)  # Field name made lowercase.
    xospfe4 = models.CharField(db_column='XOSPFE4', max_length=50, blank=True, null=True)  # Field name made lowercase.
    ospfee4 = models.CharField(db_column='OSPFEE4', max_length=50, blank=True, null=True)  # Field name made lowercase.
    xispro5 = models.CharField(db_column='XISPRO5', max_length=50, blank=True, null=True)  # Field name made lowercase.
    isprof5 = models.CharField(db_column='ISPROF5', max_length=50, blank=True, null=True)  # Field name made lowercase.
    xispfe5 = models.CharField(db_column='XISPFE5', max_length=50, blank=True, null=True)  # Field name made lowercase.
    ispfee5 = models.CharField(db_column='ISPFEE5', max_length=50, blank=True, null=True)  # Field name made lowercase.
    xospro5 = models.CharField(db_column='XOSPRO5', max_length=50, blank=True, null=True)  # Field name made lowercase.
    osprof5 = models.CharField(db_column='OSPROF5', max_length=50, blank=True, null=True)  # Field name made lowercase.
    xospfe5 = models.CharField(db_column='XOSPFE5', max_length=50, blank=True, null=True)  # Field name made lowercase.
    ospfee5 = models.CharField(db_column='OSPFEE5', max_length=50, blank=True, null=True)  # Field name made lowercase.
    xispro6 = models.CharField(db_column='XISPRO6', max_length=50, blank=True, null=True)  # Field name made lowercase.
    isprof6 = models.CharField(db_column='ISPROF6', max_length=50, blank=True, null=True)  # Field name made lowercase.
    xispfe6 = models.CharField(db_column='XISPFE6', max_length=50, blank=True, null=True)  # Field name made lowercase.
    ispfee6 = models.CharField(db_column='ISPFEE6', max_length=50, blank=True, null=True)  # Field name made lowercase.
    xospro6 = models.CharField(db_column='XOSPRO6', max_length=50, blank=True, null=True)  # Field name made lowercase.
    osprof6 = models.CharField(db_column='OSPROF6', max_length=50, blank=True, null=True)  # Field name made lowercase.
    xospfe6 = models.CharField(db_column='XOSPFE6', max_length=50, blank=True, null=True)  # Field name made lowercase.
    ospfee6 = models.CharField(db_column='OSPFEE6', max_length=50, blank=True, null=True)  # Field name made lowercase.
    xispro7 = models.CharField(db_column='XISPRO7', max_length=50, blank=True, null=True)  # Field name made lowercase.
    isprof7 = models.CharField(db_column='ISPROF7', max_length=50, blank=True, null=True)  # Field name made lowercase.
    xispfe7 = models.CharField(db_column='XISPFE7', max_length=50, blank=True, null=True)  # Field name made lowercase.
    ispfee7 = models.CharField(db_column='ISPFEE7', max_length=50, blank=True, null=True)  # Field name made lowercase.
    xospro7 = models.CharField(db_column='XOSPRO7', max_length=50, blank=True, null=True)  # Field name made lowercase.
    osprof7 = models.CharField(db_column='OSPROF7', max_length=50, blank=True, null=True)  # Field name made lowercase.
    xospfe7 = models.CharField(db_column='XOSPFE7', max_length=50, blank=True, null=True)  # Field name made lowercase.
    ospfee7 = models.CharField(db_column='OSPFEE7', max_length=50, blank=True, null=True)  # Field name made lowercase.
    xispro8 = models.CharField(db_column='XISPRO8', max_length=50, blank=True, null=True)  # Field name made lowercase.
    isprof8 = models.CharField(db_column='ISPROF8', max_length=50, blank=True, null=True)  # Field name made lowercase.
    xispfe8 = models.CharField(db_column='XISPFE8', max_length=50, blank=True, null=True)  # Field name made lowercase.
    ispfee8 = models.CharField(db_column='ISPFEE8', max_length=50, blank=True, null=True)  # Field name made lowercase.
    xospro8 = models.CharField(db_column='XOSPRO8', max_length=50, blank=True, null=True)  # Field name made lowercase.
    osprof8 = models.CharField(db_column='OSPROF8', max_length=50, blank=True, null=True)  # Field name made lowercase.
    xospfe8 = models.CharField(db_column='XOSPFE8', max_length=50, blank=True, null=True)  # Field name made lowercase.
    ospfee8 = models.CharField(db_column='OSPFEE8', max_length=50, blank=True, null=True)  # Field name made lowercase.
    xispro9 = models.CharField(db_column='XISPRO9', max_length=50, blank=True, null=True)  # Field name made lowercase.
    isprof9 = models.CharField(db_column='ISPROF9', max_length=50, blank=True, null=True)  # Field name made lowercase.
    xispfe9 = models.CharField(db_column='XISPFE9', max_length=50, blank=True, null=True)  # Field name made lowercase.
    ispfee9 = models.CharField(db_column='ISPFEE9', max_length=50, blank=True, null=True)  # Field name made lowercase.
    xospro9 = models.CharField(db_column='XOSPRO9', max_length=50, blank=True, null=True)  # Field name made lowercase.
    osprof9 = models.CharField(db_column='OSPROF9', max_length=50, blank=True, null=True)  # Field name made lowercase.
    xospfe9 = models.CharField(db_column='XOSPFE9', max_length=50, blank=True, null=True)  # Field name made lowercase.
    ospfee9 = models.CharField(db_column='OSPFEE9', max_length=50, blank=True, null=True)  # Field name made lowercase.
    xchg1at0 = models.CharField(db_column='XCHG1AT0', max_length=50, blank=True, null=True)  # Field name made lowercase.
    chg1at0 = models.CharField(db_column='CHG1AT0', max_length=50, blank=True, null=True)  # Field name made lowercase.
    xchg1af0 = models.CharField(db_column='XCHG1AF0', max_length=50, blank=True, null=True)  # Field name made lowercase.
    chg1af0 = models.CharField(db_column='CHG1AF0', max_length=50, blank=True, null=True)  # Field name made lowercase.
    xchg1ay0 = models.CharField(db_column='XCHG1AY0', max_length=50, blank=True, null=True)  # Field name made lowercase.
    chg1ay0 = models.CharField(db_column='CHG1AY0', max_length=50, blank=True, null=True)  # Field name made lowercase.
    xchg1at1 = models.CharField(db_column='XCHG1AT1', max_length=50, blank=True, null=True)  # Field name made lowercase.
    chg1at1 = models.CharField(db_column='CHG1AT1', max_length=50, blank=True, null=True)  # Field name made lowercase.
    xchg1af1 = models.CharField(db_column='XCHG1AF1', max_length=50, blank=True, null=True)  # Field name made lowercase.
    chg1af1 = models.CharField(db_column='CHG1AF1', max_length=50, blank=True, null=True)  # Field name made lowercase.
    xchg1ay1 = models.CharField(db_column='XCHG1AY1', max_length=50, blank=True, null=True)  # Field name made lowercase.
    chg1ay1 = models.CharField(db_column='CHG1AY1', max_length=50, blank=True, null=True)  # Field name made lowercase.
    xchg1at2 = models.CharField(db_column='XCHG1AT2', max_length=50, blank=True, null=True)  # Field name made lowercase.
    chg1at2 = models.CharField(db_column='CHG1AT2', max_length=50, blank=True, null=True)  # Field name made lowercase.
    xchg1af2 = models.CharField(db_column='XCHG1AF2', max_length=50, blank=True, null=True)  # Field name made lowercase.
    chg1af2 = models.CharField(db_column='CHG1AF2', max_length=50, blank=True, null=True)  # Field name made lowercase.
    xchg1ay2 = models.CharField(db_column='XCHG1AY2', max_length=50, blank=True, null=True)  # Field name made lowercase.
    chg1ay2 = models.CharField(db_column='CHG1AY2', max_length=50, blank=True, null=True)  # Field name made lowercase.
    xchg1at3 = models.CharField(db_column='XCHG1AT3', max_length=50, blank=True, null=True)  # Field name made lowercase.
    chg1at3 = models.CharField(db_column='CHG1AT3', max_length=50, blank=True, null=True)  # Field name made lowercase.
    xchg1af3 = models.CharField(db_column='XCHG1AF3', max_length=50, blank=True, null=True)  # Field name made lowercase.
    chg1af3 = models.CharField(db_column='CHG1AF3', max_length=50, blank=True, null=True)  # Field name made lowercase.
    xchg1ay3 = models.CharField(db_column='XCHG1AY3', max_length=50, blank=True, null=True)  # Field name made lowercase.
    chg1ay3 = models.CharField(db_column='CHG1AY3', max_length=50, blank=True, null=True)  # Field name made lowercase.
    chg1tgtd = models.CharField(db_column='CHG1TGTD', max_length=50, blank=True, null=True)  # Field name made lowercase.
    chg1fgtd = models.CharField(db_column='CHG1FGTD', max_length=50, blank=True, null=True)  # Field name made lowercase.
    xchg2at0 = models.CharField(db_column='XCHG2AT0', max_length=50, blank=True, null=True)  # Field name made lowercase.
    chg2at0 = models.CharField(db_column='CHG2AT0', max_length=50, blank=True, null=True)  # Field name made lowercase.
    xchg2af0 = models.CharField(db_column='XCHG2AF0', max_length=50, blank=True, null=True)  # Field name made lowercase.
    chg2af0 = models.CharField(db_column='CHG2AF0', max_length=50, blank=True, null=True)  # Field name made lowercase.
    xchg2ay0 = models.CharField(db_column='XCHG2AY0', max_length=50, blank=True, null=True)  # Field name made lowercase.
    chg2ay0 = models.CharField(db_column='CHG2AY0', max_length=50, blank=True, null=True)  # Field name made lowercase.
    xchg2at1 = models.CharField(db_column='XCHG2AT1', max_length=50, blank=True, null=True)  # Field name made lowercase.
    chg2at1 = models.CharField(db_column='CHG2AT1', max_length=50, blank=True, null=True)  # Field name made lowercase.
    xchg2af1 = models.CharField(db_column='XCHG2AF1', max_length=50, blank=True, null=True)  # Field name made lowercase.
    chg2af1 = models.CharField(db_column='CHG2AF1', max_length=50, blank=True, null=True)  # Field name made lowercase.
    xchg2ay1 = models.CharField(db_column='XCHG2AY1', max_length=50, blank=True, null=True)  # Field name made lowercase.
    chg2ay1 = models.CharField(db_column='CHG2AY1', max_length=50, blank=True, null=True)  # Field name made lowercase.
    xchg2at2 = models.CharField(db_column='XCHG2AT2', max_length=50, blank=True, null=True)  # Field name made lowercase.
    chg2at2 = models.CharField(db_column='CHG2AT2', max_length=50, blank=True, null=True)  # Field name made lowercase.
    xchg2af2 = models.CharField(db_column='XCHG2AF2', max_length=50, blank=True, null=True)  # Field name made lowercase.
    chg2af2 = models.CharField(db_column='CHG2AF2', max_length=50, blank=True, null=True)  # Field name made lowercase.
    xchg2ay2 = models.CharField(db_column='XCHG2AY2', max_length=50, blank=True, null=True)  # Field name made lowercase.
    chg2ay2 = models.CharField(db_column='CHG2AY2', max_length=50, blank=True, null=True)  # Field name made lowercase.
    xchg2at3 = models.CharField(db_column='XCHG2AT3', max_length=50, blank=True, null=True)  # Field name made lowercase.
    chg2at3 = models.CharField(db_column='CHG2AT3', max_length=50, blank=True, null=True)  # Field name made lowercase.
    xchg2af3 = models.CharField(db_column='XCHG2AF3', max_length=50, blank=True, null=True)  # Field name made lowercase.
    chg2af3 = models.CharField(db_column='CHG2AF3', max_length=50, blank=True, null=True)  # Field name made lowercase.
    xchg2ay3 = models.CharField(db_column='XCHG2AY3', max_length=50, blank=True, null=True)  # Field name made lowercase.
    chg2ay3 = models.CharField(db_column='CHG2AY3', max_length=50, blank=True, null=True)  # Field name made lowercase.
    chg2tgtd = models.CharField(db_column='CHG2TGTD', max_length=50, blank=True, null=True)  # Field name made lowercase.
    chg2fgtd = models.CharField(db_column='CHG2FGTD', max_length=50, blank=True, null=True)  # Field name made lowercase.
    xchg3at0 = models.CharField(db_column='XCHG3AT0', max_length=50, blank=True, null=True)  # Field name made lowercase.
    chg3at0 = models.CharField(db_column='CHG3AT0', max_length=50, blank=True, null=True)  # Field name made lowercase.
    xchg3af0 = models.CharField(db_column='XCHG3AF0', max_length=50, blank=True, null=True)  # Field name made lowercase.
    chg3af0 = models.CharField(db_column='CHG3AF0', max_length=50, blank=True, null=True)  # Field name made lowercase.
    xchg3ay0 = models.CharField(db_column='XCHG3AY0', max_length=50, blank=True, null=True)  # Field name made lowercase.
    chg3ay0 = models.CharField(db_column='CHG3AY0', max_length=50, blank=True, null=True)  # Field name made lowercase.
    xchg3at1 = models.CharField(db_column='XCHG3AT1', max_length=50, blank=True, null=True)  # Field name made lowercase.
    chg3at1 = models.CharField(db_column='CHG3AT1', max_length=50, blank=True, null=True)  # Field name made lowercase.
    xchg3af1 = models.CharField(db_column='XCHG3AF1', max_length=50, blank=True, null=True)  # Field name made lowercase.
    chg3af1 = models.CharField(db_column='CHG3AF1', max_length=50, blank=True, null=True)  # Field name made lowercase.
    xchg3ay1 = models.CharField(db_column='XCHG3AY1', max_length=50, blank=True, null=True)  # Field name made lowercase.
    chg3ay1 = models.CharField(db_column='CHG3AY1', max_length=50, blank=True, null=True)  # Field name made lowercase.
    xchg3at2 = models.CharField(db_column='XCHG3AT2', max_length=50, blank=True, null=True)  # Field name made lowercase.
    chg3at2 = models.CharField(db_column='CHG3AT2', max_length=50, blank=True, null=True)  # Field name made lowercase.
    xchg3af2 = models.CharField(db_column='XCHG3AF2', max_length=50, blank=True, null=True)  # Field name made lowercase.
    chg3af2 = models.CharField(db_column='CHG3AF2', max_length=50, blank=True, null=True)  # Field name made lowercase.
    xchg3ay2 = models.CharField(db_column='XCHG3AY2', max_length=50, blank=True, null=True)  # Field name made lowercase.
    chg3ay2 = models.CharField(db_column='CHG3AY2', max_length=50, blank=True, null=True)  # Field name made lowercase.
    xchg3at3 = models.CharField(db_column='XCHG3AT3', max_length=50, blank=True, null=True)  # Field name made lowercase.
    chg3at3 = models.CharField(db_column='CHG3AT3', max_length=50, blank=True, null=True)  # Field name made lowercase.
    xchg3af3 = models.CharField(db_column='XCHG3AF3', max_length=50, blank=True, null=True)  # Field name made lowercase.
    chg3af3 = models.CharField(db_column='CHG3AF3', max_length=50, blank=True, null=True)  # Field name made lowercase.
    xchg3ay3 = models.CharField(db_column='XCHG3AY3', max_length=50, blank=True, null=True)  # Field name made lowercase.
    chg3ay3 = models.CharField(db_column='CHG3AY3', max_length=50, blank=True, null=True)  # Field name made lowercase.
    chg3tgtd = models.CharField(db_column='CHG3TGTD', max_length=50, blank=True, null=True)  # Field name made lowercase.
    chg3fgtd = models.CharField(db_column='CHG3FGTD', max_length=50, blank=True, null=True)  # Field name made lowercase.
    xchg4ay0 = models.CharField(db_column='XCHG4AY0', max_length=50, blank=True, null=True)  # Field name made lowercase.
    chg4ay0 = models.CharField(db_column='CHG4AY0', max_length=50, blank=True, null=True)  # Field name made lowercase.
    xchg4ay1 = models.CharField(db_column='XCHG4AY1', max_length=50, blank=True, null=True)  # Field name made lowercase.
    chg4ay1 = models.CharField(db_column='CHG4AY1', max_length=50, blank=True, null=True)  # Field name made lowercase.
    xchg4ay2 = models.CharField(db_column='XCHG4AY2', max_length=50, blank=True, null=True)  # Field name made lowercase.
    chg4ay2 = models.CharField(db_column='CHG4AY2', max_length=50, blank=True, null=True)  # Field name made lowercase.
    xchg4ay3 = models.CharField(db_column='XCHG4AY3', max_length=50, blank=True, null=True)  # Field name made lowercase.
    chg4ay3 = models.CharField(db_column='CHG4AY3', max_length=50, blank=True, null=True)  # Field name made lowercase.
    xchg5ay0 = models.CharField(db_column='XCHG5AY0', max_length=50, blank=True, null=True)  # Field name made lowercase.
    chg5ay0 = models.CharField(db_column='CHG5AY0', max_length=50, blank=True, null=True)  # Field name made lowercase.
    xchg5ay1 = models.CharField(db_column='XCHG5AY1', max_length=50, blank=True, null=True)  # Field name made lowercase.
    chg5ay1 = models.CharField(db_column='CHG5AY1', max_length=50, blank=True, null=True)  # Field name made lowercase.
    xchg5ay2 = models.CharField(db_column='XCHG5AY2', max_length=50, blank=True, null=True)  # Field name made lowercase.
    chg5ay2 = models.CharField(db_column='CHG5AY2', max_length=50, blank=True, null=True)  # Field name made lowercase.
    xchg5ay3 = models.CharField(db_column='XCHG5AY3', max_length=50, blank=True, null=True)  # Field name made lowercase.
    chg5ay3 = models.CharField(db_column='CHG5AY3', max_length=50, blank=True, null=True)  # Field name made lowercase.
    xchg6ay0 = models.CharField(db_column='XCHG6AY0', max_length=50, blank=True, null=True)  # Field name made lowercase.
    chg6ay0 = models.CharField(db_column='CHG6AY0', max_length=50, blank=True, null=True)  # Field name made lowercase.
    xchg6ay1 = models.CharField(db_column='XCHG6AY1', max_length=50, blank=True, null=True)  # Field name made lowercase.
    chg6ay1 = models.CharField(db_column='CHG6AY1', max_length=50, blank=True, null=True)  # Field name made lowercase.
    xchg6ay2 = models.CharField(db_column='XCHG6AY2', max_length=50, blank=True, null=True)  # Field name made lowercase.
    chg6ay2 = models.CharField(db_column='CHG6AY2', max_length=50, blank=True, null=True)  # Field name made lowercase.
    xchg6ay3 = models.CharField(db_column='XCHG6AY3', max_length=50, blank=True, null=True)  # Field name made lowercase.
    chg6ay3 = models.CharField(db_column='CHG6AY3', max_length=50, blank=True, null=True)  # Field name made lowercase.
    xchg7ay0 = models.CharField(db_column='XCHG7AY0', max_length=50, blank=True, null=True)  # Field name made lowercase.
    chg7ay0 = models.CharField(db_column='CHG7AY0', max_length=50, blank=True, null=True)  # Field name made lowercase.
    xchg7ay1 = models.CharField(db_column='XCHG7AY1', max_length=50, blank=True, null=True)  # Field name made lowercase.
    chg7ay1 = models.CharField(db_column='CHG7AY1', max_length=50, blank=True, null=True)  # Field name made lowercase.
    xchg7ay2 = models.CharField(db_column='XCHG7AY2', max_length=50, blank=True, null=True)  # Field name made lowercase.
    chg7ay2 = models.CharField(db_column='CHG7AY2', max_length=50, blank=True, null=True)  # Field name made lowercase.
    xchg7ay3 = models.CharField(db_column='XCHG7AY3', max_length=50, blank=True, null=True)  # Field name made lowercase.
    chg7ay3 = models.CharField(db_column='CHG7AY3', max_length=50, blank=True, null=True)  # Field name made lowercase.
    xchg8ay0 = models.CharField(db_column='XCHG8AY0', max_length=50, blank=True, null=True)  # Field name made lowercase.
    chg8ay0 = models.CharField(db_column='CHG8AY0', max_length=50, blank=True, null=True)  # Field name made lowercase.
    xchg8ay1 = models.CharField(db_column='XCHG8AY1', max_length=50, blank=True, null=True)  # Field name made lowercase.
    chg8ay1 = models.CharField(db_column='CHG8AY1', max_length=50, blank=True, null=True)  # Field name made lowercase.
    xchg8ay2 = models.CharField(db_column='XCHG8AY2', max_length=50, blank=True, null=True)  # Field name made lowercase.
    chg8ay2 = models.CharField(db_column='CHG8AY2', max_length=50, blank=True, null=True)  # Field name made lowercase.
    xchg8ay3 = models.CharField(db_column='XCHG8AY3', max_length=50, blank=True, null=True)  # Field name made lowercase.
    chg8ay3 = models.CharField(db_column='CHG8AY3', max_length=50, blank=True, null=True)  # Field name made lowercase.
    xchg9ay0 = models.CharField(db_column='XCHG9AY0', max_length=50, blank=True, null=True)  # Field name made lowercase.
    chg9ay0 = models.CharField(db_column='CHG9AY0', max_length=50, blank=True, null=True)  # Field name made lowercase.
    xchg9ay1 = models.CharField(db_column='XCHG9AY1', max_length=50, blank=True, null=True)  # Field name made lowercase.
    chg9ay1 = models.CharField(db_column='CHG9AY1', max_length=50, blank=True, null=True)  # Field name made lowercase.
    xchg9ay2 = models.CharField(db_column='XCHG9AY2', max_length=50, blank=True, null=True)  # Field name made lowercase.
    chg9ay2 = models.CharField(db_column='CHG9AY2', max_length=50, blank=True, null=True)  # Field name made lowercase.
    xchg9ay3 = models.CharField(db_column='XCHG9AY3', max_length=50, blank=True, null=True)  # Field name made lowercase.
    chg9ay3_field = models.CharField(db_column='CHG9AY3 ', max_length=50, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.

    class Meta:
        managed = False
        db_table = 'ic2019_ay'


class Ic2023Ay(models.Model):
    unitid = models.IntegerField(db_column='UNITID', blank=True, null=True)  # Field name made lowercase.
    xtuit1 = models.CharField(db_column='XTUIT1', max_length=50, blank=True, null=True)  # Field name made lowercase.
    tuition1 = models.CharField(db_column='TUITION1', max_length=50, blank=True, null=True)  # Field name made lowercase.
    xfee1 = models.CharField(db_column='XFEE1', max_length=50, blank=True, null=True)  # Field name made lowercase.
    fee1 = models.CharField(db_column='FEE1', max_length=50, blank=True, null=True)  # Field name made lowercase.
    xhrchg1 = models.CharField(db_column='XHRCHG1', max_length=50, blank=True, null=True)  # Field name made lowercase.
    hrchg1 = models.CharField(db_column='HRCHG1', max_length=50, blank=True, null=True)  # Field name made lowercase.
    xtuit2 = models.CharField(db_column='XTUIT2', max_length=50, blank=True, null=True)  # Field name made lowercase.
    tuition2 = models.CharField(db_column='TUITION2', max_length=50, blank=True, null=True)  # Field name made lowercase.
    xfee2 = models.CharField(db_column='XFEE2', max_length=50, blank=True, null=True)  # Field name made lowercase.
    fee2 = models.CharField(db_column='FEE2', max_length=50, blank=True, null=True)  # Field name made lowercase.
    xhrchg2 = models.CharField(db_column='XHRCHG2', max_length=50, blank=True, null=True)  # Field name made lowercase.
    hrchg2 = models.CharField(db_column='HRCHG2', max_length=50, blank=True, null=True)  # Field name made lowercase.
    xtuit3 = models.CharField(db_column='XTUIT3', max_length=50, blank=True, null=True)  # Field name made lowercase.
    tuition3 = models.CharField(db_column='TUITION3', max_length=50, blank=True, null=True)  # Field name made lowercase.
    xfee3 = models.CharField(db_column='XFEE3', max_length=50, blank=True, null=True)  # Field name made lowercase.
    fee3 = models.CharField(db_column='FEE3', max_length=50, blank=True, null=True)  # Field name made lowercase.
    xhrchg3 = models.CharField(db_column='XHRCHG3', max_length=50, blank=True, null=True)  # Field name made lowercase.
    hrchg3 = models.CharField(db_column='HRCHG3', max_length=50, blank=True, null=True)  # Field name made lowercase.
    xtuit5 = models.CharField(db_column='XTUIT5', max_length=50, blank=True, null=True)  # Field name made lowercase.
    tuition5 = models.CharField(db_column='TUITION5', max_length=50, blank=True, null=True)  # Field name made lowercase.
    xfee5 = models.CharField(db_column='XFEE5', max_length=50, blank=True, null=True)  # Field name made lowercase.
    fee5 = models.CharField(db_column='FEE5', max_length=50, blank=True, null=True)  # Field name made lowercase.
    xhrchg5 = models.CharField(db_column='XHRCHG5', max_length=50, blank=True, null=True)  # Field name made lowercase.
    hrchg5 = models.CharField(db_column='HRCHG5', max_length=50, blank=True, null=True)  # Field name made lowercase.
    xtuit6 = models.CharField(db_column='XTUIT6', max_length=50, blank=True, null=True)  # Field name made lowercase.
    tuition6 = models.CharField(db_column='TUITION6', max_length=50, blank=True, null=True)  # Field name made lowercase.
    xfee6 = models.CharField(db_column='XFEE6', max_length=50, blank=True, null=True)  # Field name made lowercase.
    fee6 = models.CharField(db_column='FEE6', max_length=50, blank=True, null=True)  # Field name made lowercase.
    xhrchg6 = models.CharField(db_column='XHRCHG6', max_length=50, blank=True, null=True)  # Field name made lowercase.
    hrchg6 = models.CharField(db_column='HRCHG6', max_length=50, blank=True, null=True)  # Field name made lowercase.
    xtuit7 = models.CharField(db_column='XTUIT7', max_length=50, blank=True, null=True)  # Field name made lowercase.
    tuition7 = models.CharField(db_column='TUITION7', max_length=50, blank=True, null=True)  # Field name made lowercase.
    xfee7 = models.CharField(db_column='XFEE7', max_length=50, blank=True, null=True)  # Field name made lowercase.
    fee7 = models.CharField(db_column='FEE7', max_length=50, blank=True, null=True)  # Field name made lowercase.
    xhrchg7 = models.CharField(db_column='XHRCHG7', max_length=50, blank=True, null=True)  # Field name made lowercase.
    hrchg7 = models.CharField(db_column='HRCHG7', max_length=50, blank=True, null=True)  # Field name made lowercase.
    xispro1 = models.CharField(db_column='XISPRO1', max_length=50, blank=True, null=True)  # Field name made lowercase.
    isprof1 = models.CharField(db_column='ISPROF1', max_length=50, blank=True, null=True)  # Field name made lowercase.
    xispfe1 = models.CharField(db_column='XISPFE1', max_length=50, blank=True, null=True)  # Field name made lowercase.
    ispfee1 = models.CharField(db_column='ISPFEE1', max_length=50, blank=True, null=True)  # Field name made lowercase.
    xospro1 = models.CharField(db_column='XOSPRO1', max_length=50, blank=True, null=True)  # Field name made lowercase.
    osprof1 = models.CharField(db_column='OSPROF1', max_length=50, blank=True, null=True)  # Field name made lowercase.
    xospfe1 = models.CharField(db_column='XOSPFE1', max_length=50, blank=True, null=True)  # Field name made lowercase.
    ospfee1 = models.CharField(db_column='OSPFEE1', max_length=50, blank=True, null=True)  # Field name made lowercase.
    xispro2 = models.CharField(db_column='XISPRO2', max_length=50, blank=True, null=True)  # Field name made lowercase.
    isprof2 = models.CharField(db_column='ISPROF2', max_length=50, blank=True, null=True)  # Field name made lowercase.
    xispfe2 = models.CharField(db_column='XISPFE2', max_length=50, blank=True, null=True)  # Field name made lowercase.
    ispfee2 = models.CharField(db_column='ISPFEE2', max_length=50, blank=True, null=True)  # Field name made lowercase.
    xospro2 = models.CharField(db_column='XOSPRO2', max_length=50, blank=True, null=True)  # Field name made lowercase.
    osprof2 = models.CharField(db_column='OSPROF2', max_length=50, blank=True, null=True)  # Field name made lowercase.
    xospfe2 = models.CharField(db_column='XOSPFE2', max_length=50, blank=True, null=True)  # Field name made lowercase.
    ospfee2 = models.CharField(db_column='OSPFEE2', max_length=50, blank=True, null=True)  # Field name made lowercase.
    xispro3 = models.CharField(db_column='XISPRO3', max_length=50, blank=True, null=True)  # Field name made lowercase.
    isprof3 = models.CharField(db_column='ISPROF3', max_length=50, blank=True, null=True)  # Field name made lowercase.
    xispfe3 = models.CharField(db_column='XISPFE3', max_length=50, blank=True, null=True)  # Field name made lowercase.
    ispfee3 = models.CharField(db_column='ISPFEE3', max_length=50, blank=True, null=True)  # Field name made lowercase.
    xospro3 = models.CharField(db_column='XOSPRO3', max_length=50, blank=True, null=True)  # Field name made lowercase.
    osprof3 = models.CharField(db_column='OSPROF3', max_length=50, blank=True, null=True)  # Field name made lowercase.
    xospfe3 = models.CharField(db_column='XOSPFE3', max_length=50, blank=True, null=True)  # Field name made lowercase.
    ospfee3 = models.CharField(db_column='OSPFEE3', max_length=50, blank=True, null=True)  # Field name made lowercase.
    xispro4 = models.CharField(db_column='XISPRO4', max_length=50, blank=True, null=True)  # Field name made lowercase.
    isprof4 = models.CharField(db_column='ISPROF4', max_length=50, blank=True, null=True)  # Field name made lowercase.
    xispfe4 = models.CharField(db_column='XISPFE4', max_length=50, blank=True, null=True)  # Field name made lowercase.
    ispfee4 = models.CharField(db_column='ISPFEE4', max_length=50, blank=True, null=True)  # Field name made lowercase.
    xospro4 = models.CharField(db_column='XOSPRO4', max_length=50, blank=True, null=True)  # Field name made lowercase.
    osprof4 = models.CharField(db_column='OSPROF4', max_length=50, blank=True, null=True)  # Field name made lowercase.
    xospfe4 = models.CharField(db_column='XOSPFE4', max_length=50, blank=True, null=True)  # Field name made lowercase.
    ospfee4 = models.CharField(db_column='OSPFEE4', max_length=50, blank=True, null=True)  # Field name made lowercase.
    xispro5 = models.CharField(db_column='XISPRO5', max_length=50, blank=True, null=True)  # Field name made lowercase.
    isprof5 = models.CharField(db_column='ISPROF5', max_length=50, blank=True, null=True)  # Field name made lowercase.
    xispfe5 = models.CharField(db_column='XISPFE5', max_length=50, blank=True, null=True)  # Field name made lowercase.
    ispfee5 = models.CharField(db_column='ISPFEE5', max_length=50, blank=True, null=True)  # Field name made lowercase.
    xospro5 = models.CharField(db_column='XOSPRO5', max_length=50, blank=True, null=True)  # Field name made lowercase.
    osprof5 = models.CharField(db_column='OSPROF5', max_length=50, blank=True, null=True)  # Field name made lowercase.
    xospfe5 = models.CharField(db_column='XOSPFE5', max_length=50, blank=True, null=True)  # Field name made lowercase.
    ospfee5 = models.CharField(db_column='OSPFEE5', max_length=50, blank=True, null=True)  # Field name made lowercase.
    xispro6 = models.CharField(db_column='XISPRO6', max_length=50, blank=True, null=True)  # Field name made lowercase.
    isprof6 = models.CharField(db_column='ISPROF6', max_length=50, blank=True, null=True)  # Field name made lowercase.
    xispfe6 = models.CharField(db_column='XISPFE6', max_length=50, blank=True, null=True)  # Field name made lowercase.
    ispfee6 = models.CharField(db_column='ISPFEE6', max_length=50, blank=True, null=True)  # Field name made lowercase.
    xospro6 = models.CharField(db_column='XOSPRO6', max_length=50, blank=True, null=True)  # Field name made lowercase.
    osprof6 = models.CharField(db_column='OSPROF6', max_length=50, blank=True, null=True)  # Field name made lowercase.
    xospfe6 = models.CharField(db_column='XOSPFE6', max_length=50, blank=True, null=True)  # Field name made lowercase.
    ospfee6 = models.CharField(db_column='OSPFEE6', max_length=50, blank=True, null=True)  # Field name made lowercase.
    xispro7 = models.CharField(db_column='XISPRO7', max_length=50, blank=True, null=True)  # Field name made lowercase.
    isprof7 = models.CharField(db_column='ISPROF7', max_length=50, blank=True, null=True)  # Field name made lowercase.
    xispfe7 = models.CharField(db_column='XISPFE7', max_length=50, blank=True, null=True)  # Field name made lowercase.
    ispfee7 = models.CharField(db_column='ISPFEE7', max_length=50, blank=True, null=True)  # Field name made lowercase.
    xospro7 = models.CharField(db_column='XOSPRO7', max_length=50, blank=True, null=True)  # Field name made lowercase.
    osprof7 = models.CharField(db_column='OSPROF7', max_length=50, blank=True, null=True)  # Field name made lowercase.
    xospfe7 = models.CharField(db_column='XOSPFE7', max_length=50, blank=True, null=True)  # Field name made lowercase.
    ospfee7 = models.CharField(db_column='OSPFEE7', max_length=50, blank=True, null=True)  # Field name made lowercase.
    xispro8 = models.CharField(db_column='XISPRO8', max_length=50, blank=True, null=True)  # Field name made lowercase.
    isprof8 = models.CharField(db_column='ISPROF8', max_length=50, blank=True, null=True)  # Field name made lowercase.
    xispfe8 = models.CharField(db_column='XISPFE8', max_length=50, blank=True, null=True)  # Field name made lowercase.
    ispfee8 = models.CharField(db_column='ISPFEE8', max_length=50, blank=True, null=True)  # Field name made lowercase.
    xospro8 = models.CharField(db_column='XOSPRO8', max_length=50, blank=True, null=True)  # Field name made lowercase.
    osprof8 = models.CharField(db_column='OSPROF8', max_length=50, blank=True, null=True)  # Field name made lowercase.
    xospfe8 = models.CharField(db_column='XOSPFE8', max_length=50, blank=True, null=True)  # Field name made lowercase.
    ospfee8 = models.CharField(db_column='OSPFEE8', max_length=50, blank=True, null=True)  # Field name made lowercase.
    xispro9 = models.CharField(db_column='XISPRO9', max_length=50, blank=True, null=True)  # Field name made lowercase.
    isprof9 = models.CharField(db_column='ISPROF9', max_length=50, blank=True, null=True)  # Field name made lowercase.
    xispfe9 = models.CharField(db_column='XISPFE9', max_length=50, blank=True, null=True)  # Field name made lowercase.
    ispfee9 = models.CharField(db_column='ISPFEE9', max_length=50, blank=True, null=True)  # Field name made lowercase.
    xospro9 = models.CharField(db_column='XOSPRO9', max_length=50, blank=True, null=True)  # Field name made lowercase.
    osprof9 = models.CharField(db_column='OSPROF9', max_length=50, blank=True, null=True)  # Field name made lowercase.
    xospfe9 = models.CharField(db_column='XOSPFE9', max_length=50, blank=True, null=True)  # Field name made lowercase.
    ospfee9 = models.CharField(db_column='OSPFEE9', max_length=50, blank=True, null=True)  # Field name made lowercase.
    xchg1at0 = models.CharField(db_column='XCHG1AT0', max_length=50, blank=True, null=True)  # Field name made lowercase.
    chg1at0 = models.CharField(db_column='CHG1AT0', max_length=50, blank=True, null=True)  # Field name made lowercase.
    xchg1af0 = models.CharField(db_column='XCHG1AF0', max_length=50, blank=True, null=True)  # Field name made lowercase.
    chg1af0 = models.CharField(db_column='CHG1AF0', max_length=50, blank=True, null=True)  # Field name made lowercase.
    xchg1ay0 = models.CharField(db_column='XCHG1AY0', max_length=50, blank=True, null=True)  # Field name made lowercase.
    chg1ay0 = models.CharField(db_column='CHG1AY0', max_length=50, blank=True, null=True)  # Field name made lowercase.
    xchg1at1 = models.CharField(db_column='XCHG1AT1', max_length=50, blank=True, null=True)  # Field name made lowercase.
    chg1at1 = models.CharField(db_column='CHG1AT1', max_length=50, blank=True, null=True)  # Field name made lowercase.
    xchg1af1 = models.CharField(db_column='XCHG1AF1', max_length=50, blank=True, null=True)  # Field name made lowercase.
    chg1af1 = models.CharField(db_column='CHG1AF1', max_length=50, blank=True, null=True)  # Field name made lowercase.
    xchg1ay1 = models.CharField(db_column='XCHG1AY1', max_length=50, blank=True, null=True)  # Field name made lowercase.
    chg1ay1 = models.CharField(db_column='CHG1AY1', max_length=50, blank=True, null=True)  # Field name made lowercase.
    xchg1at2 = models.CharField(db_column='XCHG1AT2', max_length=50, blank=True, null=True)  # Field name made lowercase.
    chg1at2 = models.CharField(db_column='CHG1AT2', max_length=50, blank=True, null=True)  # Field name made lowercase.
    xchg1af2 = models.CharField(db_column='XCHG1AF2', max_length=50, blank=True, null=True)  # Field name made lowercase.
    chg1af2 = models.CharField(db_column='CHG1AF2', max_length=50, blank=True, null=True)  # Field name made lowercase.
    xchg1ay2 = models.CharField(db_column='XCHG1AY2', max_length=50, blank=True, null=True)  # Field name made lowercase.
    chg1ay2 = models.CharField(db_column='CHG1AY2', max_length=50, blank=True, null=True)  # Field name made lowercase.
    xchg1at3 = models.CharField(db_column='XCHG1AT3', max_length=50, blank=True, null=True)  # Field name made lowercase.
    chg1at3 = models.CharField(db_column='CHG1AT3', max_length=50, blank=True, null=True)  # Field name made lowercase.
    xchg1af3 = models.CharField(db_column='XCHG1AF3', max_length=50, blank=True, null=True)  # Field name made lowercase.
    chg1af3 = models.CharField(db_column='CHG1AF3', max_length=50, blank=True, null=True)  # Field name made lowercase.
    xchg1ay3 = models.CharField(db_column='XCHG1AY3', max_length=50, blank=True, null=True)  # Field name made lowercase.
    chg1ay3 = models.CharField(db_column='CHG1AY3', max_length=50, blank=True, null=True)  # Field name made lowercase.
    chg1tgtd = models.CharField(db_column='CHG1TGTD', max_length=50, blank=True, null=True)  # Field name made lowercase.
    chg1fgtd = models.CharField(db_column='CHG1FGTD', max_length=50, blank=True, null=True)  # Field name made lowercase.
    xchg2at0 = models.CharField(db_column='XCHG2AT0', max_length=50, blank=True, null=True)  # Field name made lowercase.
    chg2at0 = models.CharField(db_column='CHG2AT0', max_length=50, blank=True, null=True)  # Field name made lowercase.
    xchg2af0 = models.CharField(db_column='XCHG2AF0', max_length=50, blank=True, null=True)  # Field name made lowercase.
    chg2af0 = models.CharField(db_column='CHG2AF0', max_length=50, blank=True, null=True)  # Field name made lowercase.
    xchg2ay0 = models.CharField(db_column='XCHG2AY0', max_length=50, blank=True, null=True)  # Field name made lowercase.
    chg2ay0 = models.CharField(db_column='CHG2AY0', max_length=50, blank=True, null=True)  # Field name made lowercase.
    xchg2at1 = models.CharField(db_column='XCHG2AT1', max_length=50, blank=True, null=True)  # Field name made lowercase.
    chg2at1 = models.CharField(db_column='CHG2AT1', max_length=50, blank=True, null=True)  # Field name made lowercase.
    xchg2af1 = models.CharField(db_column='XCHG2AF1', max_length=50, blank=True, null=True)  # Field name made lowercase.
    chg2af1 = models.CharField(db_column='CHG2AF1', max_length=50, blank=True, null=True)  # Field name made lowercase.
    xchg2ay1 = models.CharField(db_column='XCHG2AY1', max_length=50, blank=True, null=True)  # Field name made lowercase.
    chg2ay1 = models.CharField(db_column='CHG2AY1', max_length=50, blank=True, null=True)  # Field name made lowercase.
    xchg2at2 = models.CharField(db_column='XCHG2AT2', max_length=50, blank=True, null=True)  # Field name made lowercase.
    chg2at2 = models.CharField(db_column='CHG2AT2', max_length=50, blank=True, null=True)  # Field name made lowercase.
    xchg2af2 = models.CharField(db_column='XCHG2AF2', max_length=50, blank=True, null=True)  # Field name made lowercase.
    chg2af2 = models.CharField(db_column='CHG2AF2', max_length=50, blank=True, null=True)  # Field name made lowercase.
    xchg2ay2 = models.CharField(db_column='XCHG2AY2', max_length=50, blank=True, null=True)  # Field name made lowercase.
    chg2ay2 = models.CharField(db_column='CHG2AY2', max_length=50, blank=True, null=True)  # Field name made lowercase.
    xchg2at3 = models.CharField(db_column='XCHG2AT3', max_length=50, blank=True, null=True)  # Field name made lowercase.
    chg2at3 = models.CharField(db_column='CHG2AT3', max_length=50, blank=True, null=True)  # Field name made lowercase.
    xchg2af3 = models.CharField(db_column='XCHG2AF3', max_length=50, blank=True, null=True)  # Field name made lowercase.
    chg2af3 = models.CharField(db_column='CHG2AF3', max_length=50, blank=True, null=True)  # Field name made lowercase.
    xchg2ay3 = models.CharField(db_column='XCHG2AY3', max_length=50, blank=True, null=True)  # Field name made lowercase.
    chg2ay3 = models.CharField(db_column='CHG2AY3', max_length=50, blank=True, null=True)  # Field name made lowercase.
    chg2tgtd = models.CharField(db_column='CHG2TGTD', max_length=50, blank=True, null=True)  # Field name made lowercase.
    chg2fgtd = models.CharField(db_column='CHG2FGTD', max_length=50, blank=True, null=True)  # Field name made lowercase.
    xchg3at0 = models.CharField(db_column='XCHG3AT0', max_length=50, blank=True, null=True)  # Field name made lowercase.
    chg3at0 = models.CharField(db_column='CHG3AT0', max_length=50, blank=True, null=True)  # Field name made lowercase.
    xchg3af0 = models.CharField(db_column='XCHG3AF0', max_length=50, blank=True, null=True)  # Field name made lowercase.
    chg3af0 = models.CharField(db_column='CHG3AF0', max_length=50, blank=True, null=True)  # Field name made lowercase.
    xchg3ay0 = models.CharField(db_column='XCHG3AY0', max_length=50, blank=True, null=True)  # Field name made lowercase.
    chg3ay0 = models.CharField(db_column='CHG3AY0', max_length=50, blank=True, null=True)  # Field name made lowercase.
    xchg3at1 = models.CharField(db_column='XCHG3AT1', max_length=50, blank=True, null=True)  # Field name made lowercase.
    chg3at1 = models.CharField(db_column='CHG3AT1', max_length=50, blank=True, null=True)  # Field name made lowercase.
    xchg3af1 = models.CharField(db_column='XCHG3AF1', max_length=50, blank=True, null=True)  # Field name made lowercase.
    chg3af1 = models.CharField(db_column='CHG3AF1', max_length=50, blank=True, null=True)  # Field name made lowercase.
    xchg3ay1 = models.CharField(db_column='XCHG3AY1', max_length=50, blank=True, null=True)  # Field name made lowercase.
    chg3ay1 = models.CharField(db_column='CHG3AY1', max_length=50, blank=True, null=True)  # Field name made lowercase.
    xchg3at2 = models.CharField(db_column='XCHG3AT2', max_length=50, blank=True, null=True)  # Field name made lowercase.
    chg3at2 = models.CharField(db_column='CHG3AT2', max_length=50, blank=True, null=True)  # Field name made lowercase.
    xchg3af2 = models.CharField(db_column='XCHG3AF2', max_length=50, blank=True, null=True)  # Field name made lowercase.
    chg3af2 = models.CharField(db_column='CHG3AF2', max_length=50, blank=True, null=True)  # Field name made lowercase.
    xchg3ay2 = models.CharField(db_column='XCHG3AY2', max_length=50, blank=True, null=True)  # Field name made lowercase.
    chg3ay2 = models.CharField(db_column='CHG3AY2', max_length=50, blank=True, null=True)  # Field name made lowercase.
    xchg3at3 = models.CharField(db_column='XCHG3AT3', max_length=50, blank=True, null=True)  # Field name made lowercase.
    chg3at3 = models.CharField(db_column='CHG3AT3', max_length=50, blank=True, null=True)  # Field name made lowercase.
    xchg3af3 = models.CharField(db_column='XCHG3AF3', max_length=50, blank=True, null=True)  # Field name made lowercase.
    chg3af3 = models.CharField(db_column='CHG3AF3', max_length=50, blank=True, null=True)  # Field name made lowercase.
    xchg3ay3 = models.CharField(db_column='XCHG3AY3', max_length=50, blank=True, null=True)  # Field name made lowercase.
    chg3ay3 = models.CharField(db_column='CHG3AY3', max_length=50, blank=True, null=True)  # Field name made lowercase.
    chg3tgtd = models.CharField(db_column='CHG3TGTD', max_length=50, blank=True, null=True)  # Field name made lowercase.
    chg3fgtd = models.CharField(db_column='CHG3FGTD', max_length=50, blank=True, null=True)  # Field name made lowercase.
    xchg4ay0 = models.CharField(db_column='XCHG4AY0', max_length=50, blank=True, null=True)  # Field name made lowercase.
    chg4ay0 = models.CharField(db_column='CHG4AY0', max_length=50, blank=True, null=True)  # Field name made lowercase.
    xchg4ay1 = models.CharField(db_column='XCHG4AY1', max_length=50, blank=True, null=True)  # Field name made lowercase.
    chg4ay1 = models.CharField(db_column='CHG4AY1', max_length=50, blank=True, null=True)  # Field name made lowercase.
    xchg4ay2 = models.CharField(db_column='XCHG4AY2', max_length=50, blank=True, null=True)  # Field name made lowercase.
    chg4ay2 = models.CharField(db_column='CHG4AY2', max_length=50, blank=True, null=True)  # Field name made lowercase.
    xchg4ay3 = models.CharField(db_column='XCHG4AY3', max_length=50, blank=True, null=True)  # Field name made lowercase.
    chg4ay3 = models.CharField(db_column='CHG4AY3', max_length=50, blank=True, null=True)  # Field name made lowercase.
    xchg5ay0 = models.CharField(db_column='XCHG5AY0', max_length=50, blank=True, null=True)  # Field name made lowercase.
    chg5ay0 = models.CharField(db_column='CHG5AY0', max_length=50, blank=True, null=True)  # Field name made lowercase.
    xchg5ay1 = models.CharField(db_column='XCHG5AY1', max_length=50, blank=True, null=True)  # Field name made lowercase.
    chg5ay1 = models.CharField(db_column='CHG5AY1', max_length=50, blank=True, null=True)  # Field name made lowercase.
    xchg5ay2 = models.CharField(db_column='XCHG5AY2', max_length=50, blank=True, null=True)  # Field name made lowercase.
    chg5ay2 = models.CharField(db_column='CHG5AY2', max_length=50, blank=True, null=True)  # Field name made lowercase.
    xchg5ay3 = models.CharField(db_column='XCHG5AY3', max_length=50, blank=True, null=True)  # Field name made lowercase.
    chg5ay3 = models.CharField(db_column='CHG5AY3', max_length=50, blank=True, null=True)  # Field name made lowercase.
    xchg6ay0 = models.CharField(db_column='XCHG6AY0', max_length=50, blank=True, null=True)  # Field name made lowercase.
    chg6ay0 = models.CharField(db_column='CHG6AY0', max_length=50, blank=True, null=True)  # Field name made lowercase.
    xchg6ay1 = models.CharField(db_column='XCHG6AY1', max_length=50, blank=True, null=True)  # Field name made lowercase.
    chg6ay1 = models.CharField(db_column='CHG6AY1', max_length=50, blank=True, null=True)  # Field name made lowercase.
    xchg6ay2 = models.CharField(db_column='XCHG6AY2', max_length=50, blank=True, null=True)  # Field name made lowercase.
    chg6ay2 = models.CharField(db_column='CHG6AY2', max_length=50, blank=True, null=True)  # Field name made lowercase.
    xchg6ay3 = models.CharField(db_column='XCHG6AY3', max_length=50, blank=True, null=True)  # Field name made lowercase.
    chg6ay3 = models.CharField(db_column='CHG6AY3', max_length=50, blank=True, null=True)  # Field name made lowercase.
    xchg7ay0 = models.CharField(db_column='XCHG7AY0', max_length=50, blank=True, null=True)  # Field name made lowercase.
    chg7ay0 = models.CharField(db_column='CHG7AY0', max_length=50, blank=True, null=True)  # Field name made lowercase.
    xchg7ay1 = models.CharField(db_column='XCHG7AY1', max_length=50, blank=True, null=True)  # Field name made lowercase.
    chg7ay1 = models.CharField(db_column='CHG7AY1', max_length=50, blank=True, null=True)  # Field name made lowercase.
    xchg7ay2 = models.CharField(db_column='XCHG7AY2', max_length=50, blank=True, null=True)  # Field name made lowercase.
    chg7ay2 = models.CharField(db_column='CHG7AY2', max_length=50, blank=True, null=True)  # Field name made lowercase.
    xchg7ay3 = models.CharField(db_column='XCHG7AY3', max_length=50, blank=True, null=True)  # Field name made lowercase.
    chg7ay3 = models.CharField(db_column='CHG7AY3', max_length=50, blank=True, null=True)  # Field name made lowercase.
    xchg8ay0 = models.CharField(db_column='XCHG8AY0', max_length=50, blank=True, null=True)  # Field name made lowercase.
    chg8ay0 = models.CharField(db_column='CHG8AY0', max_length=50, blank=True, null=True)  # Field name made lowercase.
    xchg8ay1 = models.CharField(db_column='XCHG8AY1', max_length=50, blank=True, null=True)  # Field name made lowercase.
    chg8ay1 = models.CharField(db_column='CHG8AY1', max_length=50, blank=True, null=True)  # Field name made lowercase.
    xchg8ay2 = models.CharField(db_column='XCHG8AY2', max_length=50, blank=True, null=True)  # Field name made lowercase.
    chg8ay2 = models.CharField(db_column='CHG8AY2', max_length=50, blank=True, null=True)  # Field name made lowercase.
    xchg8ay3 = models.CharField(db_column='XCHG8AY3', max_length=50, blank=True, null=True)  # Field name made lowercase.
    chg8ay3 = models.CharField(db_column='CHG8AY3', max_length=50, blank=True, null=True)  # Field name made lowercase.
    xchg9ay0 = models.CharField(db_column='XCHG9AY0', max_length=50, blank=True, null=True)  # Field name made lowercase.
    chg9ay0 = models.CharField(db_column='CHG9AY0', max_length=50, blank=True, null=True)  # Field name made lowercase.
    xchg9ay1 = models.CharField(db_column='XCHG9AY1', max_length=50, blank=True, null=True)  # Field name made lowercase.
    chg9ay1 = models.CharField(db_column='CHG9AY1', max_length=50, blank=True, null=True)  # Field name made lowercase.
    xchg9ay2 = models.CharField(db_column='XCHG9AY2', max_length=50, blank=True, null=True)  # Field name made lowercase.
    chg9ay2 = models.CharField(db_column='CHG9AY2', max_length=50, blank=True, null=True)  # Field name made lowercase.
    xchg9ay3 = models.CharField(db_column='XCHG9AY3', max_length=50, blank=True, null=True)  # Field name made lowercase.
    chg9ay3 = models.CharField(db_column='CHG9AY3 ', max_length=50, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.

    class Meta:
        managed = False
        db_table = 'ic2023_ay'


class RankingsEconomicdata(models.Model):
    id = models.BigAutoField(primary_key=True)
    state = models.CharField(max_length=100)
    group = models.CharField(max_length=100)
    indicator = models.CharField(max_length=100)
    unit = models.CharField(max_length=50)
    source = models.CharField(max_length=200)
    year = models.IntegerField()
    value = models.FloatField()

    class Meta:
        managed = False
        db_table = 'rankings_economicdata'
        unique_together = (('state', 'indicator', 'year'),)


class RankingsGroupname(models.Model):
    id = models.BigAutoField(primary_key=True)
    index = models.CharField(max_length=20)
    name = models.CharField(max_length=200)
    weight = models.FloatField()

    class Meta:
        managed = False
        db_table = 'rankings_groupname'


class RankingsIndicator(models.Model):
    id = models.BigAutoField(primary_key=True)
    stabbr = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    group = models.CharField(max_length=100)
    indicator = models.CharField(max_length=200)
    unit = models.CharField(max_length=50)
    source = models.CharField(max_length=200)
    year = models.IntegerField()
    value = models.FloatField()
    field_value_field = models.FloatField(db_column=' Value ', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it started with '_'. Field renamed because it ended with '_'.

    class Meta:
        managed = False
        db_table = 'rankings_indicator'


class RankingsIndicatorindex(models.Model):
    id = models.BigAutoField(primary_key=True)
    group = models.CharField(max_length=20)
    indicator = models.CharField(max_length=200)
    weight = models.FloatField()
    key = models.IntegerField()
    unit = models.CharField(max_length=200)

    class Meta:
        managed = False
        db_table = 'rankings_indicatorindex'


class RankingsState(models.Model):
    id = models.BigAutoField(primary_key=True)
    r_id = models.CharField(max_length=10)
    s_id = models.CharField(max_length=10)
    region = models.CharField(max_length=50)
    name = models.CharField(max_length=200)

    class Meta:
        managed = False
        db_table = 'rankings_state'


class SurveyBusiness(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=255)
    created_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'survey_business'


class SurveyBusinessfield(models.Model):
    id = models.BigAutoField(primary_key=True)
    field = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'survey_businessfield'


class SurveyBusinesssize(models.Model):
    id = models.BigAutoField(primary_key=True)
    size = models.CharField(max_length=20)

    class Meta:
        managed = False
        db_table = 'survey_businesssize'


class SurveyBusinesstype(models.Model):
    id = models.BigAutoField(primary_key=True)
    type = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'survey_businesstype'


class SurveyGeneralfeedback(models.Model):
    id = models.BigAutoField(primary_key=True)
    feedback = models.TextField()

    class Meta:
        managed = False
        db_table = 'survey_generalfeedback'


class SurveyGeneralinformation(models.Model):
    id = models.BigAutoField(primary_key=True)
    business_name = models.CharField(max_length=255)
    year_established = models.IntegerField()
    business_address = models.CharField(max_length=255)
    respondent_name = models.CharField(max_length=255)
    email = models.CharField(max_length=254)
    phone_number = models.CharField(max_length=20)

    class Meta:
        managed = False
        db_table = 'survey_generalinformation'


class SurveyStrategyoperation(models.Model):
    id = models.BigAutoField(primary_key=True)
    vision = models.CharField(max_length=1)
    mission = models.CharField(max_length=1)
    strategic_goals = models.CharField(max_length=1)
    submitted_at = models.DateTimeField()
    competitive_advantage = models.CharField(max_length=1)
    core_values = models.CharField(max_length=1)
    core_values_building = models.CharField(max_length=1)
    customer_service = models.CharField(max_length=1)
    innovation_capacity = models.CharField(max_length=1)
    job_description = models.CharField(max_length=1)
    marketing_level = models.CharField(max_length=1)
    operational_process = models.CharField(max_length=1)
    organizational_chart = models.CharField(max_length=1)
    performance_measurement = models.CharField(max_length=1)
    r_and_d_spending = models.CharField(max_length=1)
    technology_absorption = models.CharField(max_length=1)
    technology_use = models.CharField(max_length=1)
    value_chain = models.CharField(max_length=1)

    class Meta:
        managed = False
        db_table = 'survey_strategyoperation'
