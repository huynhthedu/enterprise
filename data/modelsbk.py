# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Adm2023(models.Model):
    unitid = models.IntegerField(db_column='UNITID', blank=True, null=False, unique=True, primary_key=True)  # Field name made lowercase.
    admcon1 = models.IntegerField(db_column='ADMCON1', blank=True, null=True)  # Field name made lowercase.
    admcon2 = models.IntegerField(db_column='ADMCON2', blank=True, null=True)  # Field name made lowercase.
    admcon3 = models.IntegerField(db_column='ADMCON3', blank=True, null=True)  # Field name made lowercase.
    admcon4 = models.IntegerField(db_column='ADMCON4', blank=True, null=True)  # Field name made lowercase.
    admcon5 = models.IntegerField(db_column='ADMCON5', blank=True, null=True)  # Field name made lowercase.
    admcon6 = models.IntegerField(db_column='ADMCON6', blank=True, null=True)  # Field name made lowercase.
    admcon7 = models.IntegerField(db_column='ADMCON7', blank=True, null=True)  # Field name made lowercase.
    admcon8 = models.IntegerField(db_column='ADMCON8', blank=True, null=True)  # Field name made lowercase.
    admcon9 = models.IntegerField(db_column='ADMCON9', blank=True, null=True)  # Field name made lowercase.
    admcon10 = models.IntegerField(db_column='ADMCON10', blank=True, null=True)  # Field name made lowercase.
    admcon11 = models.IntegerField(db_column='ADMCON11', blank=True, null=True)  # Field name made lowercase.
    admcon12 = models.IntegerField(db_column='ADMCON12', blank=True, null=True)  # Field name made lowercase.
    applcn = models.IntegerField(db_column='APPLCN', blank=True, null=True)  # Field name made lowercase.
    applcnan = models.IntegerField(db_column='APPLCNAN', blank=True, null=True)  # Field name made lowercase.
    applcnm = models.IntegerField(db_column='APPLCNM', blank=True, null=True)  # Field name made lowercase.
    applcnun = models.IntegerField(db_column='APPLCNUN', blank=True, null=True)  # Field name made lowercase.
    applcnw = models.IntegerField(db_column='APPLCNW', blank=True, null=True)  # Field name made lowercase.
    admssn = models.IntegerField(db_column='ADMSSN', blank=True, null=True)  # Field name made lowercase.
    admssnan = models.IntegerField(db_column='ADMSSNAN', blank=True, null=True)  # Field name made lowercase.
    admssnm = models.IntegerField(db_column='ADMSSNM', blank=True, null=True)  # Field name made lowercase.
    admssnun = models.IntegerField(db_column='ADMSSNUN', blank=True, null=True)  # Field name made lowercase.
    admssnw = models.IntegerField(db_column='ADMSSNW', blank=True, null=True)  # Field name made lowercase.
    enrlt = models.IntegerField(db_column='ENRLT', blank=True, null=True)  # Field name made lowercase.
    enrlm = models.IntegerField(db_column='ENRLM', blank=True, null=True)  # Field name made lowercase.
    enrlw = models.IntegerField(db_column='ENRLW', blank=True, null=True)  # Field name made lowercase.
    enrlan = models.IntegerField(db_column='ENRLAN', blank=True, null=True)  # Field name made lowercase.
    enrlun = models.IntegerField(db_column='ENRLUN', blank=True, null=True)  # Field name made lowercase.
    enrlft = models.IntegerField(db_column='ENRLFT', blank=True, null=True)  # Field name made lowercase.
    enrlftm = models.IntegerField(db_column='ENRLFTM', blank=True, null=True)  # Field name made lowercase.
    enrlftw = models.IntegerField(db_column='ENRLFTW', blank=True, null=True)  # Field name made lowercase.
    enrlftan = models.IntegerField(db_column='ENRLFTAN', blank=True, null=True)  # Field name made lowercase.
    enrlftun = models.IntegerField(db_column='ENRLFTUN', blank=True, null=True)  # Field name made lowercase.
    enrlpt = models.IntegerField(db_column='ENRLPT', blank=True, null=True)  # Field name made lowercase.
    enrlptm = models.IntegerField(db_column='ENRLPTM', blank=True, null=True)  # Field name made lowercase.
    enrlptw = models.IntegerField(db_column='ENRLPTW', blank=True, null=True)  # Field name made lowercase.
    enrlptan = models.IntegerField(db_column='ENRLPTAN', blank=True, null=True)  # Field name made lowercase.
    enrlptun = models.IntegerField(db_column='ENRLPTUN', blank=True, null=True)  # Field name made lowercase.
    satnum = models.IntegerField(db_column='SATNUM', blank=True, null=True)  # Field name made lowercase.
    satpct = models.IntegerField(db_column='SATPCT', blank=True, null=True)  # Field name made lowercase.
    satvr25 = models.IntegerField(db_column='SATVR25', blank=True, null=True)  # Field name made lowercase.
    satvr50 = models.IntegerField(db_column='SATVR50', blank=True, null=True)  # Field name made lowercase.
    satvr75 = models.IntegerField(db_column='SATVR75', blank=True, null=True)  # Field name made lowercase.
    satmt25 = models.IntegerField(db_column='SATMT25', blank=True, null=True)  # Field name made lowercase.
    satmt50 = models.IntegerField(db_column='SATMT50', blank=True, null=True)  # Field name made lowercase.
    satmt75 = models.IntegerField(db_column='SATMT75', blank=True, null=True)  # Field name made lowercase.
    actcm25 = models.IntegerField(db_column='ACTCM25', blank=True, null=True)  # Field name made lowercase.
    actcm50 = models.IntegerField(db_column='ACTCM50', blank=True, null=True)  # Field name made lowercase.
    actcm75 = models.IntegerField(db_column='ACTCM75', blank=True, null=True)  # Field name made lowercase.
    acten25 = models.IntegerField(db_column='ACTEN25', blank=True, null=True)  # Field name made lowercase.
    acten50 = models.IntegerField(db_column='ACTEN50', blank=True, null=True)  # Field name made lowercase.
    acten75 = models.IntegerField(db_column='ACTEN75', blank=True, null=True)  # Field name made lowercase.
    actmt25 = models.IntegerField(db_column='ACTMT25', blank=True, null=True)  # Field name made lowercase.
    actmt50 = models.IntegerField(db_column='ACTMT50', blank=True, null=True)  # Field name made lowercase.
    actmt75_field = models.IntegerField(db_column='ACTMT75   ', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    year = models.IntegerField(db_column='year', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'adm2023'


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
    unitid = models.IntegerField(db_column='UNITID', blank=True, null=True)
    cstotlt = models.IntegerField(db_column='CSTOTLT', blank=True, null=True)
    cstotlm = models.IntegerField(db_column='CSTOTLM', blank=True, null=True)
    cstotlw = models.IntegerField(db_column='CSTOTLW', blank=True, null=True)
    csaiant = models.IntegerField(db_column='CSAIANT', blank=True, null=True)
    csaianm = models.IntegerField(db_column='CSAIANM', blank=True, null=True)
    csaianw = models.IntegerField(db_column='CSAIANW', blank=True, null=True)
    csasiat = models.IntegerField(db_column='CSASIAT', blank=True, null=True)
    csasiam = models.IntegerField(db_column='CSASIAM', blank=True, null=True)
    csasiaw = models.IntegerField(db_column='CSASIAW', blank=True, null=True)
    csbkaat = models.IntegerField(db_column='CSBKAAT', blank=True, null=True)
    csbkaam = models.IntegerField(db_column='CSBKAAM', blank=True, null=True)
    csbkaaw = models.IntegerField(db_column='CSBKAAW', blank=True, null=True)
    cshispt = models.IntegerField(db_column='CSHISPT', blank=True, null=True)
    cshispm = models.IntegerField(db_column='CSHISPM', blank=True, null=True)
    cshispw = models.IntegerField(db_column='CSHISPW', blank=True, null=True)
    csnhpit = models.IntegerField(db_column='CSNHPIT', blank=True, null=True)
    csnhpim = models.IntegerField(db_column='CSNHPIM', blank=True, null=True)
    csnhpiw = models.IntegerField(db_column='CSNHPIW', blank=True, null=True)
    cswhitt = models.IntegerField(db_column='CSWHITT', blank=True, null=True)
    cswhitm = models.IntegerField(db_column='CSWHITM', blank=True, null=True)
    cswhitw = models.IntegerField(db_column='CSWHITW', blank=True, null=True)
    cs2mort = models.IntegerField(db_column='CS2MORT', blank=True, null=True)
    cs2morm = models.IntegerField(db_column='CS2MORM', blank=True, null=True)
    cs2morw = models.IntegerField(db_column='CS2MORW', blank=True, null=True)
    csunknt = models.IntegerField(db_column='CSUNKNT', blank=True, null=True)
    csunknm = models.IntegerField(db_column='CSUNKNM', blank=True, null=True)
    csunknw = models.IntegerField(db_column='CSUNKNW', blank=True, null=True)
    csnralt = models.IntegerField(db_column='CSNRALT', blank=True, null=True)
    csnralm = models.IntegerField(db_column='CSNRALM', blank=True, null=True)
    csnralw_field = models.IntegerField(db_column='CSNRALW', blank=True, null=True)
 

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
    unitid = models.IntegerField(db_column='UNITID', primary_key=True)
    cstotlt = models.IntegerField(db_column='CSTOTLT', blank=True, null=True)
    cstotlm = models.IntegerField(db_column='CSTOTLM', blank=True, null=True)
    cstotlw = models.IntegerField(db_column='CSTOTLW', blank=True, null=True)
    csaiant = models.IntegerField(db_column='CSAIANT', blank=True, null=True)
    csaianm = models.IntegerField(db_column='CSAIANM', blank=True, null=True)
    csaianw = models.IntegerField(db_column='CSAIANW', blank=True, null=True)
    csasiat = models.IntegerField(db_column='CSASIAT', blank=True, null=True)
    csasiam = models.IntegerField(db_column='CSASIAM', blank=True, null=True)
    csasiaw = models.IntegerField(db_column='CSASIAW', blank=True, null=True)
    csbkaat = models.IntegerField(db_column='CSBKAAT', blank=True, null=True)
    csbkaam = models.IntegerField(db_column='CSBKAAM', blank=True, null=True)
    csbkaaw = models.IntegerField(db_column='CSBKAAW', blank=True, null=True)
    cshispt = models.IntegerField(db_column='CSHISPT', blank=True, null=True)
    cshispm = models.IntegerField(db_column='CSHISPM', blank=True, null=True)
    cshispw = models.IntegerField(db_column='CSHISPW', blank=True, null=True)
    csnhpit = models.IntegerField(db_column='CSNHPIT', blank=True, null=True)
    csnhpim = models.IntegerField(db_column='CSNHPIM', blank=True, null=True)
    csnhpiw = models.IntegerField(db_column='CSNHPIW', blank=True, null=True)
    cswhitt = models.IntegerField(db_column='CSWHITT', blank=True, null=True)
    cswhitm = models.IntegerField(db_column='CSWHITM', blank=True, null=True)
    cswhitw = models.IntegerField(db_column='CSWHITW', blank=True, null=True)
    cs2mort = models.IntegerField(db_column='CS2MORT', blank=True, null=True)
    cs2morm = models.IntegerField(db_column='CS2MORM', blank=True, null=True)
    cs2morw = models.IntegerField(db_column='CS2MORW', blank=True, null=True)
    csunknt = models.IntegerField(db_column='CSUNKNT', blank=True, null=True)
    csunknm = models.IntegerField(db_column='CSUNKNM', blank=True, null=True)
    csunknw = models.IntegerField(db_column='CSUNKNW', blank=True, null=True)
    csnralt = models.IntegerField(db_column='CSNRALT', blank=True, null=True)
    csnralm = models.IntegerField(db_column='CSNRALM', blank=True, null=True)
    csnralw = models.IntegerField(db_column='CSNRALW', blank=True, null=True)
    csguugun = models.IntegerField(db_column='CSGUUGUN', blank=True, null=True)
    csguugag = models.IntegerField(db_column='CSGUUGAG', blank=True, null=True)
    csguugtt = models.IntegerField(db_column='CSGUUGTT', blank=True, null=True)
    csgugun = models.IntegerField(db_column='CSGUGUN', blank=True, null=True)
    csgugag = models.IntegerField(db_column='CSGUGAG', blank=True, null=True)
    csgugtot = models.IntegerField(db_column='CSGUGTOT', blank=True, null=True)
    csgutotun = models.IntegerField(db_column='CSGUTOTUN', blank=True, null=True)
    csgutotag = models.IntegerField(db_column='CSGUTOTAG', blank=True, null=True)
    csgutot = models.IntegerField(db_column='CSGUTOT', blank=True, null=True)
    csgukn_field = models.CharField(db_column='CSGUKN', max_length=50, blank=True, null=True)

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
    unitid = models.IntegerField(db_column='UNITID', blank=True, null=True)
    effyalev = models.CharField(db_column='EFFYALEV', max_length=50, blank=True, null=True)
    effylev = models.CharField(db_column='EFFYLEV', max_length=50, blank=True, null=True)
    lstudy = models.CharField(db_column='LSTUDY', max_length=50, blank=True, null=True)
    efytotlt = models.IntegerField(db_column='EFYTOTLT', blank=True, null=True)
    efytotlm = models.IntegerField(db_column='EFYTOTLM', blank=True, null=True)
    efytotlw = models.IntegerField(db_column='EFYTOTLW', blank=True, null=True)
    efyaiant = models.IntegerField(db_column='EFYAIANT', blank=True, null=True)
    efyaianm = models.IntegerField(db_column='EFYAIANM', blank=True, null=True)
    efyaianw = models.IntegerField(db_column='EFYAIANW', blank=True, null=True)
    efyasiat = models.IntegerField(db_column='EFYASIAT', blank=True, null=True)
    efyasiam = models.IntegerField(db_column='EFYASIAM', blank=True, null=True)
    efyasiaw = models.IntegerField(db_column='EFYASIAW', blank=True, null=True)
    efybkaat = models.IntegerField(db_column='EFYBKAAT', blank=True, null=True)
    efybkaam = models.IntegerField(db_column='EFYBKAAM', blank=True, null=True)
    efybkaaw = models.IntegerField(db_column='EFYBKAAW', blank=True, null=True)
    efyhispt = models.IntegerField(db_column='EFYHISPT', blank=True, null=True)
    efyhispm = models.IntegerField(db_column='EFYHISPM', blank=True, null=True)
    efyhispw = models.IntegerField(db_column='EFYHISPW', blank=True, null=True)
    efynhpit = models.IntegerField(db_column='EFYNHPIT', blank=True, null=True)
    efynhpim = models.IntegerField(db_column='EFYNHPIM', blank=True, null=True)
    efynhpiw = models.IntegerField(db_column='EFYNHPIW', blank=True, null=True)
    efywhitt = models.IntegerField(db_column='EFYWHITT', blank=True, null=True)
    efywhitm = models.IntegerField(db_column='EFYWHITM', blank=True, null=True)
    efywhitw = models.IntegerField(db_column='EFYWHITW', blank=True, null=True)
    efy2mort = models.IntegerField(db_column='EFY2MORT', blank=True, null=True)
    efy2morm = models.IntegerField(db_column='EFY2MORM', blank=True, null=True)
    efy2morw = models.IntegerField(db_column='EFY2MORW', blank=True, null=True)
    efyunknt = models.IntegerField(db_column='EFYUNKNT', blank=True, null=True)
    efyunknm = models.IntegerField(db_column='EFYUNKNM', blank=True, null=True)
    efyunknw = models.IntegerField(db_column='EFYUNKNW', blank=True, null=True)
    efynralt = models.IntegerField(db_column='EFYNRALT', blank=True, null=True)
    efynralm = models.IntegerField(db_column='EFYNRALM', blank=True, null=True)
    efynralw = models.IntegerField(db_column='EFYNRALW', blank=True, null=True)
    efyguun = models.IntegerField(db_column='EFYGUUN', blank=True, null=True)
    efyguan = models.CharField(db_column='EFYGUAN', max_length=50, blank=True, null=True)
    efygutot = models.IntegerField(db_column='EFYGUTOT', blank=True, null=True)
    efygukn_field = models.IntegerField(db_column='EFYGUKN', blank=True, null=True)

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
    unitid = models.IntegerField(db_column='UNITID', blank=True, null=True)
    tuition1 = models.CharField(db_column='TUITION1', max_length=50, blank=True, null=True)
    fee1 = models.CharField(db_column='FEE1', max_length=50, blank=True, null=True)
    hrchg1 = models.CharField(db_column='HRCHG1', max_length=50, blank=True, null=True)
    tuition2 = models.CharField(db_column='TUITION2', max_length=50, blank=True, null=True)
    fee2 = models.CharField(db_column='FEE2', max_length=50, blank=True, null=True)
    hrchg2 = models.CharField(db_column='HRCHG2', max_length=50, blank=True, null=True)
    tuition3 = models.CharField(db_column='TUITION3', max_length=50, blank=True, null=True)
    fee3 = models.CharField(db_column='FEE3', max_length=50, blank=True, null=True)
    hrchg3 = models.CharField(db_column='HRCHG3', max_length=50, blank=True, null=True)
    tuition5 = models.CharField(db_column='TUITION5', max_length=50, blank=True, null=True)
    fee5 = models.CharField(db_column='FEE5', max_length=50, blank=True, null=True)
    hrchg5 = models.CharField(db_column='HRCHG5', max_length=50, blank=True, null=True)
    tuition6 = models.CharField(db_column='TUITION6', max_length=50, blank=True, null=True)
    fee6 = models.CharField(db_column='FEE6', max_length=50, blank=True, null=True)
    hrchg6 = models.CharField(db_column='HRCHG6', max_length=50, blank=True, null=True)
    tuition7 = models.CharField(db_column='TUITION7', max_length=50, blank=True, null=True)
    fee7 = models.CharField(db_column='FEE7', max_length=50, blank=True, null=True)
    hrchg7 = models.CharField(db_column='HRCHG7', max_length=50, blank=True, null=True)
    isprof1 = models.CharField(db_column='ISPROF1', max_length=50, blank=True, null=True)
    ispfee1 = models.CharField(db_column='ISPFEE1', max_length=50, blank=True, null=True)
    osprof1 = models.CharField(db_column='OSPROF1', max_length=50, blank=True, null=True)
    ospfee1 = models.CharField(db_column='OSPFEE1', max_length=50, blank=True, null=True)
    isprof2 = models.CharField(db_column='ISPROF2', max_length=50, blank=True, null=True)
    ispfee2 = models.CharField(db_column='ISPFEE2', max_length=50, blank=True, null=True)
    osprof2 = models.CharField(db_column='OSPROF2', max_length=50, blank=True, null=True)
    ospfee2 = models.CharField(db_column='OSPFEE2', max_length=50, blank=True, null=True)
    isprof3 = models.CharField(db_column='ISPROF3', max_length=50, blank=True, null=True)
    ispfee3 = models.CharField(db_column='ISPFEE3', max_length=50, blank=True, null=True)
    osprof3 = models.CharField(db_column='OSPROF3', max_length=50, blank=True, null=True)
    ospfee3 = models.CharField(db_column='OSPFEE3', max_length=50, blank=True, null=True)
    isprof4 = models.CharField(db_column='ISPROF4', max_length=50, blank=True, null=True)
    ispfee4 = models.CharField(db_column='ISPFEE4', max_length=50, blank=True, null=True)
    osprof4 = models.CharField(db_column='OSPROF4', max_length=50, blank=True, null=True)
    ospfee4 = models.CharField(db_column='OSPFEE4', max_length=50, blank=True, null=True)
    isprof5 = models.CharField(db_column='ISPROF5', max_length=50, blank=True, null=True)
    ispfee5 = models.CharField(db_column='ISPFEE5', max_length=50, blank=True, null=True)
    osprof5 = models.CharField(db_column='OSPROF5', max_length=50, blank=True, null=True)
    ospfee5 = models.CharField(db_column='OSPFEE5', max_length=50, blank=True, null=True)
    isprof6 = models.CharField(db_column='ISPROF6', max_length=50, blank=True, null=True)
    ispfee6 = models.CharField(db_column='ISPFEE6', max_length=50, blank=True, null=True)
    osprof6 = models.CharField(db_column='OSPROF6', max_length=50, blank=True, null=True)
    ospfee6 = models.CharField(db_column='OSPFEE6', max_length=50, blank=True, null=True)
    isprof7 = models.CharField(db_column='ISPROF7', max_length=50, blank=True, null=True)
    ispfee7 = models.CharField(db_column='ISPFEE7', max_length=50, blank=True, null=True)
    osprof7 = models.CharField(db_column='OSPROF7', max_length=50, blank=True, null=True)
    ospfee7 = models.CharField(db_column='OSPFEE7', max_length=50, blank=True, null=True)
    isprof8 = models.CharField(db_column='ISPROF8', max_length=50, blank=True, null=True)
    ispfee8 = models.CharField(db_column='ISPFEE8', max_length=50, blank=True, null=True)
    osprof8 = models.CharField(db_column='OSPROF8', max_length=50, blank=True, null=True)
    ospfee8 = models.CharField(db_column='OSPFEE8', max_length=50, blank=True, null=True)
    isprof9 = models.CharField(db_column='ISPROF9', max_length=50, blank=True, null=True)
    ispfee9 = models.CharField(db_column='ISPFEE9', max_length=50, blank=True, null=True)
    osprof9 = models.CharField(db_column='OSPROF9', max_length=50, blank=True, null=True)
    ospfee9 = models.CharField(db_column='OSPFEE9', max_length=50, blank=True, null=True)
    chg1at0 = models.CharField(db_column='CHG1AT0', max_length=50, blank=True, null=True)
    chg1af0 = models.CharField(db_column='CHG1AF0', max_length=50, blank=True, null=True)
    chg1ay0 = models.CharField(db_column='CHG1AY0', max_length=50, blank=True, null=True)
    chg1at1 = models.CharField(db_column='CHG1AT1', max_length=50, blank=True, null=True)
    chg1at3 = models.CharField(db_column='CHG1AT3', max_length=50, blank=True, null=True)
    chg1af3 = models.CharField(db_column='CHG1AF3', max_length=50, blank=True, null=True)
    chg1ay3 = models.CharField(db_column='CHG1AY3', max_length=50, blank=True, null=True)
    chg1tgtd = models.CharField(db_column='CHG1TGTD', max_length=50, blank=True, null=True)
    chg1fgtd = models.CharField(db_column='CHG1FGTD', max_length=50, blank=True, null=True)
    chg2at0 = models.CharField(db_column='CHG2AT0', max_length=50, blank=True, null=True)
    chg2af0 = models.CharField(db_column='CHG2AF0', max_length=50, blank=True, null=True)
    chg2ay0 = models.CharField(db_column='CHG2AY0', max_length=50, blank=True, null=True)
    chg2at1 = models.CharField(db_column='CHG2AT1', max_length=50, blank=True, null=True)
    chg2af1 = models.CharField(db_column='CHG2AF1', max_length=50, blank=True, null=True)
    chg2ay1 = models.CharField(db_column='CHG2AY1', max_length=50, blank=True, null=True)
    chg2at2 = models.CharField(db_column='CHG2AT2', max_length=50, blank=True, null=True)
    chg2af2 = models.CharField(db_column='CHG2AF2', max_length=50, blank=True, null=True)
    chg2ay2 = models.CharField(db_column='CHG2AY2', max_length=50, blank=True, null=True)
    chg2at3 = models.CharField(db_column='CHG2AT3', max_length=50, blank=True, null=True)
    chg2af3 = models.CharField(db_column='CHG2AF3', max_length=50, blank=True, null=True)
    chg2ay3 = models.CharField(db_column='CHG2AY3', max_length=50, blank=True, null=True)
    chg2tgtd = models.CharField(db_column='CHG2TGTD', max_length=50, blank=True, null=True)
    chg2fgtd = models.CharField(db_column='CHG2FGTD', max_length=50, blank=True, null=True)
    chg3at0 = models.CharField(db_column='CHG3AT0', max_length=50, blank=True, null=True)
    chg3af0 = models.CharField(db_column='CHG3AF0', max_length=50, blank=True, null=True)
    chg3ay0 = models.CharField(db_column='CHG3AY0', max_length=50, blank=True, null=True)
    chg3at1 = models.CharField(db_column='CHG3AT1', max_length=50, blank=True, null=True)
    chg3af1 = models.CharField(db_column='CHG3AF1', max_length=50, blank=True, null=True)
    chg3ay1 = models.CharField(db_column='CHG3AY1', max_length=50, blank=True, null=True)
    chg3at2 = models.CharField(db_column='CHG3AT2', max_length=50, blank=True, null=True)
    chg3af2 = models.CharField(db_column='CHG3AF2', max_length=50, blank=True, null=True)
    chg3ay2 = models.CharField(db_column='CHG3AY2', max_length=50, blank=True, null=True)
    chg3at3 = models.CharField(db_column='CHG3AT3', max_length=50, blank=True, null=True)
    chg3af3 = models.CharField(db_column='CHG3AF3', max_length=50, blank=True, null=True)
    chg3ay3 = models.CharField(db_column='CHG3AY3', max_length=50, blank=True, null=True)
    chg3tgtd = models.CharField(db_column='CHG3TGTD', max_length=50, blank=True, null=True)
    chg3fgtd = models.CharField(db_column='CHG3FGTD', max_length=50, blank=True, null=True)
    chg4ay0 = models.CharField(db_column='CHG4AY0', max_length=50, blank=True, null=True)
    chg4ay1 = models.CharField(db_column='CHG4AY1', max_length=50, blank=True, null=True)
    chg4ay2 = models.CharField(db_column='CHG4AY2', max_length=50, blank=True, null=True)
    chg4ay3 = models.CharField(db_column='CHG4AY3', max_length=50, blank=True, null=True)
    chg5ay0 = models.CharField(db_column='CHG5AY0', max_length=50, blank=True, null=True)
    chg5ay1 = models.CharField(db_column='CHG5AY1', max_length=50, blank=True, null=True)
    chg5ay2 = models.CharField(db_column='CHG5AY2', max_length=50, blank=True, null=True)
    chg5ay3 = models.CharField(db_column='CHG5AY3', max_length=50, blank=True, null=True)
    chg6ay0 = models.CharField(db_column='CHG6AY0', max_length=50, blank=True, null=True)
    chg6ay1 = models.CharField(db_column='CHG6AY1', max_length=50, blank=True, null=True)
    chg6ay2 = models.CharField(db_column='CHG6AY2', max_length=50, blank=True, null=True)
    chg6ay3 = models.CharField(db_column='CHG6AY3', max_length=50, blank=True, null=True)
    chg7ay0 = models.CharField(db_column='CHG7AY0', max_length=50, blank=True, null=True)
    chg7ay1 = models.CharField(db_column='CHG7AY1', max_length=50, blank=True, null=True)
    chg7ay2 = models.CharField(db_column='CHG7AY2', max_length=50, blank=True, null=True)
    chg7ay3 = models.CharField(db_column='CHG7AY3', max_length=50, blank=True, null=True)
    chg8ay0 = models.CharField(db_column='CHG8AY0', max_length=50, blank=True, null=True)
    chg8ay1 = models.CharField(db_column='CHG8AY1', max_length=50, blank=True, null=True)
    chg8ay2 = models.CharField(db_column='CHG8AY2', max_length=50, blank=True, null=True)
    chg8ay3 = models.CharField(db_column='CHG8AY3', max_length=50, blank=True, null=True)
    chg9ay0 = models.CharField(db_column='CHG9AY0', max_length=50, blank=True, null=True)
    chg9ay1 = models.CharField(db_column='CHG9AY1', max_length=50, blank=True, null=True)
    chg9ay2 = models.CharField(db_column='CHG9AY2', max_length=50, blank=True, null=True)
    chg9ay3 = models.CharField(db_column='CHG9AY3', max_length=50, blank=True, null=True)
    chg9ay3_field = models.CharField(db_column='CHG9AY3 ', max_length=50, blank=True, null=True)



    class Meta:
        managed = False
        db_table = 'ic2019_ay'


class Ic2023Ay(models.Model):
    unitid = models.IntegerField(db_column='UNITID', blank=True, null=True)
    tuition1 = models.CharField(db_column='TUITION1', max_length=50, blank=True, null=True)
    fee1 = models.CharField(db_column='FEE1', max_length=50, blank=True, null=True)
    hrchg1 = models.CharField(db_column='HRCHG1', max_length=50, blank=True, null=True)
    tuition2 = models.CharField(db_column='TUITION2', max_length=50, blank=True, null=True)
    fee2 = models.CharField(db_column='FEE2', max_length=50, blank=True, null=True)
    hrchg2 = models.CharField(db_column='HRCHG2', max_length=50, blank=True, null=True)
    tuition3 = models.CharField(db_column='TUITION3', max_length=50, blank=True, null=True)
    fee3 = models.CharField(db_column='FEE3', max_length=50, blank=True, null=True)
    hrchg3 = models.CharField(db_column='HRCHG3', max_length=50, blank=True, null=True)
    tuition5 = models.CharField(db_column='TUITION5', max_length=50, blank=True, null=True)
    fee5 = models.CharField(db_column='FEE5', max_length=50, blank=True, null=True)
    hrchg5 = models.CharField(db_column='HRCHG5', max_length=50, blank=True, null=True)
    tuition6 = models.CharField(db_column='TUITION6', max_length=50, blank=True, null=True)
    fee6 = models.CharField(db_column='FEE6', max_length=50, blank=True, null=True)
    hrchg6 = models.CharField(db_column='HRCHG6', max_length=50, blank=True, null=True)
    tuition7 = models.CharField(db_column='TUITION7', max_length=50, blank=True, null=True)
    fee7 = models.CharField(db_column='FEE7', max_length=50, blank=True, null=True)
    hrchg7 = models.CharField(db_column='HRCHG7', max_length=50, blank=True, null=True)
    isprof1 = models.CharField(db_column='ISPROF1', max_length=50, blank=True, null=True)
    ispfee1 = models.CharField(db_column='ISPFEE1', max_length=50, blank=True, null=True)
    osprof1 = models.CharField(db_column='OSPROF1', max_length=50, blank=True, null=True)
    ospfee1 = models.CharField(db_column='OSPFEE1', max_length=50, blank=True, null=True)
    isprof2 = models.CharField(db_column='ISPROF2', max_length=50, blank=True, null=True)
    ispfee2 = models.CharField(db_column='ISPFEE2', max_length=50, blank=True, null=True)
    osprof2 = models.CharField(db_column='OSPROF2', max_length=50, blank=True, null=True)
    ospfee2 = models.CharField(db_column='OSPFEE2', max_length=50, blank=True, null=True)
    isprof3 = models.CharField(db_column='ISPROF3', max_length=50, blank=True, null=True)
    ispfee3 = models.CharField(db_column='ISPFEE3', max_length=50, blank=True, null=True)
    osprof3 = models.CharField(db_column='OSPROF3', max_length=50, blank=True, null=True)
    ospfee3 = models.CharField(db_column='OSPFEE3', max_length=50, blank=True, null=True)
    isprof4 = models.CharField(db_column='ISPROF4', max_length=50, blank=True, null=True)
    ispfee4 = models.CharField(db_column='ISPFEE4', max_length=50, blank=True, null=True)
    osprof4 = models.CharField(db_column='OSPROF4', max_length=50, blank=True, null=True)
    ospfee4 = models.CharField(db_column='OSPFEE4', max_length=50, blank=True, null=True)
    isprof5 = models.CharField(db_column='ISPROF5', max_length=50, blank=True, null=True)
    ispfee5 = models.CharField(db_column='ISPFEE5', max_length=50, blank=True, null=True)
    osprof5 = models.CharField(db_column='OSPROF5', max_length=50, blank=True, null=True)
    ospfee5 = models.CharField(db_column='OSPFEE5', max_length=50, blank=True, null=True)
    isprof6 = models.CharField(db_column='ISPROF6', max_length=50, blank=True, null=True)
    ispfee6 = models.CharField(db_column='ISPFEE6', max_length=50, blank=True, null=True)
    osprof6 = models.CharField(db_column='OSPROF6', max_length=50, blank=True, null=True)
    ospfee6 = models.CharField(db_column='OSPFEE6', max_length=50, blank=True, null=True)
    isprof7 = models.CharField(db_column='ISPROF7', max_length=50, blank=True, null=True)
    ispfee7 = models.CharField(db_column='ISPFEE7', max_length=50, blank=True, null=True)
    osprof7 = models.CharField(db_column='OSPROF7', max_length=50, blank=True, null=True)
    ospfee7 = models.CharField(db_column='OSPFEE7', max_length=50, blank=True, null=True)
    isprof8 = models.CharField(db_column='ISPROF8', max_length=50, blank=True, null=True)
    ispfee8 = models.CharField(db_column='ISPFEE8', max_length=50, blank=True, null=True)
    osprof8 = models.CharField(db_column='OSPROF8', max_length=50, blank=True, null=True)
    ospfee8 = models.CharField(db_column='OSPFEE8', max_length=50, blank=True, null=True)
    isprof9 = models.CharField(db_column='ISPROF9', max_length=50, blank=True, null=True)
    ispfee9 = models.CharField(db_column='ISPFEE9', max_length=50, blank=True, null=True)
    osprof9 = models.CharField(db_column='OSPROF9', max_length=50, blank=True, null=True)
    ospfee9 = models.CharField(db_column='OSPFEE9', max_length=50, blank=True, null=True)
    chg1at0 = models.CharField(db_column='CHG1AT0', max_length=50, blank=True, null=True)
    chg1af0 = models.CharField(db_column='CHG1AF0', max_length=50, blank=True, null=True)
    chg1ay0 = models.CharField(db_column='CHG1AY0', max_length=50, blank=True, null=True)
    chg1at1 = models.CharField(db_column='CHG1AT1', max_length=50, blank=True, null=True)
    chg1ay1 = models.CharField(db_column='CHG1AY1', max_length=50, blank=True, null=True)
    chg1at2 = models.CharField(db_column='CHG1AT2', max_length=50, blank=True, null=True)
    chg1af2 = models.CharField(db_column='CHG1AF2', max_length=50, blank=True, null=True)
    chg1ay2 = models.CharField(db_column='CHG1AY2', max_length=50, blank=True, null=True)
    chg1at3 = models.CharField(db_column='CHG1AT3', max_length=50, blank=True, null=True)
    chg1af3 = models.CharField(db_column='CHG1AF3', max_length=50, blank=True, null=True)
    chg1ay3 = models.CharField(db_column='CHG1AY3', max_length=50, blank=True, null=True)
    chg1tgtd = models.CharField(db_column='CHG1TGTD', max_length=50, blank=True, null=True)
    chg1fgtd = models.CharField(db_column='CHG1FGTD', max_length=50, blank=True, null=True)
    chg2at0 = models.CharField(db_column='CHG2AT0', max_length=50, blank=True, null=True)
    chg2af0 = models.CharField(db_column='CHG2AF0', max_length=50, blank=True, null=True)
    chg2ay0 = models.CharField(db_column='CHG2AY0', max_length=50, blank=True, null=True)
    chg2at1 = models.CharField(db_column='CHG2AT1', max_length=50, blank=True, null=True)
    chg2af1 = models.CharField(db_column='CHG2AF1', max_length=50, blank=True, null=True)
    chg2ay1 = models.CharField(db_column='CHG2AY1', max_length=50, blank=True, null=True)
    chg2at2 = models.CharField(db_column='CHG2AT2', max_length=50, blank=True, null=True)
    chg2af2 = models.CharField(db_column='CHG2AF2', max_length=50, blank=True, null=True)
    chg2ay2 = models.CharField(db_column='CHG2AY2', max_length=50, blank=True, null=True)
    chg2at3 = models.CharField(db_column='CHG2AT3', max_length=50, blank=True, null=True)
    chg2af3 = models.CharField(db_column='CHG2AF3', max_length=50, blank=True, null=True)
    chg2ay3 = models.CharField(db_column='CHG2AY3', max_length=50, blank=True, null=True)
    chg2tgtd = models.CharField(db_column='CHG2TGTD', max_length=50, blank=True, null=True)
    chg2fgtd = models.CharField(db_column='CHG2FGTD', max_length=50, blank=True, null=True)
    chg3at0 = models.CharField(db_column='CHG3AT0', max_length=50, blank=True, null=True)
    chg3af0 = models.CharField(db_column='CHG3AF0', max_length=50, blank=True, null=True)
    chg3ay0 = models.CharField(db_column='CHG3AY0', max_length=50, blank=True, null=True)
    chg3at1 = models.CharField(db_column='CHG3AT1', max_length=50, blank=True, null=True)
    chg3af1 = models.CharField(db_column='CHG3AF1', max_length=50, blank=True, null=True)
    chg3ay1 = models.CharField(db_column='CHG3AY1', max_length=50, blank=True, null=True)
    chg3at2 = models.CharField(db_column='CHG3AT2', max_length=50, blank=True, null=True)
    chg3af2 = models.CharField(db_column='CHG3AF2', max_length=50, blank=True, null=True)
    chg3ay2 = models.CharField(db_column='CHG3AY2', max_length=50, blank=True, null=True)
    chg3at3 = models.CharField(db_column='CHG3AT3', max_length=50, blank=True, null=True)
    chg3af3 = models.CharField(db_column='CHG3AF3', max_length=50, blank=True, null=True)
    chg3ay3 = models.CharField(db_column='CHG3AY3', max_length=50, blank=True, null=True)
    chg3tgtd = models.CharField(db_column='CHG3TGTD', max_length=50, blank=True, null=True)
    chg3fgtd = models.CharField(db_column='CHG3FGTD', max_length=50, blank=True, null=True)
    chg4ay0 = models.CharField(db_column='CHG4AY0', max_length=50, blank=True, null=True)
    chg4ay1 = models.CharField(db_column='CHG4AY1', max_length=50, blank=True, null=True)
    chg4ay2 = models.CharField(db_column='CHG4AY2', max_length=50, blank=True, null=True)
    chg4ay3 = models.CharField(db_column='CHG4AY3', max_length=50, blank=True, null=True)
    chg5ay0 = models.CharField(db_column='CHG5AY0', max_length=50, blank=True, null=True)
    chg5ay1 = models.CharField(db_column='CHG5AY1', max_length=50, blank=True, null=True)
    chg5ay2 = models.CharField(db_column='CHG5AY2', max_length=50, blank=True, null=True)
    chg5ay3 = models.CharField(db_column='CHG5AY3', max_length=50, blank=True, null=True)
    chg6ay0 = models.CharField(db_column='CHG6AY0', max_length=50, blank=True, null=True)
    chg6ay1 = models.CharField(db_column='CHG6AY1', max_length=50, blank=True, null=True)
    chg6ay2 = models.CharField(db_column='CHG6AY2', max_length=50, blank=True, null=True)
    chg6ay3 = models.CharField(db_column='CHG6AY3', max_length=50, blank=True, null=True)
    chg7ay0 = models.CharField(db_column='CHG7AY0', max_length=50, blank=True, null=True)
    chg7ay1 = models.CharField(db_column='CHG7AY1', max_length=50, blank=True, null=True)
    chg7ay2 = models.CharField(db_column='CHG7AY2', max_length=50, blank=True, null=True)
    chg7ay3 = models.CharField(db_column='CHG7AY3', max_length=50, blank=True, null=True)
    chg8ay0 = models.CharField(db_column='CHG8AY0', max_length=50, blank=True, null=True)
    chg8ay1 = models.CharField(db_column='CHG8AY1', max_length=50, blank=True, null=True)
    chg8ay2 = models.CharField(db_column='CHG8AY2', max_length=50, blank=True, null=True)
    chg8ay3 = models.CharField(db_column='CHG8AY3', max_length=50, blank=True, null=True)

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
